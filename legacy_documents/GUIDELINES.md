# Language: Markdown
# Lines of Code: 33
# File: guidelines-repos-rodchemist/GUIDELINES.md
# Version: 1.0.0
# Project: AI_RodChem_Crypto_Predictor
# Repository: AI_RodChem_Crypto_Predictor
# Author: Rod Sanchez
# Created: 2024-07-12 00:00
# Last Edited: 2025-07-12 04:58

# Universal Guidelines (Pragmatic & Multi-Agent Friendly)

## Philosophy
- **Single Source of Truth** for configs, constants, and docs; reference don’t duplicate.
- **Orthogonality**: modules self-contained; changes don’t ripple.
- **Tracer Bullets**: ship thin vertical slices to validate direction.
- **No Broken Windows**: fix red builds/tests before adding features.
- **Always Shippable**: `main` must be releasable at all times.

## Structure & Ownership
- Structure by feature/domain. Each module contains its own `src/`, `tests/`, `docs/`, `assets/`, `vendor/` as needed.
- Module ownership is explicit via `CODEOWNERS`.
- Public interfaces live in `interfaces/` (or language-native equivalents).

## Collaboration
- Branch-per-change; small PRs with isolated blast radius.
- Avoid hot spots: split frequently edited files into smaller parts.
- Document architectural decisions in `docs/adr/` (short, factual ADRs).

## Tooling
- Auto-detect stack(s) and run language-appropriate validators.
- Pre-commit for formatters + basic static checks.
- `./scripts/validate_repo.sh` is the single entry point for repo health.

## Policies as Data
- Put constraints in `/.repo-spec.yaml` and `/policies/*.yaml` rather than hardcoding.
- CI reads policies and fails with clear remediation steps.

## Acceptance Criteria
- `validate_repo.sh` passes.
- New contributors can run the project within 1 hour using `README.md` only.
- PRs merge with minimal conflicts; ownership respected.
- Docs, tests, and code stay in sync.