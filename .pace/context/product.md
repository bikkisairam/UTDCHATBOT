## Vision
Purpose: Provide a UT Dallas RAG chatbot answering UTD content questions
Users: Prospective students, current students, staff needing UTD info

## Target Personas
| Persona | Pain Point | Goal |
|---|---|---|
| Prospective Student | Hard to find accurate UTD info | Get concise answers about UTD |
| Current Student | Searching UTD site is slow | Quick answers with sources |
| Staff/Faculty | Repetitive questions | Provide consistent responses |

## MVP Scope
In Scope:
- Flask API with /ask endpoint
- Retrieval over FAISS index
- GPT-4 answer generation with context
- Web chat UI (templates/index.html)
Out of Scope:
- User accounts/auth
- Admin analytics dashboard
- Multi-tenant data sources

## Strategic Constraints
| Constraint | Reason |
|---|---|
| Requires OpenAI API key | Embeddings + GPT-4 calls |
| Needs prebuilt embeddings pickle | app.py loads chunks_with_openai_embeddings.pkl |
| Source data limited to UTD pages | Retrieval from preprocessed UTD content |
