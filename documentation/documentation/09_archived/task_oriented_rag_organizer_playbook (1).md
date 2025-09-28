# Task‑Oriented RAG Organizer Playbook

Turn the “Intelligent Folder Organizer with RAG Indexing” into a **general task system** for:
- Scientific reports
- Software development
- Book writing
- Topic investigations
- Cloning & making a GitHub repo work

The pattern: **Project Workspace → Ingest → RAG Index → Agent/API → Task‑specific checklists & queries**.

---
## 0) Base Setup (one‑time)

```bash
# (Optional) create env per your convention
mamba create -n env_rag_org python=3.12 -y && mamba activate env_rag_org
pip install -r requirements.txt
```

Core scripts used here:
- `intelligent_organizer_rag.py` → builds organized folder + knowledge base
- `agent_query_interface.py` → serves a REST API over the knowledge base

---
## 1) Universal Project Skeleton

Use the same skeleton for **any** task type; each project becomes a self‑contained workspace:

```
/projects/
  <PROJECT_NAME>/
    00_inbox/              # raw inputs: PDFs, notes, code, datasets
    01_sources/            # curated sources (papers, repos, docs)
    02_working/            # drafts, notebooks, experiments
    03_output/             # final deliverables (PDF, slides, release)
    rag_out/               # ← organizer output here
      organized/
      knowledge/
      organization_report.json
    configs/
      rag_organizer_config.yaml
    checklists/
      TASK_CHECKLIST.md
    notes/
      decisions.md
      questions.md
```

**How to build the RAG index for the workspace:**
```bash
python intelligent_organizer_rag.py ./00_inbox ./rag_out --copy
```
> Re‑run anytime after dropping new material into `00_inbox` or `01_sources`.

Start the query API (optional):
```bash
python agent_query_interface.py ./rag_out/knowledge --server --port 8000
```

---
## 2) “Task Packs” (templates you can reuse)

Each pack = **folder tips + config + checklist + query recipes**. Copy the block, tweak the names, go.

### A) Scientific Report Pack

**Folder Tips**
- Place papers, datasets, lab notes into `00_inbox/` and `01_sources/`.

**Config (`configs/rag_organizer_config.yaml`)**
```yaml
chunking:
  target_tokens: 800
  overlap_tokens: 120
embeddings:
  model: all-MiniLM-L6-v2
extraction:
  extract_text: true
  max_file_size_mb: 200
categories:
  custom_rules:
    Research:
      subcategories:
        Papers:
          extensions: [".pdf", ".md"]
          content_patterns: ["abstract", "method", "results", "doi:", "references"]
        Data:
          extensions: [".csv", ".tsv", ".xlsx"]
          name_patterns: ["dataset", "results", "measurements"]
```

**Checklist (`checklists/TASK_CHECKLIST.md`)**
- [ ] Define research question & hypotheses
- [ ] Collect key papers (min 10)
- [ ] Summarize methods and results per paper
- [ ] Draft intro → methods → results → discussion → references
- [ ] Validate all claims with citations

**Query Recipes**
- “summaries of transformer‑based microscopy between 2022–2024”
- Filters: `{"category":"Documents","tags":["research","papers"]}`
- “extract sentences about *limitation* or *future work*”

---
### B) Software Development Pack

**Folder Tips**
- Put README, issues dump, design notes, and code skeletons in `00_inbox/`.
- Put external API docs, examples, ADRs in `01_sources/`.

**Config**
```yaml
chunking:
  target_tokens: 600
  overlap_tokens: 80
categories:
  custom_rules:
    Code:
      subcategories:
        Python:
          extensions: [".py", ".ipynb"]
          content_patterns: ["def ", "class ", "import "]
        Web:
          extensions: [".ts", ".tsx", ".js", ".jsx", ".html", ".css"]
    Documents:
      subcategories:
        ADR:
          extensions: [".md"]
          name_patterns: ["adr", "decision", "architecture"]
```

