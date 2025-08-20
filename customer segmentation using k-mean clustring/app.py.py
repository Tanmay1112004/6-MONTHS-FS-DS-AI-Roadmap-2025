# -*- coding: utf-8 -*-
"""
Advanced Customer Segmentation — Colab + Gradio (Stable Full Version)
- K-Means, Hierarchical, DBSCAN
- Robust file upload (works in Colab)
- Clean metrics + dashboard
- 2D/3D visualizations with PCA
- Dendrogram + Elbow + Silhouette
"""

# =========================
# Imports & Setup
# =========================
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score
from sklearn.decomposition import PCA

import scipy.cluster.hierarchy as sch

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import io
import base64

# Gradio 4.x
import gradio as gr

# Matplotlib defaults
plt.style.use('default')
sns.set_palette("husl")

COLORS = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFBE0B', '#FB5607',
          '#8338EC', '#3A86FF', '#38B000', '#9D4EDD', '#F72585',
          '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']  # extra buffer

# =========================
# Data Loading
# =========================
def _safe_read_csv(uploaded_file):
    """
    Gradio File can be:
      - a tempfile-like object with .name
      - a str path
      - a dict with {'name': '/tmp/...'}
    """
    if uploaded_file is None:
        return None
    if isinstance(uploaded_file, str):
        return pd.read_csv(uploaded_file)
    if hasattr(uploaded_file, "name"):
        return pd.read_csv(uploaded_file.name)
    if isinstance(uploaded_file, dict) and "name" in uploaded_file:
        return pd.read_csv(uploaded_file["name"])
    # Fallback (rare)
    return pd.read_csv(uploaded_file)

def load_data(uploaded_file=None):
    """Load dataset or generate a synthetic sample."""
    try:
        if uploaded_file is not None:
            df = _safe_read_csv(uploaded_file)
            # Minimal validation/auto-rename
            required = ['Annual Income (k$)', 'Spending Score (1-100)']
            if not all(c in df.columns for c in required):
                income_cols = [c for c in df.columns if "income" in c.lower() or "annual" in c.lower()]
                spend_cols  = [c for c in df.columns if "spend" in c.lower() or "score" in c.lower()]
                if income_cols and spend_cols:
                    df = df.rename(columns={
                        income_cols[0]: 'Annual Income (k$)',
                        spend_cols[0]: 'Spending Score (1-100)'
                    })
                else:
                    # If user file doesn't match, fall back to sample
                    return create_sample_data()
            return df
        return create_sample_data()
    except Exception as e:
        print("Error loading file:", e)
        return create_sample_data()

def create_sample_data(n_samples=250, seed=42):
    np.random.seed(seed)
    data = {
        'CustomerID': np.arange(1, n_samples + 1),
        'Gender': np.random.choice(['Male', 'Female'], n_samples),
        'Age': np.random.normal(38, 12, n_samples).astype(int),
        'Annual Income (k$)': np.random.normal(60, 18, n_samples).astype(int),
        'Spending Score (1-100)': np.random.normal(50, 22, n_samples).astype(int)
    }
    # Clip to reasonable ranges
    data['Age'] = np.clip(data['Age'], 18, 70)
    data['Annual Income (k$)'] = np.clip(data['Annual Income (k$)'], 15, 140)
    data['Spending Score (1-100)'] = np.clip(data['Spending Score (1-100)'], 1, 100)

    # Inject some structure (optional, helps show nice clusters)
    df = pd.DataFrame(data)
    return df

# =========================
# Feature Prep
# =========================
def prepare_features(dataset, features):
    """
    Returns:
      X            : np.ndarray of shape (n_samples, n_features)
      encoders     : dict of encoders used (for categorical)
      used_features: list of feature names actually used
    """
    used_features = []
    encoders = {}

    # Keep only requested features that exist
    for f in features:
        if f in dataset.columns:
            used_features.append(f)

    if not used_features:
        # Always ensure at least these two if present
        fallback = ['Annual Income (k$)', 'Spending Score (1-100)']
        used_features = [c for c in fallback if c in dataset.columns]

    X_list = []
    for f in used_features:
        col = dataset[f]
        if col.dtype == 'object':
            le = LabelEncoder()
            vals = le.fit_transform(col.astype(str))
            encoders[f] = le
            X_list.append(vals.astype(float))
        else:
            X_list.append(col.astype(float).values)

    X = np.vstack(X_list).T if X_list else np.empty((len(dataset), 0))
    return X, encoders, used_features

