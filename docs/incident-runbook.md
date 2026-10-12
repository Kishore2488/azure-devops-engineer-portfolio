# Deployment Incident Runbook

A practical triage template for the portfolio's CI/CD, container, Kubernetes and Microsoft Fabric examples. Use it as a repeatable checklist, and record the evidence gathered during each incident.

## 1. Incident record

- **Incident / ticket:**
- **Service / environment:**
- **First observed (UTC):**
- **Reporter / owner:**
- **Customer or business impact:**
- **Last known good release:**
- **Current status:** Investigating / Mitigating / Monitoring / Resolved
- **Communication channel:**

Do not paste access tokens, secret values, customer data, or sensitive log payloads into this record.

## 2. Stabilize first

1. Confirm scope: one deployment, one service, one environment, or a broader platform incident?
2. Identify the last known good version and compare it with the failing release.
3. Stop additional promotion if new releases could increase impact.
4. Preserve timestamps, run IDs, commit SHAs, sanitized logs, and the exact error message.
5. Prefer a known-good rollback or traffic-safe mitigation when impact is ongoing and the rollback has been assessed.
6. Assign an incident owner and keep updates factual.

Do not run destructive commands against production as a diagnostic shortcut. Confirm the target account, cluster, namespace and environment before taking action.

## 3. GitHub Actions / CI-CD failure

### Triage

- Open the failed run and identify the first failing step, not just the final summary.
- Record the workflow file, commit SHA, branch, trigger event, run ID and runner type.
- Separate code/test failures from permissions, dependency download, artifact, environment approval and deployment failures.
- Check recent changes to action versions, package lockfiles, runner images, workflow permissions and environment protection rules.
- Inspect sanitized logs; never print secrets or enable verbose output that could reveal credentials.

### Useful checks

```bash
git status --short
git log -5 --oneline
git diff <last-known-good-sha>...<failing-sha>
```

For GitHub-hosted runs, use the Actions run page to inspect job and step logs. If the failure is reproducible locally, run the narrowest failing test or validation command before retrying the full workflow.

### Recovery

- Fix the root cause on a branch and let required checks run.
- Re-run only after confirming the failure is transient or the fix is present.
- Do not bypass required checks or production approvals to make a badge green.
- Confirm the deployment target and verify health after a successful deploy.

## 4. Kubernetes / AKS rollout failure

### Read-only diagnosis

Confirm you are connected to the intended cluster before querying it:

```bash
kubectl config current-context
kubectl get deployments,pods,services
kubectl rollout status deployment/<deployment-name>
kubectl describe deployment/<deployment-name>
kubectl get events --sort-by=.metadata.creationTimestamp
kubectl logs deployment/<deployment-name> --all-containers=true --tail=100
```

Use the correct namespace with `-n <namespace>` where applicable. Review pod events for image pull errors, failed probes, unschedulable resources, missing configuration or crash loops. Do not dump Secret objects or environment values into shared logs.

### Rollback decision

```bash
kubectl rollout history deployment/<deployment-name>
kubectl rollout undo deployment/<deployment-name>
kubectl rollout status deployment/<deployment-name>
```

Only perform a rollback after confirming the context, namespace, deployment owner and previous revision. A rollback changes the selected cluster. Afterwards, verify ready replicas, service endpoints, health checks and application-level behavior. Record the revision and outcome.

## 5. Container build / registry failure

- Confirm the build context and Dockerfile path are correct.
- Inspect the first failing build step and dependency resolution output.
- Confirm the workflow has only the required package permissions.
- For GHCR image pull failures, verify the image name/tag, package visibility, push result and cluster pull permissions.
- Prefer immutable version tags or commit SHAs for repeatable releases; use mutable tags such as `latest` cautiously.
- Verify the image architecture and runtime port match the deployment manifest.

Never put registry credentials into a Dockerfile, source file or build log.

## 6. Microsoft Fabric release validation failure

- Confirm the workspace and target environment are correct.
- Compare expected and actual Lakehouse/Warehouse table synchronization state.
- Validate the business keys and freshness/tiebreaker fields defined by the owning data team.
- Check the deployment/run history, dependency status and capacity signals available to the operator.
- Separate local sample validation from a real tenant/API operation.
- Do not rerun data-changing jobs until ownership, idempotency, downstream effects and recovery steps are understood.

The portfolio's sample validator is a local demonstration. A PASS on sample JSON does not establish that a live Fabric workspace or data pipeline is healthy.

## 7. Recovery verification checklist

- [ ] New deployments or promotions are stable.
- [ ] Health/readiness checks pass.
- [ ] Expected replicas or service capacity are available.
- [ ] Application or data-level smoke checks pass.
- [ ] Monitoring shows no new elevated errors or saturation.
- [ ] Stakeholders have received a concise status update.
- [ ] The failing release, mitigation and evidence are recorded.
- [ ] Follow-up actions have owners and due dates.

## 8. Post-incident review

Document the timeline, user/business impact, root cause, contributing factors, detection gap, recovery actions and evidence. Focus on system improvements rather than blame.

Possible follow-ups include adding a regression test, tightening a readiness probe, pinning a dependency/action version, adding a pre-deployment check, improving rollback rehearsal, or making an alert more actionable.

## 9. Short status update template

> **Status:** Investigating / Mitigating / Monitoring / Resolved  
> **Impact:** [confirmed scope and effect]  
> **Current action:** [specific mitigation or diagnostic step]  
> **Evidence:** [run ID, commit SHA, timestamp, sanitized error]  
> **Next update:** [time or condition]

Only report an incident as resolved after post-deployment verification, not merely because a workflow completed successfully.
