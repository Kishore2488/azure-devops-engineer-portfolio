# Project 04 — Microsoft Fabric Deployment Operations

Includes local release validation and an integration-ready REST client for retrieving a Fabric workspace.

## Run the local validation
```bash
python validate.py sample.json
```

## Connect to a Fabric workspace
Set a valid Fabric API access token and workspace ID in the environment, never in source:
```bash
# PowerShell
$env:FABRIC_TOKEN = "<runtime-token>"
$env:FABRIC_WORKSPACE_ID = "<workspace-id>"
python api_client.py
```

The REST client requires an identity/token authorized for the Fabric API. The local validator runs without cloud credentials. A successful local check does not imply that a live Fabric tenant was accessed.
