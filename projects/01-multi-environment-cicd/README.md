# 01 — Multi-Environment CI/CD Platform

A production-style GitHub Actions deployment pattern demonstrating how an application moves through **Dev → QA → SIT → UAT → PERF → PROD** with validation, approvals and deployment strategies.

## Demonstrates
- GitHub Actions and reusable YAML
- Environment separation
- Release promotion
- Rolling, incremental and blue-green deployment concepts
- Pre/post deployment validation
- Least-privilege workflow permissions

## Flow

`commit → CI validation → Dev → QA → SIT → UAT → PERF → Prod`

This demo is intentionally cloud-credential-free. Deployment commands are represented by safe simulation steps.

## Run

Trigger `.github/workflows/deploy-demo.yml` manually and select an environment and strategy.

## Hiring signal

Shows practical ownership of multi-environment CI/CD rather than only knowing YAML syntax.
