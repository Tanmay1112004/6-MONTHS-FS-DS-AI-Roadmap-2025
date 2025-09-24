import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# ===== LangSmith Tracking =====
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "your api key"
os.environ["LANGCHAIN_PROJECT"] = "Geminitor"

# ===== Gemini API Key =====
os.environ["GOOGLE_API_KEY"] = "your api key"

# ===== LangChain Chain Setup =====
system_message = "You are Geminitor, a helpful, smart chatbot that answers clearly and suggests the next follow-up question."
prompt = ChatPromptTemplate.from_messages([
    ("system", system_message),
    ("user", "{question}")
])
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# ===== Streamlit Chat UI Setup =====
st.set_page_config(page_title="Geminitor 💬", page_icon="🤖")
st.title("🤖 Geminitor: Smart Gemini Chatbot with LangSmith Monitoring")

# Session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input area
user_input = st.chat_input("Type your message here...")

if user_input:
    # Append user message to chat history
    st.session_state.chat_history.append(("user", user_input))

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate Gemini response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chain.invoke({"question": user_input})
            st.markdown(response)
            st.session_state.chat_history.append(("assistant", response))

        # OPTIONAL: Ask Gemini to suggest a follow-up question
        follow_up_prompt = ChatPromptTemplate.from_messages([
            ("system", "Given the last user message and your answer, suggest one useful follow-up question the user might ask next."),
            ("user", f"User: {user_input}\nAssistant: {response}")
        ])
        follow_up_chain = follow_up_prompt | llm | output_parser
        follow_up = follow_up_chain.invoke({})

        # Display suggested follow-up
        st.markdown(f"💡 **Suggested follow-up:** _{follow_up.strip()}_")

# Display full chat history (on page reload)
for role, msg in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(msg)
