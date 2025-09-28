# Rod-Corp Operational Workflows

These automation templates plug directly into the Rod-Corp multi-agent stack. Import each JSON into n8n, map credentials, and activate.

| Workflow | Purpose | Trigger |
|----------|---------|---------|
| `customer_sentiment_router.json` | Classify inbound support sentiment and log actions via AI Interaction Server | Webhook |
| `ticket_urgency_triage.json` | Score ticket urgency, route to escalation channels, notify agents | Webhook |
| `competitor_digest.json` | Generate competitor price digest using local data + AI summary | Daily Cron (06:00) |
| `morning_briefing.json` | Build morning status brief from repo notes and audits | Daily Cron (07:00) |
| `daily_email_digest.json` | Aggregate inbox threads and archive daily digest to database | Daily Cron (09:00) |

Each workflow relies on the AI Interaction Server (`http://localhost:49152/interact`). Ensure the server is running and agent commands are authorized before activating.