# =========================
# Core Clustering
# =========================
def kmeans_cluster(X, n_clusters=5, random_state=42):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    km = KMeans(n_clusters=n_clusters, init='k-means++', random_state=random_state, n_init=10)
    labels = km.fit_predict(X_scaled)
    # Metrics
    sil = silhouette_score(X_scaled, labels) if len(np.unique(labels)) > 1 else -1
    cal = calinski_harabasz_score(X_scaled, labels) if len(np.unique(labels)) > 1 else -1
    dbi = davies_bouldin_score(X_scaled, labels) if len(np.unique(labels)) > 1 else float('inf')
    # Centroids back to original scale
    centroids_orig = scaler.inverse_transform(km.cluster_centers_)
    return labels, (sil, cal, dbi), scaler, km, centroids_orig

def hierarchical_cluster(X, n_clusters=5, linkage='ward'):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    hc = AgglomerativeClustering(n_clusters=n_clusters, linkage=linkage)
    labels = hc.fit_predict(X_scaled)
    sil = silhouette_score(X_scaled, labels) if len(np.unique(labels)) > 1 else -1
    cal = calinski_harabasz_score(X_scaled, labels) if len(np.unique(labels)) > 1 else -1
    dbi = davies_bouldin_score(X_scaled, labels) if len(np.unique(labels)) > 1 else float('inf')
    return labels, (sil, cal, dbi), scaler

def dbscan_cluster(X, eps=0.5, min_samples=5):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    db = DBSCAN(eps=eps, min_samples=min_samples)
    labels = db.fit_predict(X_scaled)
    if len(np.unique(labels[labels >= 0])) > 1:
        sil = silhouette_score(X_scaled, labels)
        cal = calinski_harabasz_score(X_scaled, labels)
        dbi = davies_bouldin_score(X_scaled, labels)
    else:
        sil, cal, dbi = -1, -1, float('inf')
    return labels, (sil, cal, dbi), scaler

# =========================
# Visualizations (Matplotlib)
# =========================
def to_2d(X, n_components=2):
    if X.shape[1] <= n_components:
        return X.copy(), None
    pca = PCA(n_components=n_components, random_state=42)
    return pca.fit_transform(X), pca

def to_3d(X):
    if X.shape[1] >= 3:
        pca = PCA(n_components=3, random_state=42)
        X3 = pca.fit_transform(X)
        explained = pca.explained_variance_ratio_ * 100
        axes = [f"PC{i+1} ({explained[i]:.1f}%)" for i in range(3)]
        return X3, axes
    else:
        # pad
        if X.shape[1] == 2:
            X3 = np.hstack([X, np.zeros((X.shape[0], 1))])
            axes = ["Feature 1", "Feature 2", ""]
            return X3, axes
        elif X.shape[1] == 1:
            X3 = np.hstack([X, np.zeros((X.shape[0], 2))])
            axes = ["Feature 1", "", ""]
            return X3, axes
        else:
            return np.zeros((len(X), 3)), ["", "", ""]

