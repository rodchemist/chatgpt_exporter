---
Record ID: RC-VER-2025-003
Title: Verification Evidence – NC-005 API Gateway Liveness
Date: 2025-09-22
Prepared By: API Engineering Lead
Reviewed By: Quality Lead
Status: In Progress
Related Corrective Action: CA-2025-004; CA-2025-005
---

# Evidence Summary
- **Manifest Update:** Liveness probe updated to `/v3/healthz` in deployment manifest commit `api-gateway@b71f2db`.
- **Deployment Timestamp:** 2025-09-22 09:05 CST
- **Post-Deployment Check:** `kubectl get deployment api-gateway -o jsonpath='{.status.readyReplicas}'` returned `3`.

## Liveness Probe Output
```
$ curl -s https://api-gateway.internal/v3/healthz | jq .status
"ok"
```

## Attachments
- Screenshot of Grafana dashboard `API Gateway Health` stored in monitoring share (2025-09-22 09:10).
- Updated runbook reference `docs/runbooks/api-gateway.md` with new probe endpoint.

## Reviewer Notes
- Confirm runbook changes merged to main.
- Schedule follow-up load test to validate stability.
