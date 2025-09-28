# Qwen Context Documentation

## Repository Overview

This repository serves as a comprehensive documentation hub for AI agent development, project structuring, and repository management guidelines. It contains standardized templates, validation scripts, and best practices for creating consistent, maintainable projects.

## Key Documentation Files

### Core Guidelines
- `Full_Guidelines.md` - Universal Project Playbook with comprehensive development guidelines from Phase 0 through Deployment
- `AGENTS.md` - Prototyping guidelines specifically for AI agents (MANDATORY for all agents)
- `CLAUDE.md` - Platform-specific guidelines for Claude/Anthropic
- `GEMINI.md` - Platform-specific guidelines for Gemini/Google
- `AUDIT.md` - Repository audit criteria and scoring rubric

### Project Management
- `PROJECTS_INDEX.md` - Navigation hub with quick links to notable subprojects
- `PROJECTS_MASTER_LIST.md` - Complete list of all projects in the main repository
- `FOLDERS_AUDIT.md` - Detailed audit of each top-level folder's structure and readiness
- `FOLDER_TODOS.md` - Actionable task list for bringing structure and consistency to folders

### Specialized Directories
- `claude_codex/` - Contains presentation slides and assets for Empiric Presentation Modular system

## Directory Structure

```
DOCUMENTATION/
├── AGENTS.md                 # Prototyping guidelines for AI agents
├── CLAUDE.md                 # Platform-specific guidelines for Claude
├── GEMINI.md                 # Platform-specific guidelines for Gemini
├── Full_Guidelines.md        # Universal Project Playbook
├── AUDIT.md                  # Repository audit criteria
├── PROJECTS_INDEX.md         # Navigation hub for subprojects
├── PROJECTS_MASTER_LIST.md   # Complete list of all projects
├── FOLDERS_AUDIT.md          # Detailed folder audit report
├── FOLDER_TODOS.md           # Actionable task list for folders
├── claude_codex/             # Presentation slides system
│   ├── README.md             # Empiric Presentation Modular documentation
│   ├── index.html            # Main presentation entry point
│   ├── assets/               # CSS, JS, images, and configuration
│   ├── slides/               # Individual slide content
│   └── validate_prototype.py # Prototype validation script
└── QWEN_CONTEXT.md           # This file
```

## AI Agent Development Guidelines

### Prototyping Guidelines (Mandatory for All Agents)

All AI agents must follow the prototyping guidelines defined in `AGENTS.md`, which includes:

1. **Required Project Structure**:
   ```
   project_name/
   ├── README.md
   └── src/
       └── [main_file_with_appropriate_extension]
   ```

2. **Mandatory README.md Template**:
   ```markdown
   # [Project Name]
   
   [One sentence describing what this project does]
   
   ## How to Run
   
   1. [First step]
   2. [Second step]
   3. [Third step]
   
   ## Features
   
   - [Key feature 1]
   - [Key feature 2]
   - [Key feature 3]
   ```

3. **Required File Headers**:
   Every source file must start with:
   ```
   Language: [language_version]
   Lines of Code: [count_non_blank_non_header_lines]
   File: [relative_path_from_project_root]
   Version: 1.0.0
   Project: [project_name]
   Repository: AI_[project_name]
   Author: Rod Sanchez
   Created: [YYYY-MM-DD HH:MM]
   Last Edited: [YYYY-MM-DD HH:MM]
   ```

### Core Principles

1. **Speed First** - Get to working demo in minutes, not hours
2. **Self-Contained** - Must run with minimal setup
3. **Clear Structure** - Anyone should understand the layout immediately
4. **Working Demo** - Must actually function, not just code snippets

## Repository Management

### Audit Process

The repository follows a structured audit process defined in `AUDIT.md` with 12 categories covering:
1. Identity & Governance (5%)
2. Structure & Hygiene (10%)
3. Build & Reproducibility (10%)
4. Code Quality & Style (10%)
5. Testing & Quality Gates (12%)
6. Security & Secrets (15%)
7. Dependencies & Supply Chain (8%)
8. Documentation (8%)
9. CI/CD & Release Management (10%)
10. Observability, Config & Runtime (5%)
11. Data & File Validation Readiness (4%)
12. Maintainability & Project Health (3%)

### Folder Standardization

Each folder in the repository should follow the guidelines to achieve:
- Clear README with purpose and usage instructions
- Proper source code organization under `src/`
- Tests under `tests/` where applicable
- Configuration files and documentation

## Validation Tools

### Prototype Validator

The repository includes a prototype validation script (`claude_codex/validate_prototype.py`) that ensures projects comply with prototyping guidelines by checking:
- Project structure (README.md, src/ directory)
- README.md template compliance
- Required file headers in source files

## Usage Instructions

### For AI Agents

1. Always start with the prototyping guidelines in `AGENTS.md`
2. Follow the mandatory structure and templates
3. Include all required file headers
4. Validate your prototype using the validation script
5. Upgrade to full guidelines when needed for production-ready code

### For Repository Management

1. Refer to `FOLDERS_AUDIT.md` for current folder status
2. Use `FOLDER_TODOS.md` to track improvement tasks
3. Follow the audit criteria in `AUDIT.md` for quality assurance
4. Consult `Full_Guidelines.md` for comprehensive development practices

## Platform-Specific Considerations

### Claude/Anthropic
- Refer to `CLAUDE.md` for platform-specific guidelines
- Follow the same prototyping guidelines with Claude-specific considerations

### Gemini/Google
- Refer to `GEMINI.md` for platform-specific guidelines
- Follow the same prototyping guidelines with Gemini-specific considerations

## Best Practices

1. **Consistency** - Apply the same structure and guidelines across all projects
2. **Documentation** - Maintain clear, up-to-date documentation for all components
3. **Validation** - Use the provided validation tools to ensure compliance
4. **Progressive Enhancement** - Start with prototyping guidelines and upgrade to full guidelines when needed
5. **Audit Readiness** - Follow audit criteria to maintain repository quality

This documentation serves as the reference for all AI agent development and repository management within this organization.