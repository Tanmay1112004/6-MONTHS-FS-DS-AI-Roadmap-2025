import streamlit as st
from transformers import BertTokenizer, BertModel
import torch
from sklearn.metrics.pairwise import cosine_similarity

# ------------------- Dark Mode Toggle -------------------
dark_mode = st.sidebar.checkbox("🌙 Dark Mode", value=False)

def add_custom_css(dark):
    if dark:
        user_bg = "#0A84FF"  # iMessage blue
        bot_bg = "#2C2C2E"   # dark grey
        bg_gradient = "linear-gradient(-45deg, #000000, #1C1C1E, #2C2C2E, #3A3A3C)"
        font_color = "white"
    else:
        user_bg = "#00c6ff"
        bot_bg = "#FFD93D"
        bg_gradient = "linear-gradient(-45deg, #ff9a9e, #fad0c4, #a18cd1, #fbc2eb)"
        font_color = "black"

    st.markdown(f"""
        <style>
        body {{
            font-family: 'Segoe UI', sans-serif;
            color: {font_color};
        }}
        .chat-box {{
            max-height: 450px;
            overflow-y: auto;
            padding: 15px;
            border-radius: 12px;
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(12px);
        }}
        .user-bubble {{
            align-self: flex-end;
            background: {user_bg};
            color: white;
            padding: 12px 15px;
            border-radius: 18px 18px 0 18px;
            margin: 8px 0;
            max-width: 70%;
            font-size: 16px;
            text-align: right;
            box-shadow: 0px 2px 6px rgba(0,0,0,0.2);
        }}
        .bot-bubble {{
            align-self: flex-start;
            background: {bot_bg};
            color: {font_color};
            padding: 12px 15px;
            border-radius: 18px 18px 18px 0;
            margin: 8px 0;
            max-width: 70%;
            font-size: 16px;
            box-shadow: 0px 2px 6px rgba(0,0,0,0.2);
        }}
        .stApp {{
            background: {bg_gradient};
            background-size: 400% 400%;
            animation: gradientBG 12s ease infinite;
        }}
        @keyframes gradientBG {{
            0% {{background-position: 0% 50%;}}
            50% {{background-position: 100% 50%;}}
            100% {{background-position: 0% 50%;}}
        }}
        </style>
    """, unsafe_allow_html=True)

add_custom_css(dark_mode)

# ------------------- Load BERT -------------------
@st.cache_resource
def load_bert_model():
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    model = BertModel.from_pretrained("bert-base-uncased")
    return tokenizer, model

tokenizer, model = load_bert_model()

# ------------------- Expanded Knowledge Base -------------------
qa_pairs = {
    "What is your name?": "🤖 I am a chatbot powered by BERT!",
    "How are you?": "💻 I'm just a bunch of code, but I'm doing great!",
    "Tell me a joke.": "😂 Why don't programmers like nature? It has too many bugs.",
    "What is BERT?": "📚 BERT stands for Bidirectional Encoder Representations from Transformers. It’s a powerful NLP model.",
    "What is AI?": "🧠 Artificial Intelligence makes machines simulate human intelligence.",
    "What is machine learning?": "🤖 Machine Learning is teaching computers to learn from data without being explicitly programmed.",
    "What is deep learning?": "🧠 Deep Learning is a subset of ML that uses neural networks with many layers.",
    "What is NLP?": "💬 Natural Language Processing helps machines understand human language.",
    "What is data science?": "📊 Data Science is about analyzing data, finding patterns, and making smart decisions.",
    "What is cloud computing?": "☁️ Cloud computing is using remote servers to store and run apps instead of local machines.",
    "What is Microsoft Azure?": "☁️ Azure is Microsoft’s cloud platform for apps, AI, and data.",
    "What is GitHub?": "🐙 GitHub is a platform for hosting and collaborating on code using Git.",
    "What is Python?": "🐍 Python is a powerful high-level programming language widely used in AI and Data Science.",
    "What is JavaScript?": "⚡ JavaScript powers the interactive behavior of websites.",
    "What is Next.js?": "⚛️ Next.js is a React framework for building fast, modern web apps.",
    "Who built you?": "👨‍💻 I was proudly built by Tanmay ✨",
    "What is love?": "❤️ Love is the universal language humans use. Sadly, I only know Python and Transformers 😅."
}

def get_bert_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).numpy()

predefined_embeddings = {q: get_bert_embedding(q) for q in qa_pairs}

def chatbot_response(user_input):
    user_emb = get_bert_embedding(user_input)
    similarities = {q: cosine_similarity(user_emb, predefined_embeddings[q])[0][0] for q in qa_pairs}
    best_match = max(similarities, key=similarities.get)
    if similarities[best_match] > 0.5:
        return qa_pairs[best_match]
    else:
        return "🤔 I'm not sure how to respond to that."

# ------------------- Streamlit UI -------------------
st.title("💬 BERT Chatbot")
st.write("🚀 A smart chatbot built with **BERT + Streamlit**, deployed in **GitHub Codespaces** ☁️")

# Sidebar info
st.sidebar.title("ℹ️ About")
st.sidebar.write("""
This chatbot uses **BERT embeddings** + **cosine similarity** for answering queries.  
✨ Designed for LinkedIn showcase (WhatsApp-style).  
👨‍💻 Built by **Tanmay**.  
""")

# Session state for chat
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input box
user_input = st.text_input("👤 You:", placeholder="Type your question here...")

if user_input:
    response = chatbot_response(user_input)
    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("bot", response))

# Display chat
st.markdown("<div class='chat-box'>", unsafe_allow_html=True)
for role, msg in st.session_state.chat_history:
    if role == "user":
        st.markdown(f"<div class='user-bubble'>{msg}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot-bubble'>{msg}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("✨ Built by Tanmay | Powered by BERT + Streamlit ✨")