def plot_clusters_2d(X, labels, name="Clustering", feature_names=None, centroids=None):
    """
    Projects to 2D with PCA if needed.
    Returns a Matplotlib Figure.
    """
    X2, pca2 = to_2d(X, 2)
    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111)

    unique_labels = sorted(np.unique(labels))
    # Noise (-1) last for DBSCAN clarity
    unique_labels = [l for l in unique_labels if l != -1] + ([-1] if -1 in unique_labels else [])

    for i, lab in enumerate(unique_labels):
        idx = labels == lab
        color = COLORS[i % len(COLORS)]
        lab_name = f"Cluster {lab+1}" if lab != -1 else "Noise"
        ax.scatter(X2[idx, 0], X2[idx, 1], s=60, alpha=0.8, edgecolor='w', linewidth=0.5,
                   label=lab_name, c=color)

    # Project centroids to 2D if provided
    if centroids is not None:
        if X.shape[1] > 2 and pca2 is not None:
            cent2 = pca2.transform(centroids)
        else:
            cent2 = centroids[:, :2] if centroids.shape[1] >= 2 else np.hstack([centroids, np.zeros((centroids.shape[0], 1))])
        ax.scatter(cent2[:, 0], cent2[:, 1], s=300, c='yellow', marker='*', edgecolor='black', linewidth=2, label='Centroids')

    ax.set_title(f'Customer Segments — {name}', fontsize=15, fontweight='bold')
    ax.set_xlabel('Component 1' if feature_names is None else feature_names[0])
    ax.set_ylabel('Component 2' if feature_names is None else (feature_names[1] if len(feature_names) > 1 else ''))
    ax.grid(True, alpha=0.3)
    ax.legend(bbox_to_anchor=(1.04, 1), loc='upper left')
    plt.tight_layout()
    return fig

def plot_clusters_3d(X, labels, name="Clustering"):
    X3, axes = to_3d(X)
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    unique_labels = sorted(np.unique(labels))
    unique_labels = [l for l in unique_labels if l != -1] + ([-1] if -1 in unique_labels else [])

    for i, lab in enumerate(unique_labels):
        idx = labels == lab
        color = COLORS[i % len(COLORS)]
        lab_name = f"Cluster {lab+1}" if lab != -1 else "Noise"
        ax.scatter(X3[idx, 0], X3[idx, 1], X3[idx, 2], s=50, alpha=0.8, c=color, label=lab_name)

    ax.set_title(f'3D View — {name}', fontsize=15, fontweight='bold')
    ax.set_xlabel(axes[0]); ax.set_ylabel(axes[1]); ax.set_zlabel(axes[2])
    ax.legend(loc='best')
    plt.tight_layout()
    return fig

def plot_elbow_silhouette(X, max_k=10):
    # Use scaled data
    scaler = StandardScaler()
    Xs = scaler.fit_transform(X)

    wcss, sils = [], []
    ks = range(2, max_k + 1)
    for k in ks:
        km = KMeans(n_clusters=k, init='k-means++', random_state=42, n_init=10)
        labels = km.fit_predict(Xs)
        wcss.append(km.inertia_)
        sils.append(silhouette_score(Xs, labels) if len(np.unique(labels)) > 1 else 0)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
    ax1.plot(list(ks), wcss, marker='o', linestyle='--', linewidth=2)
    ax1.set_title('Elbow Method (WCSS)', fontsize=13, fontweight='bold')
    ax1.set_xlabel('k'); ax1.set_ylabel('WCSS'); ax1.grid(True, alpha=0.3)

    ax2.plot(list(ks), sils, marker='s', linestyle='--', linewidth=2)
    ax2.set_title('Silhouette Score vs k', fontsize=13, fontweight='bold')
    ax2.set_xlabel('k'); ax2.set_ylabel('Silhouette'); ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    return fig

def plot_dendrogram(X, linkage='ward'):
    scaler = StandardScaler()
    Xs = scaler.fit_transform(X)
    Z = sch.linkage(Xs, method=linkage)
    fig = plt.figure(figsize=(12, 6))
    sch.dendrogram(Z, no_labels=True, color_threshold=0.7 * np.max(Z[:, 2]))
    plt.title('Dendrogram', fontsize=15, fontweight='bold')
    plt.xlabel('Samples'); plt.ylabel('Distance')
    plt.axhline(y=0.7 * np.max(Z[:, 2]), color='r', linestyle='--', linewidth=1)
    plt.tight_layout()
    return fig

