from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
import faiss
from openai import OpenAI

app = Flask(__name__)

# --- Load Data & Build Index on Startup ---
df = pd.read_pickle("chunks_with_openai_embeddings.pkl")  
# Ensure df has columns: url, section, chunk_id, text, embedding (np.array)

# Normalize helper
def normalize(v: np.ndarray) -> np.ndarray:
    return v / np.linalg.norm(v)

# Build FAISS index
emb_matrix = np.stack(df["embedding"].apply(normalize).values)
d = emb_matrix.shape[1]
index = faiss.IndexFlatIP(d)
index.add(emb_matrix)

# OpenAI client for embeddings & chat
client = OpenAI(api_key="Your OpenAiApi Key")


# --- Retrieval Function ---
def retrieve_chunks(query: str, k: int = 5):
    resp = client.embeddings.create(
        input=[query], model="text-embedding-ada-002"
    )
    qv = normalize(np.array(resp.data[0].embedding))
    D, I = index.search(qv.reshape(1, -1), k)
    results = []
    for idx in I[0]:
        row = df.iloc[idx]
        results.append({
            "url": row.url,
            "section": row.section,
            "text": row.text
        })
    return results


# --- RAG Answer Function ---
def generate_answer(query: str) -> str:
    top = retrieve_chunks(query, k=5)
    context = "\n\n".join(
        f"{c['text']}\n(Source: {c['url']}, Section: {c['section']})"
        for c in top
    )
    prompt = (
        "You are a helpful UT Dallas assistant.\n\n"
        "Use only the context below to answer the question. "
        "If you list items, format them as bullet points.\n\n"
        f"Context:\n{context}\n\n"
        f"Question:\n{query}\n\n"
        "Answer:"
    )
    resp = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return resp.choices[0].message.content


# --- Routes ---
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "")
    answer = generate_answer(question)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
