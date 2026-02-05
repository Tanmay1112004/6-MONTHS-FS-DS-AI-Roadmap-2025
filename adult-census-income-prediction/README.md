# Adult Census Income Prediction: Binary Classification Case Study

## 📌 Business Problem & Context

Understanding the socioeconomic factors that drive income levels is critical for policy-making and targeted marketing. This project develops a predictive model to classify individuals into two income brackets ( vs. ) using the **UCI Adult Census Dataset**.

The primary goal is to identify the most significant predictors of high-income earners while maintaining a balance between **model interpretability** and **predictive accuracy**.

---

## 🛠️ Technical Stack

* **Core:** `Python 3.x`
* **Data Manipulation:** `Pandas`, `NumPy`
* **Modeling & Metrics:** `Scikit-Learn` (Logistic Regression, Multinomial Naive Bayes)
* **Visualization:** `Matplotlib`, `Seaborn`

---

## 📊 Methodology & Workflow

The project follows a standard Data Science Lifecycle:

### 1. Data Engineering & Preprocessing

* **Imputation:** Handled missing values (marked as `?` in the dataset) using statistical modes.
* **Feature Transformation:** Applied **One-Hot Encoding** to categorical variables and **Standard Scaling** to numerical features to ensure convergence for Logistic Regression.
* **Target Encoding:** Transformed binary labels into numeric format for model consumption.

### 2. Exploratory Data Analysis (EDA)

Performed multivariate analysis to identify feature correlations.

* **Observation:** Significant correlation found between `Education-Num` and `Income`.
* **Observation:** High variance in `Capital-Gain` indicated the need for robust scaling.

### 3. Model Development & Evaluation

I implemented and compared two distinct algorithms to evaluate the trade-off between speed and performance:

| Metric | Logistic Regression | Naive Bayes |
| --- | --- | --- |
| **Accuracy** | *Insert Value*% | *Insert Value*% |
| **F1-Score** | *Insert Value* | *Insert Value* |
| **ROC-AUC** | *Insert Value* | *Insert Value* |

---

## 📈 Key Insights & Results

* **Top Predictors:** `Capital-Gain`, `Age`, and `Education-Num` were the strongest positive drivers of income.
* **Model Performance:** Logistic Regression outperformed Naive Bayes in this high-dimensional space, providing a more reliable **ROC-AUC** curve.
* **Interpretability:** By analyzing the model coefficients, we can quantify how a unit increase in education level significantly raises the probability of earning .

---

## 📂 Repository Structure

```text
├── 📓 adult_income_case_study.ipynb  # Comprehensive analysis & modeling
├── 🧠 final_model_weights.pkl        # (Optional) Saved model weights
├── 📋 requirements.txt               # Environment dependencies
└── 📖 README.md                      # Project documentation

```

---

## 🚀 Installation & Execution

1. **Clone the Repo:**
```bash
git clone https://github.com/<your-username>/adult-census-income-prediction.git

```


2. **Setup Environment:**
```bash
pip install -r requirements.txt

```


3. **Run Analysis:**
Launch the Jupyter notebook to view the step-by-step implementation:
```bash
jupyter notebook adult_income_case_study.ipynb

```
