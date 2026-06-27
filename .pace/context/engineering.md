---
language: python
package_manager: pip
test_runner: N/A
test_command: N/A
test_file_pattern: N/A
require_tests: false
---
## Module Map
| Directory | Language | Purpose |
|---|---|---|
| . | Python | Flask RAG API server and notebooks |
| templates/ | HTML/CSS/JS | Web chat UI template |

## Tech Stack
| Component | Technology |
|---|---|
| Backend API | Flask |
| Vector Search | FAISS (IndexFlatIP) |
| Embeddings | OpenAI text-embedding-ada-002 |
| LLM | OpenAI GPT-4 |
| Data | Pandas DataFrame pickle |
| Frontend | Vanilla HTML/CSS/JS |

## System Architecture
| Flow | Details |
|---|---|
| Startup | app.py loads chunks_with_openai_embeddings.pkl, builds FAISS index |
| Query | /ask -> generate_answer -> retrieve_chunks -> OpenAI embeddings + FAISS search |
| Response | GPT-4 chat completion with retrieved context |
| UI | templates/index.html calls /ask via fetch |

## Key Interfaces & Contracts
| Interface | Type | Details |
|---|---|---|
| GET / | HTTP | Renders templates/index.html |
| POST /ask | HTTP JSON | Request: {"question": "..."}; Response: {"answer": "..."} |
| chunks_with_openai_embeddings.pkl | Data file | Columns: url, section, chunk_id, text, embedding |

## Coding Conventions
| Topic | Convention |
|---|---|
| Functions | snake_case (normalize, retrieve_chunks, generate_answer) |
| Flask | app = Flask(__name__), route decorators |
| Embedding normalization | L2 normalization before FAISS search |

## Test Patterns
| Area | Status |
|---|---|
| Automated tests | None detected |
