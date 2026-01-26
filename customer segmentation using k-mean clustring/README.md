# 🎯 Customer Segmentation via K-Means Clustering

### 📊 Turning Raw Data into Marketing Intelligence

Businesses often struggle to understand their diverse customer base. This project implements a **K-Means Clustering** algorithm to group customers by behavioral patterns (Annual Income vs. Spending Score), allowing for hyper-targeted marketing and improved ROI.

---

## 🔍 The Workflow

1. **Exploratory Data Analysis (EDA):** Identifying correlations and distributions.
2. **Feature Scaling:** Normalizing data to ensure the algorithm isn't biased by units.
3. **Optimal 'K' Selection:** Utilizing the **Elbow Method** and **Silhouette Analysis** to find the mathematical "sweet spot" for the number of clusters.
4. **Modeling:** Fitting the K-Means algorithm to the multi-dimensional data.
5. **Interactive Deployment:** A Gradio-based UI for real-time segmentation.

---

## 📈 Key Insights & Results

By analyzing the clusters, we can typically categorize the audience into four or five distinct personas:

| Cluster | Persona | Strategy |
| --- | --- | --- |
| **Cluster 1** | 🛍️ High Earners, High Spenders | **Target with Premium/Luxury offers.** |
| **Cluster 2** | 💸 High Earners, Low Spenders | **Target with Value-based or Loyalty rewards.** |
| **Cluster 3** | 🎉 Average Earners/Spenders | **Standard promotional newsletters.** |
| **Cluster 4** | 💤 Low Earners, Low Spenders | **Discount-heavy win-back campaigns.** |

---

## 🛠️ Tech Stack

* **Core:** `Python 3.x`, `Scikit-learn`
* **Data:** `Pandas`, `NumPy`
* **Visuals:** `Matplotlib`, `Seaborn`, `Plotly` (for 3D cluster rotation)
* **Interface:** `Gradio` (for the web-based dashboard)

---

## 🚀 Installation & Usage

### 1. Clone & Setup

```bash
git clone https://github.com/your-username/customer-segmentation-kmeans.git
cd customer-segmentation-kmeans
pip install -r requirements.txt

```

### 2. Launch the Application

```bash
python app.py

```

*The Gradio interface will launch in your browser, allowing you to upload a CSV and visualize segments instantly.*

---

## 📸 Visualization Preview

> **Note:** Below is a representation of the 3D cluster separation. The interactive version in the notebook allows for 360° rotation to inspect outlier boundaries.

---

## 🌟 Roadmap & Improvements

* [ ] **Automated K-Selection:** Integrating the KneeLocator library.
* [ ] **Hybrid Models:** Testing **DBSCAN** to identify density-based noise (outliers).
* [ ] **Cloud Deployment:** Moving the Gradio app to Hugging Face Spaces.

## 🤝 Contributing & License

Contributions are what make the open-source community an amazing place to learn! Feel free to **Fork** this project and submit a **Pull Request**. Distributed under the MIT License.

---