**Checklist**
- [ ] Define MVP scope & success metrics
- [ ] Architecture Decision Records (ADRs)
- [ ] API contract (OpenAPI or README endpoints)
- [ ] Unit tests & CI job
- [ ] Release notes / CHANGELOG

**Query Recipes**
- “list all TODOs and FIXMEs across codebase”
- “find examples using FastAPI BackgroundTasks”
- “summarize ADR decisions referencing ‘caching’ or ‘retry’”

---
### C) Book Writing Pack

**Folder Tips**
- `01_sources/` → research references & style guides
- `02_working/` → outline.md, chapter drafts per file

**Config**
```yaml
chunking:
  target_tokens: 900
  overlap_tokens: 150
rag:
  collections:
    - { name: "outline", security: "internal" }
    - { name: "chapters", security: "internal" }
```

**Checklist**
- [ ] Define table of contents
- [ ] Character/voice or style sheet
- [ ] Chapter beats → draft → revise
- [ ] Back matter: acknowledgments, references, index

**Query Recipes**
- “pull all excerpts tagged ‘theme:resilience’ from chapters 1–4”
- “find continuity conflicts for character ages”

---
### D) Topic Investigation Pack

**Folder Tips**
- Dump links (as .md notes), PDFs, transcripts into `00_inbox/`.
- Curate the best into `01_sources/`.

**Config**
```yaml
chunking: { target_tokens: 700, overlap_tokens: 120 }
categories:
  custom_rules:
    Claims:
      subcategories:
        Evidence:
          extensions: [".md", ".txt", ".pdf"]
          name_patterns: ["evidence", "source", "quote"]
```

**Checklist**
- [ ] Define key questions
- [ ] Map claims ↔ evidence ↔ sources
- [ ] Identify gaps & design follow‑ups

**Query Recipes**
- “show every paragraph mentioning ‘confounding variable’”
- “rank sources by frequency of being cited”

---
### E) GitHub Clone‑n‑Run Pack

**Folder Tips**
- Clone into `02_working/repo/`, drop issues/notes into `00_inbox/`.

**Config**
```yaml
chunking: { target_tokens: 500, overlap_tokens: 60 }
extraction:
  extract_text: true
categories:
  custom_rules:
    Code:
      subcategories:
        Build:
          extensions: [".toml", ".yaml", ".yml", ".json"]
          name_patterns: ["requirements", "pyproject", "package", "docker", "compose"]
```

**Checklist**
- [ ] Capture install steps & errors (paste logs as .md into `00_inbox/`)
- [ ] Build succeeds locally (record exact commands)
- [ ] Minimal example runs
- [ ] Create a “WORKING_NOTES.md” with fixes/workarounds

**Query Recipes**
- “find all installation instructions”
- “extract observed error messages and nearby fixes”

---
## 3) Commands Cookbook

Re‑index after you add new files:
```bash
python intelligent_organizer_rag.py ./00_inbox ./rag_out --copy --config ./configs/rag_organizer_config.yaml
```

Quick semantic search (after index exists):
```python
from agent_query_interface import QueryEngine
from pathlib import Path
engine = QueryEngine(Path("./rag_out/knowledge"))
res = engine.search("installation steps for CUDA on Windows", top_k=5,
                    filters={"category":"Documents"})
print(res[:2])
```

Serve API for agents:
```bash
python agent_query_interface.py ./rag_out/knowledge --server --port 8000
```

---
## 4) Working Notes Practice

- Any time you do a step (run code, test an idea), **paste the command & output** into a timestamped `.md` in `02_working/`.
- The organizer will chunk/index your notes → you can **query your own process** later.

**Tip:** keep a `notes/decisions.md` file with short ADR‑style entries; it becomes a powerful searchable memory.

---
## 5) Minimal “Agent‑Ready” Prompts

- “Given the RAG index, produce a one‑page outline for the report/book based on the top 15 relevant chunks for ‘X’.”
- “Plan the next 3 coding tasks by clustering TODOs and error logs.”
- “Generate a claims‑evidence table with citations to source filenames + chunk ids.”

---
## 6) When to Create Multiple Collections

