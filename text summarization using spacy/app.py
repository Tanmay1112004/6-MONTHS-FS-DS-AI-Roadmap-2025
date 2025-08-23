# text_summarizer_app.py
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
import streamlit as st

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def text_summarizer(raw_text, summary_ratio=0.3):
    """
    Extractive summarization using word frequency scoring
    """
    doc = nlp(raw_text)

    # Word frequencies
    word_frequencies = {}
    for word in doc:
        if word.text.lower() not in STOP_WORDS and word.text.lower() not in punctuation:
            word_frequencies[word.text.lower()] = word_frequencies.get(word.text.lower(), 0) + 1

    # Normalize frequencies
    max_freq = max(word_frequencies.values(), default=1)
    for word in word_frequencies:
        word_frequencies[word] = word_frequencies[word] / max_freq

    # Sentence scoring
    sentence_scores = {}
    for sent in doc.sents:
        for word in sent:
            if word.text.lower() in word_frequencies:
                sentence_scores[sent] = sentence_scores.get(sent, 0) + word_frequencies[word.text.lower()]

    # Pick top N sentences
    select_length = max(1, int(len(list(doc.sents)) * summary_ratio))
    summary_sentences = nlargest(select_length, sentence_scores, key=sentence_scores.get)

    final_summary = " ".join([sent.text for sent in summary_sentences])
    return final_summary, doc, sentence_scores

# ================== STREAMLIT FRONTEND ==================
st.set_page_config(page_title="📝 Text Summarizer", layout="wide")

st.title("📝 Extractive Text Summarizer (spaCy)")
st.write("Paste your text below and get a concise summary!")

# Sidebar settings
st.sidebar.header("⚙️ Settings")
summary_ratio = st.sidebar.slider("Summary Length (% of text)", 10, 80, 30, step=5) / 100

# Text input
raw_text = st.text_area("Enter text here:", height=300)

if st.button("Summarize"):
    if raw_text.strip() == "":
        st.warning("⚠️ Please enter some text to summarize!")
    else:
        summary, doc, scores = text_summarizer(raw_text, summary_ratio)

        st.subheader("📌 Original Text")
        st.write(raw_text)

        st.subheader("✅ Summary")
        st.success(summary)

        st.subheader("📊 Token & Sentence Analysis")
        st.write(f"Total Sentences: {len(list(doc.sents))}")
        st.write(f"Total Tokens: {len(doc)}")
        st.write(f"Summary covers ~{int(summary_ratio*100)}% of sentences")
