## Sensitive Data

| Data | Where Stored | Protection |
|---|---|---|
| OpenAI API key | Hardcoded in app.py, Embedding.ipynb | **CRITICAL: Exposed in code** |
| User queries | Sent to OpenAI API | Subject to OpenAI privacy policy |
| Scraped content | scraped_pages.json, .pkl files | Public UTD web data |
| Embeddings | chunks_with_openai_embeddings.pkl | Derived from public data |

## Trust Boundaries

| Caller | Callee | Auth Method |
|---|---|---|
| Browser | Flask /ask endpoint | None (unauthenticated) |
| Flask app | OpenAI API | Bearer token (API key) |
| Scraper | UTD web pages | Public HTTP (no auth) |

## Security Requirements

- OpenAI API key MUST be moved to environment variable or secrets manager
- Never commit API keys to version control (already violated in Embedding.ipynb)
- Flask debug mode MUST be disabled in production (currently debug=True)
- Input sanitization needed: user queries passed directly to OpenAI without validation
- Rate limiting required on /ask endpoint to prevent abuse
- HTTPS required for production deployment (no TLS config present)
- CORS policy undefined (default Flask behavior)

## Security Checklist

- [ ] API key removed from source code
- [ ] Environment variables used for secrets
- [ ] Flask debug=False in production
- [ ] Input length validation on user queries
- [ ] Rate limiting on /ask endpoint
- [ ] HTTPS/TLS certificate configured
- [ ] CORS policy defined
- [ ] .gitignore includes .env and *.pkl
- [ ] User query logging reviewed for PII
- [ ] OpenAI data retention policy understood
