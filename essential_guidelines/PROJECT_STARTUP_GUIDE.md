# Essential Project Startup Guidelines

🚨 **MANDATORY FOR ALL NEW PROJECTS** 🚨

## Quick Start Checklist

For ANY new project, follow this exact sequence:

### Step 1: Initialize Git Repository
```bash
git init
git add .
git commit -m "Initial commit"
```

### Step 2: Create Standard Structure

**Web Applications:**
```
project_name/
├── README.md
└── src/
    ├── index.html
    ├── style.css
    └── main.js
```

**Python Applications:**
```
project_name/
├── README.md
└── src/
    └── main.py
```

**Other Applications:**
```
project_name/
├── README.md
└── src/
    └── [main_file]
```

### Step 3: Create README.md

Use this exact template:

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

### Step 4: Add File Headers

Every source file must start with:

```
Language: [language_version]
Lines of Code: [count]
File: [path_from_root]
Version: 1.0.0
Project: [project_name]
Repository: AI_[project_name]
Author: Rod Sanchez
Created: [YYYY-MM-DD HH:MM]
Last Edited: [YYYY-MM-DD HH:MM]
```

**Comment syntax:**
- Python: `# Language: Python 3.12`
- JavaScript: `// Language: JavaScript ES6`
- HTML: `<!-- Language: HTML5 -->`
- CSS: `/* Language: CSS3 */`

## Core Principles

1. **Speed First** - Working demo in minutes
2. **Self-Contained** - Minimal setup required
3. **Clear Structure** - Immediately understandable
4. **Working Demo** - Actually functions

## Final Checklist

Before project is complete:
- [ ] Git repository initialized
- [ ] Standard folder structure created
- [ ] README.md follows template
- [ ] All files have headers
- [ ] Code runs successfully
- [ ] Can be executed following README

## When These Guidelines Apply

✅ **Use for:**
- ANY new project request
- "Build me a..." requests
- "Create a..." requests
- "Develop a..." requests
- Initial prototypes and demos

❌ **Skip only when:**
- User explicitly says "skip prototyping guidelines"
- User requests "full production guidelines"