# UT Dallas RAG Chatbot 

An end-to-end Retrieval-Augmented Generation (RAG) chatbot for University of Texas at Dallas content, built entirely in a Jupyter/Colab notebook with a Gradio interface.

---

## 🚀 Project Overview

This notebook demonstrates how to:

1. **Chunk** 4,600+ UTD web pages under headings with 150-token windows (50-token overlap).
2. **Embed** \~49K text chunks using OpenAI’s `text-embedding-ada-002` in batched calls.
3. **Index** the normalized embeddings in a FAISS vector store for sub-second retrieval.
4. **Retrieve** top-K relevant chunks for any user query.
5. **Generate** concise, bullet-formatted answers with GPT-4.
6. **Validate** accuracy on a ground-truth QA set.
7. **Launch** an interactive Gradio chat UI—straight from the notebook.

---

## 🔧 Key Steps in the Notebook

1. **Chunking**

   - Load `scraped_pages.json` containing `{url, elements}`
   - Group by `<h1>`/`<h2>` and apply a sliding window
   - Filter out navigation/junk lines

2. **Embedding**

   - Read `heading_sliding_chunks.csv` (columns: url, section, chunk\_id, text)
   - Batch-encode with OpenAI in 64-item batches, printing progress every 2,000
   - Save embeddings back to a DataFrame

3. **Indexing**

   - Normalize all vectors
   - Build a FAISS `IndexFlatIP` for cosine similarity

4. **Retrieval & Generation**

   - Define `retrieve_chunks(query, k=5)` → returns top-K `{url, section, text}`
   - Define `generate_answer(query)` → builds GPT-4 prompt and returns the bot’s reply

5. **Validation**

   - Prepare `validation.csv` (50 QA pairs)
   - Compute a similarity score (difflib ratio) vs. ground truth
   - Report overall accuracy and low-confidence cases

6. **Gradio UI**

   - Use `gradio` Blocks in-notebook
   - Chatbot with user/bot bubbles, Clear button, real-time conversation

---

## 📋 Prerequisites

- Python ≥ 3.8
- Jupyter Notebook or Google Colab
- An OpenAI API key with access to `text-embedding-ada-002` and `gpt-4`
- A recent CPU/GPU for faster embedding & inference (optional)

---

## 🛠️ Installation

In your notebook or Colab:

```bash
!pip install openai faiss-cpu pandas numpy gradio
```

---

## ⚙️ Configuration

```python
import os
os.environ["OPENAI_API_KEY"] = "sk-…"   # set your key
```

---

## 📓 Notebook Outline

1. **Imports & Data Load**
2. **Chunking function** (`heading_sliding_chunker`)
3. **Batch embedding** with progress prints
4. **FAISS index build**
5. `** + **`
6. **Validation** on `validation.csv`
7. **Gradio Blocks UI**
   ```python
   with gr.Blocks() as demo:
       gr.Markdown("## 🎓 UT Dallas RAG Chatbot")
       chatbot = gr.Chatbot()
       txt = gr.Textbox(placeholder="Ask me about UTD…")
       clear = gr.Button("Clear")
       txt.submit(chat_interface, [txt, chatbot], [chatbot, chatbot])
       clear.click(lambda: [], None, chatbot)
   demo.launch()
   ```

---

## 📈 Validation

After running the validation cells, aim for ≥ 90 % accuracy. Use a hybrid static-KB fallback for core facts (e.g. president name, address) to guarantee 100 % on those.

---

## 🎯 Next Steps

- Swap GPT-4 for a local model (Mistral-7B) if desired.
- Add BM25 hybrid retrieval for exact-match queries.
- Publish as a Colab link for easy sharing.

---

*Developed by Sai Ram Bikki, July 2025*

