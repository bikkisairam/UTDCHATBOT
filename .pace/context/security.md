## Sensitive Data
| Data | Where Stored | Protection |
|---|---|---|
| OpenAI API key | app.py (hardcoded string) | None in code; should use env var |
| UTD content embeddings | chunks_with_openai_embeddings.pkl | Local file only |

## Trust Boundaries
| Caller | Callee | Auth Method |
|---|---|---|
| Browser UI | Flask /ask | None |
| Flask app | OpenAI API | API key in client |

## Security Requirements
- Use environment variable for OPENAI_API_KEY
- Do not log user queries with PII
- Validate /ask input is JSON with question string
- Restrict model access keys to required scopes

## Security Checklist
- [fail] API key is hardcoded in app.py
- [fail] No input validation on /ask
- [pass] Uses POST for queries
