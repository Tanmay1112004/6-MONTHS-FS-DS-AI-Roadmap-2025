# 📊 PCA + Logistic Regression on the Adult Dataset

This repository demonstrates **Principal Component Analysis (PCA)** — the most popular dimensionality reduction technique — applied to the **UCI Adult dataset**.  
We then train a **Logistic Regression** model on the transformed features and analyze performance.

---

## 🚀 Project Overview
- **Dataset:** [UCI Adult Dataset](https://archive.ics.uci.edu/ml/datasets/adult)
- **Goal:** Reduce dataset dimensions using PCA while retaining 90% variance.
- **Model:** Logistic Regression
- **Key Finding:** Maximum accuracy of **0.8227** achieved using the first **12 principal components**.

---

## 📂 Repository Structure
├── data/ # Dataset files
├── notebooks/ # Jupyter Notebook implementation
├── src/ # Python scripts
├── plots/ # Generated visualizations
├── README.md # Project documentation
└── requirements.txt # Dependencies



---

## 📈 Results
- **Number of dimensions to preserve 90% variance:** `12`
- **Accuracy with first 12 components:** `0.8227`
- **Explained variance plot** confirms ~90% variance captured by first 12 PCs.

![Explained Variance Plot](plots/explained_variance.png)

---
## 📈 Results
- **Number of dimensions to preserve 90% variance:** `12`
- **Accuracy with first 12 components:** `0.8227`
- **Explained variance plot** confirms ~90% variance captured by first 12 PCs.

## ⚙️ Installation & Usage
# Clone the repository
git clone https://github.com/<your-username>/pca-logistic-regression-adult-dataset.git
cd pca-logistic-regression-adult-dataset

# Install dependencies
pip install -r requirements.txt

# Run the notebook
jupyter notebook notebooks/pca_logistic_regression.ipynb

📊 PCA Explained Variance Plot
The plot shows the cumulative variance explained by each principal component, with a marker at 12 components where we hit 90% variance.

🛠 Tech Stack
Python 3.x

Pandas, NumPy

Scikit-learn

Matplotlib

Jupyter Notebook

🤝 Contributing
Pull requests are welcome!
For major changes, please open an issue first to discuss what you’d like to change.



