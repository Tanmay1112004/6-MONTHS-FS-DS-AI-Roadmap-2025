# 🍴 Restaurant Review Sentiment Analysis 🤖

This repository contains an **end-to-end NLP pipeline** for analyzing restaurant reviews and predicting customer sentiment (**positive / negative**).

## 🚀 Features
- ✅ Text preprocessing (cleaning, stopwords removal, stemming)
- ✅ Feature extraction with **Bag-of-Words (BOW)** and **TF-IDF**
- ✅ Multiple classifiers:
  - Logistic Regression
  - Naive Bayes
  - SVM (Linear & RBF)
  - KNN
  - Decision Tree
  - Random Forest
  - Gradient Boosting
  - **XGBoost**
  - **LightGBM**
- ✅ Model evaluation with:
  - Accuracy, Precision, Recall, F1-score
  - ROC-AUC
  - Confusion Matrix & ROC Curves
- ✅ Cross-validation for robust performance comparison

---

## 📊 Dataset
- **Restaurant_Reviews.tsv**  
- 1000 restaurant reviews labeled as **Liked (1) / Not Liked (0)**.  
- Can be scaled to larger datasets (IMDb, Yelp, Amazon Reviews).

---

## 🛠️ Installation
```bash
# Clone repo
git clone https://github.com/your-username/Restaurant-Review-Sentiment-Analysis.git
cd Restaurant-Review-Sentiment-Analysis

# Create env (optional but recommended)
conda create -n nlp_env python=3.12 -y
conda activate nlp_env

# Install requirements
pip install -r requirements.txt
