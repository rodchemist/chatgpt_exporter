# Qwen Context Documentation - SCRIPTS Repository

## Overview
This repository contains utility scripts and tools for managing software projects, particularly focused on prototype validation and project merging.

## Key Files

### merge_tempering_projects.py
A Python script that merges multiple tempering projects into a single folder structure. It:
- Copies files from projects under `Meging_Tempering_projects` 
- Places each project in a separate subfolder in `tempering_prediction_merged`
- Renames files to prevent naming collisions
- Handles missing projects gracefully

### validate_prototype.py
A Python script that validates projects against prototyping guidelines:
- Checks for required directory structure (README.md, src/)
- Validates README.md format and content
- Ensures source files have required headers
- Enforces prototyping standards across projects

### utility_scripts/AGENTS.md
Contains mandatory prototyping guidelines for AI agents:
- Required project structure templates
- README.md formatting requirements
- Source file header specifications
- Core principles for rapid prototyping

### utility_scripts/GEMINI.md
Appears to be a duplicate of prototyping guidelines combined with the validate_prototype.py script content.

### o00_Sandbox_AI
Contains a list of git branches, likely from a repository management system.

## Usage Patterns
1. **Prototype Validation**: Run `validate_prototype.py` to ensure projects follow guidelines
2. **Project Merging**: Use `merge_tempering_projects.py` to consolidate related projects
3. **Guideline Reference**: Consult AGENTS.md for prototyping standards

## Repository Purpose
This repository serves as a toolkit for maintaining consistent project structures and validating that new projects adhere to established prototyping guidelines. It's particularly focused on ensuring quick, standardized prototype development.