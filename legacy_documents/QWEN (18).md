# Repository Context Documentation

This repository contains a collection of tools and utilities for terminal management, file indexing, and project organization. The main focus is on a multi-terminal launcher with advanced features including WSL support and file indexing capabilities.

## Repository Structure

```
_repo/
├── 0000_Guidelines/           # Project guidelines and validation tools
├── src/                       # Main source code directory
│   ├── main.py                # Main entry point
│   └── terminal_launcher_advanced.py  # Advanced terminal launcher
├── README.md                  # Project overview and usage instructions
├── QWEN.md                    # This file - Repository context documentation
├── open_terminals_simple.py   # Simple terminal launcher
├── file_index.json            # File index (generated)
├── file_index.json.gz         # Compressed file index (generated)
└── [other utility scripts]    # Additional tools for file management
```

## Key Components

### Terminal Launcher Tools

#### src/terminal_launcher_advanced.py
Advanced multi-terminal launcher with WSL support. Features include:
- Support for multiple terminal types (Windows Terminal, WSL, CMD, PowerShell)
- Tabbed interface support
- File indexing capabilities
- GUI-based configuration
- Cross-platform compatibility

#### open_terminals_simple.py
Simplified terminal launcher for basic terminal opening needs.

### File Indexing System
File indexing capabilities that scan folders and create JSON descriptions of contents:
- Supports compact paths, content previews, binary file exclusion, and SHA256 hashing
- Generates `file_index.json` or compressed `file_index.json.gz` files
- GUI options for configuring indexing profiles
- CLI support for automation

### Project Organization Tools

#### archive_to_md.py
Tool for converting archive files to markdown format for documentation purposes.

#### compare_files.py
Utility for comparing files and identifying differences between them.

#### find_duplicate_files.py
Script for identifying and locating duplicate files within a directory structure.

#### restore_organization.py
Tool for restoring file organization based on predefined rules or previous states.

#### restore_language_organization.py
Specialized tool for organizing files based on programming language or file type.

#### repo_ignore_and_sync.py
Utility for managing repository ignore patterns and synchronizing files.

### Validation and Quality Tools

#### fileHeaderValidator.py
Validates that source files contain proper headers according to project guidelines.

#### 0000_Guidelines/validate_prototype.py
Ensures projects follow the PROTOTYPING_GUIDELINES.md standards.

### Utility Scripts

#### requirements_parser.py
Parses and processes requirements files for Python projects.

## How to Use

1. Run the main entry point: `python src/main.py`
2. For terminal launching: Run `python src/terminal_launcher_advanced.py` for full features or `python open_terminals_simple.py` for basic functionality
3. For file indexing: Use the GUI in `src/terminal_launcher_advanced.py` and click "📁 Index Files"
4. For other utilities: Run any of the Python scripts directly with `python script_name.py`

## Features

- Advanced multi-terminal launcher with WSL support
- File indexing system with configurable options
- Project organization and file management utilities
- Cross-platform compatibility (Windows, Linux, WSL)
- Duplicate file detection
- File comparison tools
- Archive and restore functionality
- Validation tools for ensuring code quality