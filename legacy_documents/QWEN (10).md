# Qwen Context Documentation - ARCHIVES_AND_BACKUPS Directory

## Overview
This directory contains archived repositories and important data backups. The main focus is on the `_repo_maturity_scanner` project, which is a Python-based CLI tool for evaluating repository maturity.

## Key Projects

### _repo_maturity_scanner
A cross-platform CLI tool that scores a repository against a 5-tier maturity model (L1-L5) and outputs JSON/Markdown reports.

#### Project Structure
```
_repo_maturity_scanner/
├── pyproject.toml              # Project configuration and dependencies
├── README.md                   # Project documentation and usage instructions
├── .github/
│   └── workflows/
│       └── maturity.yml       # GitHub Actions workflow for scanning repos
├── examples/
│   └── repo-profile.yml       # Example repository profile template
└── src/
    └── repo_maturity_scanner/
        ├── __init__.py         # Package initialization
        ├── cli.py              # Command-line interface implementation
        ├── criteria.py         # Maturity criteria definitions and scoring logic
        ├── scanner.py          # File system scanning and evidence collection
        └── scorer.py           # Main scoring algorithm and report generation
```

#### Features
- Scores repositories on a 0-100 scale with 5 maturity levels (L1-L5)
- Evaluates 5 key dimensions:
  1. Code Quality
  2. Documentation & Examples
  3. Tests & Coverage
  4. CI/CD & Releases
  5. Security & Compliance
- Zero external dependencies
- Outputs JSON or Markdown reports
- Provides actionable recommendations for improvement

#### Installation
```bash
# Install in editable mode
pip install -e .
```

#### Usage Examples
```bash
# Basic usage with JSON output
repo-maturity PATH/TO/REPO --json --pretty

# Generate markdown report
repo-maturity . --report md --out report.md

# Set minimum score threshold
repo-maturity C:\Repos\myproj --max-depth 5 --fail-under 60
```

#### Scoring Dimensions
1. **Code Quality** (20 points max)
   - Standard project structure (src/, pyproject.toml)
   - Linter configuration
   - Modularity indicators
   - Logging practices

2. **Documentation & Examples** (20 points max)
   - README presence and quality
   - Documentation site configuration
   - Changelog maintenance

3. **Tests & Coverage** (20 points max)
   - Test directory structure
   - Test configuration files
   - Coverage reporting
   - CI integration

4. **CI/CD & Releases** (20 points max)
   - GitHub Actions workflows
   - Release automation
   - Packaging configuration
   - Build matrix support

5. **Security & Compliance** (20 points max)
   - License files
   - Security policy
   - SAST/SCA tools
   - SBOM generation

## Other Archived Items
- `_repo_maturity_scanner.zip` - Archived version of the repo maturity scanner
- `extracted_important_data.zip` - Important data backups
- `Game_Tetris.zip` - Archived Tetris game project
- `mcp_ollama_langchain.zip` - Archived project related to MCP, Ollama, and Langchain

## Context Notes
- The repo maturity scanner is implemented in Python with minimal dependencies
- It uses heuristic-based analysis rather than executing tests
- The tool can be integrated into CI/CD pipelines via GitHub Actions
- Reports include scores, evidence, and actionable recommendations