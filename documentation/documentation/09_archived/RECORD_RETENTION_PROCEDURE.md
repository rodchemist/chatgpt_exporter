---
Document ID: RC-QMS-004
Title: Documented Information Retention Procedure
Version: 1.0.0
Effective Date: 2025-09-22
Prepared By: Documentation Automation Team
Reviewed By: Pending
Approved By: Pending
Related Documents: RC-QMS-001, RC-QMS-003, RC-QMS-005
---

# Documented Information Retention Procedure

## 1. Purpose
Establish retention and disposition rules for controlled documents and records to satisfy legal, regulatory, and organizational requirements.

## 2. Scope
Applies to all documented information managed by the Rod-Corp QMS, including controlled documents, audit reports, test evidence, contracts, and operational logs kept within version control or approved storage systems.

## 3. Responsibilities
- **Documentation Manager**: Maintains retention schedule, approves disposal of expired records.
- **Process Owners**: Ensure records for their processes are stored in approved locations and retained per schedule.
- **IT Operations**: Provide secure backups and access controls for archived records.

## 4. Retention Schedule Overview
| Record Type | Minimum Retention | Storage Location | Disposal Method |
|-------------|-------------------|------------------|-----------------|
| Controlled Documents (superseded) | 3 years | `docs/archive/` | Secure deletion after approval |
| Audit Reports & Findings | 5 years | `records/audits/` | Secure deletion |
| Corrective Action Records | 4 years | `records/corrective_actions/` | Secure deletion |
| Training Records | Duration of employment + 1 year | HR system / `records/training/` | Per HR policy |
| Deployment & Test Evidence | 3 years | `records/verification/` | Secure deletion |
| Customer Complaints | 5 years | CRM / `records/customer_feedback/` | Secure deletion |

## 5. Record Identification
- Records receive IDs `RC-REC-###` and entries within the record register (to be created).
- Metadata must include owner, retention duration, and disposal date.

## 6. Storage & Protection
- Repositories protected by access controls; backups performed daily.
- Sensitive records encrypted where applicable.
- Access logs maintained by IT Operations.

## 7. Disposal & Destruction
- Disposal requests submitted to Documentation Manager with justification.
- Approval documented in change log before removal.
- Secure deletion executed using approved tools; verification recorded.

## 8. Monitoring & Review
- Retention schedule reviewed annually or upon regulatory change.
- Records audited during internal audits to confirm compliance.

---
**Change History**
- 1.0.0 (2025-09-22): Initial retention procedure issued.
