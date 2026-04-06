# 🎓 Student Mark Prediction System

> **Predict academic performance using data — turning study habits into measurable outcomes.**

A full-stack **Machine Learning web application** that predicts student exam scores based on study hours using a highly interpretable **Linear Regression model**. Built to demonstrate **end-to-end ML deployment** — from training to real-world usage via a web interface.

---

## 🚀 Demo Preview

![demo](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/Student%20mark%20Predictor%20using%20gradio%20ui/screenshots/Screenshot%202025-08-19%20205404.png)

![demo](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/Student%20mark%20Predictor%20using%20gradio%20ui/screenshots/Screenshot%202025-08-19%20205646.png)


---

## 💡 Problem Statement

Students often ask:
👉 *“How much should I study to score better?”*

This project answers that with data.

It transforms **study hours → predicted marks**, enabling smarter decisions instead of guesswork.

---

## 🎯 Business / Real-World Impact

### 👨‍🎓 Students

* Understand optimal study time
* Avoid burnout (diminishing returns)
* Set realistic score targets

### 👩‍🏫 Educators

* Identify low-performing students early
* Provide targeted interventions

### 🏫 Institutions

* Data-driven academic planning
* Resource allocation for tutoring

---

## 🧠 Machine Learning Engine

### 🔹 Model Used

* **Linear Regression (Supervised Learning)**

### 🔹 Why Linear Regression?

* High interpretability 📊
* Fast training ⚡
* Perfect for continuous prediction problems

### 🔹 Model Performance

* **R² Score:** `0.95+`
* Strong linear correlation between study hours and marks

### 🔹 Prediction Logic

```
Predicted Marks = m × Study Hours + c
```

---

## 🏗️ System Architecture

```
User Input (Study Hours)
        ↓
Frontend (HTML/CSS/JS)
        ↓
Flask Backend API
        ↓
Loaded ML Model (Joblib)
        ↓
Prediction Output (Marks)
        ↓
UI Display
```

---

## 🛠️ Tech Stack

| Layer             | Technology                       |
| ----------------- | -------------------------------- |
| **Backend**       | Flask (Python)                   |
| **Frontend**      | HTML5, CSS3, JavaScript          |
| **ML Model**      | Scikit-learn (Linear Regression) |
| **Data Handling** | Pandas, NumPy                    |
| **Model Storage** | Joblib                           |

---

## 📂 Project Structure

```
student-mark-prediction/
├── app/
│   ├── main.py                # Flask app (API + routing)
│   ├── static/                # CSS, JS
│   └── templates/             # HTML templates (UI)
│
├── training/
│   ├── train_model.py         # Model training pipeline
│   └── student_data.csv       # Dataset
│
├── models/
│   └── predictor_model.pkl    # Trained model
│
└── requirements.txt
```

---

## ⚡ Quick Start

### 🔹 1. Clone Repository

```bash
git clone https://github.com/your-username/student-mark-prediction.git
cd student-mark-prediction
```

### 🔹 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔹 3. Run Application

```bash
python app/main.py
```

Open browser →
👉 `http://127.0.0.1:5000`

---

## 📊 Sample Predictions

| Study Hours | Predicted Marks | Insight              |
| ----------- | --------------- | -------------------- |
| **4 hrs**   | 66%             | Moderate performance |
| **8 hrs**   | 82%             | Strong improvement   |
| **12 hrs**  | 97%             | Near saturation      |

➡️ Insight: Performance improves with study time, but gains slow down at higher hours.

---

## 🔥 Key Highlights

✔ End-to-end ML pipeline (training → deployment)
✔ Real-time prediction via web app
✔ Clean separation of frontend & backend
✔ High model interpretability
✔ Beginner-friendly + production mindset

---

## 🧪 Challenges & Learnings

* Translating ML model into a **real-world web app**
* Managing **model serialization (Joblib)**
* Building clean **Flask API structure**
* Connecting frontend inputs with backend predictions

---

## 🔮 Future Enhancements

* 📊 Add interactive charts (Plotly / Chart.js)
* 📚 Multi-variable model (attendance, past scores)
* 🤖 Upgrade to advanced models (Random Forest, XGBoost)
* 🌐 Deploy on cloud (Render / AWS / Vercel)

---

## 💼 Why This Project Matters

This project proves you can:

👉 Build **ML models**
👉 Deploy them in **real applications**
👉 Think in terms of **business impact**

That’s exactly what recruiters look for.

---

## 🤝 Contributing

Contributions are welcome! Fork → Improve → PR 🚀

---

## 📜 License

MIT License

---

## 👨‍💻 Author

**Tanmay Kshirsagar**
💼 Data Science | ML Engineering | Full Stack

---
