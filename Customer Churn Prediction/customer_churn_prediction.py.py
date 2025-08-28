import gradio as gr
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import json
import time

# --------------------------
# 1) DATA + MODEL
# --------------------------

def create_data_and_train(n_samples: int = 2000, seed: int = 42):
    """Create a small synthetic churn dataset and train a simple model.
    Features kept intentionally minimal for clarity + maintenance.
    """
    rng = np.random.default_rng(seed)

    data = {
        "MonthlyCharges": rng.uniform(20, 120, n_samples),          # $ per month
        "Contract": rng.integers(0, 3, n_samples),                  # 0=Month-to-month, 1=One year, 2=Two year
        "InternetService": rng.integers(0, 3, n_samples),           # 0=DSL, 1=Fiber optic, 2=No
        "Tenure": rng.integers(0, 60, n_samples),                   # months
    }
    df = pd.DataFrame(data)

    # Churn probability business rules (intentionally simple and readable)
    churn_prob = (
        (df["MonthlyCharges"] > 70) * 0.30 +
        (df["Contract"] == 0) * 0.40 +      # Month-to-month churns more
        (df["InternetService"] == 1) * 0.20  # Fiber optic churns more in this toy setup
    )
    y = (np.random.default_rng(seed + 7).random(n_samples) < churn_prob).astype(int)
    df["Churn"] = y

    model = GradientBoostingClassifier(n_estimators=120, max_depth=5, random_state=seed)
    model.fit(df[["MonthlyCharges", "Contract", "InternetService", "Tenure"]], y)

    acc = accuracy_score(y, model.predict(df[["MonthlyCharges", "Contract", "InternetService", "Tenure"]]))
    return model, df, acc

model, sample_data, train_acc = create_data_and_train()
SAMPLE_CSV_PATH = "sample_churn_data.csv"
sample_data.to_csv(SAMPLE_CSV_PATH, index=False)

# Helpful mappings (kept in one place)
CONTRACT_TO_INT = {"Month-to-month": 0, "One year": 1, "Two year": 2}
INT_TO_CONTRACT = {v: k for k, v in CONTRACT_TO_INT.items()}
INTERNET_TO_INT = {"DSL": 0, "Fiber optic": 1, "No": 2}
INT_TO_INTERNET = {v: k for k, v in INTERNET_TO_INT.items()}

# --------------------------
# 2) CORE HELPERS
# --------------------------

def _predict_proba(monthly_charges: float, contract: str, internet_service: str, tenure: int) -> float:
    X = pd.DataFrame([{
        "MonthlyCharges": monthly_charges,
        "Contract": CONTRACT_TO_INT[contract],
        "InternetService": INTERNET_TO_INT[internet_service],
        "Tenure": tenure,
    }])
    return float(model.predict_proba(X)[0, 1]) * 100.0


def _trend_figure(monthly_charges: float, contract: str, internet_service: str, tenure: int, label: str = "Your Input"):
    charges_range = np.linspace(20, 120, 120)
    probs = []
    for c in charges_range:
        probs.append(_predict_proba(c, contract, internet_service, tenure))

    fig, ax = plt.subplots()
    ax.plot(charges_range, probs, label="Churn Probability vs Monthly Charges")
    ax.axvline(monthly_charges, linestyle="--", label=label)
    ax.set_xlabel("Monthly Charges ($)")
    ax.set_ylabel("Churn Probability (%)")
    ax.set_title("Churn Probability Trend")
    ax.legend()
    fig.tight_layout()
    return fig


def _dual_trend_figure(a, b):
    # a/b are dicts with keys: monthly_charges, contract, internet_service, tenure, label
    charges_range = np.linspace(20, 120, 120)
    probs_a, probs_b = [], []
    for c in charges_range:
        probs_a.append(_predict_proba(c, a["contract"], a["internet_service"], a["tenure"]))
        probs_b.append(_predict_proba(c, b["contract"], b["internet_service"], b["tenure"]))

    fig, ax = plt.subplots()
    ax.plot(charges_range, probs_a, label=f"A Trend ({a['label']})")
    ax.plot(charges_range, probs_b, label=f"B Trend ({b['label']})")
    ax.axvline(a["monthly_charges"], linestyle="--", label="A charges")
    ax.axvline(b["monthly_charges"], linestyle="--", label="B charges")
    ax.set_xlabel("Monthly Charges ($)")
    ax.set_ylabel("Churn Probability (%)")
    ax.set_title("Compare: Churn Probability vs Monthly Charges")
    ax.legend()
    fig.tight_layout()
    return fig

