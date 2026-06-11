# 🤖 NLTK Rule-Based Chatbot with Streamlit UI

> A lightweight, production-ready chatbot powered by rule-based NLP and delivered through a modern Streamlit interface.

Simple by design. Powerful by intent. Zero overengineering.

---


## ✨ Key Highlights

* 🧠 **Rule-Based NLP Engine**
  Built using NLTK’s classic `Chat` utility with regex-driven conversational rules.

* 🎨 **Modern Streamlit Interface**
  Minimal, responsive design optimized for usability.

* ⚡ **Dynamic Intents Handling**
  Supports greetings, introductions, bot metadata, weather demo, sports Q&A, and arithmetic.

* ☁️ **Cloud-Ready Setup**
  Dev Container support for GitHub Codespaces execution.

* 🛠️ **Extensible Architecture**
  Add or modify intents by editing a single file.

---

## 📸 Demo Conversation

```
User: hi
Bot: Hey there!

User: my name is Tanmay
Bot: Nice to meet you, Tanmay!

User: sum 12 and 30
Bot: Quick math: 12 + 30 = 42

User: who is your favorite cricketer?
Bot: Virat Kohli — clutch gene.
```

---

## 🏗 Architecture Overview

User Input
⬇
Streamlit UI
⬇
NLTK Regex Pattern Matching
⬇
Intent Detection
⬇
Dynamic Response Rendering

This project demonstrates:

* NLP fundamentals
* Regex-based intent recognition
* Web app integration
* Session state handling
* Clean modular architecture

---

## 📂 Project Structure

```bash
.
├── app.py
├── bot.py
├── requirements.txt
├── README.md
└── .devcontainer/
```

---

## 🚀 Getting Started

### 🔹 Run Locally

```bash
git clone https://github.com/Tanmay1112004/nltk-streamlit-chatbot.git
cd nltk-streamlit-chatbot
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Access at:
👉 [http://localhost:8501](http://localhost:8501)

---

### 🔹 Run via GitHub Codespaces

```bash
pip install -r requirements.txt
streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```

Open forwarded port 8501.

No local config required.

---

## 🎯 Supported Intents

| Category     | Example                |
| ------------ | ---------------------- |
| Greetings    | hi, hello              |
| Introduction | my name is Tanmay      |
| Identity     | what’s your name?      |
| Help         | help                   |
| Location     | where are you located? |
| Weather      | is it raining in Pune? |
| Sports       | favorite cricketer?    |
| Math         | sum 12 and 30          |

---

## 🛠️ Tech Stack

* Python 3.11
* NLTK (Rule-based NLP)
* Streamlit (Frontend UI)
* GitHub Codespaces (Cloud Dev)

---

## 🧩 Customization

Add new intents in `bot.py`:

```python
[
  r"what is your favorite (.*)?",
  ["I really like %1!"]
]
```

Regex capture groups automatically substitute variables into responses.

---

## 🎯 Why This Project Matters

In a world full of LLM wrappers, this project shows:

* Understanding of classic NLP
* Pattern-based conversational logic
* Structured rule design
* Lightweight chatbot engineering

Sometimes simplicity wins.

---

## 📜 License

MIT License
© 2026 — Built by Tanmay

---
