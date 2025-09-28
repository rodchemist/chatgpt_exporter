---
Document ID: RC-QMS-013
Title: Enterprise Risk Register
Version: 1.0.0
Effective Date: 2025-09-22
Prepared By: Risk Manager
Reviewed By: Quality Lead
Approved By: Chief Operating Officer
Related Documents: RC-QMS-001; RC-QMS-007; RC-NC-2025-001
---

# Enterprise Risk Register (Initial Baseline)

| Risk ID | Category | Description | Likelihood | Impact | Mitigation Owner | Mitigation Plan | Status | Next Review |
|---------|----------|-------------|------------|--------|------------------|-----------------|--------|-------------|
| RSK-2025-001 | Operations | Autoscale nodes missing critical secrets causing service downtime | Medium | High | Platform Operations Lead | Harden deployment checklist and enforce secret validation job in CI | In progress | 2025-10-05 |
| RSK-2025-002 | Infrastructure | Shared storage mounts remount read-only after kernel updates | Medium | Medium | Infrastructure Lead | Update fstab defaults, automate mount validation post-patch | In progress | 2025-10-10 |
| RSK-2025-003 | Documentation | Legacy docs diverge from production runbooks leading to invalid configs | High | High | Documentation Manager | Complete legacy migration plan and add sync checks in CI | Open | 2025-09-29 |
| RSK-2025-004 | Security | Unreviewed GitHub Actions pull requests from forks execute privileged steps | Low | High | DevOps Lead | Require approval for forked workflow runs and review permissions; implement notification channel per policy | In progress | 2025-10-01 |

## Notes
- Register will be reviewed during each management review and after significant incidents.
- Additional risks will be appended with new IDs in chronological order.