# --------------------------
# 3) GRADIO CALLBACKS
# --------------------------

def predict_single(monthly_charges, contract, internet_service, tenure):
    proba = _predict_proba(monthly_charges, contract, internet_service, tenure)
    label = "🚨 High Churn Risk" if proba >= 50 else "✅ Low Churn Risk"
    msg = f"{label} ({proba:.1f}%)."
    fig = _trend_figure(monthly_charges, contract, internet_service, tenure, label="Selected Charges")

    # Prepare a JSON export (as string). In UI we allow user to download.
    payload = {
        "timestamp": int(time.time()),
        "inputs": {
            "MonthlyCharges": monthly_charges,
            "Contract": contract,
            "InternetService": internet_service,
            "Tenure": tenure,
        },
        "prediction": {
            "churn_probability_percent": round(proba, 2),
            "label": "High" if proba >= 50 else "Low",
        },
        "model": {
            "estimator": "GradientBoostingClassifier",
            "train_accuracy": round(float(train_acc), 3),
            "note": "Toy synthetic model for demo; not for production."
        },
    }
    json_path = "single_prediction.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)

    return msg, fig, json_path


def random_example():
    row = sample_data.sample(1).iloc[0]
    return (
        float(row["MonthlyCharges"]),
        INT_TO_CONTRACT[int(row["Contract"])],
        INT_TO_INTERNET[int(row["InternetService"])],
        int(row["Tenure"]),
    )


def reset_defaults():
    return (60.0, "Month-to-month", "DSL", 24)


def compare_customers(mc1, c1, net1, t1, mc2, c2, net2, t2):
    p1 = _predict_proba(mc1, c1, net1, t1)
    p2 = _predict_proba(mc2, c2, net2, t2)

    msg1 = ("🚨 High" if p1 >= 50 else "✅ Low") + f" ({p1:.1f}%)"
    msg2 = ("🚨 High" if p2 >= 50 else "✅ Low") + f" ({p2:.1f}%)"
    diff = abs(p1 - p2)

    comparison_text = (
        f"👤 Customer A: {msg1}\n"
        f"👤 Customer B: {msg2}\n\n"
        f"📊 Difference in Churn Risk: {diff:.1f}%"
    )

    a = {"monthly_charges": mc1, "contract": c1, "internet_service": net1, "tenure": t1, "label": "A"}
    b = {"monthly_charges": mc2, "contract": c2, "internet_service": net2, "tenure": t2, "label": "B"}
    fig = _dual_trend_figure(a, b)

    # Export as JSON
    payload = {
        "timestamp": int(time.time()),
        "customer_A": {"MonthlyCharges": mc1, "Contract": c1, "InternetService": net1, "Tenure": t1, "probability_percent": round(p1, 2)},
        "customer_B": {"MonthlyCharges": mc2, "Contract": c2, "InternetService": net2, "Tenure": t2, "probability_percent": round(p2, 2)},
        "difference_percent": round(diff, 2),
    }
    json_path = "comparison_result.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)

    return comparison_text, fig, json_path

