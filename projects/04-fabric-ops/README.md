# 04 — Microsoft Fabric Deployment Operations

A real integration-ready Fabric operations project. It includes a REST client skeleton for authenticated workspace access plus local release validation.

## Local validation
```bash
python validate.py sample.json
```

## Real Fabric integration
Set runtime credentials only in your shell or CI secret store:
```bash
export FABRIC_API_BASE="https://api.fabric.microsoft.com/v1"
export FABRIC_TOKEN="<runtime-token>"
export FABRIC_WORKSPACE_ID="<workspace-id>"
python api_client.py
```
Never commit the token.

## Demonstrates
Fabric API integration, workspace-aware operations, release validation, table synchronization checks and capacity monitoring.
