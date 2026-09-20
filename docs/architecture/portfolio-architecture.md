# Portfolio Architecture

```text
Developer
   |
   v
GitHub Repository
   |
   +--> Pull Request --> CI validation --> Review / CODEOWNERS
   |
   v
GitHub Actions
   |
   +--> Dev --> QA --> SIT --> UAT --> PERF --> PROD
   |                         |
   |                         +--> Environment approvals
   |
   +--> Azure Key Vault / Entra ID / RBAC
   |
   +--> Azure / AKS / Fabric deployment
   |
   v
Post-deployment validation
   |
   +--> Application health
   +--> Fabric synchronization / metadata
   +--> Monitoring / Log Analytics
   +--> Runbook / evidence
```

This is a portfolio architecture, not a claim that every component is deployed by this repository in production.
