# CODE_REVIEW_SPECIALIST Agent

A specialized code review agent combining the expertise of Rod-Corp's ECHO (Quality Assurance) and ALEX_ENGINEERING_DIRECTOR (Engineering Leadership) agents.

## Overview

CODE_REVIEW_SPECIALIST provides comprehensive code review capabilities focusing on:

- **Security Analysis**: OWASP Top 10, vulnerability detection, secure coding practices
- **Architectural Assessment**: Design patterns, scalability, integration best practices
- **Quality Assurance**: Code complexity, maintainability, testing coverage
- **Performance Analysis**: Bottleneck identification, optimization opportunities
- **Rod-Corp Integration**: Full ecosystem compatibility and standards compliance

## Quick Start

1. **Initialize Agent**:
   ```bash
   ./init.sh
   ```

2. **Start Agent**:
   ```bash
   python3 start_agent.py
   ```

3. **Verify Registration**:
   ```bash
   python3 register_agent.py
   ```

## Usage

### Custom Instructions
The agent includes comprehensive custom instructions in `templates/custom_instructions.md` that define:
- Security-first review methodology
- Architectural assessment criteria
- Quality metrics and thresholds
- Rod-Corp integration standards

### Review Templates
- `templates/review_checklist.yaml`: Comprehensive review checklist
- `templates/review_report_template.md`: Standardized report format

### Configuration
- `config.py`: Agent configuration and settings
- `config/config.json`: JSON configuration for service integration
- `.env`: Environment variables and secrets

## Integration

### Rod-Corp Ecosystem
- Database: MSSQL integration for agent registry
- Services: AI Interaction Server compatibility
- Coordination: 48-agent ecosystem integration
- Standards: Rod-Corp naming and quality conventions

### Supported Languages
Python, JavaScript, TypeScript, Java, Go, Rust, SQL, Docker, YAML, JSON

## Agent Lineage

**Based on Rod-Corp Elite Agents**:
- **ECHO**: Quality assurance, backup systems, validation, multiple validation methods
- **ALEX_ENGINEERING_DIRECTOR**: Engineering leadership, technical architecture, system integration

## Directory Structure

```
code-review-specialist/
├── config.py              # Agent configuration
├── config/
│   └── config.json        # JSON configuration
├── templates/
│   ├── custom_instructions.md
│   ├── review_checklist.yaml
│   └── review_report_template.md
├── workspace/
│   ├── reviews/           # Review outputs
│   ├── reports/          # Generated reports
│   └── temp/             # Temporary files
├── logs/                  # Agent logs
├── init.sh               # Initialization script
├── start_agent.py        # Startup script
├── register_agent.py     # Registration with Rod-Corp
└── README.md             # This file
```

## Contact

For questions or integration support, engage through the Rod-Corp agent coordination system.
