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
| . | Python | Flask RAG server, notebooks, data files |
| templates | HTML/JS/CSS | Chat UI template |

## Tech Stack
| Component | Technology |
|---|---|
| Backend | Flask |
| RAG Index | FAISS IndexFlatIP |
| Embeddings | OpenAI text-embedding-ada-002 |
| LLM | OpenAI GPT-4 |
| Data | pandas DataFrame, pickle |
| UI | HTML/CSS/JS (vanilla) |

## System Architecture
| Flow | Details |
|---|---|
| Startup | app.py loads chunks_with_openai_embeddings.pkl, normalizes vectors, builds FAISS index |
| Query | /ask POST -> generate_answer -> retrieve_chunks -> OpenAI embeddings + FAISS search |
| Response | GPT-4 completion built from retrieved context -> JSON {answer} -> browser UI |

## Key Interfaces & Contracts
| Interface | Input | Output |
|---|---|---|
| POST /ask | JSON {question:string} | JSON {answer:string} |
| GET / | None | templates/index.html |
| DataFrame schema | url, section, chunk_id, text, embedding(np.array) | Used by retrieval |

## Coding Conventions
| Area | Convention |
|---|---|
| Functions | snake_case (normalize, retrieve_chunks) |
| Responses | Flask jsonify for JSON |
| Prompting | Context + question, bullet format instruction |

## Test Patterns
| Aspect | Status |
|---|---|
| Test framework | None detected |
| Test files | None detected |
| Execution | N/A |