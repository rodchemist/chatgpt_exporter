---
Document ID: RC-QMS-003
Title: Document Control Procedure
Version: 1.0.0
Effective Date: 2025-09-22
Prepared By: Documentation Automation Team
Reviewed By: Pending
Approved By: Pending
Related Documents: RC-QMS-001, RC-QMS-002, RC-QMS-004
---

# Document Control Procedure

## 1. Purpose
To define the controls needed for creation, approval, distribution, maintenance, and archival of Rod-Corp documented information.

## 2. Scope
Applies to all documents listed in `DOCUMENT_REGISTER.csv`, including policies, manuals, SOPs, work instructions, and external standards stored within Rod-Corp repositories.

## 3. Responsibilities
- **Documentation Manager**: Oversees register accuracy, approves major releases, assigns reviewers.
- **Document Owner**: Drafts content, coordinates review, ensures metadata accuracy.
- **Reviewer**: Validates technical correctness and compliance.
- **Approver**: Grants final authorization for release.

## 4. Process Flow
1. **Initiation**
   - Submit change request via issue tracker referencing target document ID.
   - Assign owner, reviewer, approver.
2. **Drafting**
   - Update document in feature branch, include metadata block with proposed version.
   - Update entry in `CHANGE_LOG.md` (Pending status).
3. **Review**
   - Reviewer performs content and compliance check.
   - Feedback addressed before approval.
4. **Approval**
   - Approver signs off via pull request approval or documented consent.
   - Change log entry updated to Approved with date and approver name.
5. **Release**
   - Merge changes, tag version if applicable, update register (version, effective date, owner).
   - Notify stakeholders via repository announcement channel.
6. **Distribution**
   - Controlled copies reside in repository; offline exports marked "Uncontrolled".
7. **Archival & Retention**
   - Superseded versions stored in `docs/archive/` with retention per RC-QMS-004.

## 5. Document Identification & Formatting
- IDs follow prefixes: `RC-QMS-###`, `RC-SOP-###`, `RC-WI-###`, `RC-REC-###` (records).
- Metadata block required at top of each controlled document (see Appendix A).
- File naming matches document title with underscores (e.g., `QMS_MANUAL.md`).

## 6. Review Cadence
- Standard documents: Annual review.
- High-risk (security, compliance): Quarterly review.
- Automated reminder list maintained in `REVIEW_CALENDAR.md`.

## 7. External Documents
- External standards or contracts referenced must include source, version, and storage location.
- External documents are referenced but not duplicated; control limited to ensuring availability and monitoring updates.

## 8. Emergency Changes
- In urgent cases, approver may authorize immediate release post-review.
- Emergency flag noted in change log; retrospective review required within 5 business days.

## 9. Noncompliance Handling
- Deviations recorded as nonconformities (RC-QMS-005) and resolved with corrective action.

## Appendix A: Metadata Template
```
---
Document ID: <ID>
Title: <Title>
Version: X.Y.Z
Effective Date: YYYY-MM-DD
Prepared By: <Name/Role>
Reviewed By: <Name/Role>
Approved By: <Name/Role>
Related Documents: <IDs>
---
```

---
**Change History**
- 1.0.0 (2025-09-22): Initial procedure issued.