# --------------------------
# 4) UI
# --------------------------
with gr.Blocks(title="Customer Churn Predictor — BA Dashboard", theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # 🎯 Customer Churn Prediction — Simple, Readable, Useful
    **What to enter:**
    - **💰 Monthly Charges ($):** 20 to 120. *Higher charges → usually higher churn risk.*
    - **📜 Contract:** Month-to-month / One year / Two year. *Month-to-month churns more.*
    - **🌐 Internet Service:** DSL / Fiber optic / No. *Fiber shows higher churn in this toy data.*
    - **📆 Tenure (months):** 0 to 60. *Longer tenure → more loyal.*
    """)

    with gr.Accordion("ℹ️ Model Card / Notes", open=False):
        gr.Markdown(
            f"""
            **Model:** GradientBoostingClassifier  
            **Training accuracy (on synthetic data):** {train_acc:.2f}  
            **Disclaimer:** This is a synthetic demo model. Do **not** use for real decisions.  
            **Encodings:** Contract → 0 M2M, 1 One-year, 2 Two-year. Internet → 0 DSL, 1 Fiber, 2 No.
            """
        )

    with gr.Tabs():
        with gr.Tab("🔍 Single Prediction"):
            with gr.Row():
                monthly_charges = gr.Slider(20, 120, value=60, step=1, label="💰 Monthly Charges ($)", info="Higher charges → more likely to churn")
                contract = gr.Dropdown(["Month-to-month", "One year", "Two year"], value="Month-to-month", label="📜 Contract", info="Month-to-month = higher churn risk")
                internet_service = gr.Dropdown(["DSL", "Fiber optic", "No"], value="DSL", label="🌐 Internet Service", info="Fiber optic users churn more often in this toy dataset")
                tenure = gr.Slider(0, 60, value=24, step=1, label="📆 Tenure (months)", info="Longer tenure → more loyalty")

            with gr.Row():
                predict_btn = gr.Button("🔮 Predict", variant="primary")
                random_btn = gr.Button("🎲 Random Example")
                reset_btn = gr.Button("♻️ Reset")

            output_text = gr.Textbox(label="Prediction", lines=2)
            output_plot = gr.Plot(label="Churn Probability Chart")

            with gr.Row():
                gr.Markdown("**Export last prediction as JSON:**")
                single_json = gr.File(label="single_prediction.json")

            predict_btn.click(
                fn=predict_single,
                inputs=[monthly_charges, contract, internet_service, tenure],
                outputs=[output_text, output_plot, single_json]
            )
            random_btn.click(fn=random_example, inputs=[], outputs=[monthly_charges, contract, internet_service, tenure])
            reset_btn.click(fn=reset_defaults, inputs=[], outputs=[monthly_charges, contract, internet_service, tenure])

        with gr.Tab("⚖️ Compare Two Customers"):
            with gr.Row():
                with gr.Column():
                    gr.Markdown("**Customer A**")
                    mc1 = gr.Slider(20, 120, value=55, step=1, label="Monthly Charges A")
                    c1 = gr.Dropdown(["Month-to-month", "One year", "Two year"], value="One year", label="Contract A")
                    net1 = gr.Dropdown(["DSL", "Fiber optic", "No"], value="DSL", label="Internet A")
                    t1 = gr.Slider(0, 60, value=12, step=1, label="Tenure A (months)")
                with gr.Column():
                    gr.Markdown("**Customer B**")
                    mc2 = gr.Slider(20, 120, value=85, step=1, label="Monthly Charges B")
                    c2 = gr.Dropdown(["Month-to-month", "One year", "Two year"], value="Month-to-month", label="Contract B")
                    net2 = gr.Dropdown(["DSL", "Fiber optic", "No"], value="Fiber optic", label="Internet B")
                    t2 = gr.Slider(0, 60, value=6, step=1, label="Tenure B (months)")

            compare_btn = gr.Button("⚖️ Compare", variant="primary")
            compare_text = gr.Textbox(label="Comparison Result", lines=4)
            compare_plot = gr.Plot(label="Comparison Chart")
            with gr.Row():
                gr.Markdown("**Export comparison as JSON:**")
                compare_json = gr.File(label="comparison_result.json")

            compare_btn.click(
                fn=compare_customers,
                inputs=[mc1, c1, net1, t1, mc2, c2, net2, t2],
                outputs=[compare_text, compare_plot, compare_json]
            )

    gr.Markdown("---")
    gr.Markdown("### 📂 Download the Synthetic Training Data")
    gr.File(value=SAMPLE_CSV_PATH, label="sample_churn_data.csv")

if __name__ == "__main__":
    print("🚀 App starting...")
    demo.launch(share=True, debug=True)
