# 03 — AKS Kubernetes Deployment

A Kubernetes deployment pattern designed for Azure Kubernetes Service (AKS), with safe defaults for probes, resource limits, rolling updates and service exposure.

## Demonstrates
- Kubernetes Deployments and Services
- Readiness and liveness probes
- CPU/memory requests and limits
- Rolling update strategy
- Environment overlays
- Container-first deployment thinking

## Validate

`kubectl apply --dry-run=client -f manifests/`

No cluster or cloud credentials are required for validation.
