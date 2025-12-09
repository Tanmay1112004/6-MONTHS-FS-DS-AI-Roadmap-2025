# 🎯 **Customer Churn Prediction Dashboard**

An interactive and business-focused **churn prediction dashboard** built using **Gradio** and **scikit-learn**.
This tool demonstrates how organizations can **predict**, **compare**, and **visualize** customer churn risk in real-time — perfect for showcasing ML + UI skills in a practical business context.

The project simulates a **telecom industry scenario**, where churn likelihood depends on factors such as:

* **Monthly Charges** 💰
* **Contract Type** 📜
* **Internet Service** 🌐
* **Tenure (Months)** 📆

---

## ✨ **Core Highlights**

✔️ **Single Prediction Mode** → Predict churn for one customer with a probability visualization
✔️ **Random Example Generator** → Auto-fills realistic synthetic customer data
✔️ **Two-Customer Comparison Mode** → Side-by-side risk scoring & graphs
✔️ **Downloadable Dataset** → Synthetic telecom churn dataset for practice
✔️ **Prediction Export** → Save model outputs as JSON for reporting
✔️ **Model Card Included** → Clear description of assumptions, limitations & usage

This dashboard is designed to be **clean**, **interactive**, and **portfolio-ready**.

---

# 📸 **Demo Previews**

![demo](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/Customer%20Churn%20Prediction/screenshots/Screenshot%202025-08-28%20112452.png)

![demo](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/Customer%20Churn%20Prediction/screenshots/Screenshot%202025-08-28%20112643.png)

![demo](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/Customer%20Churn%20Prediction/screenshots/Screenshot%202025-08-28%20112715.png)

![demo](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/Customer%20Churn%20Prediction/screenshots/Screenshot%202025-08-28%20112809.png)

![demo](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/Customer%20Churn%20Prediction/screenshots/Screenshot%202025-08-28%20112825.png)

---

## 🚀 **Quickstart**

### **1. Clone the Repository**

```bash
git clone https://github.com/yourusername/churn-dashboard.git
cd churn-dashboard
```

### **2. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **3. Launch the App**

```bash
python app.py
```

Gradio provides both a **local URL** and a **shareable public link**.

---

## 🧠 **Model Details**

* **Model Type:** Gradient Boosting Classifier
* **Dataset:** 2000-row synthetic telecom dataset
* **Feature Encoding:**

  * Contract: Month-to-month = 0, One year = 1, Two year = 2
  * InternetService: DSL = 0, Fiber optic = 1, No = 2
* **Note:**
  This is a **demonstration model**, built to explain concepts — not for production deployment.
  (Training & evaluation occur on the same dataset.)

---

## 📂 **Project Structure**

```
churn-dashboard/
│── app.py                  # Main dashboard application
│── sample_churn_data.csv   # Synthetic dataset
│── requirements.txt         # Dependencies
│── README.md                # Documentation
```

---

## 📊 **Where This Project Shines**

* **Data Science Portfolios** → Clean ML pipeline + UI + business integration
* **Business Analyst Learning** → Interpreting model outputs & customer risk
* **Classroom/Education** → Ideal for teaching predictive analytics
* **Interview Demo** → Shows practical understanding of churn, ML & UX

---

## 🛠 **Requirements**

* Python 3.9+
* gradio
* scikit-learn
* pandas
* numpy
* matplotlib

---

## 🧭 **Roadmap**

* [ ] Add SHAP-based explainability
* [ ] Deploy using Docker + Render/Cloud Run
* [ ] Integrate real Telco Customer Churn dataset
* [ ] Add login/authentication for enterprise use
* [ ] Multi-model comparison page (LogReg vs XGBoost vs GBM)

---

## 🏆 **Author**

👤 **Tanmay**
*Data Science • Machine Learning • Business Analytics*

---
