# 01 — Production CI/CD FastAPI Service

A real runnable Python API with tests, a hardened container image and GitHub Actions CI.

## Run locally

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate
pip install -r requirements.txt pytest httpx
uvicorn app.main:app --reload
```

Open `http://localhost:8000/docs`.

## Engineering demonstrated

- Automated unit/API tests
- Docker build
- GitHub Actions
- Non-root container
- Health endpoint
- Pull-request validation
