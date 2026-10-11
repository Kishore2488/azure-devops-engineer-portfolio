# GitHub Actions → Azure Service Principal Authentication

This repository uses **GitHub OIDC (federated identity)** for Azure authentication. No Azure client secret is stored in the repository.

## Required GitHub secrets

Add these under:

**Repository → Settings → Secrets and variables → Actions**

| Secret | Value |
|---|---|
| `AZURE_CLIENT_ID` | Microsoft Entra application / service principal client ID |
| `AZURE_TENANT_ID` | Microsoft Entra tenant ID |
| `AZURE_SUBSCRIPTION_ID` | Azure subscription ID |

## Azure Service Principal

The service principal must have an appropriate Azure RBAC role at the required scope, such as:

- Resource group scope for a portfolio deployment
- Subscription scope only when genuinely required

For GitHub OIDC, create a **federated credential** on the Entra application that trusts this repository and the intended branch/environment.

Recommended subject restriction for the main branch:

```text
repo:Kishore2488/azure-devops-engineer-portfolio:ref:refs/heads/main
```

For production, prefer a GitHub Environment and restrict the federated credential to that environment rather than broadly trusting the whole repository.

## Security rules

- Do **not** commit `AZURE_CLIENT_SECRET`, passwords, tokens, certificates, or private keys.
- Prefer OIDC over long-lived client secrets for GitHub Actions.
- Keep the service principal least-privileged.
- Use GitHub Environment approvals for production deployments.
- Rotate or revoke credentials/federated trust when no longer required.

The workflow `.github/workflows/azure-auth.yml` performs a manual Azure login and verifies the active subscription without printing secrets.
