# Project 03 — Containerized AKS Application

FastAPI app, non-root Docker image, Kubernetes Deployment and ClusterIP Service.

Run locally:
```bash
docker build -t aks-demo .
docker run --rm -p 8000:8000 aks-demo
```

Deploy to a Kubernetes context you control:
```bash
kubectl apply -f k8s/
kubectl rollout status deployment/aks-demo
kubectl get pods,svc
```

The GHCR workflow publishes the image on pushes affecting this project. Check Actions before using the published image; publishing is not the same as a live AKS deployment.
