# 🍴 Restaurant Review Sentiment Analysis

> Turning raw customer feedback into data-driven business intelligence using NLP & Machine Learning.

An end-to-end **Natural Language Processing pipeline** designed to classify restaurant reviews as positive or negative with high precision and strong generalization capability.

---

## 🖼️ Project Visuals

### 📊 Model Performance Comparison


---

## 🚀 Key Features

### 🧹 Advanced Text Preprocessing

* Noise removal (HTML tags, special characters, numbers)
* Stopword filtering
* Porter Stemming
* Lowercasing normalization

### 📊 Dual Vectorization Strategy

* **Bag-of-Words (BoW)**
* **TF-IDF (Term Frequency–Inverse Document Frequency)**

Comparative analysis to evaluate feature engineering impact.

---

## 🧠 Model Benchmarking (9+ Algorithms)

### 📈 Linear & Distance-Based Models

* Logistic Regression
* Support Vector Machine (Linear / RBF)
* K-Nearest Neighbors

### 🌳 Tree-Based Models

* Decision Tree
* Random Forest

### 🚀 Boosting Frameworks

* Gradient Boosting
* XGBoost
* LightGBM

Each model was evaluated using consistent cross-validation protocols.

---

## 📊 Dataset Overview

The project uses `Restaurant_Reviews.tsv` containing **1,000 labeled reviews**.

| Column | Description                                   |
| ------ | --------------------------------------------- |
| Review | Customer text feedback                        |
| Liked  | Binary sentiment (1 = Positive, 0 = Negative) |

The architecture is scalable to larger datasets like Yelp, IMDb, or Amazon Reviews.

---

## 📈 Methodology

1️⃣ **Data Cleaning**
Remove noise and normalize text.

2️⃣ **Tokenization**
Split text into meaningful word units.

3️⃣ **Vectorization**
Convert text into numerical representation using BoW & TF-IDF.

4️⃣ **Model Training & Hyperparameter Tuning**
Grid Search with Cross-Validation.

5️⃣ **Evaluation Metrics**

* Accuracy
* Precision
* Recall
* F1-Score
* ROC-AUC
* Confusion Matrix

---

## 🎯 Key Outcomes

* Compared traditional ML vs boosting methods
* Identified optimal feature-model combinations
* Validated model robustness using ROC curves
* Built scalable NLP pipeline architecture

---

## 🛠️ Installation & Setup

```bash id="2nt8hz"
git clone https://github.com/Tanmay1112004/Restaurant-Review-Sentiment-Analysis.git
cd Restaurant-Review-Sentiment-Analysis
conda create -n nlp_env python=3.12 -y
conda activate nlp_env
pip install -r requirements.txt
```

---

## 🧰 Tech Stack

* Python 3.12
* Scikit-learn
* XGBoost
* LightGBM
* NLTK
* Pandas
* Matplotlib / Seaborn

---

## 💡 Business Impact

This project demonstrates how restaurants can:

* Detect dissatisfaction early
* Improve service quality
* Identify recurring complaints
* Enhance customer retention strategies

Text → Insights → Strategy.

---

## 📜 License

MIT License.

---
