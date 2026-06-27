## Sensitive Data
| Data | Where Stored | Protection |
|---|---|---|
| OpenAI API key | app.py in code (client = OpenAI(api_key=...)) | None in repo; should use env var |
| UTD content chunks | chunks_with_openai_embeddings.pkl | Local file, no encryption noted |

## Trust Boundaries
| Caller | Callee | Auth Method |
|---|---|---|
| Browser | Flask /ask | None |
| Flask | OpenAI API | API key |

## Security Requirements
- Use environment variable for OpenAI API key
- Validate JSON input for /ask
- Avoid exposing internal file paths in errors
- Run server without debug in production

## Security Checklist
OpenAI API key not hardcoded: fail
/ask input validation: fail
HTTPS enforced: fail
Debug mode disabled: fail