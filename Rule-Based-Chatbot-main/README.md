# 🤖 NLTK Rule-Based Chatbot with Streamlit UI

A **lightweight, production-ready chatbot** built using **NLTK’s rule-based NLP engine** and delivered through a **clean, interactive Streamlit interface**.
Designed for quick setup, easy customization, and seamless execution both **locally** and via **GitHub Codespaces**.

> Simple by design. Powerful by intent. Zero overengineering.

---

## ✨ Key Highlights

* 🧠 **Rule-Based NLP Engine**
  Built on `nltk.chat.util.Chat`, leveraging regex-driven conversational patterns.

* 🎨 **Modern Streamlit Interface**
  Clean, responsive UI optimized for desktop and mobile.

* ⚡ **Dynamic Intents Handling**
  Supports greetings, introductions, chatbot metadata, weather demo, sports Q&A, and basic arithmetic.

* ☁️ **Cloud-Ready Setup**
  Preconfigured **Dev Container** for instant execution in GitHub Codespaces.

* 🛠️ **Highly Extensible Architecture**
  Add or modify intents in minutes by editing a single file.

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

## 📂 Project Structure

```
.
├── app.py                   # Streamlit frontend
├── bot.py                   # NLTK chatbot logic & intent rules
├── requirements.txt         # Python dependencies
├── README.md                # Documentation
└── .devcontainer/
    └── devcontainer.json    # GitHub Codespaces configuration
```

---

## 🚀 Getting Started

### 🔹 Run Locally

```bash
# Clone the repository
git clone https://github.com/your-username/nltk-streamlit-chatbot.git
cd nltk-streamlit-chatbot

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the application
streamlit run app.py
```

Access the app at:
👉 **[http://localhost:8501](http://localhost:8501)**

---

### 🔹 Run in GitHub Codespaces

1. Open the repository in **GitHub Codespaces**.
2. Execute:

```bash
pip install -r requirements.txt
streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```

3. Open the forwarded **8501** port.

No local setup. Zero friction.

---

## 🎯 Supported Intents

| Category       | Example Input             | Example Response                          |
| -------------- | ------------------------- | ----------------------------------------- |
| Greetings      | `hi`, `hello`             | "Hey there!"                              |
| Introduction   | `my name is Tanmay`       | "Nice to meet you, Tanmay!"               |
| Bot Identity   | `what's your name?`       | "You can call me RoboTan ✨"               |
| Help           | `help`, `can you help me` | "Sure — tell me what you need help with." |
| Location       | `where are you located?`  | "Hyderabad, India ☁️"                     |
| Weather (Demo) | `is it raining in Pune?`  | "Pack an umbrella for Pune ☔"             |
| Sports         | `favorite cricketer?`     | "Virat Kohli — clutch gene."              |
| Math Utility   | `sum 12 and 30`           | "Quick math: 42"                          |

---

## 🛠️ Technology Stack

* **Python 3.11**
* **NLTK** — Rule-based conversational engine
* **Streamlit** — Frontend framework
* **GitHub Codespaces** — Cloud development environment

---

## 🧩 Customization & Extension

Adding new intents is straightforward:

1. Open `bot.py`
2. Add a new **regex → response** pair inside the `pairs` list
3. Restart the Streamlit app

Example:

```python
[
  r"what is your favorite (.*)?",
  ["I really like %1!"]
],
```

Regex groups (`%1`, `%2`, etc.) are automatically substituted in responses.

---

## 📜 License

**MIT License**
© 2025 — Built with ❤️ by **Tanmay**

---

## 🤝 Contributing

Contributions are welcome and encouraged.

* Fork the repository
* Create a feature branch
* Submit a pull request

Let’s make it better together.

---

## 🌟 Acknowledgements

* Inspired by **NLTK’s classic chatbot examples**
* Built using **Streamlit** for rapid UI development
* Dev Container configuration for seamless cloud workflows

---

> 💡 **Pro Tip:** Try asking
> *“sum 7 and 13”* or *“who is your favorite cricketer?”*

Clean. Practical. Interview-ready. 🚀
