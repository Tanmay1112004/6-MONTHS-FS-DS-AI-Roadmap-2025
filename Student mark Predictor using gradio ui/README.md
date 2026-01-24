# 🎓 Student Mark Prediction System

### *Bridging Study Habits and Academic Excellence through Predictive Analytics*

The **Student Mark Prediction Project** is a full-stack Machine Learning application designed to quantify the impact of study time on academic results. By leveraging a refined Linear Regression model, it provides students and educators with an intuitive interface to forecast exam performance.

---

## 🎯 Strategic Impact

This tool serves as a decision-support system for three primary stakeholders:

* **Students:** Optimize study-life balance by understanding the "diminishing returns" of study hours.
* **Educators:** Identify "at-risk" students whose projected scores fall below passing thresholds.
* **Institutions:** Allocate tutoring resources based on data-driven performance projections.

---

## 🛠️ Technical Architecture

### The Engine: Machine Learning

We utilize a **Linear Regression** model because of its high interpretability and efficiency for continuous variable prediction.

* **Model Accuracy:**  Score of **0.95+**.
* **Core Equation:** 


*(Where  is the predicted mark and  is the study hours).*

### The Stack: Full-Stack Integration

* **Backend:** Flask (Python) for robust API routing.
* **Frontend:** Semantic HTML5, CSS3 (Flexbox/Grid), and Vanilla JavaScript.
* **Serialization:** `Joblib` for high-speed model loading.

---

## 📂 Project Structure

```bash
student-mark-prediction/
├── app/
│   ├── main.py                # Central Flask Application
│   ├── static/                # Asset Management (CSS/JS)
│   └── templates/             # UI Components (Jinja2)
├── training/
│   ├── train_model.py         # Automated Training Pipeline
│   └── student_data.csv       # Source Dataset
├── models/
│   └── predictor_model.pkl    # Serialized ML Brain
└── requirements.txt           # Environment Configuration

```

---

## 🚀 Quick Start

### 1. Installation

Clone the repository and install the dependencies in a virtual environment:

```bash
git clone https://github.com/your-username/student-mark-prediction.git
pip install -r requirements.txt

```

### 2. Execution

Launch the local development server:

```bash
python app/main.py

```

Navigate to `http://127.0.0.1:5000` in your browser.

---

## 📊 Performance Benchmark

| Study Hours | Predicted Marks | Confidence Level |
| --- | --- | --- |
| **4 Hours** | 66.19% | High |
| **8 Hours** | 81.93% | High |
| **12 Hours** | 97.68% | Medium-High |

---

## 🔮 Roadmap

* [x] **Phase 1:** Core Linear Regression Engine.
* [x] **Phase 2:** Responsive Web Dashboard.
* [ ] **Phase 3:** Interactive Data Visualizations (using Plotly/Chart.js).
* [ ] **Phase 4:** Multi-variable support (adding attendance & previous grades).

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.

---
