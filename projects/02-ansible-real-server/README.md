# Project 02 — Ansible Real Server Deployment

Installs Nginx, deploys a landing page and manages the service using an Ansible role and handler.

Update `inventory/dev.ini` with your Linux host and SSH user, then run:
```bash
ansible-playbook -i inventory/dev.ini site.yml --syntax-check
ansible-playbook -i inventory/dev.ini site.yml --check
ansible-playbook -i inventory/dev.ini site.yml --ask-become-pass
```

Only run the final command against a host you administer. CI validates syntax/lint; it does not change a production server.
