## Vision
Purpose: RAG chatbot answering UT Dallas questions from indexed web content
Users: Prospective/current students, staff, visitors seeking UTD info

## Target Personas
| Persona | Pain Point | Goal |
|---|---|---|
| Prospective student | Needs quick answers about programs | Get accurate program details |
| Current student | Finds UTD site info fragmented | Retrieve specific policies/info fast |
| Visitor | Doesn’t know where to look on UTD site | Ask questions in natural language |

## MVP Scope
In Scope:
- RAG retrieval over UTD web content
- Chat UI with /ask endpoint
- GPT-4 answer generation with citations in context
Out of Scope:
- User accounts/authentication
- Admin content management
- Analytics/telemetry

## Strategic Constraints
| Constraint | Reason |
|---|---|
| OpenAI API key required | Embeddings + GPT-4 calls |
| Prebuilt embeddings pickle needed | Server loads chunks_with_openai_embeddings.pkl on startup |
| Data limited to indexed UTD pages | Retrieval from local FAISS index only |