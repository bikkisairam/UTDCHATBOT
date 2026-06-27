## Sensitive Data
| Data | Where Stored | Protection |
|---|---|---|
| OpenAI API key | app.py client initialization | None in code; should be env var |
| Indexed content embeddings | chunks_with_openai_embeddings.pkl | File-based, no explicit encryption |

## Trust Boundaries
| Caller | Callee | Auth Method |
|---|---|---|
| Browser JS | Flask /ask | None |
| Flask app | OpenAI API | API key |

## Security Requirements
- Set OpenAI API key via environment variable, not hardcoded
- Validate and sanitize JSON input for /ask
- Restrict network exposure if running locally

## Security Checklist
OpenAI key hardcoded: fail
Auth on /ask: fail
Input validation on /ask: fail
TLS enforced: unknown