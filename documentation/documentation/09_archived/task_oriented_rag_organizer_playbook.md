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

