import pickle
import numpy as np
import streamlit as st
from PIL import Image

# ------------------- CONFIG -------------------
st.set_page_config(
    page_title="Weight Prediction App",
    page_icon="⚖️",
    layout="centered",
)

# ------------------- LOAD MODEL -------------------
filename = 'final_model.pkl'
with open(filename, 'rb') as file:
    loaded_model = pickle.load(file)

# ------------------- CUSTOM CSS -------------------
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #f3ec78, #af4261);
        font-family: 'Segoe UI', sans-serif;
    }
    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        color: white;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.3);
        margin-bottom: 10px;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #f7f7f7;
        margin-bottom: 30px;
    }
    .stNumberInput > label {
        font-size: 18px;
        font-weight: bold;
        color: white !important;
    }
    .prediction-card {
        background-color: rgba(255,255,255,0.9);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        color: #6C3483;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------- TITLE -------------------
st.markdown('<div class="main-title">⚖️ Weight Prediction App</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enter your height (in feet) and get an instant weight prediction!</div>', unsafe_allow_html=True)

# ------------------- INPUT -------------------
default_height = 5.8
height_input = st.number_input("Enter the height in feet:", value=default_height, min_value=0.0, step=0.1)

# ------------------- PREDICTION -------------------
if st.button("🚀 Predict Weight"):
    height_input_2d = np.array(height_input).reshape(1, -1)
    predicted_weight = loaded_model.predict(height_input_2d)

    st.markdown(f"""
        <div class="prediction-card">
            Predicted Weight: {predicted_weight[0, 0]:.2f} kg
        </div>
    """, unsafe_allow_html=True)

# ------------------- FOOTER -------------------
st.markdown("<br><center style='color:white'>Made with ❤️ using Streamlit</center>", unsafe_allow_html=True)
