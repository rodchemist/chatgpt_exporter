# Repository Guidelines
read always file_index.json
This repository hosts multiple, self‑contained projects. Work inside one subproject at a time and avoid cross‑project dependencies at the repo root.

## Project Structure & Module Organization
- Python projects: source in `src/`, tests in `tests/`, optional utilities in `scripts/`.
- Web apps: app code in `src/`, static assets in `assets/` (for example, `Game_Tetris/assets`).
- Examples in this repo: `ai_independent_agent/src`, `AGiXT/agixt`, `AGiXT/tests`.
- Keep each subproject independent; do not share code at the repository root.

## Build, Test, and Development Commands
- Python env: `python -m venv .venv` then activate (`source .venv/bin/activate` or `./.venv/Scripts/Activate.ps1`).
- Install deps: `pip install -r requirements.txt` or editable: `pip install -e .`.
- Tests (Python): `pytest -q` or `python -m pytest` (run from the subproject root).
- Node/Web: install `npm ci` (fallback `npm install`); dev `npm run dev`; build `npm run build`; tests `npm test`.
- Containers (where provided, e.g., `AGiXT/`): `docker-compose up -d`.

## Coding Style & Naming Conventions
- Python: PEP 8, 4‑space indent; `snake_case` for modules/functions, `PascalCase` for classes.
- Format/lint when configured: `black .` and `ruff .` (run within the subproject).
- JS/TS: follow each project’s Prettier/ESLint config; prefer kebab‑case for folders.
- Keep changes minimal and consistent with local patterns.

## Testing Guidelines
- Framework: `pytest` for Python projects.
- Naming: `tests/` with `test_*.py` or `*_test.py`.
- Coverage: target ≥80% in changed areas; add regression tests for fixes.
- Run tests from the subproject root to ensure correct paths and configs.

## Commit & Pull Request Guidelines
- Use Conventional Commits (e.g., `feat(agent): add MCP smoke test`, `fix(tetris): resolve rotation bug`).
- PRs should include a clear description, linked issue (e.g., `Closes #123`), steps to test, and screenshots for UI changes.
- Scope PRs to a single subproject; update docs (`README` or this file) when behavior changes. Note any migrations or config updates.

## Security & Configuration Tips
- Never commit secrets. Use a local `.env`; provide `.env.example` when needed.
- Create per‑project virtual envs (e.g., `project/.venv`); avoid installing at the repo root.
- Large artifacts belong in releases or archives, not in source folders.