# =========================
# Dashboard Visualization (Matplotlib)
# =========================
def create_dashboard(dataset_with_clusters):
    df = dataset_with_clusters.copy()
    # Guard if expected cols missing
    for col in ['Annual Income (k$)', 'Spending Score (1-100)', 'Age', 'Gender', 'Cluster']:
        if col not in df.columns:
            if col == 'Gender':
                df['Gender'] = 'Unknown'
            else:
                df[col] = np.nan

    n_clusters = len([c for c in sorted(df['Cluster'].unique()) if c != -1]) + (1 if (-1 in df['Cluster'].unique()) else 0)

    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    
    # Scatter plot: Income vs Spending
    for i, lab in enumerate(sorted(df['Cluster'].unique())):
        subset = df[df['Cluster'] == lab]
        name = f"Cluster {lab+1}" if lab != -1 else "Noise"
        axes[0, 0].scatter(subset['Annual Income (k$)'], subset['Spending Score (1-100)'],
                          s=60, c=COLORS[i % len(COLORS)], alpha=0.7, label=name)
    axes[0, 0].set_title('Income vs Spending by Cluster', fontsize=14, fontweight='bold')
    axes[0, 0].set_xlabel('Annual Income (k$)')
    axes[0, 0].set_ylabel('Spending Score (1-100)')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)
    
    # Box plot: Age distribution by cluster
    age_data = [df[df['Cluster'] == lab]['Age'] for lab in sorted(df['Cluster'].unique())]
    axes[0, 1].boxplot(age_data, labels=[f'Cluster {lab+1}' if lab != -1 else 'Noise' 
                                        for lab in sorted(df['Cluster'].unique())])
    axes[0, 1].set_title('Age Distribution by Cluster', fontsize=14, fontweight='bold')
    axes[0, 1].set_ylabel('Age')
    axes[0, 1].grid(True, alpha=0.3)
    
    # Bar chart: Gender distribution by cluster
    ct = pd.crosstab(df['Cluster'], df['Gender'])
    x = np.arange(len(ct))
    width = 0.35
    for i, gender in enumerate(ct.columns):
        axes[1, 0].bar(x - width/2 + i*width/len(ct.columns), ct[gender], width/len(ct.columns), 
                      label=gender, color=COLORS[i % len(COLORS)])
    axes[1, 0].set_title('Gender Distribution by Cluster', fontsize=14, fontweight='bold')
    axes[1, 0].set_xlabel('Cluster')
    axes[1, 0].set_ylabel('Count')
    axes[1, 0].set_xticks(x)
    axes[1, 0].set_xticklabels([f'Cluster {lab+1}' if lab != -1 else 'Noise' for lab in ct.index])
    axes[1, 0].legend()
    axes[1, 0].grid(True, alpha=0.3)
    
    # Bar chart: Cluster sizes
    sizes = df['Cluster'].value_counts().sort_index()
    axes[1, 1].bar([f'Cluster {lab+1}' if lab != -1 else 'Noise' for lab in sizes.index], 
                  sizes.values, color=[COLORS[i % len(COLORS)] for i in range(len(sizes))])
    axes[1, 1].set_title('Cluster Sizes', fontsize=14, fontweight='bold')
    axes[1, 1].set_xlabel('Cluster')
    axes[1, 1].set_ylabel('Number of Customers')
    for i, v in enumerate(sizes.values):
        axes[1, 1].text(i, v + 0.5, str(v), ha='center')
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.suptitle("Customer Segmentation Dashboard", fontsize=16, fontweight='bold')
    plt.tight_layout()
    return fig

# =========================
# Cluster Analysis Table
# =========================
def analyze_clusters(dataset, labels):
    df = dataset.copy()
    df['Cluster'] = labels

    # Only compute stats if numeric cols present
    numeric_cols = [c for c in ['Age', 'Annual Income (k$)', 'Spending Score (1-100)'] if c in df.columns]
    if not numeric_cols:
        return pd.DataFrame()

    stats = df.groupby('Cluster').agg({
        'Age': ['mean', 'std', 'count'] if 'Age' in df.columns else [],
        'Annual Income (k$)': ['mean', 'std'] if 'Annual Income (k$)' in df.columns else [],
        'Spending Score (1-100)': ['mean', 'std'] if 'Spending Score (1-100)' in df.columns else []
    }).round(2)

    # Flatten columns
    stats.columns = ['_'.join([c for c in col if c]).strip() for col in stats.columns.values]
    if 'Age_count' in stats.columns:
        stats = stats.rename(columns={'Age_count': 'Count'})
    stats = stats.reset_index()

    # Interpretation
    interpretations = []
    for _, row in stats.iterrows():
        income = row.get('Annual Income (k$)_mean', np.nan)
        spending = row.get('Spending Score (1-100)_mean', np.nan)
        age = row.get('Age_mean', np.nan)

        interp = "📈 Balanced shoppers."
        if pd.notna(income) and pd.notna(spending):
            if income > 75 and spending > 60:
                interp = "💎 Premium: high income, high spend."
            elif income > 75 and spending <= 60:
                interp = "💰 Affluent but cautious."
            elif income <= 75 and spending > 60:
                interp = "🎯 Value seekers: spend more despite moderate income."
            elif income <= 40 and spending <= 40:
                interp = "📊 Budget-conscious."

        if pd.notna(age):
            if age < 30:
                interp += " Mostly young."
            elif age > 50:
                interp += " Mostly mature."
            else:
                interp += " Mixed age."

        interpretations.append(interp)

    stats['Interpretation'] = interpretations
    return stats

