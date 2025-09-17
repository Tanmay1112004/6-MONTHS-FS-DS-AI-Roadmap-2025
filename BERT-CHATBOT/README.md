# 🤖 BERT Chatbot with Streamlit  

A modern **AI-powered chatbot** built using **BERT (Bidirectional Encoder Representations from Transformers)** and **Streamlit**.  
This project provides an interactive web interface where users can ask questions, and the chatbot responds intelligently using semantic similarity with pre-trained BERT embeddings.  

## ✨ Features
- 🔥 **BERT-based NLP** for context-aware responses  
- 🎨 **Beautiful UI with gradient backgrounds & chat bubbles** (WhatsApp-like)  
- 💬 **Pre-trained Q&A pairs** with cosine similarity matching  
- ⚡ **Fast inference** using PyTorch  
- 🖼️ Customizable **backgrounds / gradients / 3D feel**  
- 🏷️ **Built by Tanmay** 💻  

## 📸 Screenshots  

### Chat Interface  
*(WhatsApp-style chat bubbles for conversation)*  
![Chat Screenshot](screenshots/chat_ui.png)  

### Gradient Background  
*(Clean gradient background for an attractive UI)*  
![Gradient Background](screenshots/gradient_bg.png)  

## 🚀 Getting Started  

### 1️⃣ Clone this repo  
```bash
git clone https://github.com/Tanmay1112004/bert-chatbot.git
cd bert-chatbot
````

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run in GitHub Codespaces / Local

```bash
streamlit run app.py
```

## 🛠️ Tech Stack

* **Python 3.10+**
* [Streamlit](https://streamlit.io/) – frontend framework
* [HuggingFace Transformers](https://huggingface.co/transformers/) – BERT model
* [PyTorch](https://pytorch.org/) – embeddings & inference
* [scikit-learn](https://scikit-learn.org/) – cosine similarity

## 📚 Predefined Knowledge Base

The bot is trained on a set of common questions like:

* 🤔 *What is AI?*
* 📊 *What is Data Science?*
* ☁️ *What is Microsoft Azure?*
* 🧠 *What is BERT?*
* 😂 *Tell me a joke*
* 🙋 *How are you?*
* … and more!

Easily extendable – just add more Q\&A pairs in `qa_pairs` dictionary.

## 📌 Customization

* Change background: update `set_background()` function in `app.py`
* Add more questions: edit `qa_pairs` in `app.py`
* Change threshold for similarity: tweak `if similarities[best_match] > 0.5`

## 📢 Author

👨‍💻 Built with ❤️ by **Tanmay**

* LinkedIn: [Your LinkedIn](https://linkedin.com/in/tanmay-kshirsagar)
* GitHub: [Your GitHub](https://github.com/Tanmay1112004)

---

⭐ Don’t forget to **star this repo** if you like it!

```
