# Gemini 2.0 Flash — Streamlit Test UI

This project provides a **minimal Streamlit interface** to test prompts using **Google Gemini 2.0 Flash** through the official REST API. It is designed for fast experimentation, debugging, and Hugging Face Space deployment.

---

## Task A — Vectorization with Hugging Face
This part of the project demonstrates how to perform **text vectorization and similarity search** using the model **`intfloat/e5-small-v2`**.

### ✅ Features
- Load the `intfloat/e5-small-v2` embedding model using `sentence-transformers`
- Extract text from PDF files (or fallback to sample sentences)
- Convert sentences into vector embeddings
- Perform cosine similarity search against a user query
- Streamlit-based UI for testing and exploring embeddings

### 🧪 How It Works
1. Load sentences from a PDF or example list
2. Generate embeddings using the E5 model
3. Embed the user query (with required prefix `query:`)
4. Compute cosine similarity
5. Rank and display top-matching sentences

### 📦 Requirements
```
streamlit
sentence-transformers
pypdf
numpy
torch
```

---

## 🚀 Features
- Prompt input box
- Temperature slider
- Max output token limit
- Safety toggle
- Optional raw JSON debug output
- REST API integration (no SDK)
- Fully compatible with Hugging Face Spaces

---

## 🛠️ Tech Stack
- **Streamlit** for UI
- **Google Gemini 2.0 Flash REST API**
- **Requests** for HTTP calls
- **python-dotenv** for environment variables

---

## 📂 Installation (Local)
```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🔐 Environment Variables
Create a `.env` file:
```env
GEMINI_API_KEY=your_api_key_here
```
For testing, you can use a temporary API key.

---

## 📡 API Endpoint
```
POST https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent
```

### Payload Example
```json
{
  "contents": [
    {
      "parts": [
        { "text": "Your prompt here" }
      ]
    }
  ],
  "generationConfig": {
    "temperature": 0.7,
    "maxOutputTokens": 256
  }
}
```

---

## ▶️ Running on Hugging Face Spaces
Simply upload these files:
- `app.py`
- `requirements.txt`
- `.env`
- `README.md`

Spaces automatically executes:
```
streamlit run app.py
```

---

## 📄 License
Free to use for testing and educational purposes.

