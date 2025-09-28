# Universal Project Playbook

*A generic, platform‑aware, repo‑ready blueprint you can drop into any project.*

> **How to use this doc**
>
> 1. Copy relevant sections into your repo as `README.md`, `docs/FOUNDATIONAL.md`, `docs/DEPLOYMENT.md`, and platform files (`CLAUDE.md`, `GEMINI.md`, `AGENTS.md`).
> 2. Every section includes conditional rules: **If the project has … then implement …**.
> 3. Stage your work in two sets: **Foundational** (first dev stage) and **Deployment** (hardening & scale).

---

## Table of Contents

- [Visual Roadmap / Decision Tree](#visual-roadmap--decision-tree)
- [One-Page Quick Start (Adoption Guide)](#one-page-quick-start-adoption-guide)
- [Why This Playbook Works (Executive Summary)](#why-this-playbook-works-executive-summary)
- [Principles](#principles)
- [PHASE 0 (Idea & First Tests)](#phase-0-idea--first-tests)
- [Universal Guidelines (Pragmatic & Multi-Agent Friendly)](#universal-guidelines-pragmatic--multi-agent-friendly)
  - [Philosophy](#philosophy)
  - [Structure & Ownership](#structure--ownership)
  - [Collaboration](#collaboration)
  - [Tooling](#tooling)
  - [Policies as Data](#policies-as-data)
- [Universal Repository Guidelines](#universal-repository-guidelines)
  - [Key Ideas](#key-ideas)
  - [Quick Start](#quick-start)
  - [Layout](#layout)
  - [Multi-Agent Collaboration](#multi-agent-collaboration)
  - [CI](#ci)
  - [Logo Integration](#logo-integration)
- [Repository Blueprint](#repository-blueprint)
- [FOUNDATIONAL (Stage 1)](#foundational-stage-1)
  - [Definition of Done](#definition-of-done)
  - [Environment & Tooling](#environment--tooling)
  - [Configuration](#configuration)
  - [Logging & Run IDs](#logging--run-ids)
  - [Validation & QA (Basic)](#validation--qa-basic)
  - [Security Baseline](#security-baseline)
  - [Data Handling](#data-handling)
  - [ML/Analytics (optional)](#mlanalytics-optional)
  - [Web/API (optional)](#webapi-optional)
  - [Agents & Tool‑Use (optional)](#agents--tooluse-optional)
  - [Agent Safety & Governance](#agent-safety--governance)
  - [Provider Adapter & Fallback](#provider-adapter--fallback)
  - [Token & Cost Budgets](#token--cost-budgets)
  - [Data Contracts (Optional)](#data-contracts-optional)
- [DEPLOYMENT (Stage 2+)](#deployment-stage-2)
  - [Infra Patterns](#infra-patterns)
  - [Security Hardening](#security-hardening)
  - [Observability](#observability)
  - [Run Registry & Retention](#run-registry--retention)
  - [Feature Flags & Experiments](#feature-flags--experiments)
  - [Caching Strategy](#caching-strategy)
  - [Data & Model Management](#data--model-management)
  - [Release & Change Management](#release--change-management)
  - [Performance & Cost](#performance--cost)
  - [Ops Playbooks](#ops-playbooks)
  - [Threat Model (lite)](#threat-model-lite)
  - [Service Catalog & SLOs](#service-catalog--slos)
  - [Backups & Disaster Recovery](#backups--disaster-recovery)
  - [LLM Evaluation Harness](#llm-evaluation-harness)
- [Templates & Snippets](#templates--snippets)
- [Platform Guides](#platform-guides)
  - [Provider Capabilities Matrix](#provider-capabilities-matrix)
  - [CLAUDE.md (Anthropic)](#claudemd-anthropic)
  - [GEMINI.md (Google)](#geminimd-google)
  - [AGENTS.md (OpenAI/ChatGPT + multi‑agent orchestration)](#agentsmd-openaichatgpt--multiagent-orchestration)

---

## Visual Roadmap / Decision Tree

**Start → Pick your lane → Build only what you need right now.**

```
Idea →  Phase 0  ──[Gate: Phase 0 → Foundational]──▶  Stage 1 (Foundational)  ──▶  Stage 2+ (Deployment)
```

```mermaid
flowchart TD
  A[Idea] --> B[Phase 0]
  B -->|Gate met| C[Foundational (Stage 1)]
  B -->|Gate not met| B
  C --> D[Deployment (Stage 2+)]
```

**Pick your path:**

- **CLI tool?** Focus on **Phase 0**, **Foundational → Environment & Tooling**, **Configuration**, **Logging & Run IDs**, **Validation & QA (Basic)**.
- **Web/API?** Add **Web/API (optional)** and **Security Baseline (Stage‑1 Checklist)**; later **Observability**.
- **Data/ML?** Add **Data Handling**, **ML/Analytics (optional)**; consider **Token & Cost Budgets** for LLM usage.
- **Agents?** Add **Agents & Tool‑Use**, **Agent Safety & Governance**, and **Provider Adapter & Fallback**.

> Rule of thumb: if a section doesn’t reduce current risk or help you demo value this week, defer it.

---

## One-Page Quick Start (Adoption Guide)

**Goal:** adopt incrementally without reading everything.

1. **Decide your lane** (CLI, Web/API, Data/ML, Agents).
2. **Phase 0**: run a 60‑min validation → complete `docs/phase0_checklist.md`.
3. **Gate check**: if ≥3 criteria met, move to **Foundational (Stage 1)**.
4. **Stage 1 setup**: create repo skeleton, enable pre‑commit, add JSONL logs + `run_id`, wire config validation.
5. Ship a **single thin slice** to a real user; add minimal security checklist.

**Tracks (what to read & do):**

- **CLI** → Phase 0 • Foundational → *Environment & Tooling* • *Configuration* • *Logging & Run IDs* • *Validation & QA (Basic)* • *Stage‑1 Minimal Security*.
- **Web/API** → Phase 0 • Foundational + *Web/API (optional)* • *Security Baseline* • later *Observability*.
- **Data/ML** → Phase 0 • *Data Handling* • *ML/Analytics (optional)* • *Token & Cost Budgets*.
- **Agents** → Phase 0 • *Agents & Tool‑Use* • *Agent Safety & Governance* • *Provider Adapter & Fallback* • *Token & Cost Budgets* • *Stage‑1 Minimal Security*.

**Commands to know:**

- `./scripts/install_hooks.sh` → enable formatters/linters.
- `./scripts/validate_repo.sh` → repo health.
- `./scripts/test.sh` → run tests + smoke.

---

## Why This Playbook Works (Executive Summary)

- **AI is first‑class**: agent safety levels (L0–L3), provider adapters, and token/cost budgets are integrated across phases—not bolted on later.
- **Pragmatism embodied**: orthogonality, DRY/SSOT configs, reversibility (feature flags, kill‑switches) are applied as concrete practices.
- **Quality culture by design**: “always‑shippable main,” red builds fixed immediately, and validation gates create guardrails from day one.
- **Progressive enhancement**: Phase 0 → Foundational → Deployment gives teams a realistic path; each stage stands alone yet sets up the next.

---

## Principles

## Principles

- **Bias to working software**: Ship a minimal, testable slice first; harden later.
- **Platform‑aware outputs**: Tune prompts, function schemas, and streaming by model/provider.
- **Auditability**: Everything important gets a **run\_id**, structured logs, and reproducible config.
- **Modular > monolithic**: Separate concerns (UI/API/Jobs/Agents).
- **Fail safely**: Timeouts, retries, idempotency, and kill‑switches.

---

## PHASE 0 (Idea & First Tests)

*A 0‑overhead checklist to validate an idea in hours, not weeks.*

### Goal (decide in ≤1 day)

- **Proceed** if a thin slice works end‑to‑end and feels valuable.
- **Park** if blocked by data/access; write blockers.
- **Pivot** if assumptions break; write the new hypothesis.

### Scope

- Local only. No cloud, no secrets, no databases.
- 1 path only (CLI **or** notebook **or** API stub **or** UI stub).
- Logs to **stdout** + a single JSONL file.

### Success Criteria

- One demo command runs and produces a believable output.
- Observed behavior logged with a **run\_id** and simple timings.
- A 10‑line note captures what worked, what failed, and next steps.

### 60‑Minute Setup

```bash
mkdir -p src scripts logs docs && git init
python -m venv .venv && source .venv/bin/activate || .venv\Scripts\activate
pip install ruff pytest
printf "env: development
" > config.yaml
cat > scripts/phase0_run.sh <<'SH' 
#!/usr/bin/env bash
python - <<'PY'
import uuid, json, time, os
rid=str(uuid.uuid4())
start=time.time()
print('[demo] hello, world')
rec={"run_id":rid,"ts":time.time(),"event":"demo","latency_ms":round((time.time()-start)*1000,2)}
os.makedirs('logs', exist_ok=True)
open('logs/phase0.jsonl','a').write(json.dumps(rec)+'
')
print('[ok]',rec)
PY
SH
chmod +x scripts/phase0_run.sh
./scripts/phase0_run.sh
```

**If Windows‑only:** use PowerShell `python - <<'PY'` via `py -` or run a `.py` file instead.\
**If GPU available:** add a single check (`torch.cuda.is_available()`) and log the result.

### 120‑Minute Prototype (pick one)

- **CLI**: add 1 argument (`--input file_or_text`), validate, print a result + write one log line.
- **Notebook**: `notebooks/phase0.ipynb` with 3 cells: load sample data → run tiny transform → show chart/table.
- **API stub**: FastAPI with `/healthz` + `/demo` that echoes an input and adds a timestamp.
- **UI stub**: single HTML page with one input and a result area; no framework required.

**If the project has data:** create `data/sample.csv` (≤100 rows).\
**If the project needs an agent:** define **one** tool with fixed schema; add a **kill‑switch** env (`PHASE0_DISABLE_TOOLS=1`).

### 30‑Minute Validation

Create `docs/phase0_checklist.md` with:

- Assumption proved/invalidated.
- Sample input and output pasted.
- Rough timing and any cost estimates (even if \$0).
- Top 3 risks / blockers.
- Go/No‑Go (and why).

### Deliverables

- `scripts/phase0_run.sh` (or `phase0.py`), `logs/phase0.jsonl`, `docs/phase0_checklist.md`.
- Optional: `notebooks/phase0.ipynb` **or** `/demo` endpoint **or** `demo.html`.

### Out of Scope (Phase 0)

- No CI/CD, no containers, no databases, no secret keys, no production data, no multi‑agent orchestration.

---

## Phase Gate: Phase 0 → Foundational

**Move to Foundational when** (meet ≥ 3):

- You have **3+ real users** (or stakeholders) who successfully ran the demo and want more.
- A **single thin slice** works end‑to‑end locally and is **repeatable** (scripted or notebook).
- **Core technical risks identified** and captured in `docs/phase0_checklist.md` (≤ 5 items).
- You can name a **primary owner** and **2+ months of runway** (time/budget) are committed.
- You can state a **one‑sentence value prop** and a **metric to improve** in Stage 1 (e.g., time saved/run, accuracy\@K, p95 latency).

**Blockers to resolve before moving on:** secrets required but no store, production data access needed, or unclear ownership.

---

## Universal Guidelines (Pragmatic & Multi-Agent Friendly)

### Philosophy

- **Single Source of Truth** for configs, constants, and docs; reference don’t duplicate.
- **Orthogonality**: modules are self-contained; changes don’t ripple.
- **Tracer Bullets**: ship thin vertical slices to validate direction quickly.
- **No Broken Windows**: fix red builds/tests before adding features.
- **Always Shippable**: `main` must be releasable at all times.

**If the project spans multiple languages:** centralize cross-language constants in `/config/*.yaml` and generate language-specific stubs during build.

### Structure & Ownership

- Structure primarily by **feature/domain**. Each module may include its own `src/`, `tests/`, `docs/`, `assets/`, `vendor/` as needed.
- Ownership is explicit via \`\`; each path maps to maintainers/oncall.
- Public contracts live in an `interfaces/` folder (or language-native equivalent packages).

**If a module exposes an API or SDK:** document it in `interfaces/` and add contract tests.\
**If a module becomes a hotspot (frequently edited):** split into smaller submodules to reduce merge contention.

### Collaboration

- **Branch-per-change**; keep PRs small with isolated blast radius.
- Document architecture decisions in \`\` (short, factual ADRs).
- Avoid hotspots: refactor large files; favor composition over inheritance.

**If a change affects more than one module:** include an ADR and a coordination checklist linking all impacted modules and owners.

### Tooling

- Auto-detect stack(s) and run language-appropriate validators.
- **Pre-commit** for formatters + basic static checks.
- **Single entry point** for health: `./scripts/validate_repo.sh`.

**If monorepo:** include workspace-level validation and per-package lint/test runners.\
**If CI present:** gate merges on `validate_repo.sh` success and tests.

`scripts/validate_repo.sh` (starter)

```bash
#!/usr/bin/env bash
set -euo pipefail

printf "
[1/6] Checking required files...
"
ls README.md CHANGELOG.md >/dev/null

printf "[2/6] Lint/format...
"
if command -v ruff >/dev/null; then ruff check .; fi
if command -v ruff >/dev/null; then ruff format --check . || ruff format .; fi
if command -v eslint >/dev/null; then npx eslint . || true; fi

printf "[3/6] Type checks...
"
if command -v pyright >/dev/null; then pyright || true; fi

printf "[4/6] Unit tests...
"
if command -v pytest >/dev/null; then pytest -q || true; fi
if [ -f package.json ]; then (npm test || true); fi

printf "[5/6] Repo spec validation...
"
python - <<'PY'
import os, sys, yaml, glob
spec_path = os.environ.get('REPO_SPEC', '.repo-spec.yaml')
if not os.path.exists(spec_path):
    print('[info] no .repo-spec.yaml found; skipping')
    sys.exit(0)
spec = yaml.safe_load(open(spec_path)) or {}
for req in spec.get('required_paths', []):
    if not glob.glob(req):
        print(f'[error] missing required path: {req}')
        sys.exit(1)
print('[ok] repo-spec satisfied')
PY

printf "[6/6] Smoke run...
"
python -m src.app --dry-run 2>/dev/null || true

printf "
All checks completed.
"
```

### Policies as Data

- Put constraints in machine-readable files: `and` rather than hardcoding.
- Drive validators and CI gates from these specs.

**If a policy changes:** update YAML first; validators read it at runtime.\
**If a team needs exceptions:** encode allowlists in the YAML and expire them with dates.

Example `.repo-spec.yaml`

```yaml
required_paths:
  - "README.md"
  - "CHANGELOG.md"
  - "docs/adr/*.md"
  - "scripts/test.sh"
  - "config/app.yaml"
  - "src/**"
policy:
  max_file_kb: 512
  forbid_extensions: [".pem", ".key", ".p12"]
  require_codeowners: true
exceptions:
  - path: "docs/assets/*"
    expires: 2026-01-01
    reason: "Large images allowed for branding"
```

---

## Universal Repository Guidelines

A drop-in, stack-agnostic set of **Pragmatic Programmer**-aligned guidelines, validators, and automation to make any repository **multi-agent friendly**, **merge-safe**, and **always shippable**.

### Key Ideas

- **Orthogonality** & **Single Source of Truth (SSOT)**
- **Tracer bullets** before big refactors
- **No broken windows**: keep `main` green
- **Small, modular PRs** with clear ownership (`CODEOWNERS`)
- **Language auto-detection** → pluggable validators
- **Policy as data** via `/.repo-spec.yaml` and `/policies/*.yaml`

### Quick Start

```bash
# 1) (optional) Install pre-commit hooks to auto-format/statically-lint
./scripts/install_hooks.sh

# 2) Validate repo health (auto-detects languages)
./scripts/validate_repo.sh

# 3) See reports
cat reports/manifest.json
```

### Layout

```
.
├── .editorconfig
├── .gitattributes
├── .gitignore
├── .pre-commit-config.yaml
├── .repo-spec.yaml
├── .github/workflows/validate.yml
├── CODEOWNERS
├── GUIDELINES.md
├── CHANGELOG.md
├── README.md
├── policies/
│   ├── policy.yaml
│   └── wcag-aa.md
├── validators/
│   ├── python/
│   │   ├── lint.sh
│   │   ├── test.sh
│   │   ├── build.sh
│   │   └── audit.sh
│   ├── node/
│   │   ├── lint.sh
│   │   ├── test.sh
│   │   ├── build.sh
│   │   └── audit.sh
│   ├── go/
│   │   ├── lint.sh
│   │   ├── test.sh
│   │   ├── build.sh
│   │   └── audit.sh
│   └── rust/
│       ├── lint.sh
│       ├── test.sh
│       ├── build.sh
│       └── audit.sh
├── scripts/
│   ├── validate_repo.sh
│   └── install_hooks.sh
└── docs/
    ├── tech_debt.md
    └── adr/0001-repo-structure.md
```

### Multi-Agent Collaboration

- Use `feature/*`, `fix/*`, `experiment/*` branches.
- Keep PRs ≤ 500 LOC when feasible.
- Respect `CODEOWNERS`; update `docs/adr/` for non-obvious decisions.

### CI

GitHub Actions runs `./scripts/validate_repo.sh` on PR and push to keep `main` shippable.

### Logo Integration

- Your logo can live at `assets/logo.png` with theme-aware styles in `assets/logo.css`.
- Preview in a browser via `docs/logo_preview.html` (supports light/dark, accent demo).
- Usage:
  ```html
  <link rel="stylesheet" href="/assets/logo.css">
  <img src="/assets/logo.png" class="themed-logo" alt="Logo">
  ```

## Repository Blueprint

```
repo/
├─ src/                      # app code (modules by domain)
│  ├─ api/                   # REST/GraphQL endpoints
│  ├─ ui/                    # web app / components
│  ├─ agents/                # LLM tools, schemas, planners
│  ├─ jobs/                  # batch/cron workers
│  ├─ utils/                 # shared helpers (logging, io, feature_gates)
│  └─ ml/                    # optional: data prep, training, inference
├─ config/                   # *.yaml + .env.example
├─ data/                     # local dev data (never commit secrets)
│  ├─ raw/  └─ processed/
├─ logs/                     # jsonl logs by date/agent/run_id
├─ tests/                    # unit/integration tests
├─ scripts/                  # dev/test/lint/ci helpers
├─ docs/                     # this playbook split into files
│  ├─ FOUNDATIONAL.md
│  ├─ DEPLOYMENT.md
│  ├─ CLAUDE.md
│  ├─ GEMINI.md
│  └─ AGENTS.md
├─ .editorconfig  .gitignore  .pre-commit-config.yaml
├─ pyproject.toml  (or) requirements.txt  (and) package.json if web
├─ Dockerfile  docker-compose.yml (optional in Stage 1)
└─ README.md  CHANGELOG.md  LICENSE
```

**If the project has a mono‑repo:** add `/packages/*` and `/apps/*` with shared tooling at the root.\
**If the project is Python‑only:** keep Node assets out; use Ruff/Black/pytest only.\
**If the project ships a design system:** add `/src/ui/design_system` and Storybook config.

---

## FOUNDATIONAL (Stage 1)

### Definition of Done

- One real user flow works end‑to‑end in local dev.
- `scripts/test.sh` passes: lint, type‑check, unit tests, smoke run.
- Logs are structured JSONL with **run\_id** and minimal PII‑safe fields.
- Doc set includes: README (setup/run/test), CHANGELOG (SemVer), this Foundational guide.
- Optional subsystem (API/UI/ML/Agents) has basic tests and an example.

### Environment & Tooling

- **Language toolchain**: pin versions (e.g., Python ≥3.11, Node ≥20).
- **Linters/formatters**: Python (Ruff/Black), JS (ESLint/Prettier).
- **Pre‑commit**: enforce lint/format on staged files.
- **Testing**: pytest + coverage (Python), Vitest/Jest (JS).
- **Make/dev scripts**: `scripts/dev_up.sh`, `scripts/test.sh`, `scripts/format.sh`.

**If the project uses GPUs:** include `scripts/nvidia_check.sh` to print CUDA, driver, and device list.\
**If multi‑OS support is needed:** prefer `uv`/`pipx` or `uvx` (Python) and `corepack`/`pnpm` (Node) for reproducible installs.

### Configuration

- Use `` (local only) + **YAML** under `config/`.
- `config/app.yaml` minimal keys:
  - `env: development|staging|production`
  - `logging: {level, dir, rotation_mb, retention_days}`
  - `features: {}` (empty in Stage 1)
  - `providers: {openai|anthropic|gemini: {model, api_key_env, timeouts}}`

**If secrets are required:** refer only by env var, commit `.env.example`, never actual keys.\
**If multiple environments:** support `config/app.<env>.yaml` with merge semantics.

#### Validate config at startup (fail fast)

Use a schema so misconfig is caught on boot, not in a deep code path.

```python
# src/config.py
from pydantic import BaseModel, Field
from typing import Optional
import os, yaml

class LoggingCfg(BaseModel):
    level: str = "INFO"
    dir: str = "logs"
    rotation_mb: int = 64
    retention_days: int = 90

class ProviderCfg(BaseModel):
    model: str
    api_key_env: str
    timeout_s: int = 60

class AppCfg(BaseModel):
    env: str = Field(pattern=r"^(development|staging|production)$")
    logging: LoggingCfg
    features: dict = {}
    providers: dict[str, ProviderCfg]

def load() -> AppCfg:
    with open("config/app.yaml", "r", encoding="utf-8") as f:
        raw = yaml.safe_load(f) or {}
    cfg = AppCfg(**raw)
    # ensure any declared api_key_env exists (in dev we warn, in prod we fail)
    missing = [p.api_key_env for p in cfg.providers.values() if not os.getenv(p.api_key_env)]
    if cfg.env == "production" and missing:
        raise RuntimeError(f"Missing required secrets: {missing}")
    return cfg
```

**If running under container/orchestrator:** surface a clear startup error and exit non‑zero.

### Logging & Run IDs

- Every entry point (CLI/API request/agent loop) generates a **UUID **``.
- Log structure (JSONL): `{ts, level, run_id, component, event, input_hash?, output_hash?, status, latency_ms, extras}`.
- File layout: `logs/YYYY/MM/DD/<component>/<run_id>.jsonl`.

**If PII may appear:** add a redaction helper; never log secrets, access tokens, or raw user data.\
**If SQLite is handy in dev:** mirror a subset to `logs/dev_runs.sqlite` for ad‑hoc queries (no dashboards yet).

#### Log levels (when to use what)

| Level     | Use in dev                                                                                       | Use in prod                                                                 |
| --------- | ------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------- |
| **DEBUG** | Verbose details (payload shapes, branch choices). Enable only when debugging a specific issue.   | Off by default; enable per‑component temporarily.                           |
| **INFO**  | One line per meaningful step: start/stop, external call, cache hit/miss, feature flag decisions. | Default level for business events and major state changes.                  |
| **WARN**  | Recoverable anomalies: retryable API failure, fallback taken, partial results.                   | Alert if rate exceeds threshold; include `trace_id` and `retry_count`.      |
| **ERROR** | Unrecoverable in the current flow; user‑visible failure.                                         | Always emit with `run_id`/`trace_id`, include upstream codes and durations. |
| **FATAL** | Process cannot continue (config invalid, migrations missing).                                    | Crash early with clear remediation; ensure crash loops are throttled.       |

**Rule:** prefer **INFO** for the golden path; push details to **DEBUG** and metrics to the **/metrics** endpoint later.

### Validation & QA (Basic)

- `scripts/test.sh` runs: format → lint → type check → unit tests → smoke run (`python -m src.app --dry-run`).
- Minimal **validator** checks: required folders/files exist; README has install/run instructions; no large files in Git.

#### Composable validator modules

Start tiny and add modules as you grow.

```
validators/
  python/{lint.sh,test.sh,audit.sh}
  node/{lint.sh,test.sh,audit.sh}
validate.d/
  10-required.sh
  20-python.sh
  30-node.sh
```

`./scripts/validate_repo.sh` (driver):

```bash
#!/usr/bin/env bash
set -euo pipefail
for s in $(ls validate.d/*.sh 2>/dev/null | sort); do
  echo "[validate] $s"; bash "$s" || exit 1; done
```

Example `validate.d/20-python.sh`:

```bash
#!/usr/bin/env bash
set -euo pipefail
if ls **/*.py >/dev/null 2>&1; then
  ./validators/python/lint.sh || true
  ./validators/python/test.sh || true
  ./validators/python/audit.sh || true
else
  echo "[skip] no python"
fi
```

**If monorepo:** create one `validate.d` per package, and a root driver that iterates over packages.

### Security Baseline

- Pin dependencies; activate `pip audit` / `npm audit` locally (no CI gates yet).
- `.env` is **git‑ignored**; examples go to `.env.example`.
- Rotate keys manually if leaked.

#### Stage‑1 Minimal Security Checklist (progressive)

- **Secret scanning**: enable a pre‑commit hook or `git-secrets`/`trufflehog` locally.
- **Input validation**: validate and sanitize all external inputs (CLI args, HTTP bodies) using a schema (Pydantic/Zod).
- **Dependency hygiene**: `pip audit` / `npm audit --audit-level=high` at least weekly.
- **Least privilege**: local API keys with minimal scopes; never share prod keys in dev.
- **Safe logging**: redact tokens/PII; cap log line length; ban binary blobs in logs.
- **Sample data**: use synthetic/minimized datasets in `data/sample.*`.

**If handling PII even in dev:** encrypt local storage, scrub logs, and require explicit consent notes in `docs/data_notes.md`.

### Data Handling

- Keep a **data README** in `data/` describing sources and licenses.
- Track dataset versions by folder name + `DATASET_VERSION` env.

**If CSV/Parquet ingestion:** validate headers and types; sample top/bottom rows to detect corruption.\
**If joins/merges:** add row counts pre/post with assertions in logs.

### ML/Analytics (optional)

- Directory: `src/ml/{prep,models,infer}`.
- Repro seed: `PYTHONHASHSEED`, torch/numpy seeds.
- Save metrics as JSON (per run) under `logs/ml/`.

**If training:** write `train.py --config config/train.yaml` and persist `metrics.json` + artifact path.\
**If GPU available:** autocast/mixed precision, gradient clipping, batch size explore.\
**If timeseries:** split by time (no leakage), baseline vs model chart saved to `reports/`.

### Web/API (optional)

- API: FastAPI/Express with `/healthz`, `/version`, `/metrics` (noop in Stage 1).
- UI: modular components, global CSS vars, dark/light toggle.

**If file uploads:** size limits + MIME whitelist.\
**If streaming:** use server‑sent events or WebSocket with backpressure.

### Agents & Tool‑Use (optional)

- Keep tools deterministic: idempotent, validated inputs, timeouts, retries.
- Define function schemas (JSON Schema) per provider.
- Start with a **single agent** and 1–3 tools.

**If calling external APIs:** wrap with circuit breakers and rate‑limiters.\
**If planning/multi‑step needed:** add a light planner (react‑style) with a max‑steps guard.

### Agent Safety & Governance

- **Autonomy levels**:
  - **L0**: prompt‑only; no tools; read‑only outputs.
  - **L1**: safe tools (search, summarize); sandboxed FS; no network writes.
  - **L2**: modifies files/services in dev; **dry‑run diff required**; reviewer approval.
  - **L3**: prod changes behind **feature flag**, change ticket, and explicit approval.
- **Kill‑switch**: global env var + runtime flag to disable tool‑calls instantly.
- **Sandboxes**: FS allowlist per tool, outbound egress allowlist, per‑tool rate limits.
- **No silent edits**: every write yields a preview/diff + log entry with reviewer.

**If an agent touches prod or secrets:** require 4‑eyes approval and log consent IDs.\
**If human input is ambiguous:** escalate with a clarifying question before execution.

### Provider Adapter & Fallback

- **Adapter layer**: `src/agents/provider_adapter.py` normalizes calls for OpenAI/Anthropic/Gemini.
- **Primary/fallback**: choose primary via `APP_PRIMARY_PROVIDER`; fallback after N failures/M minutes.
- **Backoff**: exponential with jitter; respect provider rate‑limit headers.

**If outage/cost spike is detected:** failover behind a feature flag; degrade to "fast" models.\
**If responses are cacheable:** enable prompt+tools+params **response cache** with TTL.

### Token & Cost Budgets

- **Per‑request caps**: max tokens, max tool‑calls, max latency.
- **Per‑run budget**: cumulative token limit; stop when exceeded.
- **Monthly budget guard**: degrade models and disable non‑essential features when budget reached.

**If a call exceeds limits:** cut off generation (stream), summarize partials, and record a budget event.\
**If heavy flows (RAG/codegen):** prefetch/cache deterministic steps.

### Data Contracts (Optional)

- Define **input/output schemas** with Pydantic or JSON Schema; validate at boundaries.
- Add **Great Expectations** or lightweight checks for files (columns, types, ranges).

**If a contract breaks:** fail fast with a human‑readable diff and guidance in logs.\
**If contracts evolve:** version schemas and support backward‑compatible transitions.

---

## DEPLOYMENT (Stage 2+)

### Infra Patterns

- **Small apps**: Docker Compose with 1–3 services (api/ui/worker).
- **Growing apps**: Kubernetes (Helm), external Postgres/Redis, object storage.
- **Edge/Realtime**: colocate near users; ensure low‑latency model endpoints.

**If cron/batch exists:** use a separate worker deployment and a queue (e.g., Redis, SQS, Pub/Sub).\
**If GPU inference:** node selectors/taints; GPU quotas; warm pools.

### Security Hardening

- Secrets: managed store (Vault/Cloud KMS/Secrets Manager).
- SBOM: CycloneDX; SCA in CI (fail on critical).
- SAST/DAST: Bandit/ESLint‑security, ZAP baseline scan.
- Supply chain: pin registries, verify signatures, provenance attestations.

**If handling PII:** DLP policies, encryption at rest and in transit, field‑level redaction in logs.\
**If multi‑tenant:** per‑tenant keys, row‑level security, authz middleware.

### Observability

- Metrics: request counts, error rates, P50/P95 latency, queue depth.
- Tracing: propagate `trace_id`/`span_id`, instrument hot paths.
- Logs: ship to ELK/Cloud Logging; keep JSON structure.

**If realtime/WS:** expose event loop metrics and dropped‑message counters.\
**If batch:** surface runtime histograms and failure reasons.

### Run Registry & Retention

- Create `runs.sqlite` or external DB with `runs(run_id, start_ts, end_ts, status, owner, tags, env)`.
- Prune policy by env: dev 90 days, prod 365 days.

**If compliance requires longer storage:** move cold logs to object storage with lifecycle rules.\
**If analytics needed:** mirror to Parquet for BI.

### Feature Flags & Experiments

- `config/features.yaml` with `enabled`, `owners`, and optional rollout % or allowlist.
- Kill‑switch checks at entry points.

**If A/B tests:** randomize by stable unit (user/org), log exposure + outcome.

### Caching Strategy

- Levels: in‑process (LRU), distributed (Redis), and CDN for static assets.
- Define TTLs by data volatility; include cache keys in logs.

**If LLM calls are pricey:** enable response caching keyed by (prompt+tools+params).\
**If embeddings used:** cache vectors; manage drift with versioned namespaces.

### Data & Model Management

- Migrations: Alembic/Prisma; versioned scripts in `/migrations`.
- Artifacts: model registry/folder with metadata and checksum.
- Evals: golden sets, regression thresholds, skew/drift monitors.

**If fine‑tuning:** track dataset lineage; archive prompts/labels; eval before/after.\
**If online inference:** shadow traffic and canary before 100% rollout.

### Release & Change Management

- Versioning: Semantic Versioning; **changelog required** for each release.
- CI/CD: build, test, scan, sign, deploy; blue/green or canary.

**If mobile/desktop clients:** feature toggles tied to minimum app versions.\
**If schema changes:** contract tests; backward‑compatible migrations.

### Performance & Cost

- Budgets: p95 latencies per endpoint; monthly spend guards per provider.
- Load test: staged RPS sweeps; capture saturation curves.

**If vector DB:** measure ingestion QPS and recall vs cost; pre‑filter aggressively.\
**If realtime voice:** measure end‑to‑end RTT with cold vs warm paths.

### Ops Playbooks

- **Incident**: severities, comms templates, oncall rotation, status page.
- **Rollback**: fast revert, data restore steps, verification checks.
- **Runbooks**: top 10 alerts each have a resolution guide.

---

## Templates & Snippets

### `scripts/test.sh`

```bash
#!/usr/bin/env bash
set -euo pipefail

# Format & lint
ruff check .
ruff format --check . || ruff format .

# Type checks (optional)
if command -v pyright >/dev/null; then pyright ; fi

# Unit tests
pytest -q --disable-warnings --maxfail=1 --cov=src --cov-report=term-missing

# Smoke run (no side effects)
python -m src.app --dry-run || true
```

### Minimal Python logger (`src/utils/logger.py`)

```python
from __future__ import annotations
import json, os, time, uuid, pathlib
from typing import Any, Mapping

LOG_DIR = os.getenv("LOG_DIR", "logs")

def _path(component: str, run_id: str) -> pathlib.Path:
    ts = time.gmtime()
    d = pathlib.Path(LOG_DIR)/f"{ts.tm_year:04d}"/f"{ts.tm_mon:02d}"/f"{ts.tm_mday:02d}"/component
    d.mkdir(parents=True, exist_ok=True)
    return d / f"{run_id}.jsonl"

def new_run_id() -> str:
    return str(uuid.uuid4())

def log(component: str, run_id: str, event: str, level: str = "INFO", **extras: Any) -> None:
    rec = {
        "ts": int(time.time() * 1000),
        "level": level,
        "run_id": run_id,
        "component": component,
        "event": event,
        **extras,
    }
    p = _path(component, run_id)
    with p.open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "
")
```

### Feature gates (`src/utils/feature_gate.py`)

```python
import yaml, os
from functools import lru_cache

@lru_cache(maxsize=1)
def _cfg():
    path = os.getenv("FEATURES_YAML", "config/features.yaml")
    if not os.path.exists(path):
        return {"features": {}}
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {"features": {}}

def enabled(name: str, default: bool = False) -> bool:
    return (_cfg().get("features", {}).get(name, {}) or {}).get("enabled", default)
```

### `config/app.yaml` (excerpt)

```yaml
env: development
logging:
  level: INFO
  dir: logs
  rotation_mb: 64
  retention_days: 90
providers:
  openai:
    model: auto
    api_key_env: OPENAI_API_KEY
    timeout_s: 60
  anthropic:
    model: auto
    api_key_env: ANTHROPIC_API_KEY
    timeout_s: 60
  gemini:
    model: auto
    api_key_env: GEMINI_API_KEY
    timeout_s: 60
features: {}
```

### CHANGELOG template (`CHANGELOG.md`)

```markdown
# Changelog
All notable changes are documented here. Format follows Keep‑a‑Changelog; versions follow SemVer.

## [Unreleased]
### Added
### Changed
### Fixed
### Deprecated
### Removed
### Security

## [1.0.0] – YYYY‑MM‑DD
- Initial release.
```

### ADR template (`docs/adr/0001-title.md`)

```markdown
# 0001 – Title
Date: YYYY‑MM‑DD
Status: Proposed | Accepted | Superseded

## Context
Why a decision is needed.

## Decision
What is chosen and why.

## Consequences
Trade‑offs and follow‑ups.
```

### `scripts/install_hooks.sh`

```bash
#!/usr/bin/env bash
set -euo pipefail

if command -v pre-commit >/dev/null; then
  pre-commit install --install-hooks
else
  echo "[warn] pre-commit not installed. Install with: pip install pre-commit" >&2
fi
```

### GitHub Actions CI (`.github/workflows/validate.yml`)

```yaml
name: Validate Repo
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Install Python tooling
        run: |
          python -m pip install --upgrade pip
          pip install ruff pytest pyyaml
      - name: Validate repository
        run: |
          bash ./scripts/validate_repo.sh
      - name: Run tests
        run: |
          bash ./scripts/test.sh || true
```



---

## Case Study: Tempo Agents (A2A) — Drop‑in Integration

*This maps the Playbook to your A2A micro‑system (FastAPI + JSON‑RPC‑like envelopes) so it’s shippable in Stage 1 and easy to harden in Stage 2.*

### Objectives

- **Dynamic intent routing** via `configs/routes.yaml` (overridden by `ROUTES_CONFIG`).
- **Stable envelopes** for request/response with validation.
- **Structured logs** that satisfy the Agent Action Logging Standard.
- **Portable scripts** for local dev (`run_all`, `send_rpc`).

### Envelope (request/response)

```jsonc
// Request
{
  "id": "uuid-4",
  "intent": "echo.ping",           // dot-namespaced
  "payload": {"hello": "world"},   // arbitrary JSON payload
  "meta": {
    "ts": "2025-08-10T12:00:00Z",
    "run_id": "...",                 // generated per call
    "trace_id": "...",               // stable across hops
    "src": "gateway",
    "version": "1"
  }
}

// Response
{
  "id": "same-as-request",
  "ok": true,
  "result": {"hello": "world"},
  "error": null,
  "meta": {"ts": "...", "run_id": "...", "trace_id": "..."}
}
```

**If ****\`\`**** is false:**

```json
{"id":"...","ok":false,"error":{"code":"INTENT_NOT_FOUND","message":"...","data":{}}}
```

### Pydantic models (gateway)

```python
from pydantic import BaseModel, Field
from typing import Any, Optional, Dict

class Meta(BaseModel):
    ts: Optional[str] = None
    run_id: Optional[str] = None
    trace_id: Optional[str] = None
    src: Optional[str] = None
    version: str = "1"

class RpcRequest(BaseModel):
    id: str
    intent: str = Field(pattern=r"^[A-Za-z][A-Za-z0-9_.]{2,64}$")
    payload: Dict[str, Any] | None = None
    meta: Meta | None = None

class RpcError(BaseModel):
    code: str
    message: str
    data: Dict[str, Any] | None = None

class RpcResponse(BaseModel):
    id: str
    ok: bool = True
    result: Any | None = None
    error: RpcError | None = None
    meta: Meta | None = None
```

### `configs/routes.yaml` (example)

```yaml
# intent → agent base URL
routes:
  echo.:  http://127.0.0.1:8101
  math.:  http://127.0.0.1:8102
  task.:  http://127.0.0.1:8103
  policy.: http://127.0.0.1:8104
timeouts:
  connect_s: 2
  total_s: 10
retries:
  max_attempts: 2
  backoff_s: 0.2
```

### FastAPI gateway (core)

```python
from fastapi import FastAPI, Request
import httpx, time, uuid
from .models import RpcRequest, RpcResponse, RpcError, Meta
from .logging import log, new_run_id
from .routes import resolve_target

app = FastAPI()

@app.post("/rpc", response_model=RpcResponse)
async def rpc(req: RpcRequest, request: Request) -> RpcResponse:
    run_id = req.meta.run_id if req.meta and req.meta.run_id else new_run_id()
    trace_id = request.headers.get("x-trace-id", req.meta.trace_id if req.meta else str(uuid.uuid4()))
    t0 = time.time()

    target = resolve_target(req.intent)
    if not target:
        log("gateway", run_id, "route.miss", intent=req.intent)
        return RpcResponse(id=req.id, ok=False, error=RpcError(code="INTENT_NOT_FOUND", message=req.intent))

    # forward
    payload = req.model_dump()
    payload.setdefault("meta", {})
    payload["meta"].update({"run_id": run_id, "trace_id": trace_id, "src": "gateway", "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())})

    try:
        async with httpx.AsyncClient(timeout=httpx.Timeout(10.0)) as client:
            r = await client.post(f"{target}/rpc", json=payload, headers={"x-run-id": run_id, "x-trace-id": trace_id})
            r.raise_for_status()
            data = r.json()
    except httpx.HTTPError as e:
        log("gateway", run_id, "forward.error", intent=req.intent, error=str(e))
        return RpcResponse(id=req.id, ok=False, error=RpcError(code="UPSTREAM_ERROR", message=str(e)))

    log("gateway", run_id, "forward.ok", intent=req.intent, ms=int((time.time()-t0)*1000))
    return RpcResponse(**data)
```

### Logging — map to the standard

Record per call: `{ts, run_id, trace_id, component, event, intent, target, status, latency_ms}`. Store under `logs/YYYY/MM/DD/gateway/<run_id>.jsonl`.

**If the agent performs writes:** include `diff_uri` or `artifact_uri` in `output_refs` and require a reviewer on L2+.

### Minimal handlers

```python
# echo agent
async def echo_ping(payload: dict) -> dict: return payload

# math agent
async def math_add(payload: dict) -> dict:
    a, b = int(payload.get("a", 0)), int(payload.get("b", 0))
    return {"sum": a + b}
```

### Tests (Stage 1)

- Happy paths: `echo.ping`, `math.add` → 200 with expected bodies.
- Routing: unknown intent → `{ok:false, error.code: INTENT_NOT_FOUND}`.
- Validation: invalid `intent` pattern → 422; missing `id` → 422.
- Timeouts/retries: simulate slow agent; assert gateway surfaces `UPSTREAM_ERROR` after N retries.

### Security & hardening (Stage 2)

- **Auth**: JWT on `/rpc` (aud/iss checks) or mTLS between gateway ↔ agents.
- **Rate limit**: per source IP and per intent; log drops.
- **Registry**: persistent service registry (health, version, owner); expose `/healthz`, `/version`.
- **Headers**: propagate `x-run-id`/`x-trace-id`; forbid hop-by-hop headers.

#!/usr/bin/env python3
"""
Prototype Validation Script
Ensures any project follows PROTOTYPING_GUIDELINES.md
"""

import os
import sys
from pathlib import Path

def validate_structure():
    """Check if project follows required structure"""
    errors = []
    
    # Check README.md exists
    if not Path("README.md").exists():
        errors.append("❌ Missing README.md")
    
    # Check src/ directory exists
    if not Path("src").exists():
        errors.append("❌ Missing src/ directory")
    
    # Check for at least one file in src/
    src_files = list(Path("src").glob("*")) if Path("src").exists() else []
    if not src_files:
        errors.append("❌ src/ directory is empty")
    
    return errors

def validate_readme():
    """Check if README.md follows template"""
    errors = []
    
    if not Path("README.md").exists():
        return ["❌ README.md missing"]
    
    content = Path("README.md").read_text()
    
    required_sections = ["# ", "## How to Run", "## Features"]
    for section in required_sections:
        if section not in content:
            errors.append(f"❌ README.md missing section: {section}")
    
    return errors

def validate_file_headers():
    """Check if source files have required headers"""
    errors = []
    
    src_path = Path("src")
    if not src_path.exists():
        return ["❌ src/ directory missing"]
    
    source_files = []
    for ext in ["*.py", "*.js", "*.html", "*.css"]:
        source_files.extend(src_path.glob(ext))
    
    for file_path in source_files:
        content = file_path.read_text()
        
        # Check for header elements
        required_headers = ["Language:", "File:", "Version:", "Project:", "Author: Rod Sanchez"]
        missing_headers = [h for h in required_headers if h not in content]
        
        if missing_headers:
            errors.append(f"❌ {file_path}: Missing headers: {missing_headers}")
    
    return errors

def main():
    print("🔍 Validating prototype against PROTOTYPING_GUIDELINES.md")
    print("=" * 60)
    
    all_errors = []
    
    # Validate structure
    print("Checking project structure...")
    structure_errors = validate_structure()
    all_errors.extend(structure_errors)
    
    # Validate README
    print("Checking README.md...")
    readme_errors = validate_readme()
    all_errors.extend(readme_errors)
    
    # Validate file headers
    print("Checking file headers...")
    header_errors = validate_file_headers()
    all_errors.extend(header_errors)
    
    print("=" * 60)
    
    if all_errors:
        print("❌ VALIDATION FAILED")
        for error in all_errors:
            print(f"  {error}")
        print("\n🔧 Please fix these issues to comply with PROTOTYPING_GUIDELINES.md")
        sys.exit(1)
    else:
        print("✅ VALIDATION PASSED")
        print("🎉 Project complies with PROTOTYPING_GUIDELINES.md")
        sys.exit(0)

if __name__ == "__main__":
    main()