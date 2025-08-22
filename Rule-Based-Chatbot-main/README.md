# 🤖 NLTK Rule-based Chatbot with Streamlit UI

A **lightweight, professional, and extensible chatbot** built using [NLTK](https://www.nltk.org/)’s rule-based `Chat` utility and powered by a sleek [Streamlit](https://streamlit.io/) frontend. Ready to run locally or in **GitHub Codespaces** 🚀.

---

## ✨ Features

* 🧠 **Rule-based NLP** — Powered by regex patterns with `nltk.chat.util.Chat`.
* 🎨 **Modern Streamlit UI** — Clean, simple, and mobile-friendly.
* ⚡ **Dynamic Intents** — Supports greetings, name recognition, bot info, location, weather demo, cricket Q\&A, and even basic math.
* ☁️ **Cloud-Ready** — Pre-configured `.devcontainer` for GitHub Codespaces with automatic port forwarding.
* 🛠️ **Easily Extensible** — Add your own intents by editing `bot.py`.

---

## 📸 Demo Preview

👉 Launch the chatbot and start chatting:

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
├── bot.py                   # NLTK Chat logic + expanded rules
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── .devcontainer/
    └── devcontainer.json    # Codespaces config
```

---

## 🚀 Getting Started

### 🔹 Run Locally

```bash
# Clone the repo
 git clone https://github.com/your-username/nltk-streamlit-chatbot.git
 cd nltk-streamlit-chatbot

# Create & activate virtual environment
 python -m venv .venv
 source .venv/bin/activate   # Windows: .venv\Scripts\activate

# Install dependencies
 pip install -r requirements.txt

# Launch chatbot
 streamlit run app.py
```

App will be available at **[http://localhost:8501](http://localhost:8501)**.

### 🔹 Run in GitHub Codespaces

1. Open the repo in **GitHub Codespaces**.
2. Run:

   ```bash
   pip install -r requirements.txt
   streamlit run app.py --server.address 0.0.0.0 --server.port 8501
   ```
3. Open the forwarded **8501** port.

---

## 🎯 Supported Intents

| Intent         | Example Input                     | Example Response                          |
| -------------- | --------------------------------- | ----------------------------------------- |
| Greetings      | `hi`, `hello`, `good morning`     | "Hey there!"                              |
| Introductions  | `my name is Tanmay`               | "Nice to meet you, Tanmay!"               |
| Bot Info       | `what's your name?`               | "You can call me RoboTan ✨"               |
| Help           | `help`, `can you help`            | "Sure — tell me what you need help with." |
| Location       | `your location?`                  | "Hyderabad, India ☁️"                     |
| Weather (demo) | `is it raining in Pune?`          | "Pack an umbrella for Pune ☔"             |
| Sports         | `who is your favorite cricketer?` | "Virat Kohli — clutch gene."              |
| Quick Math     | `sum 12 and 30`                   | "Quick math: 42"                          |

---

## 🛠️ Tech Stack

* **Python 3.11**
* [NLTK](https://www.nltk.org/) → rule-based Chat class
* [Streamlit](https://streamlit.io/) → modern frontend
* GitHub Codespaces (Dev Container ready)

---

## 🧩 How to Extend

Want to add new intents? It’s simple:

1. Open `bot.py`.
2. Add a new regex → response pair in the `pairs` list.
3. Responses can use placeholders (`%1`, `%2`) for regex groups.
4. Restart Streamlit.

Example:

```python
[ r"what is your favorite (.*)?", ["I love %1!"] ],
```

---

## 📜 License

MIT License © 2025 — Built with ❤️ by Tanmay.

---

## 🤝 Contributing

Contributions are welcome! If you’d like to improve the chatbot, fork the repo and submit a pull request.

---

## 🌟 Acknowledgements

* Inspired by **NLTK’s built-in chatbot** examples.
* Built with **Streamlit** for simplicity and beauty.
* Codespaces config for hassle-free cloud dev.

---

> ⚡ Pro tip: Try asking *“sum 7 and 13”* or *“who is your favorite cricketer?”*
