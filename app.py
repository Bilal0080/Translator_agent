import streamlit as st
from deep_translator import GoogleTranslator
import pyttsx3

st.set_page_config(page_title="🌐 Text Translator", layout="centered")
st.title("🌍 Multi-Language Translator Agent")

# Supported languages
language_options = {
    "English": "en",
    "Urdu": "ur",
    "Chinese": "zh-CN",
    "French": "fr",
    "Japanese": "ja",
    "Arabic": "ar"
}

# Text-to-Speech
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

# Select language
target_language = st.selectbox("Select target language", list(language_options.keys()))

# Input text
text_input = st.text_area("Enter text to translate", height=150)

# Translate and speak
if st.button("Translate"):
    if text_input.strip():
        lang_code = language_options[target_language]
        try:
            translated = GoogleTranslator(source='auto', target=lang_code).translate(text_input)
            st.success("Translation:")
            st.text_area(f"{target_language} Translation", translated, height=150)
            speak(translated)
        except Exception as e:
            st.error("Translation failed.")
            st.exception(e)