Use separate **collections** for:
- Different deliverables (e.g., `outline`, `chapters`, `appendix`)
- Different source classes (`papers`, `data`, `code`, `notes`)
- Different security tiers (`public`, `internal`)

---
## 7) Quality Guardrails

- Keep chunks ~600–900 tokens with 80–150 overlap for long‑form texts.
- Prefer `.md` for notes and logs → great for chunking.
- Export PDFs to text when possible for better searchability.
- Re‑run indexing after major edits; keep `organization_report.json` under VCS.

---
## 8) Quick Start Template (copy/paste)

```bash
# 1) create workspace
mkdir -p projects/MyTask/{00_inbox,01_sources,02_working,03_output,configs,checklists,notes}
cp rag_organizer_config.yaml projects/MyTask/configs/  # or craft a new one

# 2) drop materials into 00_inbox & 01_sources

# 3) build index
python intelligent_organizer_rag.py projects/MyTask/00_inbox projects/MyTask/rag_out --copy \
  --config projects/MyTask/configs/rag_organizer_config.yaml

# 4) query (Python or REST)
python agent_query_interface.py projects/MyTask/rag_out/knowledge --server --port 8000
```

---
## 9) Done Right, This Becomes

- A **unified pattern** for any task.
- Repeatable ingestion → searchable context → consistent outputs.
- Agent‑friendly (your broader automation system can call the API, filter by metadata, and produce artifacts).



---
## 10) ADHD‑Friendly PM Recommendation & Setup

**Short answer:** Use **Plane** plus an **ADHD simplification layer** (agents + views). It’s the best mix of low cognitive load, clean API for your agents, and enough PM features without the enterprise bloat. If you ever need budgets/Gantt later, mirror to OpenProject just for portfolio snapshots.

### Why Plane for ADHD
- **One queue, few views:** Backlog → Today → This Week; avoids tab‑hopping.
- **Docs in context:** Decisions/notes live next to issues; no context switching.
- **Agent‑first:** Simple REST; your bots can plan, re‑prioritize, and brief you.

### Optional alternative
- **Leantime** if you want built‑in “strategy→execution” feel and a softer UX for non‑tech collaborators. Keep in mind the API ergonomics aren’t as clean as Plane.

### Your “ADHD Mode” Preset (copy this into the PM app)
- **Labels:** `now`, `next`, `blocked`, `deep‑work`, `quick‑win`, `risk`, `decision`.
- **Custom fields:** `impact (H/M/L)`, `effort (1‑5)`, `energy (low/med/high)`.
- **Saved Views:**
  - **Today (max 3)** → show `now` OR due today, sort by impact desc, effort asc.
  - **This Week (top 7)** → due≤Friday + `next`, hide blocked.
  - **Risks** → label:`risk` OR `blocked`, grouped by owner.
  - **Decisions Log** → issues/comments tagged `decision`.

### Agent Automations (ready to implement)
1) **Triage‑Agent**
   - Input: new issues / meeting transcripts (from Docs)
   - Output: adds `impact/effort/energy`, assigns `now/next/quick‑win`, suggests due dates.
2) **Planner‑Agent (Mon 09:00)**
   - Picks **3 “Today”** and **7 “This Week”** based on scores + calendar load.
3) **Focus‑Coach (09:15, 13:15)**
   - Posts a comment: *“Pick one: quick‑win, deep‑work, or highest‑impact?”*
   - If you choose deep‑work → creates a 90‑min focus block and silences other pings.
4) **Reporter‑Agent (Fri 16:00)**
   - Publishes **Black‑Belt Brief**: Done, Slipped, New Risks, Top Decisions, Next Week.

### Integration glue (starter config)
```
# env
mamba create -n env_agent_pm python=3.12 -y && mamba activate env_agent_pm
pip install fastapi uvicorn httpx pydantic python-dotenv

# services
agents/pm_bridge.py        # webhook → RAG mirror → scoring → write‑back
agents/briefs.py           # generates weekly “Black‑Belt Brief” Plane Doc
configs/plane.json         # PATs, project ids, label ids, field ids

# routes
POST /webhooks/plane       # receive issue/doc changes
POST /plan/daily           # recompute Today/Week, push labels/dates
GET  /briefs/weekly        # returns markdown + posts to Docs
```

