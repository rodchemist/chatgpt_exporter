# Language: Markdown
# Lines of Code: 11
# File: guidelines-repos-rodchemist/docs/adr/0001-repo-structure.md
# Version: 1.0.0
# Project: AI_RodChem_Crypto_Predictor
# Repository: AI_RodChem_Crypto_Predictor
# Author: Rod Sanchez
# Created: 2024-07-12 00:00
# Last Edited: 2025-07-12 04:58

# ADR 0001: Repository Structure

## Context
We need a portable, multi-agent-friendly structure that minimizes merge conflicts.

## Decision
Adopt modular, feature-oriented layout with per-language validators and CI gating via a single `validate_repo.sh` entry point.

## Consequences
- Easier parallel work and ownership boundaries.
- Slight duplication across modules is acceptable to preserve orthogonality.
