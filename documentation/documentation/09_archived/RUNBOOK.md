# Rod-Corp AI System Runbook

## Services

- AI Interaction Server: http://localhost:49152 (FastAPI)
- MCP Server Suite: http://localhost:49200 (FastAPI)
- n8n Workflows: import JSON templates from `n8n_workflows/templates/`

## Start

1) AI Interaction Server
   cd services/ai-interaction-server
   ./start.sh

2) MCP Server Suite
   cd services/mcp-servers
   ./deploy_mcp.sh

3) n8n Workflows
   - In n8n UI, import templates from `n8n_workflows/templates/`
   - New automations:
     - `librosynth_repo_training_automation.json` – nightly qwen repo trainer + notification
     - `personal_data_training_pipeline.json` – weekly Takeout refresh + DB sync
     - `rod_corp/customer_sentiment_router.json` – sentiment classification + codex logging
     - `rod_corp/ticket_urgency_triage.json` – webhook triage with agent escalation
     - `rod_corp/competitor_digest.json` – daily competitor pricing digest
     - `rod_corp/morning_briefing.json` – morning status briefing
     - `rod_corp/daily_email_digest.json` – daily inbox summarization
   - Activate flows in `n8n_workflows/active/` as needed

## Health Checks

- curl http://localhost:49152/health
- curl http://localhost:49200/

## Config

Copy `.env.example` to `.env` and adjust secrets for production.

## Port Registry

- The registry uses MSSQL if available, otherwise a local SQLite DB at `~/.rod_corp_port_registry.db`.

## Logs

- AI Interaction Server: services/ai-interaction-server (venv logs) and /tmp/ai_interaction_server_autostart.log
- MCP Server: uvicorn console output; docker/systemd can be added as needed

## Security

- Set a strong `SECRET_KEY` and disable DEBUG in production
- Move DB credentials to env and restrict network
