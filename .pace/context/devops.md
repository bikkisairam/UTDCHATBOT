## CI/CD

| Trigger | Workflow | Jobs |
|---|---|---|
| None | No CI/CD configured | — |

## Environment Variables

| Name | Required | Purpose |
|---|---|---|
| OPENAI_API_KEY | Yes | OpenAI API authentication for embeddings + GPT-4 |
| FLASK_ENV | No | Set to "production" to disable debug mode |
| PORT | No | Server port (default: 8000) |

## Local Dev

1. Clone repo and install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Set OpenAI API key (currently hardcoded, should be env var):
   ```
   export OPENAI_API_KEY="sk-..."
   ```

3. Ensure data files exist:
   - `chunks_with_openai_embeddings.pkl` (required at startup)
   - If missing, run `Embedding.ipynb` to generate from `heading_sliding_chunks.csv`

4. Run Flask server:
   ```
   python app.py
   ```

5. Access UI at `http://localhost:8000`

## Deployment

Deploy: Manual deployment (no Dockerfile or platform config)

**Pre-deployment steps:**
- Generate embeddings: Run `Embedding.ipynb` to create `.pkl` file
- Upload `.pkl` file via git-lfs (listed in requirements.txt)
- Set OPENAI_API_KEY environment variable
- Set FLASK_ENV=production
- Configure HTTPS/reverse proxy (e.g., nginx)

**Recommended platform:** Heroku, Fly.io, or AWS EC2 with gunicorn
