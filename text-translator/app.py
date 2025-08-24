import streamlit as st
from gtts import gTTS
from langdetect import detect, lang_detect_exception
from googletrans import Translator
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
import nltk

# Download NLTK data
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("words")

# Function to generate and play audio
def read_aloud(text, language="en"):
    try:
        tts = gTTS(text=text, lang=language)
        tts.save("temp.mp3")
        st.audio("temp.mp3", format="audio/mp3")
    except Exception:
        st.warning(f"🔇 Audio not supported for language: {language}")

# Function to generate word cloud
def generate_wordcloud(text):
    from nltk.corpus import words
    english_words = set(words.words())
    tokens = word_tokenize(text)
    english_tokens = [word for word in tokens if word.lower() in english_words]
    clean_text = " ".join(english_tokens)

    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(clean_text)
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    plt.tight_layout()
    return fig

# -------------------- UI START --------------------
st.set_page_config(page_title="🌍 Globalize App", layout="wide")

st.title("🌍 Globalize")
st.caption("Translate text, listen to it, and visualize keywords with AI power 🚀")

col1, col2 = st.columns([1, 1])

# Input Area
with col1:
    st.subheader("✍️ Enter Text")
    paragraph = st.text_area("Type or paste a paragraph:", height=200)

    if st.button("🧹 Clear"):
        paragraph = ""

# Output / Actions
with col2:
    st.subheader("⚙️ Options")
    translator = Translator()

    # Supported languages by Google Translate (shortlist for demo)
    supported_languages = {
        "English": "en",
        "Hindi": "hi",
        "French": "fr",
        "Spanish": "es",
        "German": "de",
        "Chinese (Simplified)": "zh-cn",
        "Japanese": "ja",
        "Russian": "ru",
        "Arabic": "ar"
    }

    target_languages_input = st.multiselect(
        "🌐 Select languages to translate into:",
        list(supported_languages.keys()),
    )

    # Detect Language
    if paragraph.strip():
        try:
            detected_lang = detect(paragraph)
            st.success(f"✅ Detected language: {detected_lang.upper()}")
        except lang_detect_exception.LangDetectException:
            detected_lang = "en"
            st.warning("⚠️ Could not detect language, defaulting to English.")

    # Actions
    if st.button("🎧 Translate & Read Aloud"):
        if not paragraph.strip():
            st.error("Please enter some text first.")
        else:
            for lang in target_languages_input:
                lang_code = supported_languages[lang]
                try:
                    translated_text = translator.translate(paragraph, dest=lang_code).text
                    st.markdown(f"**🌐 Translation in {lang}:**")
                    st.write(translated_text)
                    read_aloud(translated_text, lang_code)
                except Exception as e:
                    st.error(f"❌ Translation to {lang} failed: {e}")

# Sidebar → Word Cloud
st.sidebar.header("☁️ Word Cloud")
if paragraph.strip():
    try:
        wordcloud_fig = generate_wordcloud(paragraph)
        st.sidebar.pyplot(wordcloud_fig)
    except Exception as e:
        st.sidebar.error(f"Word cloud error: {e}")

st.sidebar.markdown("---")
st.sidebar.info("💡 Tip: Try pasting text in Hindi, French, or Japanese and see the magic!")
