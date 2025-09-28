# Agent Prototyping Guidelines

## Overview
These are the mandatory prototyping guidelines for all AI agents working with this repository. Follow these guidelines for any new project, prototype, or initial implementation unless explicitly told otherwise.

## When to Apply
- ✅ ANY new project request
- ✅ "Build me a..." requests
- ✅ "Create a..." requests  
- ✅ "Develop a..." requests
- ✅ Initial prototypes and demos
- ❌ Only when user says "use full Guidelines.md instead"

## Required Project Structure

### For Web Applications:
```
project_name/
├── README.md
└── src/
    ├── index.html
    ├── style.css
    └── main.js
```

### For Python Applications:
```
project_name/
├── README.md
└── src/
    └── main.py
```

### For Other Applications:
```
project_name/
├── README.md
└── src/
    └── [main_file_with_appropriate_extension]
```

## Mandatory README.md Template

Every project MUST have a README.md with exactly this structure:

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

## Required File Headers

Every source file must start with this header:

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

**Comment syntax by language:**
- Python: `# Language: Python 3.12`
- JavaScript: `// Language: JavaScript ES6`
- HTML: `<!-- Language: HTML5 -->`
- CSS: `/* Language: CSS3 */`

## Core Principles

1. **Speed First** - Get to working demo in minutes, not hours
2. **Self-Contained** - Must run with minimal setup
3. **Clear Structure** - Anyone should understand the layout immediately
4. **Working Demo** - Must actually function, not just code snippets

## Quality Gates

Before considering the prototype "done":
- [ ] All files follow the structure above
- [ ] README.md follows the template
- [ ] Code actually runs and produces expected output
- [ ] File headers are present and accurate
- [ ] Project can be run by following README instructions

## When to Upgrade to Full Guidelines

Move to the comprehensive Guidelines.md when:
- User explicitly requests production-ready code
- Project needs deployment/scaling
- Multiple team members will work on it
- Security/compliance requirements emerge

## Agent Compliance

**As an agent, you MUST:**
- Apply this structure to EVERY new project automatically
- Never skip these guidelines unless explicitly told
- Ask for clarification if unsure, but default to applying them
- Include ALL required elements (structure, README, headers)

**Violation of these guidelines is considered an error that must be corrected immediately.**