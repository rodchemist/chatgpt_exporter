# Qwen Context Documentation

This document provides context about the directories and projects in this repository for Qwen Code, an AI coding assistant.

## Directory Structure

```
PERSONAL/
├── paulina_profile/
├── personal_budget_tools/
└── personal_projects/
```

## Directory Descriptions

### 1. paulina_profile/

This directory contains professional profile information for Paulina Matamala, including:
- Career transition reports
- Professional profile documentation
- Career assessment quizzes related to the charity sector
- Configuration files for AI assistants (CLAUDE.md, GEMINI.md, AGENTS.md)

The main profile document (`paulina_matamala_profile.md`) contains detailed information about Paulina's professional background, including her work experience at Omnia Packaging Inc, education from Universidad Santo Tomás in Chile, certifications in food safety and quality assurance, and her expertise in quality management systems.

### 2. personal_budget_tools/

This directory contains tools and scripts for personal budget management and financial data processing:
- Python scripts for parsing financial transaction data (`01_parsing_file.py`, `02_debit_parsing.py`)
- SQL query files for budget analysis (`02_query.sql`)
- Data files in CSV format (`balances.csv`, `transactions.csv`)
- Validation scripts (`validate_prototype.py`)
- Configuration and documentation files (CLAUDE.md, GEMINI.md, AGENTS.md, AUDIT.md, Full_Guidelines.md)

The Python scripts appear to be designed to:
- Parse and standardize financial transaction data from multiple CSV files
- Merge data from various sources into a unified format
- Store financial records in a MySQL database with a structured schema

### 3. personal_projects/

This directory contains general project guidelines and documentation:
- Universal project playbook and guidelines (`Full_Guidelines.md`)
- Configuration and documentation files (CLAUDE.md, GEMINI.md, AGENTS.md, AUDIT.md)
- Validation scripts (`validate_prototype.py`)

The `Full_Guidelines.md` file contains a comprehensive "Universal Project Playbook" that provides templates, guidelines, and best practices for structuring software projects. It covers topics like:
- Project phases (Phase 0, Foundational, Deployment)
- Repository structure guidelines
- Code quality and testing practices
- Security baselines
- CI/CD practices
- Documentation standards

## Common Files

Several directories contain similar configuration files:
- `CLAUDE.md`, `GEMINI.md`, `AGENTS.md` - Provider-specific configuration files for AI assistants
- `Full_Guidelines.md` - Comprehensive project guidelines
- `AUDIT.md` - Repository audit criteria and checklists
- `validate_prototype.py` - Scripts for validating project structure and compliance

These files suggest a standardized approach to project setup and AI assistant integration across different projects in this repository.