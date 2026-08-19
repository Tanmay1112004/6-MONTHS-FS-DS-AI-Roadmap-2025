# 🤖 **BERT Chatbot — Streamlit Edition**

A sleek, modern, and production-ready **AI chatbot** powered by **BERT (Bidirectional Encoder Representations from Transformers)** and shipped with a clean, responsive **Streamlit UI**.
This project delivers an intuitive chat experience using **semantic similarity** on top of **pre-trained BERT embeddings**, enabling smart, context-aware responses.

---

## ✨ **Key Features**

* ⚡ **BERT-powered intelligence** for meaningful, context-driven conversations
* 💬 **Polished chat UI** with gradient backgrounds & WhatsApp-style bubbles
* 🎨 Fully editable **themes, gradients, and background styling**
* 🧠 **Pre-trained knowledge base** with cosine similarity response ranking
* 🚀 Optimized **PyTorch inference** for near-instant replies
* 🔧 Designed to be **modular, extensible, and beginner-friendly**
* 🏷️ Crafted with precision by **Tanmay**

---

## 📸 **Screenshots**

> UI snapshots for a quick look under the hood:

![demo](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/BERT-CHATBOT/screenshots/chat_ui.png.png)

![demo](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/BERT-CHATBOT/screenshots/Screenshot%202025-09-17%20111611.png)

![demo](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/BERT-CHATBOT/screenshots/gradient_bg.png.png)

---

## 🚀 **Getting Started**

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Tanmay1112004/bert-chatbot.git
cd bert-chatbot
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run locally or in Codespaces

```bash
streamlit run app.py
```

---

## 🛠️ **Tech Stack**

* **Python 3.10+**
* **Streamlit** – Modern interactive UI framework
* **HuggingFace Transformers** – BERT model loading & tokenization
* **PyTorch** – Embedding generation & model inference
* **scikit-learn** – Cosine similarity computation

---

## 📚 **Preloaded Knowledge Base**

The chatbot includes common queries such as:

* 🤖 *What is AI?*
* 📊 *Explain Data Science.*
* ☁️ *What is Microsoft Azure?*
* 🧠 *What is BERT?*
* 😂 *Tell me a joke.*
* 🙋 *How are you?*

Extend easily — just add more Q&A pairs inside `qa_pairs` in `app.py`.

---

## 🎛️ **Customization Guide**

* 🎨 **Change Theme/Background**: Modify the `set_background()` function
* ➕ **Add New Q&A**: Update `qa_pairs` dictionary
* 🎯 **Adjust Response Sensitivity**: Tune the similarity threshold

  ```python
  if similarities[best_match] > 0.5:
  ```
* 🧪 **Swap Models**: Replace the BERT model name in the `transformers` pipeline

---

## 👨‍💻 **Author**

Built with passion & caffeine by **Tanmay**

* LinkedIn: [tanmay-kshirsagar](https://linkedin.com/in/tanmay-kshirsagar)
* GitHub: [Tanmay1112004](https://github.com/Tanmay1112004)

---

⭐ If this project adds value, drop a **star** — it keeps the innovation engine running!

---
