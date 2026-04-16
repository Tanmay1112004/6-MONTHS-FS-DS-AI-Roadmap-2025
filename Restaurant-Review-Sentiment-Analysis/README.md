# 🍴 Restaurant Review Sentiment Analysis — NLP for Business Intelligence

<p align="center">
  <b>Transform customer reviews into actionable insights using Machine Learning & NLP</b><br>
  End-to-end sentiment classification system with multi-model benchmarking
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/NLP-NLTK-green?style=flat-square"/>
  <img src="https://img.shields.io/badge/ML-Scikit--learn-orange?style=flat-square"/>
  <img src="https://img.shields.io/badge/Boosting-XGBoost%20%7C%20LightGBM-yellow?style=flat-square"/>
  <img src="https://img.shields.io/badge/Focus-Sentiment%20Analysis-brightgreen?style=flat-square"/>
</p>

---

## 💡 What This Project Does

Customer reviews are gold — but only if you can **understand them at scale**.

👉 This project converts raw text reviews into:

* 📊 Sentiment classifications
* 📈 Model-driven insights
* 🧠 Actionable business intelligence

---

## 🚨 Problem Statement

Businesses receive thousands of reviews.

Challenges:

* Hard to manually analyze
* Hidden patterns in text
* Delayed response to negative feedback

👉 Result: Missed opportunities & poor customer experience

---

## 🎯 Solution

A scalable **NLP-based sentiment analysis pipeline** that:

✅ Cleans and processes raw text
✅ Converts text → numerical features
✅ Trains and compares multiple ML models
✅ Identifies the best-performing approach

---

## ⚡ Key Features

### 🧹 Advanced Text Preprocessing

* HTML & noise removal
* Stopword filtering
* Porter stemming
* Lowercase normalization

### 🔄 Dual Feature Engineering

* Bag-of-Words (BoW)
* TF-IDF vectorization
  👉 Enables performance comparison

### 🧠 Multi-Model Benchmarking

* 9+ ML algorithms tested
* Consistent evaluation framework

### 📊 Performance Evaluation

* Accuracy, Precision, Recall
* F1 Score, ROC-AUC
* Confusion Matrix analysis

---

## 🧠 Why This Project Stands Out (Recruiter POV)

Most NLP projects:
👉 Train one model and stop

This project:

✅ Compares multiple algorithms
✅ Applies proper evaluation metrics
✅ Shows understanding of **model trade-offs**
✅ Demonstrates scalable pipeline thinking

👉 Translation: *You think like a data scientist, not just a coder.*

---

## 🧬 Methodology

```id="method55"
Raw Reviews
   │
   ▼
Text Cleaning & Preprocessing
   │
   ▼
Tokenization
   │
   ▼
Vectorization (BoW / TF-IDF)
   │
   ▼
Model Training (9+ Models)
   │
   ▼
Evaluation & Comparison
   │
   ▼
Best Model Selection
```

---

## 📊 Models Used

### 📈 Linear & Distance-Based

* Logistic Regression
* Support Vector Machine (Linear & RBF)
* K-Nearest Neighbors

### 🌳 Tree-Based

* Decision Tree
* Random Forest

### 🚀 Boosting Models

* Gradient Boosting
* XGBoost
* LightGBM

---

## 📂 Dataset Overview

* **File**: `Restaurant_Reviews.tsv`
* **Size**: 1,000 labeled reviews

| Column | Description                            |
| ------ | -------------------------------------- |
| Review | Customer feedback text                 |
| Liked  | Sentiment (1 = Positive, 0 = Negative) |

👉 Easily scalable to real-world datasets (Yelp, Amazon, IMDb)

---

## 🛠 Tech Stack

| Layer         | Tools             |
| ------------- | ----------------- |
| Programming   | Python            |
| NLP           | NLTK              |
| ML            | Scikit-learn      |
| Boosting      | XGBoost, LightGBM |
| Data Handling | Pandas            |
| Visualization | Matplotlib        |

---

## 🚀 Setup & Run

```bash id="run55"
git clone https://github.com/Tanmay1112004/Restaurant-Review-Sentiment-Analysis.git
cd Restaurant-Review-Sentiment-Analysis
conda create -n nlp_env python=3.12 -y
conda activate nlp_env
pip install -r requirements.txt
```

---

## 📈 Key Outcomes

* Identified best-performing model across multiple algorithms
* Demonstrated impact of feature engineering (BoW vs TF-IDF)
* Built a reusable NLP pipeline
* Validated results using multiple evaluation metrics

---

## 💼 Business Impact

This system enables businesses to:

* Detect negative feedback early
* Improve service quality
* Identify recurring issues
* Enhance customer satisfaction

👉 Text → Insight → Action

---

## 🔮 Future Enhancements

* [ ] Deep learning models (LSTM / BERT)
* [ ] Real-time sentiment API
* [ ] Dashboard visualization
* [ ] Multi-language support
* [ ] Deployment on cloud

---

## 🤝 Contributing

```bash id="contri55"
git checkout -b feature/improvement
git commit -m "Improvement added"
git push origin feature/improvement
```

---

## ⭐ Support

If this project helped you:

* ⭐ Star the repo
* 🍴 Fork it
* 🚀 Share it

---

## 👨‍💻 Developer Mindset

**From raw text → structured insight → business value**

---

## 🔥 Final Thought

Data is everywhere.

👉 The real skill is turning it into decisions.

---

<p align="center">
  🍴 <b>Listen to your customers. At scale.</b>
</p>
