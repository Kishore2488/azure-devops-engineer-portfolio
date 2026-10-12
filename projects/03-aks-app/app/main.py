from fastapi import FastAPI
app = FastAPI(title="AKS Demo")
@app.get("/")
def root():
    return {"service": "aks-demo", "status": "running"}
@app.get("/health")
def health():
    return {"status": "healthy"}
