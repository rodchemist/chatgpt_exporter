# Language: Markdown
# Lines of Code: 71
# File: guidelines-repos-rodchemist/README.md
# Version: 1.0.0
# Project: AI_RodChem_Crypto_Predictor
# Repository: AI_RodChem_Crypto_Predictor
# Author: Rod Sanchez
# Created: 2024-07-12 00:00
# Last Edited: 2025-07-12 04:58

# Universal Repository Guidelines

A drop-in, stack-agnostic set of **Pragmatic Programmer**-aligned guidelines, validators, and automation
to make any repository **multi-agent friendly**, **merge-safe**, and **always shippable**.

## Key Ideas
- **Orthogonality** & **Single Source of Truth** (SSOT)
- **Tracer bullets** before big refactors
- **No broken windows**: keep `main` green
- **Small, modular PRs** with clear ownership (`CODEOWNERS`)
- **Language auto-detection** → pluggable validators
- **Policy as data** via `/.repo-spec.yaml` and `/policies/*.yaml`

## Quick Start
```bash
# 1) (optional) Install pre-commit hooks to auto-format/statically-lint
./scripts/install_hooks.sh

# 2) Validate repo health (auto-detects languages)
./scripts/validate_repo.sh

# 3) See reports
cat reports/manifest.json
```

## Layout
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

## Multi-Agent Collaboration
- Use `feature/*`, `fix/*`, `experiment/*` branches.
- Keep PRs ≤ 500 LOC when feasible.
- Respect `CODEOWNERS`; update `docs/adr/` for non-obvious decisions.

## CI
GitHub Actions runs `./scripts/validate_repo.sh` on PR and push to keep `main` shippable.


## Logo Integration
- Your logo was added at `assets/logo.png` with theme-aware styles in `assets/logo.css`.
- Preview in a browser: `docs/logo_preview.html` (supports light/dark, accent demo).
- Usage:
  ```html
  <link rel="stylesheet" href="/assets/logo.css">
  <img src="/assets/logo.png" class="themed-logo" alt="Logo">
  ```