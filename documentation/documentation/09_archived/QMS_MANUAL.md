---
Document ID: RC-QMS-001
Title: Quality Management System Manual
Version: 1.0.0
Effective Date: 2025-09-22
Prepared By: Documentation Automation Team
Reviewed By: Pending
Approved By: Pending
Related Documents: RC-QMS-002, RC-QMS-003, RC-QMS-004
---

# Quality Management System Manual

## 1. Purpose & Scope
- Defines the Rod-Corp AI System Quality Management System (QMS) covering design, development, deployment, and maintenance of AI agents, automations, and supporting services.
- Applies to all activities performed within `rod-corp` and associated operational repositories, including legacy knowledge retained for reference.
- Exclusions: Physical manufacturing processes (handled externally) and third-party hosted services outside Rod-Corp control.

## 2. Normative References
- ISO 9001:2015 Quality Management Systems Requirements.
- ISO/IEC 27001:2022 (informative alignment for information security).
- Rod-Corp corporate governance guidelines.

## 3. Terms & Definitions
- **Documented Information**: Controlled documents and records defined in this manual.
- **Controlled Document**: Any item listed in `DOCUMENT_REGISTER.csv` with an assigned Document ID.
- **Record**: Evidence captured through audits, reviews, testing, or operations; listed in `RECORD_REGISTER` (to be established).

## 4. Context of the Organization
- Internal issues: Rapid evolution of AI services, need for consistent documentation, and reliance on automated agents.
- External issues: Regulatory compliance, client assurance, data privacy expectations.
- Interested parties: Executive leadership, engineering teams, compliance officers, customers, and integration partners.

## 5. Leadership
- Executive leadership commits to quality through policy RC-QMS-002 and ensures sufficient resources.
- Responsibilities and authorities defined in Section 8; the Documentation Manager is custodian of controlled documentation.

## 6. Planning
- Risks and opportunities tracked via the Enterprise Risk Register (RC-QMS-013) with quarterly review.
- Quality objectives defined in RC-QMS-002 with metrics for documentation accuracy, review cadence, and audit closure.
- Change management executed per RC-QMS-004.

## 7. Support
- Resources: Version control (Git), automation scripts, knowledge base.
- Competence: Personnel managing documentation must complete ISO 9001 awareness training.
- Awareness: All contributors briefed on document control procedure (RC-QMS-003).
- Communication: Change notifications issued to stakeholders upon document approval.
- Documented information maintained via registers and stored within repository-managed folders.
- CI/CD governance (RC-QMS-014) enforces consistent automation practices that protect documentation integrity.

## 8. Operation
- Operational planning relies on runbooks, SOPs, and workflows catalogued in `docs/knowledge/`.
- Design & development controls follow project lifecycle documented in RC-SOP series (to be issued).
- External provider management handled through vendor checklists (planned deliverable).
- Production and service provision guided by service manuals and test reports stored as controlled documents.
- Automated register validation workflow (`.github/workflows/ci.yml`) ensures documentation control remains auditable.

## 9. Performance Evaluation
- Monitoring & measurement: Dashboards, automated tests, deployment health reports.
- Internal audits scheduled per RC-QMS-006.
- Management reviews conducted quarterly using RC-QMS-007 template; outputs tracked in `CHANGE_LOG.md` and action registers.
- Customer feedback consolidated via support workflows (workflow documentation pending migration).

## 10. Improvement
- Nonconformities handled through RC-QMS-005 with corrective action tracking.
- Continual improvement driven by lessons learned during audits, incident response, and retrospectives.
- Opportunities logged in improvement backlog (to be integrated with project management tooling).

## 11. QMS Process Interaction Map (summary)
- Governance (policy, objectives) feeds into Planning (risk, resources).
- Planning informs Support (training, infrastructure) and Operation (service delivery).
- Operation produces performance data for Evaluation and drives Improvement loops.
- Change requests feed back into Governance ensuring continuous alignment.

## 12. Document Control
- All controlled documents require metadata block, review, approval, and register entry.
- Obsolete versions archived under `docs/archive/` with clear supersession notices.
- Emergency updates follow expedited approval with retrospective review.

## 13. Record Control
- Records stored within `records/` (to be established) or designated system-of-record.
- Retention schedules defined in RC-QMS-004 (Record Retention Procedure).

## 14. Appendices
- Appendix A: Stakeholder Roles & Responsibilities (draft pending HR confirmation).
- Appendix B: Process Metrics Catalogue (to be developed with operations team).

---
**Change History**
- 1.0.0 (2025-09-22): Initial ISO 9001-aligned QMS manual established.
