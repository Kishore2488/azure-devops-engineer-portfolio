# 02 — Real Server Configuration with Ansible

This is an executable Ansible deployment, not a simulation. It installs Nginx, writes the application page and ensures the service is running.

## Run against a Linux VM

Update `inventory/dev.ini` with the VM address and SSH user, then:

```bash
ansible-playbook -i inventory/dev.ini site.yml --ask-become-pass
```

For a safe preview:

```bash
ansible-playbook -i inventory/dev.ini site.yml --check
```

## Demonstrates

Ansible roles, inventory, idempotency, handlers, privilege escalation and real server configuration.
