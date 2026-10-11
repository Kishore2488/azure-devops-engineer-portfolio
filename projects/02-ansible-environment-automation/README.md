# 02 — Ansible Environment Automation

Reusable Ansible automation for standardizing application-server configuration across Dev, QA, UAT and Production.

## Demonstrates
- Idempotent Ansible roles
- Inventory separation
- Variables and templates
- Handler-driven service restarts
- Repeatable environment configuration
- Reduced manual setup and configuration drift

## Structure

```
ansible/
├── inventory/
├── playbook.yml
└── roles/webserver/
    ├── tasks/
    ├── handlers/
    ├── templates/
    └── defaults/
```

## Run locally

`ansible-playbook -i inventory/dev.ini playbook.yml --check`

The check mode keeps the portfolio demonstration safe and does not require production access.
