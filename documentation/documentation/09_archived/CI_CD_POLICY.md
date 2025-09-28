---
Document ID: RC-QMS-014
Title: CI/CD Governance Policy
Version: 1.0.0
Effective Date: 2025-09-22
Prepared By: DevOps Lead
Reviewed By: Quality Lead
Approved By: Chief Operating Officer
Related Documents: RC-QMS-001; RC-QMS-003; RC-QMS-013
---

# CI/CD Governance Policy

## 1. Purpose
Define standards for GitHub Actions workflows supporting the Rod-Corp ISO 9001 QMS, ensuring pipelines remain secure, efficient, and auditable.

## 2. Workflow Structure Requirements
- Maintain separate workflows for continuous integration (`Continuous Integration`) and reusable validation logic (`Documentation Register Validation`).
- Workflows must use descriptive job and step names aligned with functional outcomes (e.g., "Validate Documentation Registers").
- Trigger filters (`paths`, branch restrictions) shall ensure runs execute only for relevant changes.
- Reusable workflows (`workflow_call`) are required for common validation logic to enforce DRY principles.

## 3. Performance & Reliability Controls
- Cache language dependencies using `actions/cache` with commit-pinned SHAs.
- Configure concurrency to cancel superseded runs on identical refs.
- Enforce workflow and job timeouts (default ≤ 15 minutes) to prevent runaway executions.
- Order jobs so quick validation steps execute before long-running tasks; additional jobs must declare explicit dependencies.

## 4. Security Controls
- Pin all third-party actions to full-length commit SHAs.
- Restrict `GITHUB_TOKEN` permissions to least privilege (read-only for CI validation).
- Store secrets exclusively in GitHub encrypted secrets or environment-level secrets; no secrets committed to repository files.
- Require manual approval (protected environments) for deployments that access production secrets.
- Disable automatic execution of workflows from untrusted forks; require manual approval for `pull_request_target` events.

## 5. Monitoring & Reporting
- Each workflow must append concise run outcomes to `$GITHUB_STEP_SUMMARY` to surface critical metrics (e.g., register counts, test coverage).
- Configure notifications via approved channels (Slack/Teams/email) following `docs/iso9001/templates/NOTIFICATION_GUIDANCE.md`.
- Review GitHub Actions insights monthly to identify bottlenecks and optimize caching/matrix strategies.

## 6. Compliance & Maintenance
- DevOps Lead owns upkeep of CI/CD workflows, with annual review captured in `docs/iso9001/REVIEW_CALENDAR.md`.
- Changes to workflows must reference this policy in pull request descriptions and update `docs/iso9001/CHANGE_LOG.md`.
- Nonconformities discovered in CI/CD pipelines are logged via RC-QMS-005 and tracked in corrective action records.

## 7. References
- GitHub Actions security hardening guide
- Rod-Corp Secure Coding Standard (pending migration)
- ISO 9001:2015 Clauses 7.1 (Resources) and 8.5 (Production and service provision)

---
**Change History**
- 1.0.0 (2025-09-22): Initial CI/CD governance policy issued.
