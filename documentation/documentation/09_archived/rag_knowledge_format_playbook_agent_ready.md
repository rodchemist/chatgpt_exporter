# RAG Knowledge Format Playbook (Agent‑Ready)

This is a pragmatic guide to **store, exchange, and index knowledge** for Retrieval‑Augmented Generation (RAG) with automation/agent workflows.

---

## TL;DR
- **Author in:** Markdown or docs/PDF → normalize to **Markdown (.md)** with **YAML front‑matter**.
- **Exchange & ingestion pipeline:** **JSONL**, one record per chunk (append‑only, streamable, tool‑friendly).
- **At‑scale analytics/storage:** **Parquet/Delta** tables for cheap, columnar ops (Spark/DuckDB/Polars friendly).
- **Indexes:** Vector store of your choice + a light **SQLite** (or DuckDB) for provenance & routing.
- **Metadata is king:** stable IDs, source path, semantic section path, timestamps, tags, security tier.
- **Chunking:** semantic+layout aware, 500–1,200 tokens, with **overlap** and **titles** preserved.

---

## Why these formats?
- **Markdown (.md)** with YAML front‑matter is human‑first (easy to author/review/PR) and loss‑minimal after OCR.
- **JSONL** is agent‑friendly: streamable, append‑only, trivial to validate, compatible with most RAG tools.
- **Parquet/Delta** is machine‑first for scale: columnar compression, schema evolution, blazing filters/joins.

---

## Canonical Authoring Format
Prefer **Markdown with YAML front‑matter** as the canonical source of truth.

**Example (`/knowledge/canonical/guide_to_tempering.md`):**
```markdown
---
id: doc:choco-tempering:2024-11-18
source: "Dare Foods / Lab SOP"
author: Rodrigo
lang: es
doc_type: SOP
version: 3
security: internal
created_at: 2024-11-18
updated_at: 2025-09-24
tags: [chocolate, tempering, QA]
---
# Guía de templado de chocolate

## Objetivo
Establecer el procedimiento estándar...

### Parámetros críticos
- Temperatura curva A...
```

**Notes**
- Keep headings hierarchical (H1/H2/H3) → helps semantic chunking.
- Use lists and tables; avoid giant paragraphs.
- If you must keep PDFs, store **both**: the original PDF and an **extracted .md**.

---

## Exchange / Ingestion Format (JSONL)
JSON Lines where **each line = one chunk**. Stable, streamable, easy to diff.

**Recommended minimal schema**
```json
{
  "id": "chunk:choco-tempering:0001",
  "doc_id": "doc:choco-tempering:2024-11-18",
  "source": "knowledge/canonical/guide_to_tempering.md",
  "title_path": ["Guía de templado de chocolate", "Parámetros críticos"],
  "text": "- Temperatura curva A...",
  "lang": "es",
  "tags": ["chocolate", "tempering", "QA"],
  "security": "internal",
  "created_at": "2024-11-18T00:00:00Z",
  "updated_at": "2025-09-24T00:00:00Z",
  "hash": "sha256:...",
  "page": 7,
  "section_ix": 2,
  "chunk_ix": 1,
  "chunk_size_tokens": 420,
  "overlap_tokens": 80,
  "embeddings": null
}
```

**Variants**
- Add `citations: [{span: [0,120], target: "ISO22000:2018 8.5"}]` when mapping to standards.
- Add `permissions: {allow: ["qa"], deny: ["external"]}` for agent routing.

---

## Analytics / Lakehouse Format (Parquet or Delta)
- Mirror the JSONL schema into a **Parquet** table (or **Delta** for ACID/time‑travel).
- Keep **one table per collection** (e.g., `docs`, `chunks`, `embeddings`, `events`).
- Use **DuckDB/Polars** locally; **Spark** in clusters.

**Minimal tables**
- `docs(doc_id, path, version, lang, tags, security, created_at, updated_at, hash)`
- `chunks(id, doc_id, title_path, text, page, section_ix, chunk_ix, chunk_size_tokens, overlap_tokens, lang, tags, security, hash)`
- `embeddings(id, vector, model, dims, norm, created_at)`
- `events(ts, type, actor, doc_id, chunk_id, payload)`  

---

## Vector Index & DB Layer
- **Vector store:** FAISS/HNSW/Qdrant/Weaviate/Chroma—all are fine. Choose based on ops:
  - **FAISS**: local, fast, no server (great for your workstation).
  - **Qdrant/Weaviate**: server mode, filters, sharding, cloud options.
- **Relational sidecar:** **SQLite** (or DuckDB) to store metadata/provenance, and to route queries (security filters, languages, collections). Keep vectors separate but joinable on `chunk_id`.

**Example sidecar schema (SQLite)**
```sql
CREATE TABLE chunks (
  id TEXT PRIMARY KEY,
  doc_id TEXT,
  lang TEXT,
  security TEXT,
  tags TEXT, -- JSON
  title_path TEXT, -- JSON array
  path TEXT,
  created_at TEXT,
  updated_at TEXT
);
```

---

