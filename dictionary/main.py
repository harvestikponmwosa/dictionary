import streamlit as st
from languages import yoruba, igbo, hausa, tiv

languages = {
    "Hausa": hausa.translations,
    "Yoruba": yoruba.translations,
    "Igbo": igbo.translations,
    "Tiv": tiv.translations
}


st.title("🇳🇬 Nigerian Language Translator")
st.write("Translate English words into local languages.")

choice = st.selectbox("Choose a language:", list(languages.keys()))

word = st.text_input("Enter English word:").strip().lower()

if word:
    translations = languages[choice]
    
    if word in translations:
        st.success(f"**Translation:** {translations[word]}")
    else:
        st.warning(f"The word '{word}' is missing from the {choice} dictionary.")

st.info("Note: Make sure your translation files are in the same folder.")
