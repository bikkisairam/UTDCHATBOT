---
language: python
package_manager: pip
test_runner: none
test_command: N/A
test_file_pattern: N/A
require_tests: false
---
## Module Map
| Directory | Language | Purpose |
|---|---|---|
| . | Python | Flask RAG server, notebooks, data, config |
| templates/ | HTML/CSS/JS | Web chat UI |

## Tech Stack
| Component | Technology |
|---|---|
| Backend | Flask |
| RAG | FAISS, OpenAI embeddings/chat |
| Data | Pandas, NumPy, pickle DataFrame |
| Frontend | HTML, CSS, Vanilla JS |

## System Architecture
| Step | Interaction |
|---|---|
| UI → API | Browser sends POST /ask with JSON {question} |
| API → Retrieval | app.py embeds query, FAISS top-k search over embeddings |
| API → LLM | OpenAI GPT-4 generates answer from retrieved context |
| API → UI | JSON {answer} response |

## Key Interfaces & Contracts
| Interface | Contract |
|---|---|
| GET / | Renders templates/index.html |
| POST /ask | Request: {question: string} → Response: {answer: string} |
| Data file | chunks_with_openai_embeddings.pkl with columns url, section, chunk_id, text, embedding |
| OpenAI | model=text-embedding-ada-002, model=gpt-4 |

## Coding Conventions
| Area | Convention |
|---|---|
| Functions | snake_case (normalize, retrieve_chunks, generate_answer) |
| Errors | no explicit handling; exceptions bubble |
| Globals | index and df created at import/startup |

## Test Patterns
| Aspect | Details |
|---|---|
| Test framework | none detected |
| Test location | N/A |
| Execution | N/A |