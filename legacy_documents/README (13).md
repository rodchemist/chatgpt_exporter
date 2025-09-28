# Guidelines_Full

> A fullstack project following Universal AI Guidelines and PROTOTYPING_GUIDELINES.md standards.

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](CHANGELOG.md)
[![Guidelines](https://img.shields.io/badge/guidelines-universal-green.svg)](docs/UNIVERSAL_GUIDELINES.md)
[![Security](https://img.shields.io/badge/security-first-red.svg)](docs/SECURITY.md)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Development](#development)
- [AI Agent Prompts](#ai-agent-prompts)
- [Security](#security)
- [Contributing](#contributing)
- [License](#license)

## Overview

Guidelines_Full is a fullstack application built with security-first principles and designed for multi-agent AI collaboration.

**Repository:** AI_GUIDELINES_FULL  
**Created:** 2025-08-22 13:03  
**Author:** Rod Sanchez  

## Features

- ✅ Structured following PROTOTYPING_GUIDELINES.md
- 🔒 Security-first approach (no secrets in code)
- 📊 Comprehensive logging with run_id tracking
- 🤖 Multi-agent collaboration ready
- 🧪 Comprehensive testing framework
- 📝 Well-documented with AI prompts
- 🚀 Production-ready configuration

## Quick Start

### Prerequisites

- Python 3.12+
- Node.js 18+
- npm or yarn

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd Guidelines_Full

# Run setup script
./scripts/setup.sh

# Copy environment template
cp config/.env.example config/.env
# Edit config/.env with your actual values

# Start the application
./scripts/start.sh
```

### Development Commands

```bash
# Run tests
./scripts/test.sh

# Security check
./scripts/security_check.sh

# Validate structure
python scripts/validate_structure.py

# Full-stack specific
npm run dev:all  # Run frontend and backend
```

## Project Structure

```
Guidelines_Full/
├── README.md                 # This file
├── .gitignore               # Comprehensive ignore rules
├── config/                  # Configuration files (no secrets)
│   ├── app.yaml            # Application configuration
│   └── .env.example        # Environment template
├── src/                     # Source code
│   └── utils/              # Utility modules
├── tests/                   # Test files
│   ├── unit/              # Unit tests
│   ├── integration/       # Integration tests
│   └── fixtures/          # Test fixtures
├── scripts/                 # Development scripts
│   ├── setup.sh           # Setup script
│   ├── test.sh            # Test runner
│   ├── start.sh           # Start application
│   └── security_check.sh  # Security validation
├── docs/                    # Documentation
│   ├── UNIVERSAL_GUIDELINES.md
│   ├── CLAUDE_GUIDELINES.md
│   ├── GPT_GUIDELINES.md
│   └── SECURITY.md
├── data/                    # Data files (gitignored)
│   ├── raw/               # Raw data
│   ├── processed/         # Processed data
│   ├── sample/            # Sample data for testing
│   └── cache/             # SQLite cache databases
└── logs/                    # Application logs (gitignored)
├── web/                     # Web assets
│   ├── html/               # HTML files
│   ├── css/                # Stylesheets
│   ├── js/                 # JavaScript
│   └── assets/             # Images, fonts, etc.
```

## Development

### File Headers

All source files must include the standard header:

```python
# Language: Python 3.12
# Lines of Code: [count]
# File: [path]
# Version: [version]
# Project: Guidelines_Full
# Repository: AI_GUIDELINES_FULL
# Author: Rod Sanchez
# Created: [date]
# Last Edited: [date]
```

### Logging Standard

Use structured JSON logging with run_id:

```python
{
  "ts": "2025-01-20T14:30:00Z",
  "level": "INFO",
  "run_id": "uuid-here",
  "component": "module",
  "event": "action.completed",
  "extras": {}
}
```

## AI Agent Prompts

### 🔧 Development Tasks

#### Initial Setup Review
```
Review this project structure against PROTOTYPING_GUIDELINES.md:
1. Check all file headers are present and correct
2. Validate security compliance (no hardcoded secrets)
3. Verify logging implementation with run_id
4. Ensure comprehensive .gitignore
5. Suggest any missing components
```

#### Feature Development
```
Create [feature_name] following Universal Guidelines:
- Include proper file headers with all metadata
- Implement structured logging with unique run_id
- Use environment variables for all configuration
- Add comprehensive error handling
- Include type hints and documentation
- Write corresponding unit tests
```

#### Code Generation with Security
```
Generate secure implementation for [component]:
Requirements:
- No hardcoded credentials or secrets
- Input validation and sanitization
- Proper error handling without exposing internals
- Rate limiting and abuse prevention
- Audit logging for security events
- Follow OWASP best practices
```

### 🧪 Testing Tasks

#### Comprehensive Test Suite
```
Create test suite for [module/feature]:
- Unit tests with 80%+ coverage
- Integration tests for API endpoints
- Security tests (injection, auth bypass)
- Performance benchmarks
- Mock all external dependencies
- Use fixtures from tests/fixtures/
```

#### Security Testing
```
Perform security testing on this codebase:
- SQL injection vulnerabilities
- XSS attack vectors
- Authentication bypass attempts
- Authorization flaws
- Session management issues
- Input validation gaps
- Information disclosure risks
```

### 🚀 Deployment Tasks

#### Pre-deployment Audit
```
Audit for production readiness:
1. Scan for hardcoded secrets or API keys
2. Verify all debug flags are disabled
3. Check error messages don't expose internals
4. Validate environment configuration
5. Review logs for sensitive data
6. Ensure .gitignore completeness
7. Check for development-only code
8. Verify HTTPS enforcement
9. Review CORS configuration
10. Generate deployment checklist
```

#### Metadata Stripping
```
Prepare for hosting upload:
1. Strip all file headers and metadata
2. Remove development configurations
3. Minimize and obfuscate JavaScript
4. Optimize images and assets
5. Remove source maps
6. Clear all comments from production code
7. Validate no sensitive data remains
8. Create production build
```

### 🔍 Analysis & Review

#### Architecture Review
```
Review project architecture:
- Analyze component dependencies
- Identify circular dependencies
- Check separation of concerns
- Validate design patterns usage
- Suggest scalability improvements
- Review error handling flow
- Assess monitoring coverage
- Recommend performance optimizations
```

#### Code Quality Audit
```
Perform code quality audit:
- Check PROTOTYPING_GUIDELINES.md compliance
- Analyze code complexity metrics
- Review documentation completeness
- Validate test coverage
- Check for code duplication
- Review naming conventions
- Assess maintainability index
- Identify technical debt
```

### 🛡️ Security Tasks

#### Vulnerability Assessment
```
Conduct security vulnerability assessment:
- Check for OWASP Top 10 vulnerabilities
- Scan dependencies for known CVEs
- Review authentication implementation
- Validate authorization checks
- Assess encryption usage
- Check for timing attacks
- Review random number generation
- Validate certificate pinning
```

#### Compliance Verification
```
Verify security compliance:
- No secrets in version control
- Environment variables properly used
- Secure logging (no PII/secrets)
- Data encryption at rest and transit
- Access control implementation
- Audit trail completeness
- GDPR/privacy compliance
- Security headers configuration
```

### 🤖 Multi-Agent Coordination

#### Cross-Platform Sync
```
Coordinate with other AI agents:
- Ensure Universal Guidelines compliance
- Sync on file naming conventions
- Coordinate on API contracts
- Share security validation results
- Document all decisions with run_id
- Maintain consistent error codes
- Align on logging formats
```

#### Knowledge Transfer
```
Transfer project knowledge to [Claude/GPT/Gemini]:
- Project architecture overview
- Key design decisions
- Security considerations
- Performance bottlenecks
- Technical debt items
- Testing strategy
- Deployment process
Include all context from docs/
```

## Security

### 🔐 Security Checklist

Before any commit or deployment:

- [ ] No hardcoded secrets, passwords, or API keys
- [ ] All sensitive config in environment variables
- [ ] .env file is in .gitignore
- [ ] No sensitive data in logs
- [ ] Input validation on all user inputs
- [ ] SQL injection prevention
- [ ] XSS protection enabled
- [ ] CSRF tokens implemented
- [ ] Rate limiting configured
- [ ] Security headers set
- [ ] HTTPS enforced
- [ ] Dependencies scanned for vulnerabilities
- [ ] Error messages don't expose internals
- [ ] Audit logging enabled
- [ ] Access control properly implemented

### 🚨 Security Incident Response

If you discover a security issue:

1. Do NOT commit the vulnerability
2. Document the issue privately
3. Fix the vulnerability
4. Run security tests
5. Update security documentation
6. Notify team members

## Contributing

1. Follow PROTOTYPING_GUIDELINES.md
2. Include proper file headers
3. Write tests for new features
4. Run security checks before commits
5. Update documentation
6. Use structured logging

## Version History

- v1.0.0 - Initial project setup with Universal Guidelines

## License

[Choose appropriate license]

---

*Generated by Universal Project Setup Script v2.0.0*  
*Following PROTOTYPING_GUIDELINES.md and Universal AI Guidelines*  
*Repository: AI_GUIDELINES_FULL*  
*Author: Rod Sanchez*  
*Created: 2025-08-22 13:03*
