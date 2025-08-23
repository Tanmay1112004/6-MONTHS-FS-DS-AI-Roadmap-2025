# Text Summarization using spacy

 Extractive text summarization using spaCy (en\_core\_web\_sm) with a clean Streamlit frontend. Fast, lightweight, and perfect for demos — paste text or upload documents to get concise summaries.

---

## 🚀 Project Overview

This repository implements an **extractive text summarization** pipeline using spaCy for NLP and Streamlit for the frontend. The summarizer scores sentences by normalized word-frequency (excluding stopwords and punctuation), then selects the top N sentences to form a concise summary. The app is designed for easy demos and quick local use.

**Why this repo exists:** to provide a minimal, production-minded demo that showcases classical extractive summarization, with clear extension points for OCR/PDF input, abstractive models, or deployment.

---

## ✨ Key Features

* Extractive summarization using spaCy (`en_core_web_sm`).
* Streamlit UI with adjustable summary length slider.
* Token and sentence analysis (counts + coverage).
* Clean, single-file starter app (easy to extend).
* Instructions for local setup and deployment.

---

## 📦 Repo Structure (suggested)

```
extractive-summarizer-spacy-streamlit/
├─ README.md
├─ requirements.txt
├─ text_summarizer_app.py       # Streamlit app
├─ summarizer/                  # optional module for cleaner code
│  ├─ __init__.py
│  ├─ core.py                   # summarization logic
│  └─ utils.py                  # helpers (PDF/Docx loaders, OCR later)
├─ tests/
│  └─ test_summarizer.py
└─ examples/
   └─ sample_texts.txt
```

---

## 🛠️ Setup & Installation

1. Create virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate     # Windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
# or
pip install streamlit spacy
python -m spacy download en_core_web_sm
```

**requirements.txt (suggested)**

```
streamlit
spacy
pdfplumber     # optional, for PDF text extraction
python-docx     # optional, for .docx support
pytesseract     # optional, for OCR (requires Tesseract installation)
```

---

## ▶️ Run the App

```bash
streamlit run text_summarizer_app.py
```

Open the shown local URL (usually `http://localhost:8501`) — paste text or upload a file and click **Summarize**.

---

## 🧠 How it Works (short)

1. Load text into spaCy `nlp` pipeline.
2. Build frequency dictionary for non-stopword, non-punctuation tokens.
3. Normalize frequencies by the maximum frequency.
4. Score each sentence by summing normalized frequencies of its words.
5. Pick top-k sentences (k based on user-selected ratio) and return them in original order.

---

## ✅ Example Usage (Python function)

```python
from summarizer.core import text_summarizer

text = open('examples/sample_texts.txt').read()
summary, doc, scores = text_summarizer(text, summary_ratio=0.3)
print(summary)
```

---

## 🔧 Extensions & Roadmap

* Add file upload support (PDF / DOCX) using `pdfplumber` and `python-docx`.
* Integrate OCR for scanned PDFs with `pytesseract` and `pdf2image`.
* Add unit tests and GitHub Actions for CI.
* Add an abstractive option (Hugging Face transformers: BART / T5) for smoother, human-like summaries.
* Containerize with Docker and add a simple deployment guide.

---

## 🤝 Contributing

Contributions welcome! Fork, create a feature branch, and send a PR. Keep changes small and focused. Add tests for any new logic.

---

## 📝 License

MIT License — feel free to use this for demos and learning. If you ship publicly, consider attribution.

---

## Contact

Maintainer: Tanmay (you can update this section with your contact/LinkedIn/GitHub links)

---

*P.S. Need me to scaffold the repo with code files, unit tests, and a GitHub Actions CI workflow? I can generate those next.*
