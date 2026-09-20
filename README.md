# Azure DevOps Engineer Portfolio

Production-style DevOps portfolio demonstrating the skills represented in my resume: Azure DevOps, GitHub Actions, YAML multi-stage CI/CD, Ansible, Kubernetes/AKS, Microsoft Fabric, Azure Key Vault, Microsoft Entra ID, RBAC, GitHub Advanced Security, monitoring, and AWS certifications.

> **Portfolio goal:** demonstrate how I design, automate, secure, validate, deploy, and troubleshoot cloud workloads rather than simply listing technologies.

## What this repository demonstrates

| Area | Demonstration |
|---|---|
| CI/CD | Reusable GitHub Actions workflows, environment gates, release tagging, validation and rollback patterns |
| Azure | Bicep structure for resource groups, Key Vault, Storage, VNets and AKS |
| Ansible | Reusable roles/playbooks for standardized environment configuration |
| Kubernetes | Base + Dev/Prod overlays, probes, resource limits and rollout strategy |
| Microsoft Fabric | Deployment validation, Lakehouse/Warehouse checks, sync/runbook patterns |
| Security | Key Vault references, Entra ID/RBAC, CODEOWNERS, secret scanning and dependency scanning |
| Operations | Azure Monitor/Log Analytics concepts, incident runbooks and post-deployment checks |
| Certifications | Evidence index for AWS Certified DevOps Engineer and AWS Certified Cloud Practitioner |

## Portfolio projects

### 01 — Multi-environment CI/CD
`/.github/workflows/`

A reusable pipeline pattern for **Dev → QA → SIT → UAT → PERF → PROD**, including validation gates and environment-specific configuration.

### 02 — Ansible Environment Automation
`/ansible/`

Reusable Ansible role structure for repeatable server/application configuration with inventory separation and idempotent tasks.

### 03 — AKS Deployment Pattern
`/kubernetes/`

Kubernetes manifests organized using a base and environment overlays. Includes health probes, resource controls and safe rollout conventions.

### 04 — Azure Infrastructure as Code
`/azure/bicep/`

Bicep starter modules showing how Azure infrastructure can be version-controlled and deployed consistently.

### 05 — Microsoft Fabric Deployment Operations
`/fabric/`

Runbooks and validation patterns for Fabric Lakehouse/Warehouse deployments, post-deployment notebook execution, synchronization checks and capacity monitoring.

### 06 — DevSecOps Governance
`/security/` and `.github/`

Repository governance patterns including CODEOWNERS, dependency/secret scanning, least-privilege access and secure secret handling.

## Certifications

- AWS Certified DevOps Engineer
- AWS Certified Cloud Practitioner

Certification details and verification links should be added in [`docs/certifications/README.md`](docs/certifications/README.md).

## Architecture

See [`docs/architecture/portfolio-architecture.md`](docs/architecture/portfolio-architecture.md).

## Security principles

- Never commit credentials, tokens, private keys or real connection strings.
- Use Azure Key Vault / GitHub environment secrets for runtime secrets.
- Use managed identities or federated identity where supported.
- Keep deployment permissions scoped to the required environment.
- Treat this repository as public-safe: examples use placeholders only.

## Suggested GitHub repository settings

1. Protect `main`.
2. Require pull requests and successful CI checks.
3. Add `CODEOWNERS` review requirements.
4. Enable secret scanning and dependency scanning where available.
5. Create GitHub Environments: `dev`, `qa`, `sit`, `uat`, `perf`, `prod`.
6. Store cloud credentials as environment secrets or use OIDC/federated credentials.
7. Require approval for production deployments.

## Resume alignment

This portfolio maps directly to the resume's stated experience in CI/CD, GitHub administration, Ansible automation, AKS, Microsoft Fabric, RBAC, Entra ID, Key Vault, monitoring and governance. The resume reports a 25% deployment-reliability improvement and 40% reduction in manual environment setup time; those figures should remain tied to real project evidence when presented externally.
