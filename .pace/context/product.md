## Vision
Purpose: Provide a UT Dallas information assistant using RAG over UTD web content
Users: Prospective students, current students, staff seeking UTD info

## Target Personas
| Persona | Pain Point | Goal |
|---|---|---|
| Prospective student | Hard to find accurate program details | Ask questions and get concise answers |
| Current student | Navigating UTD policies and services | Quick answers with sources |
| Staff/faculty | Repetitive information requests | Fast retrieval from UTD pages |

## MVP Scope
In Scope:
- RAG chatbot over UTD web content
- Web UI chat interface
- Top-K retrieval and GPT-4 answer generation
Out of Scope:
- Authentication or user accounts
- Data ingestion pipeline in app server
- Mobile app deployment

## Strategic Constraints
| Constraint | Reason |
|---|---|
| OpenAI API dependency | Embeddings and GPT-4 generation required |
| Prebuilt embeddings file | Server loads chunks_with_openai_embeddings.pkl at startup |
| Web-only UI | Single HTML template in templates/index.html |