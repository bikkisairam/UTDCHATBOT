---
language: python
package_manager: pip
test_runner: none
test_command: none
test_file_pattern: none
require_tests: false
---
## Module Map
| Directory | Language | Purpose |
|---|---|---|
| . | Python | Flask app, data files, notebooks |
| templates/ | HTML/JS/CSS | Chat UI template |

## Tech Stack
| Component | Technology |
|---|---|
| Backend | Flask |
| RAG Retrieval | FAISS, NumPy, pandas |
| LLM/Embeddings | OpenAI API (gpt-4, text-embedding-ada-002) |
| Frontend | HTML, CSS, Vanilla JS |
| Notebooks | Jupyter (.ipynb) |

## System Architecture
| Step | Component | Interaction |
|---|---|---|
| 1 | Browser | Loads / (index.html) |
| 2 | Browser → Flask | POST /ask with question JSON |
| 3 | Flask | Embeds query, searches FAISS index |
| 4 | Flask → OpenAI | Chat completion with context |
| 5 | Flask → Browser | JSON response {answer} |

## Key Interfaces & Contracts
| Interface | Method | Input | Output |
|---|---|---|---|
| / | GET | none | HTML page |
| /ask | POST | JSON {question: string} | JSON {answer: string} |
| Data file | N/A | chunks_with_openai_embeddings.pkl | DataFrame with url, section, chunk_id, text, embedding |

## Coding Conventions
| Item | Convention |
|---|---|
| Functions | snake_case (normalize, retrieve_chunks, generate_answer) |
| API | Flask route decorators |
| Vector search | L2-normalize then FAISS IndexFlatIP |

## Test Patterns
| Item | Details |
|---|---|
| Tests | None detected |
| Runner | none |
