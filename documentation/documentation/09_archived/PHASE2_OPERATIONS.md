# Phase 2 Operations

## Bring Up
```bash
cp infra/.env.sample infra/.env
docker compose -f infra/docker-compose.yml --env-file infra/.env up -d
```

## Seed RAG
```bash
python agents/rag/agent_rag.py --ingest ./docs/MASTER_COMPENDIUM.md
```

## Validate
- Plane → http://localhost:3000
- Grafana → http://localhost:5601
- Prometheus → http://localhost:9090
- n8n → http://localhost:5678
- Home Assistant → http://localhost:8123
