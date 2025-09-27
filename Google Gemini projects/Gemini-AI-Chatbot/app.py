# app.py - SaaS-like Gemini AI Chatbot
import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# --- Helper function ---
def get_gemini_response(question):
    """Generate response from Gemini AI using gemini-2.5-flash model."""
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content(question)
    return response.text

# --- Streamlit UI setup ---
st.set_page_config(
    page_title="Gemini Q&A Chatbot",
    page_icon="🤖",
    layout="wide",
)

# Sidebar with dark/light mode toggle
with st.sidebar:
    st.title("Gemini Q&A 🤖")
    st.markdown(
        """
        **Ask any question and get answers powered by Google Gemini AI.**

        ⚡ Features:
        - Interactive Q&A
        - Chat history
        - Modern SaaS-like UI
        - Dark/Light mode
        """
    )
    st.image(
        "https://miro.medium.com/v2/resize:fit:1200/format:webp/1*XJU_Hv9zW0H-6iOaAYHf8Q.png",
        use_container_width=True
    )
    # Dark/Light mode
    theme = st.radio("Choose Theme:", ["Light", "Dark"], index=0)

# Theme colors
if theme == "Dark":
    user_bg = "#1E3A8A"
    user_color = "white"
    ai_bg = "#374151"
    ai_color = "white"
    page_bg = "#111827"
else:
    user_bg = "#4B8BBE"
    user_color = "white"
    ai_bg = "#FFF5BA"
    ai_color = "black"
    page_bg = "#F0F2F6"

# Page styling
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {page_bg};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>🤖 Gemini AI Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #306998;'>Ask anything and get instant AI responses!</h4>", unsafe_allow_html=True)

# Initialize session history
if "history" not in st.session_state:
    st.session_state.history = []

# Scrollable chat container
chat_container = st.container()

# User input form
with st.form(key="user_input_form", clear_on_submit=True):
    user_question = st.text_input("Type your question here...", "")
    submitted = st.form_submit_button("Ask 🚀")

# Handle submission
if submitted and user_question.strip() != "":
    try:
        answer = get_gemini_response(user_question)
        st.session_state.history.append({"question": user_question, "answer": answer})
    except Exception as e:
        st.error(f"Error: {e}")

# Display chat history in reverse (latest at bottom)
for chat in st.session_state.history:
    # User bubble
    chat_container.markdown(
        f"""
        <div style="
            display:flex;
            align-items:flex-start;
            margin-bottom:10px;
        ">
            <img src='https://cdn-icons-png.flaticon.com/512/147/147144.png' width='40' style='border-radius:50%; margin-right:8px'/>
            <div style='
                background: {user_bg};
                color: {user_color};
                padding:12px;
                border-radius:12px;
                max-width:70%;
                word-wrap: break-word;
            '>
                <strong>You:</strong> {chat['question']}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    # AI bubble
    chat_container.markdown(
        f"""
        <div style="
            display:flex;
            align-items:flex-start;
            margin-bottom:10px;
        ">
            <img src='https://cdn-icons-png.flaticon.com/512/4712/4712027.png' width='40' style='border-radius:50%; margin-right:8px'/>
            <div style='
                background: {ai_bg};
                color: {ai_color};
                padding:12px;
                border-radius:12px;
                max-width:70%;
                word-wrap: break-word;
            '>
                <strong>Gemini:</strong> {chat['answer']}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Footer
# Footer
st.markdown(
    "<hr><p style='text-align:center;color:#999'>Powered by Google Gemini AI | Created by Tanmay</p>",
    unsafe_allow_html=True
)
