# Recruiter Guide — DevOps Portfolio

**Owner:** Venkata Kishore Vusa  
**Role focus:** Azure DevOps Engineer · DevOps Engineer · Cloud/Platform Engineering  
**Location:** Hyderabad, India  
**Portfolio:** https://kishore2488.github.io/azure-devops-engineer-portfolio/

## Suggested 5-minute walkthrough

1. **Start with the live workflow signals.** Open the [GitHub Actions runs](https://github.com/Kishore2488/azure-devops-engineer-portfolio/actions). Explain what each workflow tests and open the logs for the latest run. A badge is a live workflow signal, not a claim that Azure, AKS, or Fabric has been deployed.
2. **Show application delivery.** Open [Project 01 — FastAPI CI](../projects/01-cicd-fastapi-app/). Walk through the health endpoint, automated tests, non-root Docker image and CI workflow.
3. **Show infrastructure automation.** Open [Project 02 — Ansible](../projects/02-ansible-real-server/). Explain inventory separation, role structure, idempotency, syntax-check/check mode, and the difference between validating a playbook and applying it to a real server.
4. **Show Kubernetes operations.** Open [Project 03 — Kubernetes](../projects/03-aks-app/). Discuss rolling updates, probes, resource requests/limits, and how you would check rollout health. The manifests are ready for a configured cluster; do not describe them as running on a live AKS cluster unless you have verified that deployment.
5. **Show release controls and security.** Use [Project 04 — Fabric operations](../projects/04-fabric-ops/) to demonstrate local release validation, then [Project 05 — DevSecOps](../projects/05-devsecops-pipeline/) to explain secret scanning, vulnerability scanning and dependency review.

## Local demo commands

Run commands from the repository root unless noted.

### Project 01 — FastAPI CI

```bash
python -m pip install -r projects/01-cicd-fastapi-app/requirements.txt pytest httpx
cd projects/01-cicd-fastapi-app
pytest -q
docker build -t portfolio-fastapi .
docker run --rm -p 8000:8000 portfolio-fastapi
```

Then visit `http://localhost:8000/health`.

### Project 02 — Ansible

Install Ansible on a Linux/macOS shell or a configured WSL environment, then:

```bash
ansible-playbook -i projects/02-ansible-real-server/inventory/dev.ini projects/02-ansible-real-server/site.yml --syntax-check
ansible-playbook -i projects/02-ansible-real-server/inventory/dev.ini projects/02-ansible-real-server/site.yml --check
```

The included inventory uses localhost, while the role configures Nginx and writes to system paths. Check mode is a validation aid, not a substitute for testing on a disposable Linux VM. Only apply the playbook on a host you control and where you intend to install/configure Nginx.

### Project 03 — Kubernetes

```bash
docker build -t aks-demo:local projects/03-aks-app
docker run --rm -p 8000:8000 aks-demo:local
kubectl apply -f projects/03-aks-app/k8s/
kubectl rollout status deployment/aks-demo
kubectl get pods,svc
```

The Kubernetes manifest references a GHCR image. Build/tag/push an image you control and update the manifest before applying to a cluster. `kubectl apply` changes the selected cluster; verify `kubectl config current-context` first. A successful container workflow alone does not prove AKS runtime health.

### Project 04 — Fabric release validation

```bash
python projects/04-fabric-ops/validate.py projects/04-fabric-ops/sample.json
```

This validates the supplied sample data locally. The REST client is an integration skeleton; a real Fabric API call requires a valid workspace, tenant configuration and runtime token. Do not store tokens in source control.

### Project 05 — DevSecOps

Open the [security workflow](../.github/workflows/project-05-security.yml) and inspect the latest run. Review the Gitleaks, Trivy and dependency-review logs. Security tools can report findings that need triage; do not claim a clean security posture solely because the workflow file exists.

## What is actually live?

- **Live website:** the static portfolio hosted by GitHub Pages.
- **Workflow status:** shown by badges and the [Actions run history](https://github.com/Kishore2488/azure-devops-engineer-portfolio/actions); check the latest run before presenting a pass.
- **Locally verifiable:** FastAPI tests and Docker build, Ansible syntax/lint checks, Fabric sample validation, Kubernetes manifest review and security workflow execution.
- **Not implied:** a running public API, an active AKS cluster, or a live Fabric workspace deployment. Those require explicit target infrastructure and verification.

## Interview framing

Use the projects to explain the engineering decision, the validation performed, the failure modes considered, and the evidence in the workflow logs. Be specific about what you personally implemented and avoid presenting sample validation as production deployment experience.

## Contact

Email: [venkatakishorevusa@gmail.com](mailto:venkatakishorevusa@gmail.com)  
GitHub: https://github.com/Kishore2488
