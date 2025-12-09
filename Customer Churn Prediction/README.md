# 🎯 Customer Churn Prediction Dashboard

An **interactive churn prediction dashboard** built with **Gradio + scikit-learn**, designed to demonstrate how businesses can predict and visualize customer churn risk in real time.

This project simulates a **telecom scenario** where customers may or may not churn based on:

* Monthly Charges 💰
* Contract Type 📜
* Internet Service 🌐
* Tenure (Months) 📆

The app provides:
✅ **Single Prediction Mode** → Predict churn risk for one customer (with probability chart)
✅ **Random Example Button** → Auto-fills fields with synthetic sample customer data
✅ **Compare Two Customers Mode** → Side-by-side churn prediction and visualization
✅ **Downloadable Dataset** → Synthetic dataset for exploration & practice
✅ **Export Predictions** → Save results as JSON for reporting/business analysis
✅ **Model Card & Notes** → Explains model assumptions + guidance on inputs
--
# Demo Images

![demo](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/Customer%20Churn%20Prediction/screenshots/Screenshot%202025-08-28%20112452.png)

![demo](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/Customer%20Churn%20Prediction/screenshots/Screenshot%202025-08-28%20112643.png)

![demo](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/Customer%20Churn%20Prediction/screenshots/Screenshot%202025-08-28%20112715.png)

![demo](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/Customer%20Churn%20Prediction/screenshots/Screenshot%202025-08-28%20112809.png)

![demo](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/Customer%20Churn%20Prediction/screenshots/Screenshot%202025-08-28%20112825.png)

---

## 🚀 Quickstart

### 1. Clone Repo

```bash
git clone https://github.com/yourusername/churn-dashboard.git
cd churn-dashboard
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run App

```bash
python app.py
```

You’ll get a local + public (share) link.

---

## 🧠 Model Details

* **Algorithm:** Gradient Boosting Classifier (scikit-learn)
* **Data:** Synthetic (2000 rows) → generated with rules to mimic real churn behavior
* **Encodings:**

  * Contract → Month-to-month = 0, One year = 1, Two year = 2
  * InternetService → DSL = 0, Fiber optic = 1, No = 2
* **Important Note:** This is a **toy demo model**, **not production-ready**. Accuracy numbers are inflated since training + evaluation are on the same dataset.

---

## 📂 Project Structure

```
churn-dashboard/
│── app.py               # Main Gradio app
│── sample_churn_data.csv # Synthetic dataset (auto-generated)
│── requirements.txt      # Dependencies
│── README.md             # Documentation
```

---

## 📊 Sample Use Cases

* **Data Science Portfolio Project** → Show ML + UI + Explainability
* **Business Analyst Training** → How to interpret churn models
* **Educational Tool** → Demonstrates ML pipeline end-to-end

---

## 🛠 Requirements

* Python 3.9+
* gradio
* scikit-learn
* matplotlib
* pandas
* numpy

---

## 📌 Roadmap (Future Work)

* [ ] Deploy with Docker + Render/Cloud Run
* [ ] Add SHAP explainability for feature contribution
* [ ] Real-world dataset integration (Telco churn dataset)
* [ ] Authentication layer for enterprise use

---

## 🏆 Author

👤 **Tanmay** – Data Science | ML Engineering | Business Analytics Enthusiast

---

🔥 With this dashboard, you’re not just predicting churn—you’re **telling the story of why customers leave**. Perfect for interviews, portfolio, or client demos.

---

