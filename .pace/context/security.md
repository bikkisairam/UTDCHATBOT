## Sensitive Data
| Data | Where Stored | Protection |
|---|---|---|
| OpenAI API key | app.py (hardcoded placeholder) | Must be provided securely by operator |
| UTD content embeddings | chunks_with_openai_embeddings.pkl | Local file only |

## Trust Boundaries
| Caller | Callee | Auth Method |
|---|---|---|
| Browser | Flask /ask | None (public endpoint) |
| Flask | OpenAI API | API key |

## Security Requirements
- Do not hardcode real API keys in source files
- Restrict access to embedding pickle file to trusted hosts
- Validate/limit request size for /ask

## Security Checklist
API keys stored outside repo: fail
Authentication on /ask: fail
Rate limiting on /ask: fail
Transport security (HTTPS) specified: fail