## Chunking Policy (pragmatic)
- **Unit:** 500–1,200 tokens per chunk, **80–150 token overlap**.
- **Respect structure:** start chunks at headings; include `title_path` so answers cite section titles.
- **Deduplicate:** hash normalized text (lowercase + strip whitespace) to avoid repeated chunks.
- **Multilingual:** keep `lang` at chunk level; add `transcript_of` if translated.
- **Tables & code:** preserve as fenced blocks; consider separate `table_json` field if you’ll query cells.

---

## File/Folder Layout (agent‑friendly)
```
/knowledge
  /canonical        # human‑authored .md (plus original PDFs)
  /staging          # raw dumps before cleaning
  /exchange         # *.jsonl ready for ingestion (chunks)
  /lakehouse        # parquet/delta tables (docs, chunks, embeddings)
  /embeddings       # optional: binary shards for FAISS or .npy
  /indexes          # vector store files (FAISS) or client configs
  /manifests        # RUN sheets for agents (YAML)
```

**Ingestion manifest (`/knowledge/manifests/tempering.yaml`)**
```yaml
collection: qa-sops
source_globs: ["knowledge/canonical/**/*.md"]
chunk:
  target_tokens: 900
  overlap_tokens: 120
  keep_headings: true
  merge_small_sections: true
output:
  jsonl: knowledge/exchange/qa-sops.jsonl
  parquet: knowledge/lakehouse/chunks.parquet
embeddings:
  model: text-embedding-3-large
  dims: 3072
  out: knowledge/lakehouse/embeddings.parquet
security:
  default: internal
```

---

## Provenance, Versioning, and Auditability
- **Stable IDs**: `doc:<slug>:<date>` and `chunk:<slug>:<0001>`; never reuse.
- **Hashes**: store `sha256` per doc/chunk; recompute during ETL to detect drift.
- **Lineage**: record `source` path + git commit of canonical repo.
- **Time‑travel**: Parquet/Delta + `version` in YAML front‑matter.

---

## What do agents actually read?
1. **Planner agent** queries the sidecar DB to pick collections by `tags`, `security`, `lang`.
2. **Retriever agent** hits the vector store with filters (lang/security) + reranker.
3. **Citer agent** uses `title_path` and `source` to build citations.
4. **Memory agent** writes back **events** (feedback, thumbs, outcomes) → improves re‑ranking and freshness.

---

## Validation & Health Checks
- **Schema check**: ensure required keys (id, doc_id, text) exist per JSON line.
- **UTF‑8** only; normalize newlines; strip trailing spaces.
- **Token limits**: assert target window for your LLM.
- **Leak check**: scan `security != public` before publishing.

---

## Converters & Tooling (typical)
- **Markdown ⇄ JSONL**: simple Python scripts; or use `unstructured` processors; or LlamaIndex/LangChain loaders.
- **PDF → Markdown**: `ocrmypdf` → `pandoc` → post‑process; or `unstructured`.
- **Tables**: extract to CSV/JSON alongside chunks for precise QA.
- **Parquet**: `pyarrow`/`polars`/`duckdb`.  

---

## Minimal JSONL Contract (ready for your pipelines)
Use this **exact** header set in your agent systems for easy interoperability.

```json
{
  "id": "chunk:<collection>:<0001>",
  "doc_id": "doc:<collection>:<slug>:<yyyy-mm-dd>",
  "collection": "qa-sops",
  "text": "...",
  "title_path": ["H1", "H2", "H3"],
  "lang": "es",
  "tags": ["sop", "qa"],
  "security": "internal",
  "source": "repo://knowledge/canonical/file.md",
  "page": 7,
  "section_ix": 2,
  "chunk_ix": 1,
  "chunk_size_tokens": 900,
  "overlap_tokens": 120,
  "hash": "sha256:...",
  "created_at": "2025-09-24T00:00:00Z",
  "updated_at": "2025-09-24T00:00:00Z"
}
```

---

## Quick Checklist (printable)
- [ ] Author in Markdown + YAML front‑matter
- [ ] Semantic chunking (500–1,200 tok, 80–150 overlap)
- [ ] JSONL exchange file validated
- [ ] Parquet tables written (docs, chunks, embeddings)
- [ ] Vectors built + filters (lang/security/tags)
- [ ] Provenance (IDs, hashes, git commit) captured
- [ ] Leak scan for security tiers
- [ ] Reranker active (BM25+vector or cross‑encoder)

---

## FAQ
**Q: Is JSONL mandatory?**  
No, but it’s the most portable for agent pipelines and streaming. Keep Parquet for analytics.

**Q: Do I embed inside JSONL?**  
Prefer **separate embeddings** table or vector index. Keep JSONL text‑only for clarity unless you need self‑contained artifacts.

**Q: Best DB?**  
For a single workstation: **FAISS + SQLite/DuckDB**. For services: **Qdrant/Weaviate** + Postgres (or their built‑in filters).

**Q: Images/code snippets?**  
Store references in text; keep assets in `/assets` and add `asset_refs` metadata. Use multimodal embeddings only where needed.

---

## Next steps for your setup (Rod)
1. Create `/knowledge` tree as above.
2. Convert 5 representative docs → Markdown+YAML.
3. Run a chunker to produce `qa-sops.jsonl`.
4. Build FAISS index + SQLite sidecar.
5. Wire your retriever agent to respect `lang/security/tags` and cite `title_path`.

