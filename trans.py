import streamlit as st
from googletrans import Translator, LANGUAGES

# Initialize Google Translator
translator = Translator()

# Function to get language code from language name
def get_language_code(language_name):
    for lang_code, lang_name in LANGUAGES.items():
        if lang_name.lower() == language_name.lower():
            return lang_code
    return None

# Custom CSS for styling the app
st.markdown("""
    <style>
    body {
      background-color: #f5f5f5;
      color: #333;
      font-family: 'Roboto', sans-serif;
      margin: 20px;
    }
    .app-title {
      font-size: 2.5em;
      color: #00796b;
      text-align: center;
      margin-bottom: 20px;
    }
    .input-container {
      background-color: #fff;
      border-radius: 10px;
      padding: 20px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
      margin-bottom: 20px;
    }
    .input-field {
      border-radius: 5px;
      border: 1px solid #ccc;
      padding: 12px;
      margin-bottom: 15px;
      width: 100%;
    }
    .text-area {
      height: 150px;
    }
    .select {
      display: block;
      width: 100%;
      padding: 10px;
      border-radius: 5px;
      border: 1px solid #ccc;
    }
    .button {
      background-color: #00796b;
      color: white;
      font-size: 16px;
      padding: 12px 24px;
      border: none;
      border-radius: 5px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
      cursor: pointer;
      transition: background-color 0.2s ease-in-out;
    }
    .button:hover {
      background-color: #004d40;
    }
    .result {
      background-color: #f0f0f0;
      border-radius: 5px;
      padding: 15px;
      margin-top: 15px;
    }
    .result-title {
      font-weight: bold;
      margin-bottom: 5px;
    }
    .supported-languages {
      margin-top: 20px;
      font-style: italic;
    }
    .footer {
      text-align: center;
      padding: 15px 0;
      font-size: 14px;
      color: #777;
      border-top: 1px solid #ccc;
    }
    .footer a {
      color: #00796b;
      text-decoration: none;
    }
    .footer a:hover {
      text-decoration: underline;
    }
  </style>
    """, unsafe_allow_html=True)

# Streamlit UI
st.markdown("<h1 class='stTitle'>🌐 Language Translator</h1>", unsafe_allow_html=True)
st.write("Translate text between languages with ease using our modern, user-friendly interface.")

# Container for the input and translation section
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    # Input text
    source_text = st.text_area("📝 Enter text to translate:", "", height=150)

    # Input source language (fixed selection)
    source_lang = st.selectbox("Select source language", ["en", "fr", "es", "de", "it"], index=0)

    # Target language input (searchable by name)
    target_language_search = st.text_input("🔍 Enter target language name (e.g., French, Spanish, German):", "")

    # Dropdown for selecting the target language
    target_language_select = st.selectbox("Or select target language from dropdown", list(LANGUAGES.values()))

    # Combine the text input and dropdown selection
    if target_language_search:
        target_lang_code = get_language_code(target_language_search)
    else:
        target_lang_code = get_language_code(target_language_select)

    # Translate button
    if st.button("🌍 Translate"):
        if target_lang_code is None:
            st.error(f"⚠ Error: '{target_language_search or target_language_select}' is not a valid language name. Please try again.")
        else:
            # Using googletrans for translation
            translated_text = translator.translate(source_text, src=source_lang, dest=target_lang_code).text
            st.success(f"*Translated Text*: {translated_text}")

    st.markdown("</div>", unsafe_allow_html=True)

# Show supported languages in list format
if st.checkbox("Show supported languages"):
    st.write("Supported Languages:")
    st.write("\n".join([f"- {lang_name.capitalize()}" for lang_name in LANGUAGES.values()]))

# Footer
st.markdown("""
    <div class="footer">
        Created by <a href="https://github.com/SHARAVANAKUMAR21" target="_blank">Saravana Kumar B</a> | Powered by Streamlit & Google Translate API
    </div>
    """, unsafe_allow_html=True)
