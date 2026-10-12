from datetime import datetime, timezone
from fastapi import FastAPI

app = FastAPI(title="Kishore DevOps API", version="1.0.0")

@app.get("/health")
def health():
    return {"status": "healthy", "timestamp": datetime.now(timezone.utc).isoformat()}

@app.get("/api")
def api():
    return {"service": "cicd-fastapi-app", "version": "1.0.0"}
