## Vision
Purpose: RAG chatbot answering UT Dallas questions using indexed UTD web content
Users: Students, prospective students, and visitors seeking UTD information

## Target Personas
| Persona | Pain Point | Goal |
|---|---|---|
| Prospective Student | Hard to find accurate UTD program info | Ask questions and get concise answers |
| Current Student | Need quick campus/policy info | Retrieve trusted UTD details fast |
| Visitor/Parent | Scattered web pages | Single chat interface for UTD info |

## MVP Scope
In Scope:
- Flask web app with chat UI
- RAG pipeline with FAISS vector search
- OpenAI embeddings and GPT-4 answers
- Indexed UTD content from precomputed embeddings
Out of Scope:
- User accounts or persistence
- Live web crawling
- Admin analytics dashboard

## Strategic Constraints
| Constraint | Reason |
|---|---|
| Requires OpenAI API key | Embeddings and GPT-4 calls |
| Requires precomputed embeddings file | App loads chunks_with_openai_embeddings.pkl on startup |
| Local data storage | FAISS index built in-memory at startup |
