File: docs/repository_guidelines.md
Project: AI_Repos_Integration
Author: Rod Sanchez
Created: 2025-07-09 00:00
Last Edited: 2025-07-09 00:00
Description: Guidelines for consistent repositories under AI_Repos_Integration

# Repository Guidelines for AI_Repos_Integration

## Table of Contents
- [Overview](#overview)
- [Directory Structure](#directory-structure)
- [Docker and Local Testing](#docker-and-local-testing)
- [Logging Standards](#logging-standards)
- [Frontend Approach](#frontend-approach)
- [Testing and Code Quality](#testing-and-code-quality)
- [Customization Guidelines](#customization-guidelines)
- [WSL Environment Setup](#wsl-environment-setup)
- [Security Practices](#security-practices)
- [Git Configuration](#git-configuration)
- [Implementation Checklist](#implementation-checklist)

## Overview
Guidelines for repositories under `C:\ai_repos\AI_repos_integration`:
- Support Docker for production and WSL for local testing.
- Use structured logging with rotation.
- Prefer vanilla HTML/CSS/JS for lightweight frontends, escalating to React for complex needs.
- Follow Dare Foods Style Guide (`dare_implementation_guide.md`, `dare_stylesheet.css`).
- Use SQLite for caching in WSL.
- Ensure cybersecurity: no passwords in repos, secure libraries, prevent SQL injection.
- Use Git submodules for shared resources (e.g., `dare_style_files`).

## Directory Structure
Standardized structure:

```
<repository_name>/
├── root/                      # Orchestration scripts (e.g., run_all.sh)
├── src/                       # Source code
│   ├── backend/               # Backend services (e.g., server.py)
│   ├── etl/                   # ETL scripts
│   ├── frontend/              # Frontend code (e.g., React)
│   ├── utils/                 # Utilities (e.g., data_processing.py)
│   └── web/                   # Web assets
│       ├── index.html
│       ├── assets/
│       │   ├── css/           # e.g., main.css
│       │   └── js/            # e.g., main.js
│       └── components/        # e.g., header.html
├── config/                    # Config files (e.g., config.ini)
├── data/                      # Datasets, SQLite DBs
├── docs/                      # Docs (e.g., README.md)
├── scripts/                   # Automation (e.g., setup.sh)
├── tests/                     # Tests (e.g., test_utils.py)
├── logs/                      # Rotated logs
├── results/                   # Outputs (e.g., JSON)
├── legacy/                    # Deprecated files
├── uploads/                   # Temporary uploads
└── dare_style_files/          # Git submodule for style guide
```

### Key Files
- **root/run_all.sh**: App entry point.
- **root/docker-compose.yml**: Docker config.
- **config/.env.example**: Env variable template.
- **data/cache.sqlite**: SQLite for caching.
- **docs/README.md**: Setup instructions.
- **dare_style_files/**: Style guide submodule.

## Docker and Local Testing

### Docker (Production)
- Use multi-stage `Dockerfile` for minimal images.
- Base: `python:3.12-slim` (Python), `node:18` (frontend).
- Mount `data/` and `logs/` as volumes.
- Example `Dockerfile`:
  ```dockerfile
  # File: root/Dockerfile
  # Project: <repository_name>
  # Author: Rod Sanchez
  # Created: 2025-07-09 00:00
  # Last Edited: 2025-07-09 00:00
  # Description: Docker config

  FROM python:3.12-slim AS builder
  WORKDIR /app
  COPY requirements.txt .
  RUN pip install --no-cache-dir -r requirements.txt
  COPY . .

  FROM python:3.12-slim
  WORKDIR /app
  COPY --from=builder /app .
  CMD ["bash", "root/run_all.sh"]
  ```
- Example `docker-compose.yml`:
  ```yaml
  # File: root/docker-compose.yml
  # Project: <repository_name>
  # Author: Rod Sanchez
  # Created: 2025-07-09 00:00
  # Last Edited: 2025-07-09 00:00
  # Description: Docker Compose config

  version: '3.8'
  services:
    app:
      build: .
      volumes:
        - ./data:/app/data
        - ./logs:/app/logs
      environment:
        - DB_SERVER=${DB_SERVER_AI}
        - DB_PORT=1433
      depends_on:
        - db
    db:
      image: mcr.microsoft.com/mssql/server:2019-latest
      environment:
        - ACCEPT_EULA=Y
        - SA_PASSWORD=${MSSQL_SA_PASSWORD}
      volumes:
        - ./data:/var/opt/mssql
  ```

### Local Testing (WSL)
- Use `scripts/setup_local.sh` for setup.
- Install via `requirements.txt` or Conda `environment.yml`.
- Use SQLite (`data/cache.sqlite`) for caching.
- Example `setup_local.sh`:
  ```bash
  # File: scripts/setup_local.sh
  # Project: <repository_name>
  # Author: Rod Sanchez
  # Created: 2025-07-09 00:00
  # Last Edited: 2025-07-09 00:00
  # Description: WSL setup

  #!/bin/bash
  source ~/.bashrc
  conda activate env_<repository_name>
  pip install -r requirements.txt
  python src/main.py --local
  ```

## Logging Standards
- Store logs in `logs/` as `<module>_<YYYYMMDD_HHMMSS>.log`.
- Rotate logs: 10MB max, 5 files/module.
- Use Python’s `logging` with `RotatingFileHandler`.
- Example:
  ```python
  #!/usr/bin/env python3
  # -*- coding: utf-8 -*-
  """
  Project: <repository_name>
  File: src/utils/logging_config.py
  Version: 1.0
  Author: Rod Sanchez
  Created: 2025-07-09 00:00

  Description: Logging with rotation
  """
  import logging
  from logging.handlers import RotatingFileHandler
  import os
  from datetime import datetime

  def setup_logging(module_name):
      log_dir = "logs"
      os.makedirs(log_dir, exist_ok=True)
      log_file = f"{log_dir}/{module_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
      logger = logging.getLogger(module_name)
      logger.setLevel(logging.INFO)
      handler = RotatingFileHandler(log_file, maxBytes=10*1024*1024, backupCount=5)
      formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
      handler.setFormatter(formatter)
      logger.addHandler(handler)
      return logger
  ```

## Frontend Approach
- **Vanilla HTML/CSS/JS**: For lightweight interfaces, ensuring <100KB bundles.
- **React**: Use for complex state management or dynamic binding.
- **Dependencies**: Use CDN for JS libraries; vanilla CSS, escalate to Bootstrap if needed.
- **Performance**: Use WebP images, browser caching.

## Testing and Code Quality
- **Python**: Use `pytest` for tests; `flake8` for style.
- **Frontend**:
  - Vanilla JS: `Jest` or `Mocha`.
  - React: `Jest` with `React Testing Library`.
- **JS**: Use `ESLint` for style.
- Example `pytest`:
  ```python
  #!/usr/bin/env python3
  # -*- coding: utf-8 -*-
  """
  Project: <repository_name>
  File: tests/test_utils.py
  Version: 1.0
  Author: Rod Sanchez
  Created: 2025-07-09 00:00

  Description: Utility tests
  """
  import pytest
  from src.utils import some_utility_function

  def test_utility_function():
      assert some_utility_function() == expected_result
  ```

## Customization Guidelines
- Follow Dare Foods Style Guide.
- **Web**:
  - Use `--dare-red` (`#E31E24`) for primary elements.
  - Include `dare-logo` (`height: 60px`, `alt="Dare Foods"`).
  - Use `.dare-header`, `.btn-primary`, `.dare-card`.
- **Headers**:
  ```python
  #!/usr/bin/env python3
  # -*- coding: utf-8 -*-
  """
  Project: <repository_name>
  File: <relative_path>
  Version: 1.0
  Author: Rod Sanchez
  Created: 2025-07-09 00:00

  Description: <brief_description>
  """
  ```
- **CSS**: Import `dare_stylesheet.css`, use variables (e.g., `--dare-red`).

## WSL Environment Setup
- Source `~/.bashrc` for DB/CUDA settings.
- Use Conda, export envs to `config/envs/`.
- Use `data/cache.sqlite` for caching.
- Example SQLite:
  ```python
  #!/usr/bin/env python3
  # -*- coding: utf-8 -*-
  """
  Project: <repository_name>
  File: src/utils/db_cache.py
  Version: 1.0
  Author: Rod Sanchez
  Created: 2025-07-09 00:00

  Description: SQLite caching
  """
  import sqlite3
  import os

  def init_cache_db():
      db_path = "data/cache.sqlite"
      os.makedirs(os.path.dirname(db_path), exist_ok=True)
      conn = sqlite3.connect(db_path)
      cursor = conn.cursor()
      cursor.execute('''CREATE TABLE IF NOT EXISTS cache (
          key TEXT PRIMARY KEY,
          value BLOB,
          timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
      )''')
      conn.commit()
      return conn
  ```

## Security Practices
- Store sensitive data in `.env`, exclude via `.gitignore`.
- Use secure libraries (e.g., `requests`).
- Prevent SQL injection with parameterized queries.
- Example:
  ```python
  #!/usr/bin/env python3
  # -*- coding: utf-8 -*-
  """
  Project: <repository_name>
  File: src/backend/database.py
  Version: 1.0
  Author: Rod Sanchez
  Created: 2025-07-09 00:00

  Description: Database queries
  """
  import sqlite3

  def query_data(conn, param):
      query = "SELECT * FROM table WHERE id = ?"
      return conn.execute(query, (param,)).fetchall()
  ```
- Audit dependencies with `pip-audit`, `npm audit`.

## Git Configuration
- **.gitignore**:
  ```gitignore
  # File: .gitignore
  # Project: <repository_name>
  # Author: Rod Sanchez
  # Created: 2025-07-09 00:00
  # Last Edited: 2025-07-09 00:00
  # Description: Git ignore

  *.pyc
  __pycache__/
  .venv/
  node_modules/
  .env
  logs/
  data/cache.sqlite
  *.log
  *.zip
  *.7z
  *.bak
  *.tmp
  *.swp
  .DS_Store
  ```
- **Submodule**:
  ```bash
  git submodule add <style_repo_url> dare_style_files
  ```
- **Update Script**:
  ```bash
  # File: scripts/git-submodule-update-all.sh
  # Project: <repository_name>
  # Author: Rod Sanchez
  # Created: 2025-07-09 00:00
  # Last Edited: 2025-07-09 00:00
  # Description: Update submodules

  #!/bin/bash
  git submodule update --init --recursive
  ```

## Implementation Checklist
- [ ] Create repo with standard structure.
- [ ] Init Git with `.gitignore`, add `dare_style_files` submodule.
- [ ] Set up Docker with multi-stage builds.
- [ ] Create `setup_local.sh` for WSL.
- [ ] Implement logging with rotation.
- [ ] Use SQLite for caching.
- [ ] Apply Dare Style Guide.
- [ ] Exclude sensitive data.
- [ ] Use parameterized queries.
- [ ] Add tests with `pytest`, `Jest`.
- [ ] Enforce style with `flake8`, `ESLint`.
- [ ] Test in WSL and Docker.


is this includede?

File: docs/README.md
Project: AI_Repos_Integration
Author: Rod Sanchez
Created: 2025-07-09 11:53
Last Edited: 2025-07-09 11:53
Description: Repository README with setup instructions

# README
...