# =========================
# Orchestration
# =========================
def run_customer_segmentation(n_clusters, algorithm, linkage_method, eps, min_samples, features, uploaded_file):
    # Load & features
    dataset = load_data(uploaded_file)
    X, encoders, used_features = prepare_features(dataset, features)
    if X.size == 0:
        return None, None, None, None, None, "No valid features found.", pd.DataFrame(), pd.DataFrame()

    # Fit selected algorithm
    if algorithm == "K-Means":
        labels, (sil, cal, dbi), scaler, km, centroids = kmeans_cluster(X, n_clusters=n_clusters)
        algo_name = "K-Means"
    elif algorithm == "Hierarchical":
        labels, (sil, cal, dbi), scaler = hierarchical_cluster(X, n_clusters=n_clusters, linkage=linkage_method)
        centroids = None
        algo_name = f"Hierarchical ({linkage_method})"
    else:
        labels, (sil, cal, dbi), scaler = dbscan_cluster(X, eps=eps, min_samples=min_samples)
        centroids = None
        algo_name = f"DBSCAN (eps={eps}, min_samples={min_samples})"

    # Visualizations
    cluster_fig_2d = plot_clusters_2d(X, labels, name=algo_name, feature_names=used_features, centroids=centroids)
    cluster_fig_3d = plot_clusters_3d(X, labels, name=algo_name)

    elbow_fig = plot_elbow_silhouette(X) if algorithm == "K-Means" else None
    dendro_fig = plot_dendrogram(X, linkage=linkage_method) if algorithm == "Hierarchical" else None

    # Dashboard & stats
    dataset_with_clusters = dataset.copy()
    dataset_with_clusters['Cluster'] = labels
    dashboard_fig = create_dashboard(dataset_with_clusters)
    stats_df = analyze_clusters(dataset, labels)

    # Metrics text
    k_count = len([c for c in np.unique(labels) if c != -1]) + (1 if (-1 in labels) else 0)
    metrics_text = f"""
**Clustering Performance — {algo_name}**
- Silhouette Score: {sil:.4f} {'(higher is better)' if sil != -1 else '(n/a)'}
- Calinski–Harabasz: {cal:.2f} {'(higher is better)' if cal != -1 else '(n/a)'}
- Davies–Bouldin: {dbi:.4f} {'(lower is better)' if dbi != float('inf') else '(n/a)'}

**Summary**
- Clusters detected: {k_count}
- Total records: {len(dataset)}
- Features: {', '.join(used_features) if used_features else '—'}
"""

    return (
        cluster_fig_2d,                 # gr.Plot (matplotlib)
        elbow_fig,                      # gr.Plot (matplotlib) or None
        dendro_fig,                     # gr.Plot (matplotlib) or None
        cluster_fig_3d,                 # gr.Plot (matplotlib)
        dashboard_fig,                  # gr.Plot (matplotlib)
        metrics_text,                   # gr.Markdown
        stats_df,                       # gr.Dataframe
        dataset_with_clusters           # gr.Dataframe
    )

# =========================
# Gradio App
# =========================
CSS = """
.gradio-container { max-width: 1200px !important; }
.header {
  text-align: center;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 18px; border-radius: 12px; color: white; margin-bottom: 18px;
}
.metric-card { background: #f8f9fa; border-radius: 8px; padding: 12px; border-left: 4px solid #667eea; }
"""

