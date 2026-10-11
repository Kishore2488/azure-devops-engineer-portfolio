# 03 — Containerized Application for AKS

A real containerized FastAPI application with Kubernetes manifests and a GitHub Actions image build/publish workflow.

## Local

```bash
docker build -t aks-demo .
docker run --rm -p 8000:8000 aks-demo
```

## Kubernetes

```bash
kubectl apply -f k8s/
kubectl rollout status deployment/aks-demo
kubectl get pods,svc
```

For AKS, point the deployment image to your registry and apply the same manifests.

## Demonstrates

Container build/publish, Kubernetes rolling updates, readiness/liveness probes, resource controls and rollout verification.
