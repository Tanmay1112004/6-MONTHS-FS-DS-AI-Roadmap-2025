# 🧠 Text Summarization App — Fast, Explainable NLP

<p align="center">
  <b>Summarize long text instantly using classical NLP (no heavy models required)</b><br>
  Built with spaCy + Streamlit for speed, clarity, and real-world usability
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/NLP-spaCy-green?style=flat-square"/>
  <img src="https://img.shields.io/badge/UI-Streamlit-red?style=flat-square"/>
  <img src="https://img.shields.io/badge/Type-Extractive%20Summarization-orange?style=flat-square"/>
</p>

---

## 💡 What This Project Does

In a world of heavy AI models, this app proves:

👉 You don’t always need deep learning to build useful NLP products.

Paste any text → Get a **clean, concise summary in seconds**

---

## Demo Images 

![demo](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/text%20summarization%20using%20spacy/screenshots/Screenshot%202025-08-23%20150706.png)

![demo]()

![demo]()

![demo]()

---

## 🚨 Problem Statement

People deal with:

* Long articles
* Reports
* Documents

👉 Reading everything is time-consuming.

Most solutions:

* Require large models
* Are slow or expensive
* Lack transparency

---

## 🎯 Solution

A **lightweight extractive summarization system** that:

✅ Works instantly
✅ Requires no GPU
✅ Is fully explainable
✅ Maintains original meaning

---

## ⚡ Key Features

### 🧠 Extractive Summarization

* Sentence ranking using word-frequency scoring
* Keeps original sentences (no hallucination risk)

### ⚡ High Performance

* Runs in milliseconds
* No heavy ML models required

### 🎛️ User Control

* Adjustable summary length
* Flexible input handling

### 💻 Interactive UI

* Built with Streamlit
* Clean and minimal user experience

---

## 🧠 Why This Project Stands Out (Recruiter POV)

Most NLP projects:
👉 Use APIs or pre-trained transformers blindly

This one:

✅ Implements core NLP logic from scratch
✅ Shows understanding of tokenization & scoring
✅ Focuses on performance + explainability
✅ Built as a usable product

👉 Translation: *You understand fundamentals, not just tools.*

---

## 🔬 How It Works

### Core Idea:

Important words → Important sentences → Best summary

---

### ⚙️ Pipeline

1. **Text Processing**

   * Tokenization using spaCy
   * Stopword removal

2. **Word Scoring**

   * Compute normalized word frequencies

3. **Sentence Ranking**

   * Score sentences based on important words

4. **Summary Generation**

   * Select Top-K sentences
   * Preserve original order

---

## 🏗️ System Flow

```id="flow99"
Input Text
   │
   ▼
spaCy Tokenization
   │
   ▼
Word Frequency Scoring
   │
   ▼
Sentence Ranking
   │
   ▼
Top-K Sentences
   │
   ▼
Final Summary Output
```

---

## 🛠 Tech Stack

| Layer       | Technology               |
| ----------- | ------------------------ |
| Programming | Python                   |
| NLP Engine  | spaCy (`en_core_web_sm`) |
| Frontend    | Streamlit                |

---

## 🚀 Quick Start

```bash id="run88"
pip install streamlit spacy
python -m spacy download en_core_web_sm
streamlit run text_summarizer_app.py
```

👉 Open: `http://localhost:8501`

---

## 📈 Performance Highlights

* ⚡ Near-instant summarization
* 🧠 No external API dependency
* 💻 Runs on low-end systems

---

## 🎓 What This Project Demonstrates

* NLP fundamentals (tokenization, frequency analysis)
* Algorithmic thinking
* Lightweight system design
* Building ML-powered web apps
* Product-focused development

---

## 🔮 Future Enhancements

* [ ] PDF / DOCX support
* [ ] OCR for scanned documents
* [ ] Abstractive summarization (BART / T5)
* [ ] Multi-language support
* [ ] REST API deployment

---

## 🤝 Contributing

```bash id="contri88"
git checkout -b feature/improvement
git commit -m "Enhancement added"
git push origin feature/improvement
```

---

## 👨‍💻 About the Developer

**Tanmay**

Building at the intersection of:
👉 NLP • AI • Data • Products

---

## ⭐ Support

If you found this useful:

* ⭐ Star the repo
* 🍴 Fork it
* 🚀 Share it

---

## 🔥 Final Thought

Big models are powerful.

👉 But simple, fast, and explainable systems win in real-world use cases.

---

<p align="center">
  🧠 <b>Summarize Smarter. Read Faster.</b>
</p>
