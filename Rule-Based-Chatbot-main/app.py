import streamlit as st
from bot import get_chatbot, DEFAULT_BOT_NAME

st.set_page_config(page_title="NLTK Chatbot", page_icon="💬", layout="centered")

# --- App State ---
if "history" not in st.session_state:
    st.session_state.history = []
if "bot" not in st.session_state:
    st.session_state.bot = get_chatbot()
if "bot_name" not in st.session_state:
    st.session_state.bot_name = DEFAULT_BOT_NAME

# --- Sidebar ---
with st.sidebar:
    st.title("⚙️ Settings")
    st.write("Customize a fallback response for unmatched queries.")
    fallback = st.text_area(
        "Fallback response",
        value="Our customer service will reach you.",
        help="Shown when no rule matches."
    )
    if st.button("Apply", use_container_width=True):
        st.session_state.bot.update_fallback(fallback)
        st.success("Fallback updated.")
    st.divider()
    if st.button("Reset Chat", type="secondary", use_container_width=True):
        st.session_state.history = []
        st.rerun()

st.title("💬Rule-Based Chatbot")
st.caption("Powered by NLTK `Chat` + Streamlit. Type your message below.")

# --- Chat UI ---
chat_container = st.container()
with chat_container:
    for role, msg in st.session_state.history:
        if role == "user":
            with st.chat_message("user"):
                st.markdown(msg)
        else:
            with st.chat_message("assistant"):
                st.markdown(msg)

# --- Input box ---
prompt = st.chat_input("Type here (e.g., 'hi', 'my name is Tanmay', 'tell me a joke')")
if prompt:
    # Append user message first
    st.session_state.history.append(("user", prompt))

    # Get bot response
    response = st.session_state.bot.respond(prompt)
    if response is None:
        response = st.session_state.bot.fallback

    st.session_state.history.append(("assistant", response))
    st.rerun()
