## Vision

Purpose: Provide instant, accurate answers to UT Dallas questions using RAG over 4,600+ scraped university web pages.  
Users: UTD students, prospective students, staff seeking university information.

## Target Personas

| Persona | Pain Point | Goal |
|---|---|---|
| Prospective student | Hard to find admission requirements across scattered pages | Quick answers to program, scholarship, deadline questions |
| Current student | Navigating complex academic policies and resources | Find course info, advisors, financial aid details instantly |
| Staff/admin | Repeated questions from students | Self-service chatbot to reduce support load |

## MVP Scope

**In Scope**
- Semantic search over 4,600+ UTD web pages (Jindal School focus)
- 5-chunk retrieval with GPT-4 answer generation
- Flask web UI with chat interface
- Gradio notebook UI for prototyping
- 150-token chunks with 50-token overlap
- OpenAI embeddings + FAISS index

**Out of Scope**
- Real-time website updates (static scrape)
- Multi-turn conversation memory
- User authentication or personalization
- Hybrid BM25 keyword search
- Local LLM deployment (Mistral-7B)
- Mobile app

## Strategic Constraints

| Constraint | Reason |
|---|---|---|
| OpenAI API dependency | Requires API key with GPT-4 + embedding access |
| Static data snapshot | No live scraping; manual refresh needed |
| Single university scope | Built for UTD content only |
| No conversational state | Each query is independent |
| English only | No multilingual support |
