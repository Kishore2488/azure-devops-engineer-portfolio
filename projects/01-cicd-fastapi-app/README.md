# Project 01 — FastAPI CI/CD

Runnable FastAPI application with tests and a non-root Docker image.

Run from this directory:
```bash
pip install -r requirements.txt pytest httpx
uvicorn app.main:app --reload
pytest -q
docker build -t kishore/cicd-fastapi-app .
```

Open `http://localhost:8000/docs`. CI workflow: `.github/workflows/project-01-ci.yml`.
