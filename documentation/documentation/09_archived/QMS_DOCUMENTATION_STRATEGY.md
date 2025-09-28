---
Document ID: RC-QMS-012
Title: ISO 9001 Documentation Strategy
Version: 1.0.0
Effective Date: 2025-09-22
Prepared By: Documentation Automation Team
Reviewed By: Pending
Approved By: Pending
Related Documents: RC-QMS-001, RC-QMS-003
---

# Rod-Corp ISO 9001 Documentation Strategy

**Prepared:** 2025-09-22
**Prepared by:** Documentation Automation Team
**Scope:** Rod-Corp AI System repository (`rod-corp`) and historical repository (`rod-corp-legacy`)

---

## 1. Executive Overview
- Automated inventory confirms 3,848 controlled documents and 63,961 scripts/code artifacts across the main and legacy repositories.
- Documentation is rich but fragmented across root-level files, `docs/`, `documentation/`, and the legacy hierarchy.
- Version tracking is inconsistent; only `docs/VERSION_HISTORY.json` records a single event and most documents lack metadata (owner, revision date, approval).
- ISO 9001:2015 requires controlled documented information, explicit responsibilities, review cadences, and evidence of change control. These controls are not yet systematized.

## 2. Current-State Observations
- **Main repository (`rod-corp`)**
  - High-value reports scattered under root (e.g., `AI_SYSTEM_TEST_REPORT.md`, `COMPREHENSIVE_SYSTEM_STATUS.md`).
  - `docs/` contains guidance but lacks quality manual, document register, or control procedures.
  - `documentation/` folders exist but are largely empty, indicating incomplete migration.
  - `docs/VERSION_HISTORY.json` is present but underutilized.
- **Legacy repository (`rod-corp-legacy`)**
  - Contains critical historical audits (`audits/ISO_9001_AUDIT_2025-09-20.md`), SOPs, and migration records.
  - Extensive knowledge backups without consistent naming/metadata.
  - Scripts and documents intermixed, complicating traceability.
- **Process gaps**
  - No unified document register or status tracker.
  - No defined approval workflow, responsible owners, or retention guidance.
  - No evidence of periodic review or re-approval cycles.
  - Document IDs and version numbering are ad-hoc.

## 3. ISO 9001 Documentation Requirements Recap
- QMS scope and exclusions (Clause 4.3).
- Quality policy and measurable quality objectives (Clause 5 & 6).
- QMS process interaction map and responsibilities (Clause 4.4 & 5.3).
- Documented procedures for:
  - Control of documented information (Clause 7.5).
  - Control of records and retention.
  - Nonconformity and corrective action (Clause 10.2).
  - Internal audits and management review (Clause 9.2 & 9.3).
- Evidence of change control, approval, and distribution.
- Maintained records of reviews, audits, and corrective actions.

## 4. Target Documentation Architecture
```
docs/
  iso9001/
    QMS_MANUAL.md                ← Quality Manual & scope
    QUALITY_POLICY.md            ← Policy & objectives
    PROCESS_INTERACTION_MAP.md   ← High-level workflow map
    DOCUMENT_CONTROL_PROCEDURE.md
    RECORD_RETENTION_PROCEDURE.md
    CORRECTIVE_ACTION_PROCEDURE.md
    INTERNAL_AUDIT_PROGRAM.md
    MANAGEMENT_REVIEW_TEMPLATE.md
    DOCUMENT_REGISTER.csv        ← All controlled documents (main + legacy)
    SCRIPT_REGISTER.csv          ← Operational scripts with control metadata
    CHANGE_LOG.md                ← Chronological list of approved document changes
    REVIEW_CALENDAR.md           ← Scheduled review cycles
    LEGACY_SOURCE_MAP.md         ← Traceability map for legacy imports
  knowledge/
    ... (consolidated guides, runbooks, SOPs)
legacy/
  ... (curated imports that remain informational only)
```
- Controlled documents move into `docs/iso9001/` or `docs/knowledge/` with metadata blocks.
- Legacy content retained under `docs/legacy/` when needed for reference, with cross-links in the register.

## 5. Document Control & Versioning Approach
- **Document Identification**: `RC-QMS-###` for quality system docs, `RC-SOP-###` for operational procedures, `RC-WI-###` for work instructions.
- **Version Numbering**: `Major.Minor.Revision` (e.g., `1.2.0`). Major for scope changes, Minor for content updates, Revision for typo/format corrections.
- **Metadata Requirements** (front-matter in each controlled document):
  - Document ID, Title, Purpose
  - Version, Effective Date, Prepared By, Reviewed By, Approved By
  - Related Documents & Records
- **Register Maintenance**: `DOCUMENT_REGISTER.csv` maintained via automated script scanning + manual owner updates.
- **Change Control Workflow**:
  1. Draft update in feature branch with change description.
  2. Update `CHANGE_LOG.md` entry and modify register effective date.
  3. Peer review/approval recorded in metadata.
  4. Merge & tag release; update `docs/VERSION_HISTORY.json` for repository-level note.
- **Review Cadence**: Standard annual review; high-risk documents (security, compliance) quarterly.

## 6. Legacy Content Integration Plan
- Map each legacy document to a target status:
  - **Adopt**: migrate into controlled structure (e.g., audit reports, SOPs).
  - **Reference**: keep in `docs/legacy/` with clear "Superseded" banner.
  - **Archive**: mark as obsolete when superseded by new documentation.
- Create `LEGACY_SOURCE_MAP.md` capturing origin path, migration decision, and new canonical location.
- For scripts, ensure active ones move into main repository `scripts/` or services directories with version metadata and register entry.

## 7. Implementation Roadmap
1. Create core ISO 9001 control documents and metadata templates.
2. Generate comprehensive document and script registers (auto-populated from current inventory).
3. Migrate high-value legacy documentation into new structure; note superseded status.
4. Add document metadata blocks to critical files in priority order (starting with QMS core docs).
5. Establish automation hook (Python script) to refresh registers and validate metadata.
6. Schedule initial management review and internal audit per new templates.

## 8. Immediate Next Actions (Sprint 1)
- Stand up `docs/iso9001/` structure with control templates.
- Publish initial `DOCUMENT_CONTROL_PROCEDURE.md` and `CHANGE_LOG.md`.
- Auto-generate `DOCUMENT_REGISTER.csv` & `SCRIPT_REGISTER.csv` with current inventory.
- Produce `LEGACY_SOURCE_MAP.md` identifying migration priorities.
- Update `docs/VERSION_HISTORY.json` to log ISO 9001 rollout.

---
**Status:** Assessment complete. Proceeding to implementation (Step 3 of execution plan).
