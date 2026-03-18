## 💼 Adult Census Income Prediction — Professional README (Recruiter-Ready)

![Image](https://media.licdn.com/dms/image/v2/D4D12AQGs8wSD3XtmBg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1719446346476?e=2147483647\&t=k8pwuaAXHNkBoHKn6nDi3kx22lGfypEXOw7sVdIspAQ\&v=beta)

![Image](https://www.researchgate.net/publication/379372174/figure/fig7/AS%3A11431281275870975%401725501512704/The-domain-binary-classification-ROC-curve-plot-using-LSTM-logistic-regression-and.png)

![Image](https://www.researchgate.net/publication/360685654/figure/fig2/AS%3A1157135224307712%401652893944181/Feature-importance-bar-charts-for-several-machine-learning-algorithms.png)

![Image](https://www.researchgate.net/publication/345377656/figure/fig3/AS%3A993853305790466%401613964501902/A-bar-graph-showing-the-feature-importance-of-the-aggregated-feature-set.ppm)

# 📊 Adult Census Income Prediction

### Binary Classification Case Study | Machine Learning • Statistics • Interpretability

An end-to-end machine learning project that predicts whether an individual earns **>50K or ≤50K annually** using demographic and socioeconomic attributes from the Adult Census dataset.

> ⭐ Strong portfolio project demonstrating data preprocessing, EDA, classical ML modeling, and business-driven insights

---

## 📌 Business Problem & Context

Governments, financial institutions, and enterprises rely on income prediction to design policies, assess credit risk, and target services effectively.

This project builds a predictive system to classify individuals into income brackets while answering a key question:

👉 **Which factors most strongly influence high income?**

Key objectives:

* Predict income category accurately
* Identify major socioeconomic drivers
* Maintain model interpretability for decision-making

---

## 🧠 Dataset Overview

* 📂 Source: UCI Adult Census Dataset
* 👥 Records: ~48,000 individuals
* 🧾 Features: Demographic + employment attributes
* 🎯 Target: Income category (≤50K / >50K)

**Feature examples:**

* Age
* Education level
* Occupation
* Work hours per week
* Marital status
* Capital gain / loss

---

## 🛠️ Technical Stack

### 🔹 Programming & Data

* 🐍 Python 3.x
* 📊 Pandas, NumPy

### 🔹 Modeling & Evaluation

* 🧠 Scikit-Learn

  * Logistic Regression
  * Multinomial Naive Bayes
  * Classification metrics

### 🔹 Visualization

* 📈 Matplotlib
* 🎨 Seaborn

---

## 🔬 Methodology & Workflow

### 1️⃣ Data Engineering & Preprocessing

* Missing values (`?`) imputed using statistical modes
* One-Hot Encoding applied to categorical variables
* Numerical features standardized for model stability
* Target labels encoded into binary numeric format

---

### 2️⃣ Exploratory Data Analysis (EDA)

Multivariate analysis performed to uncover patterns.

Key observations:

* 📚 Higher education strongly correlates with higher income
* 💰 Capital gain shows extreme skewness
* 👴 Age demonstrates nonlinear relationship with income
* 🏢 Occupation and marital status significantly impact earnings

---

### 3️⃣ Model Development & Evaluation

Two baseline models implemented to compare performance:

| Metric   | Logistic Regression | Naive Bayes |
| -------- | ------------------- | ----------- |
| Accuracy | XX%                 | XX%         |
| F1-Score | X.XX                | X.XX        |
| ROC-AUC  | X.XX                | X.XX        |

👉 Logistic Regression performed better in capturing complex relationships across encoded features.

---

## 📈 Key Insights & Findings

* 🥇 **Top Predictors:** Capital Gain, Age, Education-Num
* 📊 Logistic Regression delivered superior ROC-AUC
* 🔍 Model coefficients provide interpretable relationships
* 🎯 Education level significantly increases probability of high income

---

## 🏗️ Modeling Pipeline

```text
Raw Data
   │
   ▼
Cleaning & Imputation
   │
   ▼
Encoding + Scaling
   │
   ▼
Train/Test Split
   │
   ▼
Model Training
   │
   ▼
Evaluation Metrics
   │
   ▼
Interpretation & Insights
```

---

## 📂 Repository Structure

```text
adult-census-income-prediction/
│
├── 📓 adult_income_case_study.ipynb   # Full analysis & modeling
├── 🧠 final_model_weights.pkl         # Saved model (optional)
├── 📋 requirements.txt
└── 📖 README.md
```

---

## ⚡ Installation & Execution

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/adult-census-income-prediction.git
cd adult-census-income-prediction
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Notebook

```bash
jupyter notebook adult_income_case_study.ipynb
```

---

## 🎯 Skills Demonstrated

This project showcases:

* Data cleaning & preprocessing
* Exploratory Data Analysis
* Feature engineering
* Classical machine learning
* Model evaluation techniques
* Interpretability for business use
* End-to-end DS workflow

---

## 💼 Real-World Applications

* Credit scoring & loan approval
* Targeted marketing
* Workforce analytics
* Public policy planning
* Socioeconomic research

---

## 👨‍💻 Author

**Tanmay Kshirsagar**
Final Year Computer Engineering Student

Interested in AI, Machine Learning, Data Science, and Analytics.

---

## 🤝 Opportunities & Collaboration

Open to:

* 💼 Internships
* 📊 Data Science roles
* 🧪 Research projects
* 🤖 AI/ML collaborations

⭐ If you found this useful, consider giving the repository a star!

---

## 📜 License

MIT License — Free for academic and personal use.

---