with gr.Blocks(title="Advanced Customer Segmentation", css=CSS) as demo:
    gr.Markdown("""
    <div class="header">
        <h1>🎯 Advanced Customer Segmentation Analysis</h1>
        <p>Find meaningful customer groups using K-Means, Hierarchical, and DBSCAN.</p>
    </div>
    """)

    with gr.Row():
        with gr.Column(scale=1, min_width=320):
            gr.Markdown("### ⚙️ Configuration")
            with gr.Accordion("Data", open=True):
                file_upload = gr.File(label="Upload CSV (optional)", file_types=[".csv"])
                feature_selector = gr.CheckboxGroup(
                    choices=['Age', 'Annual Income (k$)', 'Spending Score (1-100)', 'Gender'],
                    value=['Annual Income (k$)', 'Spending Score (1-100)'],
                    label="Features"
                )

            with gr.Accordion("Algorithm", open=True):
                algorithm = gr.Radio(choices=["K-Means", "Hierarchical", "DBSCAN"], value="K-Means", label="Choose")
                n_clusters = gr.Slider(2, 10, value=5, step=1, label="Number of Clusters (KMeans/Hierarchical)")
                linkage_method = gr.Dropdown(choices=["ward", "complete", "average", "single"], value="ward",
                                             label="Linkage (Hierarchical)")
                with gr.Row():
                    eps = gr.Slider(0.1, 2.0, value=0.5, step=0.1, label="DBSCAN eps")
                    min_samples = gr.Slider(2, 30, value=5, step=1, label="DBSCAN min_samples")

            run_btn = gr.Button("🚀 Run Segmentation", variant="primary")

            gr.Markdown("""
            <div class="metric-card">
                <b>How to use:</b>
                <ol>
                    <li>Upload CSV or use sample data</li>
                    <li>Select features for clustering</li>
                    <li>Pick algorithm & tune params</li>
                    <li>Hit Run and explore!</li>
                </ol>
            </div>
            """)

        with gr.Column(scale=2):
            with gr.Tab("📊 Cluster Visualization"):
                cluster_plot = gr.Plot(label="2D Cluster Plot (PCA if needed)")
                cluster_3d_plot = gr.Plot(label="3D Cluster Plot (PCA if needed)")

            with gr.Tab("📈 Analysis Tools"):
                elbow_plot = gr.Plot(label="Elbow + Silhouette (K-Means)")
                dendrogram_plot = gr.Plot(label="Dendrogram (Hierarchical)")

            with gr.Tab("📋 Results Dashboard"):
                dashboard = gr.Plot(label="Interactive Dashboard")

            with gr.Tab("📝 Metrics & Statistics"):
                metrics_output = gr.Markdown()
                cluster_stats_tbl = gr.Dataframe(label="Cluster Analysis (per cluster)", wrap=True)

            with gr.Tab("💾 Data Output"):
                data_output = gr.Dataframe(label="Data with Cluster Labels")

    # Wire events
    run_btn.click(
        fn=run_customer_segmentation,
        inputs=[n_clusters, algorithm, linkage_method, eps, min_samples, feature_selector, file_upload],
        outputs=[cluster_plot, elbow_plot, dendrogram_plot, cluster_3d_plot, dashboard,
                 metrics_output, cluster_stats_tbl, data_output]
    )

    # Handy examples
    gr.Examples(
        examples=[
            [5, "K-Means", "ward", 0.5, 5, ['Annual Income (k$)', 'Spending Score (1-100)'], None],
            [4, "Hierarchical", "complete", 0.5, 5, ['Annual Income (k$)', 'Spending Score (1-100)'], None],
            [3, "DBSCAN", "average", 0.7, 10, ['Annual Income (k$)', 'Spending Score (1-100)'], None],
            [6, "K-Means", "ward", 0.5, 5, ['Age', 'Annual Income (k$)', 'Spending Score (1-100)'], None]
        ],
        inputs=[n_clusters, algorithm, linkage_method, eps, min_samples, feature_selector, file_upload]
    )

# Launch (works in Colab)
if __name__ == "__main__":
    demo.launch(share=True, server_name="0.0.0.0")