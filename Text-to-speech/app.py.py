# ========================
# INSTALL REQUIRED LIBRARIES
# ========================
!pip install gtts pyttsx3 gradio --quiet

# ========================
# IMPORTS
# ========================
import os
import pyttsx3
from gtts import gTTS
import gradio as gr
import tempfile

# ========================
# LANGUAGE SUPPORT
# ========================
# Google TTS Language Codes (Indian + Foreign)
LANGUAGES = {
    # Indian Languages
    "Hindi": "hi", "Marathi": "mr", "Bengali": "bn", "Gujarati": "gu",
    "Kannada": "kn", "Malayalam": "ml", "Punjabi": "pa", "Tamil": "ta",
    "Telugu": "te", "Urdu": "ur", "Odia": "or", "Konkani": "gom",

    # Foreign Languages
    "English": "en", "French": "fr", "Spanish": "es", "German": "de",
    "Italian": "it", "Portuguese": "pt", "Russian": "ru", "Japanese": "ja",
    "Korean": "ko", "Chinese (Mandarin)": "zh-CN", "Arabic": "ar"
}

# ========================
# FUNCTION 1 - gTTS
# ========================
def gtts_tts(text, language, slow):
    if not text.strip():
        return None, "❌ Please enter some text."

    try:
        tts = gTTS(text=text, lang=LANGUAGES[language], slow=slow, tld='com')
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(temp_file.name)
        return temp_file.name, f"✅ Generated using Google TTS in {language}"
    except Exception as e:
        return None, f"⚠️ Error: {str(e)}"

# ========================
# FUNCTION 2 - pyttsx3 (Offline)
# ========================
def pyttsx3_tts(text, voice_gender, rate):
    if not text.strip():
        return None, "❌ Please enter some text."

    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')

        if voice_gender == "Male":
            engine.setProperty('voice', voices[0].id)
        else:
            engine.setProperty('voice', voices[1].id)

        engine.setProperty('rate', rate)
        engine.setProperty('volume', 1.0)

        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        engine.save_to_file(text, temp_file.name)
        engine.runAndWait()
        return temp_file.name, f"✅ Generated using Pyttsx3 ({voice_gender} voice)"
    except Exception as e:
        return None, f"⚠️ Error: {str(e)}"

# ========================
# GRADIO FRONTEND
# ========================
def generate_audio(text, mode, language, slow, voice_gender, rate):
    if mode == "Google TTS (Multilingual)":
        return gtts_tts(text, language, slow)
    else:
        return pyttsx3_tts(text, voice_gender, rate)

with gr.Blocks(theme=gr.themes.Soft()) as app:
    gr.Markdown("<h1 style='text-align:center;color:#4CAF50;'>🎤 Text-to-Speech Studio</h1>")
    gr.Markdown("<p style='text-align:center;'>Supports all major Indian + Foreign Languages | Online & Offline Modes</p>")

    with gr.Row():
        with gr.Column():
            text_input = gr.Textbox(label="Enter Your Text", lines=6, placeholder="Type something amazing...")
            mode = gr.Radio(["Google TTS (Multilingual)", "Pyttsx3 (Offline English Only)"], value="Google TTS (Multilingual)", label="Select Mode")
            language = gr.Dropdown(list(LANGUAGES.keys()), value="English", label="Language (Google TTS only)")
            slow = gr.Checkbox(False, label="Slow Mode (Google TTS)")
            voice_gender = gr.Radio(["Male", "Female"], value="Male", label="Voice Gender (Pyttsx3 only)")
            rate = gr.Slider(100, 250, value=150, label="Speaking Rate (Pyttsx3 only)")
            submit_btn = gr.Button("🎙 Generate Audio")

        with gr.Column():
            output_audio = gr.Audio(label="Generated Speech", type="filepath")
            output_status = gr.Label(label="Status")

    submit_btn.click(
        generate_audio,
        inputs=[text_input, mode, language, slow, voice_gender, rate],
        outputs=[output_audio, output_status]
    )

# ========================
# LAUNCH APP
# ========================
app.launch(debug=True)