# 🧠 Text Summarization App (spaCy + Streamlit)

A fast, lightweight **extractive text summarization** app built with **spaCy** and **Streamlit**. Designed for clean demos, NLP fundamentals, and portfolio showcase — paste text or upload documents to generate concise summaries instantly.

---

## 🚀 Overview

This project implements a **classical extractive summarization pipeline** using word-frequency scoring and sentence ranking. It prioritizes **clarity, explainability, and performance**, making it ideal for interviews, demos, and learning NLP basics.

---

## ✨ Features

* Extractive summarization using spaCy (`en_core_web_sm`)
* Interactive Streamlit UI with summary length control
* Sentence & token analysis
* Clean, modular, extensible codebase
* Fast execution (no heavy ML models)

---

## 🧠 How It Works

1. Tokenize text using spaCy
2. Compute normalized word frequencies (excluding stopwords)
3. Score sentences based on token importance
4. Select top-K sentences and return them in order

---

## 🛠️ Tech Stack

* **Python**
* **spaCy**
* **Streamlit**

Optional: `pdfplumber`, `python-docx`, `pytesseract`

---

## ▶️ Run Locally

```bash
pip install streamlit spacy
python -m spacy download en_core_web_sm
streamlit run text_summarizer_app.py
```

---

## 🔮 Roadmap

* PDF / DOCX support
* OCR for scanned documents
* Abstractive summarization (BART / T5)
* Docker & CI pipeline

---

## 📝 License

MIT License

---

## 👤 Author

**Tanmay**

---
