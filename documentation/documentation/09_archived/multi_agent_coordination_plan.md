# Multi-Agent Coordination Plan

Goal: orchestrate 10–25 Rod-Corp agents in parallel to ingest legacy assets, evaluate Windows tooling, and extend the AgentDirectory without losing track of dependencies.

## Pre-Flight Checklist (Run Before Spawning Agents)
1. **Verify core services**
   - AI Interaction Server reachable on `http://localhost:49152`.
   - MCP suite running on port `49200` (`curl http://localhost:49200/`).
   - MSSQL `AgentDirectory` + `RodSanchez_PersonalData` reachable (test via `scripts/tools/ai-context-status` and `sqlcmd`).
2. **Run agent notification refresh**
   - `python3 services/mcp-servers/notify_all_agents.py`
   - Confirm `AgentCapabilities` table now populated.
3. **Import pending n8n workflows** (if not already activated)
   - `customer_sentiment_router.json`
   - `ticket_urgency_triage.json`
   - `competitor_digest.json`
   - `morning_briefing.json`
   - `daily_email_digest.json`
4. **Stage shared data**
   - Ensure \`data/\` sample files represent current production snapshots before agents operate on them.

## Coordination Groups & Primary Agents
| Group | Recommended Agents | Purpose |
|-------|--------------------|---------|
| Registry & MCP | `AGENT_001` (Orchestrator), `ALEX_ENGINEERING_DIRECTOR`, `SYSTEM_ADMINISTRATOR` | Maintain registry updates, rerun MCP tools |
| Legacy Audit | `DOCUMENT_WATCHDOG`, `EDITOR_LIBROSYNTH`, `ZEN`, `HARMONY` | Scan legacy `.py`/`.md` for database/business logic |
| Windows Asset Intake | `VICTORIA`, `ZARA`, `DIANA`, `SOPHIA_HR` | Coordinate mapped Windows directories; create import manifests |
| Database Expansion | `AGENT_SCHEMA_DESIGNER`, `AGENT_DATABASE_TESTER`, `AGENT_DATA_INSPECTOR` | Design new tables (e.g. todo tracking), validate schema |
| Workflow Automation | `Workflow Automation Specialist`, `Multi Agent Coordination Specialist`, `Prompt Engineering Specialist` | Build/validate n8n flows & MCP scripts |
| Security & QA | `ELENA`, `EXCEPTION_MONITOR`, `Quality Assurance Specialist` | Monitor errors, enforce compliance |

## Task Blocks
1. **Legacy Repository Mining**
   - Search `/home/rod/rod-corp/archive/legacy-system-20250920` and related folders for `.py`/`.md` referencing MSSQL, MCP, or n8n.
   - Log findings to `data/legacy_asset_catalog.csv` (fields: file, path, summary, suggested action).
2. **Windows Asset Evaluation**
   - Mount/scan each specified Windows directory (e.g. `_tools_rod`, `prompts`, `web_app`).
   - Produce `windows_asset_report.md` summarizing tools worth migrating, licensing concerns, and dependencies.
3. **Knowledge Artifact Review**
   - Analyze `Empowering Multi-Agent Teams_ Coordination Strategies and References.docx`; convert key frameworks into Markdown for Rod-Corp wiki.
   - Assess research repositories (`self_focus_lab`, `books`, etc.) for integration opportunities.
4. **API Project Integration**
   - Evaluate `ai_image_gen_v2`, `project_locator`, `ai_image_generation_api` for compatibility; draft migration steps.
5. **Framework Adoption**
   - Review `git_documentation_agent_prompt.md` & `universal_project_setup.sh`; propose how to template these across active projects.
6. **Agent Directory Enhancements**
   - Add missing agents (if any) and design rotation schedule for leaders (e.g. enable periodic activation via n8n Cron + MCP).

## Execution Guidance
- Maintain active agent count between **10–25**; assign groups in waves (e.g. Legacy Audit + Database expansion + Automation simultaneously).
- Use AI Interaction Server `/interact` endpoint for coordination chatter; log decisions to `AgentDiscussions` via MCP tool.
- After each wave, run `scripts/tools/ai-context-status` to confirm context freshness.
- Update progress trackers (`data/legacy_asset_catalog.csv`, `windows_asset_report.md`) before switching tasks to keep state serialized.

## Deliverables Snapshot
- `data/agent_registry_snapshot.csv` – baseline registry export (already generated).
- `data/agent_comm_stack_status.md` – communication readiness report.
- `data/legacy_asset_catalog.csv` – (to be produced during audit).
- `docs/N8N_PRACTICAL_GUIDE_NOTES.md` – n8n playbook summary.
- `n8n_workflows/templates/rod_corp/` – ready-to-import operational flows.

With this plan, we can safely engage 10–25 agents in parallel, knowing which assets need attention and how their output will be captured.
