import streamlit as st
import joblib
import re
import string

# =========================
# LOAD MODEL + VECTORIZER
# =========================
model = joblib.load("model.jb")
vectorizer = joblib.load("vectorizer.jb")

# =========================
# TEXT CLEANING
# =========================
def wordopt(text):
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r"\W", " ", text)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'<.*?>+', '', text)
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub(r'\n', '', text)
    text = re.sub(r'\w*\d\w*', '', text)
    return text

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Fake News Detector",
    page_icon="📰",
    layout="centered"
)

# =========================
# HEADER UI (IMPROVED ONLY STYLE)
# =========================
st.markdown(
    """
    <style>
    .title {
        font-size:42px;
        font-weight:800;
        text-align:center;
        color:#1F4E79;
    }
    .subtitle {
        text-align:center;
        color:#6c757d;
        font-size:17px;
        margin-bottom:10px;
    }
    .block {
        padding:15px;
        border-radius:12px;
        background-color:#f8f9fa;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="title">📰 Fake News Detector</div>', unsafe_allow_html=True)

st.write("---")

# =========================
# INPUT BOX (SAME)
# =========================
news = st.text_area(
    "✍️ Enter News Article Below",
    height=200,
    placeholder="Paste news here..."
)

# =========================
# BUTTON (SAME LOGIC)
# =========================
if st.button("🔍 Analyze News"):

    if news.strip() == "":
        st.warning("⚠️ Please enter some text!")
    else:
        with st.spinner("Analyzing news..."):

            cleaned_text = wordopt(news)
            vector_input = vectorizer.transform([cleaned_text])
            prediction = model.predict(vector_input)

        st.write("---")

        # =========================
        # RESULT UI (ONLY IMPROVED STYLE)
        # =========================
        if prediction[0] == 1:
            st.markdown(
                "<h3 style='color:green;'>✅ REAL NEWS</h3>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                "<h3 style='color:red;'>🚨 FAKE NEWS</h3>",
                unsafe_allow_html=True
            )

# =========================
# FOOTER (IMPROVED)
# =========================
st.write("---")
