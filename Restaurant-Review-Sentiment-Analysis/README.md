# 🍴 Restaurant Review Sentiment Analysis

An end-to-end **Natural Language Processing (NLP)** pipeline designed to classify customer feedback with high precision. This project transforms raw text data into actionable insights, helping restaurant owners understand customer satisfaction at scale.

---

## 🚀 Key Features

* **Advanced Text Preprocessing:** Includes noise reduction, stopword removal, and Porter Stemming to normalize linguistic variations.
* **Dual Vectorization:** Implements both **Bag-of-Words (BoW)** and **TF-IDF** (Term Frequency-Inverse Document Frequency) for comparative feature engineering.
* **Extensive Model Zoo:** Benchmarks **9+ Machine Learning algorithms**, ranging from classical statistical models to modern boosting frameworks:
* Linear & Non-linear: Logistic Regression, SVM (Linear/RBF), KNN.
* Tree-based: Decision Trees, Random Forest.
* Boosting: Gradient Boosting, **XGBoost**, **LightGBM**.


* **Robust Evaluation:** Comprehensive metrics including F1-Score, ROC-AUC, and Confusion Matrices to ensure model reliability.

---

## 📊 Dataset Overview

The project utilizes the `Restaurant_Reviews.tsv` dataset, containing **1,000 curated reviews**.

| Feature | Description |
| --- | --- |
| **Review** | Raw text feedback from customers. |
| **Liked** | Binary label: `1` (Positive) |
| **Scalability** | Architecture is compatible with larger datasets like Yelp, IMDb, or Amazon Reviews. |

---

## 🛠️ Installation & Setup

Get the environment up and running in minutes:

```bash
# 1. Clone the repository
git clone https://github.com/your-username/Restaurant-Review-Sentiment-Analysis.git
cd Restaurant-Review-Sentiment-Analysis

# 2. Create and activate a clean virtual environment
conda create -n nlp_env python=3.12 -y
conda activate nlp_env

# 3. Install dependencies
pip install -r requirements.txt

```

---

## 📈 Methodology

1. **Data Cleaning:** HTML tags, special characters, and numbers are removed.
2. **Tokenization:** Breaking down sentences into individual words.
3. **Vectorization:** Converting text into numerical matrices using  weighting:


4. **Training & Tuning:** Hyperparameter optimization via Cross-Validation.
5. **Validation:** Plotting ROC Curves to visualize the Trade-off between Sensitivity and Specificity.

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---
