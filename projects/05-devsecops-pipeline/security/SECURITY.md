# Security Controls

- Secrets are supplied at runtime through GitHub/Azure secret stores.
- GitHub Actions uses least privilege permissions.
- Gitleaks blocks common credential leaks.
- Trivy blocks high/critical filesystem vulnerabilities.
- Dependency Review runs on pull requests.
- CODEOWNERS and branch protection should require review before production changes.
