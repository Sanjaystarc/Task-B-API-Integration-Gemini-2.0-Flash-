import streamlit as st
import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

st.set_page_config(page_title="Gemini 2.0 Flash Tester", layout="wide")

st.title("🔮 Gemini 2.0 Flash — Interactive Playground")
st.write("A simple UI to test Gemini 2.0 Flash using Hugging Face Spaces.")

# --------------------------------------------------
# Sidebar - Input Options
# --------------------------------------------------
with st.sidebar:
    st.header("⚙️ Model Settings")

    temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.1)
    max_output_tokens = st.number_input(
        "Max Output Tokens", 
        min_value=10, 
        max_value=2048, 
        value=256
    )

    enable_safety = st.checkbox("Enable Safety Settings (Google Default)", value=True)
    debug_mode = st.checkbox("Show Raw JSON Response")

    st.markdown("---")
    st.markdown("### 🔐 API")
    if API_KEY:
        st.success("API key loaded from .env")
    else:
        st.error("API key missing! Add GEMINI_API_KEY to your .env")

# --------------------------------------------------
# Main Input Area
# --------------------------------------------------
prompt = st.text_area("✍️ Enter your prompt:", height=200)

if st.button("Generate Response"):
    if not prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        url = f"{ENDPOINT}?key={API_KEY}"

        request_payload = {
            "contents": [
                {"parts": [{"text": prompt}]}
            ],
            "generationConfig": {
                "temperature": temperature,
                "maxOutputTokens": max_output_tokens
            }
        }

        # Safety settings optional
        if not enable_safety:
            request_payload["safetySettings"] = [{
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_NONE"
            }]

        with st.spinner("Calling Gemini 2.0 Flash..."):
            response = requests.post(url, json=request_payload)
            data = response.json()

        # Extract output
        try:
            text_output = data["candidates"][0]["content"]["parts"][0]["text"]
            st.success("Response received!")
            st.write("### 📝 Gemini Output")
            st.write(text_output)
        except:
            st.error("Unexpected response from Gemini.")
            st.json(data)

        # Debug raw JSON
        if debug_mode:
            st.write("### 🐞 Raw JSON Debug")
            st.json(data)
