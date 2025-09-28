# Agent Communication Stack Status

## Registry Snapshot
- Total agents in `AgentDirectory.dbo.GlobalAgentRegistry`: **60** (all currently marked `active`).
- Senior leadership and LibroSynth specialists present (e.g. ALEX, VICTORIA, ZARA, Workflow Automation Specialist).
- `data/agent_registry_snapshot.csv` contains the full export (agent, model, team, specialization, seniority, last seen).

## MCP + Notification Layer
- MCP server suite (`services/mcp-servers/rod_corp_mcp_suite.py`) exposes database tools, AI Interaction proxying, file processing, and workflow triggers.
- `AgentDiscussions` logs show repeated MCP deployment notices plus LibroSynth coordination messages.
- `notify_all_agents.py` attempted to activate MCP roles but logged **0% success** because the AI Interaction Server call failed; as a result, `AgentCapabilities` table remains empty.
- Recommendation: rerun notification after verifying AI Interaction Server availability (port 49152) and confirm `AgentCapabilities` rows populate per agent.

## n8n Coverage
- Legacy templates: `n8n_workflows/templates` and `n8n_workflows/active` include `backup_agent_coordination.json` and `specialist_agent_automation.json` for LibroSynth pipelines.
- New Rod-Corp operational pack added under `n8n_workflows/templates/rod_corp/` (sentiment, triage, competitor digest, morning briefing, email digest) with helper scripts in `scripts/workflows/` and sample data in `data/`.
- Runbook (`docs/RUNBOOK.md`) updated so operations know which automations to import.

## Gaps & Next Actions
1. Bring the AI Interaction Server online, then rerun `services/mcp-servers/notify_all_agents.py` so each registry entry receives capabilities and MCP tool mappings.
2. Populate `AgentCapabilities` and any missing `AgentActivityLog` tables for telemetry.
3. Import/activate the new n8n workflows, mapping credentials to the AI Interaction Server and database.
4. Decide on agents that should rotate into leadership/coordination roles and script periodic activation (e.g. via n8n scheduler or MCP job).
