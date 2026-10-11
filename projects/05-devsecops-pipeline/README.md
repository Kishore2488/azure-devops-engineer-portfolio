# 05 — Real DevSecOps Delivery Pipeline

A real GitHub Actions security gate that runs secret scanning, dependency review and filesystem vulnerability scanning.

The pipeline fails on HIGH/CRITICAL Trivy findings and detected secrets. It uses GitHub's ephemeral workflow token and does not store cloud credentials in the repository.

Push a branch or open a pull request to execute it automatically.
