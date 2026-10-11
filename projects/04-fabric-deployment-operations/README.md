# 04 — Microsoft Fabric Deployment Operations

A credential-free operations toolkit that models the validation and post-deployment checks used around Microsoft Fabric Lakehouse and Warehouse deployments.

## Demonstrates
- Pre-deployment validation
- Lakehouse/Warehouse synchronization checks
- Metadata freshness validation
- Post-deployment runbook thinking
- Capacity threshold monitoring
- Failure triage and operational documentation

## Example

`python validate_release.py sample-release.json`

The project uses local JSON fixtures so the workflow can be demonstrated without connecting to a real Fabric tenant.
