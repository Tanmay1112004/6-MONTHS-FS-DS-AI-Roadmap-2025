# Adult Census Income Prediction — ML Case Study

## 📌 Overview
This project predicts whether an individual's annual income exceeds $50K using demographic and employment attributes from the **UCI Adult Census dataset**.  
It demonstrates a complete **supervised machine learning workflow**: from data preprocessing to model evaluation and interpretability.

## 🎯 Objectives
- Load and preprocess the UCI Adult dataset.
- Perform **Exploratory Data Analysis (EDA)** with visualizations.
- Build and evaluate two supervised models:
  - Logistic Regression
  - Naive Bayes (Multinomial)
- Compare performance using **ROC-AUC**, **Precision**, **Recall**, and **F1-score**.
- Interpret the best model’s features to understand income drivers.

## 🗂 Dataset
- **Source:** [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml/datasets/Adult)
- **Target Variable:** `income` (`<=50K` or `>50K`)

## ⚙️ Tech Stack
- **Language:** Python 3.x
- **Libraries:** pandas, numpy, matplotlib, scikit-learn, seaborn

## 📊 Project Workflow
1. **Data Loading & Cleaning** — Handle missing values, clean labels.
2. **EDA** — Visualize distributions and relationships.
3. **Feature Engineering** — One-hot encoding, scaling.
4. **Model Training** — Logistic Regression, Naive Bayes with cross-validation.
5. **Model Evaluation** — Classification metrics, ROC, PR curves.
6. **Interpretability** — Coefficient analysis for Logistic Regression.

## 📈 Results
- Logistic Regression: Balanced performance, strong interpretability.
- Naive Bayes: Faster but less effective for numeric-heavy features.
- Key predictors: `capital_gain`, `education_num`, `marital_status`, `hours_per_week`.

## 🚀 How to Run
```bash
# Clone the repository
git clone https://github.com/<your-username>/adult-census-income-prediction.git
cd adult-census-income-prediction

# Install dependencies
pip install -r requirements.txt

# Run the Jupyter notebook
jupyter notebook adult_income_case_study.ipynb
