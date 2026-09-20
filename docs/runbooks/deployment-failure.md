# Deployment Failure Runbook

## 1. Detect

Capture workflow run, environment, commit/tag, failed stage and timestamp.

## 2. Classify

- Authentication / RBAC
- Secret/configuration
- Build/package
- Infrastructure
- Kubernetes workload
- Fabric synchronization/data dependency
- Capacity/performance

## 3. Contain

Pause promotion to subsequent environments when the failure could propagate.

## 4. Diagnose

Review workflow logs, Azure activity logs, Kubernetes events and relevant application/Fabric logs.

## 5. Recover

Use the approved rollback or forward-fix procedure. Never delete production resources as an improvised rollback.

## 6. Verify

Run pre-defined post-deployment checks and record evidence.

## 7. Prevent recurrence

Document root cause, contributing factors and the automation/governance change that prevents repetition.
