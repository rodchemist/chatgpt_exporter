# Configuration Files Repository

This repository contains configuration files for various development tools, projects, and environments.

## Repository Structure

```
.
├── .github/
│   └── workflows/
│       └── python.yml          # GitHub Actions CI/CD workflow for Python projects
├── .tmp.driveupload/           # Temporary directory with files for drive upload (numerous numeric files)
├── .vscode/
│   └── launch.json             # VS Code debugging configurations
├── 00_Repos_Rod.code-workspace # VS Code workspace configuration
├── .flake8                     # Flake8 linting configuration
├── .gitattributes              # Git attributes configuration
├── .gitignore                  # Git ignore patterns
├── pyproject.toml              # Python project configuration (Black and Flake8 settings)
```

## Configuration Details

### Development Environment

**VS Code Workspace** (`00_Repos_Rod.code-workspace`)
- Configured for WSL+Ubuntu remote development
- Points to `/mnt/c/00_Repos_Rod` directory

**VS Code Debug Configurations** (`.vscode/launch.json`)
- Python Debugger: Current File
- Chrome Debugger for localhost development

### Python Development

**Code Quality Tools**

1. **Black** (`.flake8` and `pyproject.toml`)
   - Line length: 88 characters (Black default)
   - Excludes: `/etl_framework/tests/` and `/build/` directories

2. **Flake8** (`.flake8` and `pyproject.toml`)
   - Max line length: 120 characters
   - Extended ignore rules: E203, W503, F401, F841, F541, F824, E501, E402, W291, E128

**GitHub Actions CI/CD** (`.github/workflows/python.yml`)
- Runs on Ubuntu with Python 3.12
- Installs dependencies: pandas, numpy, pytz, flake8, black, pytest, flask, psutil
- Performs code quality checks:
  - Black format validation
  - Flake8 linting
- Runs tests for multiple projects:
  - etl_framework
  - 06_ML_mondotherm
  - File_Scanner_Lightweight

### Git Configuration

**.gitignore**
- Ignores various build artifacts, cache directories, and temporary files
- Specific ignores for several project directories
- Python cache files and Jupyter artifacts

**.gitattributes**
- Auto line ending normalization for all text files

## Purpose

This repository serves as a centralized location for development environment configurations, code quality standards, and CI/CD workflows for Python projects. It includes settings for code formatting, linting, debugging, and automated testing across multiple related projects.