### RAG tie‑in
- Mirror Plane issues/comments/docs into `rag_out/knowledge` with metadata (`project`, `labels`, `impact`, `effort`).
- Query recipes:
  - “summarize blockers touching `repo:X` and label:`risk` for this week”
  - “list decisions made in the last 14 days with links back to issues/docs”

### Daily ritual (90 seconds)
1) Open **Today** view (max 3).
2) Pick **one** (quick‑win vs deep‑work vs highest‑impact).
3) Start a 90‑min block; everything else is agent‑driven.



---
## 11) API Decision & Cheat‑Sheet (for Agents)

**Chosen PM API:** **Plane REST API (v1)** — token‑based, predictable resources, docs/roadmaps, perfect for agent automation.

### Auth
- Personal Access Token (PAT) or Service Account token
- Header: `Authorization: Bearer <TOKEN>`
- Content type: `application/json`

### Base
- `https://<your-plane-host>/api/v1/`

### Core Endpoints (agent‑used)
- **Projects:** `GET/POST /projects` (create workspace containers)
- **Issues:** `GET/POST /issues` | `PATCH /issues/{id}` (title, description, labels, priority, due date, assignees)
- **Cycles (sprints):** `GET/POST /cycles` | `PATCH /cycles/{id}` (start/end, goal)
- **Labels:** `GET/POST /labels` (e.g., `now`, `next`, `risk`, `quick-win`, `deep-work`)
- **Docs:** `GET/POST /documents` | `PATCH /documents/{id}` (meeting notes, briefs)
- **Comments:** `POST /issues/{id}/comments` (status updates, coach nudges)

### Minimal Requests (examples)
```bash
# Create an issue
curl -X POST "$PLANE/api/v1/issues" \
 -H "Authorization: Bearer $PLANE_TOKEN" -H "Content-Type: application/json" \
 -d '{
   "project_id": "'$PLANE_PROJECT'",
   "title": "Wire FastAPI webhook",
   "description": "Receive Plane webhooks → RAG mirror → scoring",
   "priority": 3,
   "labels": ["now","quick-win"],
   "assignees": ["agent_planner"],
   "due_date": "2025-09-29"
 }'

# Post a status comment
curl -X POST "$PLANE/api/v1/issues/$ISSUE_ID/comments" \
 -H "Authorization: Bearer $PLANE_TOKEN" -H "Content-Type: application/json" \
 -d '{"body": "Triage done. Impact=High, Effort=2, Energy=Medium."}'

# Create a Doc for the Black‑Belt Brief
curl -X POST "$PLANE/api/v1/documents" \
 -H "Authorization: Bearer $PLANE_TOKEN" -H "Content-Type: application/json" \
 -d '{
   "project_id": "'$PLANE_PROJECT'",
   "title": "Weekly Brief — 2025‑09‑26",
   "content": "# Done
- …
# Slipped
- …
# Risks
- …
# Next Week
- …"
 }'
```

### Webhooks → Agent Bridge
- Configure Plane webhooks to: `POST https://<your-bridge>/webhooks/plane`
- Event payload includes changed entity (`issue|comment|document`), ids, timestamps
- Bridge tasks:
  1) Upsert change into `rag_out/knowledge` with metadata (`project`, `labels`, `impact`, `effort`, `cycle`, `status`).
  2) Trigger **Triage/Planner/Reporter** agents.

### Env & Files (starter repo)
```
.env.example
  PLANE_BASE_URL=
  PLANE_TOKEN=
  PLANE_PROJECT=

configs/plane.json         # ids for labels, fields, project
agents/pm_bridge.py        # webhook handler → RAG sync
agents/briefs.py           # weekly brief composer
Makefile                   # run bridge, test webhooks
```

> Use conda env: `env_agent_pm` as defined in §10.

