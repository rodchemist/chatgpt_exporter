# Qwen Context Documentation

This repository contains comprehensive guidelines and tools for developing AI/LLM-powered applications following best practices for prototyping, development, and deployment.

## Repository Structure

```
LLM_GUIDELINES/
├── agents_guidelines/
│   ├── AGENTS.md                 # Agent-specific development guidelines
│   ├── AUDIT.md                  # Audit and compliance guidelines
│   ├── CLAUDE.md                 # Anthropic Claude-specific guidelines
│   ├── Full_Guidelines.md        # Complete universal project playbook
│   ├── GEMINI.md                 # Google Gemini-specific guidelines
│   └── validate_prototype.py     # Prototype validation script
├── instructions_gpt/
│   ├── AI_Rod.md                 # Instructions and database correspondences
│   └── execute_query.py          # Database query execution script
└── llm_guidelines/
    ├── AGENTS.md                 # Agent-specific development guidelines
    ├── AUDIT.md                  # Audit and compliance guidelines
    ├── CLAUDE.md                 # Anthropic Claude-specific guidelines
    ├── Full_Guidelines.md        # Complete universal project playbook
    ├── GEMINI.md                 # Google Gemini-specific guidelines
    ├── kali.bat                  # Kali Linux batch script
    ├── validate_prototype.py     # Prototype validation script
    └── 00_LLM/
        ├── features_pc.py        # System specifications collector
        └── ollama.py             # Port usage detection utility
```

## Key Components

### 1. Universal Project Playbook (Full_Guidelines.md)
Located in both `agents_guidelines/` and `llm_guidelines/`, this comprehensive document provides:
- A phased approach to project development (Phase 0 → Foundational → Deployment)
- Universal guidelines for pragmatic, multi-agent friendly development
- Repository blueprint and structure recommendations
- Foundational stage requirements (Stage 1)
- Deployment stage guidelines (Stage 2+)
- Templates and snippets for common development tasks
- Platform-specific guides for Claude, Gemini, and multi-agent orchestration

### 2. Prototyping Guidelines (AGENTS.md)
Mandatory guidelines for all new projects, prototypes, and initial implementations:
- Required project structure for web, Python, and other applications
- Mandatory README.md template
- Required file headers with metadata
- Core principles: Speed First, Self-Contained, Clear Structure, Working Demo
- Quality gates for prototype validation

### 3. Prototype Validation Scripts
Python scripts in both directories that validate projects against prototyping guidelines:
- Structure validation (README.md, src/ directory)
- README template compliance
- File header requirements checking

### 4. Platform-Specific Guidelines
- **CLAUDE.md**: Guidelines for Anthropic Claude development
- **GEMINI.md**: Guidelines for Google Gemini development
- **AGENTS.md**: Guidelines for multi-agent orchestration

### 5. Audit and Compliance
- **AUDIT.md**: Guidelines for audit trails and compliance requirements

### 6. Database Tools (instructions_gpt/)
- **AI_Rod.md**: Database correspondence mappings and development guidelines
- **execute_query.py**: Script for executing database queries with connection management

### 7. System Tools (llm_guidelines/00_LLM/)
- **features_pc.py**: Collects and saves system specifications (CPU, memory, GPU, disk, OS)
- **ollama.py**: Detects processes using specific ports

## Development Workflow

### Phase 0 (Idea & First Tests)
- Validate ideas in 60-120 minutes
- Create minimal working demos
- Document assumptions and findings

### Foundational Stage (Stage 1)
- Implement core functionality end-to-end
- Add proper configuration management
- Implement structured logging with run IDs
- Set up validation and QA processes
- Establish security baseline

### Deployment Stage (Stage 2+)
- Infrastructure setup and patterns
- Security hardening
- Observability and monitoring
- Performance optimization and cost management

## Key Principles

1. **Bias to Working Software**: Ship minimal, testable slices first
2. **Platform-Aware Outputs**: Tune for specific model/providers
3. **Auditability**: Everything important gets a run_id and structured logs
4. **Modularity**: Separate concerns (UI/API/Jobs/Agents)
5. **Fail Safely**: Implement timeouts, retries, and kill-switches

## Best Practices

- Always start with prototyping guidelines for new projects
- Maintain orthogonality and single source of truth
- Use tracer bullets for quick validation
- Keep main branch always shippable
- Implement small, modular pull requests
- Use policy as data for configuration management

This documentation provides context for Qwen to understand the repository structure and development guidelines when assisting with tasks in this codebase.