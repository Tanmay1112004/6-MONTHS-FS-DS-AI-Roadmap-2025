# 📊 PCA + Logistic Regression: Adult Dataset Analysis

This repository explores **Principal Component Analysis (PCA)**—the gold standard for dimensionality reduction—applied to the **UCI Adult Income Dataset**. By compressing high-dimensional data into its most informative components, we demonstrate how to maintain high predictive accuracy while streamlining model complexity.

---

## 🚀 Project Overview

The objective of this project is to predict whether an individual's income exceeds $50K/yr based on census data. We leverage PCA to reduce noise and redundancy before feeding the data into a classification model.

* **Dataset:** [UCI Adult Dataset](https://archive.ics.uci.edu/ml/datasets/adult) (Census Income)
* **Dimensionality Reduction:** PCA (Principal Component Analysis)
* **Classification:** Logistic Regression
* **Key Achievement:** Retained **90% variance** and achieved **0.8227 accuracy** using only **12 principal components**.

---

## 📂 Repository Structure

```text
├── data/           # Raw and processed census data
├── notebooks/      # Step-by-step Jupyter Notebook implementation
├── src/            # Modular Python scripts for preprocessing and modeling
├── plots/          # Visualizations (Scree plots, Confusion Matrices)
├── README.md       # Project documentation
└── requirements.txt # Environment dependencies

```

---

## 📈 Key Results & Insights

Using PCA, we successfully compressed the feature space while keeping the model's predictive power intact.

| Metric | Result |
| --- | --- |
| **Components for 90% Variance** | 12 |
| **Logistic Regression Accuracy** | 82.27% |
| **Feature Reduction Ratio** | ~1:3 (depending on encoding) |

### Variance Analysis

The **Explained Variance Plot** (found in `/plots`) illustrates the "elbow" where adding more components yields diminishing returns. We hit our 90% information threshold at exactly 12 components, significantly reducing the computational load for the Logistic Regression model.

---

## 🛠 Tech Stack

* **Language:** Python 3.x
* **Data Manipulation:** `Pandas`, `NumPy`
* **Machine Learning:** `Scikit-learn`
* **Visualization:** `Matplotlib`, `Seaborn`
* **Environment:** `Jupyter Notebook`

---

## ⚙️ Installation & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/pca-logistic-regression-adult-dataset.git
cd pca-logistic-regression-adult-dataset

```

### 2. Set Up Environment

```bash
pip install -r requirements.txt

```

### 3. Run the Analysis

Launch the notebook to see the data cleaning, PCA transformation, and model evaluation in action:

```bash
jupyter notebook notebooks/pca_logistic_regression.ipynb

```

---

## 🤝 Contributing

Contributions make the open-source community an amazing place to learn and create.

1. **Fork** the Project
2. **Create** your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your Changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the Branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

