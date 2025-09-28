# app.py
from dotenv import load_dotenv
import streamlit as st
import os
import io
from PIL import Image
import google.generativeai as genai

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Gemini function (streaming response for faster UX)
def get_gemini_response(input_text, image=None):
    model = genai.GenerativeModel("gemini-2.5-flash")

    image_bytes = None
    if image:
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format=image.format if image.format else "PNG")
        image_bytes = img_byte_arr.getvalue()

    if input_text and image_bytes:
        response = model.generate_content(
            [input_text, {"mime_type": "image/png", "data": image_bytes}],
            stream=True
        )
    elif image_bytes:
        response = model.generate_content(
            [{"mime_type": "image/png", "data": image_bytes}],
            stream=True
        )
    else:
        response = model.generate_content(
            input_text or "Describe this image.",
            stream=True
        )

    final_text = ""
    for chunk in response:
        if chunk.text:
            final_text += chunk.text
            yield final_text


# ----------------- STREAMLIT UI -----------------
st.set_page_config(
    page_title="Gemini Vision Platform",
    page_icon="✨",
    layout="wide"
)

# Custom CSS
st.markdown(
    """
    <style>
    .main {background-color: #f4f6fa;}
    .stTextArea textarea {
        border-radius: 10px;
        border: 1px solid #ccc;
        padding: 10px;
    }
    .stButton button {
        background: linear-gradient(90deg, #ff6a00, #ee0979);
        color: white;
        border-radius: 12px;
        font-weight: bold;
        padding: 0.7rem 1.4rem;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.15);
    }
    .response-box {
        background: linear-gradient(135deg, #2193b0, #6dd5ed);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        font-size: 1.1rem;
        line-height: 1.6;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.25);
        margin-top: 1rem;
        min-height: 100px;
    }
    .uploaded-img {
        max-height: 350px;
        object-fit: contain;
        border-radius: 12px;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar info
with st.sidebar:
    st.image("https://seeklogo.com/images/G/google-gemini-logo-47BFAF1D64-seeklogo.com.png", width=80)
    st.title("Gemini Vision App")
    st.markdown("🚀 Powered by **Gemini 2.5 Flash** + Streamlit")
    st.markdown("### 📖 How to use:")
    st.markdown("""
    - Go to **Image Analysis** to analyze images + prompts  
    - Use **Text Q&A** for chat-like queries  
    - Visit **About** for app details  
    """)
    st.markdown("### ⚡ Features")
    st.success("Supports multimodal (image + text), fast streaming, and elegant UI")

# Tabs
tab1, tab2, tab3 = st.tabs(["🖼️ Image Analysis", "💬 Text Q&A", "ℹ️ About"])

# ----------------- TAB 1: IMAGE ANALYSIS -----------------
with tab1:
    st.header("🖼️ Image + Prompt Analysis")
    st.markdown("Upload an image + optional prompt → Gemini will describe or analyze it.")

    col1, col2 = st.columns([1, 1])
    with col1:
        input_text = st.text_area("💬 Your Prompt", placeholder="e.g. Identify objects in this image...", height=120)
    with col2:
        uploaded_file = st.file_uploader("📂 Upload an Image", type=["jpg", "jpeg", "png"])
        image = None
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Preview", use_container_width=True, output_format="PNG")

    if st.button("🚀 Analyze Image", use_container_width=True, key="analyze_img"):
        if not input_text and not image:
            st.warning("Please upload an image or enter a prompt.")
        else:
            st.subheader("🔎 Gemini’s Response")
            response_placeholder = st.empty()
            final_response = ""
            for partial_text in get_gemini_response(input_text, image):
                final_response = partial_text
                response_placeholder.markdown(
                    f"<div class='response-box'>{final_response}</div>",
                    unsafe_allow_html=True
                )

# ----------------- TAB 2: TEXT Q&A -----------------
with tab2:
    st.header("💬 Text-only Q&A")
    st.markdown("Ask Gemini anything without an image.")

    text_prompt = st.text_area("📝 Your Question", placeholder="e.g. Explain quantum computing in simple terms", height=120)

    if st.button("⚡ Get Answer", use_container_width=True, key="analyze_text"):
        if not text_prompt:
            st.warning("Please enter a question or prompt.")
        else:
            st.subheader("🧠 Gemini’s Response")
            response_placeholder = st.empty()
            final_response = ""
            for partial_text in get_gemini_response(text_prompt):
                final_response = partial_text
                response_placeholder.markdown(
                    f"<div class='response-box'>{final_response}</div>",
                    unsafe_allow_html=True
                )

# ----------------- TAB 3: ABOUT -----------------
with tab3:
    st.header("ℹ️ About this App")
    st.markdown("""
    This project demonstrates the power of **Gemini 2.5 Flash** by Google:  
    - 🚀 **Fast** streaming responses  
    - 🖼️ **Multimodal** → understands both text and images  
    - 🎨 **User-friendly UI** built with Streamlit  

    **Creator**: Tanmay 👨‍💻  
    **Tech Stack**: Python · Streamlit · Google Generative AI  
    """)
    st.info("Future upgrades: Dark/Light mode toggle, history of responses, multi-image support")
