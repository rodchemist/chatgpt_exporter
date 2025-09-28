---
Record ID: RC-VER-2025-001
Title: Verification Evidence – NC-001 Service Restoration
Date: 2025-09-22
Prepared By: Platform Operations Lead
Reviewed By: Quality Lead
Status: In Progress
Related Corrective Action: CA-2025-001; CA-2025-002
---

# Evidence Summary
- **Services Restored:** unified_api, leantime, prometheus
- **Restart Window:** 2025-09-22 08:15-08:32 CST
- **Verification Command:** `systemctl status` captured post-restart (see log excerpt below)
- **Checklist Update:** Deployment checklist v2025.09 appended with secret injection validation step.

## Log Excerpt
```
Sep 22 08:29:41 orchestrator systemd[1]: Started unified_api.service
Sep 22 08:29:44 orchestrator healthcheck[4123]: /health -> 200 OK
Sep 22 08:30:02 orchestrator systemd[1]: Started leantime.service
Sep 22 08:30:10 orchestrator prometheus[5198]: Completed TSDB reload in 7.2s
```

## Attachments
- `logs/unified_api-2025-09-22.log` (stored in secure operations share)
- Updated deployment checklist (Git ref `ops/deployment-checklist@2025-09-22`)

## Reviewer Notes
- Confirm checklist commit merged to main branch.
- Validate healthchecks remain green after 48h observation window.
