---
language: python
package_manager: pip
test_runner: none
test_command: ""
test_file_pattern: ""
require_tests: false
---

## Module Map

| Directory | Language | Purpose |
|---|---|---|
| . | Python | Flask web server + RAG chatbot |
| templates/ | HTML/CSS/JS | Frontend chat UI |
| Embedding.ipynb | Python | Notebook for creating FAISS embeddings |
| Scraping and Chunking.ipynb | Python | Notebook for web scraping + text chunking |

## Tech Stack

| Layer | Technology | Version/Notes |
|---|---|---|
| Language | Python | 3.8+ |
| Web Framework | Flask | Production server |
| LLM Provider | OpenAI | GPT-4 + text-embedding-ada-002 |
| Vector DB | FAISS | IndexFlatIP (cosine similarity) |
| Data | Pandas, NumPy | DataFrame manipulation |
| UI | Gradio | Notebook-based chat (optional) |
| Frontend | HTML/CSS/JS | templates/index.html |
| Scraping | aiohttp, BeautifulSoup | Async web scraping |
| Package Mgr | pip | requirements.txt |

## System Architecture

| Component | Role | Input | Output |
|---|---|---|---|
| app.py | Flask API server | HTTP POST /ask | JSON answer |
| Scraping notebook | Scrape 4,600+ UTD pages | unique_links.csv | scraped_pages.json |
| Chunking | Split text into 150-token chunks | scraped_pages.json | heading_sliding_chunks.csv |
| Embedding notebook | Batch embed with OpenAI | heading_sliding_chunks.csv | chunks_with_openai_embeddings.pkl |
| FAISS index | Normalized vector search | Query vector | Top-K chunk indices |
| retrieve_chunks() | Semantic retrieval | User query | 5 relevant text chunks |
| generate_answer() | RAG prompt + GPT-4 | Query + context | Chat response |

## Key Interfaces & Contracts

**Flask API**
- Endpoint: `POST /ask`
- Request: `{"question": "<user query>"}`
- Response: `{"answer": "<GPT-4 response>"}`

**Data Files**
- `chunks_with_openai_embeddings.pkl`: DataFrame with columns: url, section, chunk_id, text, embedding (np.array)
- `scraped_pages.json`: `[{"url": "...", "elements": [{"tag": "h1", "text": "..."}]}]`
- `heading_sliding_chunks.csv`: url, section, chunk_id, text

**Functions**
- `normalize(v: np.ndarray) -> np.ndarray`: L2 normalization
- `retrieve_chunks(query: str, k: int = 5) -> list[dict]`: Returns `[{url, section, text}]`
- `generate_answer(query: str) -> str`: Returns GPT-4 response

## Coding Conventions

| Pattern | Rule |
|---|---|
| Embedding | Batch size = 64, progress every 2,000 items |
| Normalization | Always L2-normalize before FAISS indexing/search |
| Retrieval | Default k=5 chunks, cosine similarity |
| Prompt template | "You are a helpful UTD assistant. Use only the context below..." |
| Data storage | Pickle for embeddings, CSV for chunks, JSON for raw scrape |
| Error handling | Try/except on scraping, timeout=10s |
| OpenAI client | Instantiate once on startup, reuse |

## Test Patterns

**No automated tests present.**

Manual validation approach:
- validation.csv contains 50 QA pairs
- Compute similarity score (difflib ratio) vs ground truth
- Report accurac