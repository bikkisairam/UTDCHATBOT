# UT Dallas RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot for University of Texas at Dallas content, powered by OpenAI embeddings, FAISS vector search, and GPT-4.  

## 🚀 Features

- **Hierarchical + Sliding Window Chunking**  
- **OpenAI Embeddings** (`text-embedding-ada-002`) batched for ~49K text chunks  
- **FAISS** (cosine) index for sub-second retrieval  
- **GPT-4** answer generation with source citations  
- **Flask** backend exposing `/ask` endpoint  
- **HTML/JS** chatbot UI with UTD branding  

## 📁 Repository Structure

├── app.py # Flask server + RAG pipeline
├── chunks_with_openai_embeddings.pkl # Precomputed embeddings (git-ignored)
├── heading_sliding_chunks.csv # Chunk metadata (git-ignored)
├── requirements.txt # Python dependencies
├── .gitignore # Ignore data, env, pycache
└── templates/
└── index.html # Chat UI HTML + CSS + JS


## ⚙️ Installation

1. Clone this repo  
   ```bash
   git clone https://github.com/<your-username>/utd-rag-chatbot.git
   cd utd-rag-chatbot


python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows


pip install -r requirements.txt


export OPENAI_API_KEY="sk-…"   # macOS/Linux
set OPENAI_API_KEY="sk-…"      # Windows PowerShell


python app.py
