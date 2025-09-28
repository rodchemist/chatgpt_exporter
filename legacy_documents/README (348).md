## Data Processing Isolated
The folder [data_processing_isolated/03_Data_Analysis](data_processing_isolated/03_Data_Analysis) now contains organized analysis, database, visualization, and tests with a README summarizing script differences.
=======
# Sandbox AI Repository

=======

This repository contains a variety of experimental scripts. The folder `ai_predicting_chocolate` holds early work on predicting chocolate production metrics.

File: docs/repository_guidelines.md
Project: AI_Repos_Integration
Author: Rod Sanchez
Created: 2025-07-09 00:00
Last Edited: 2025-07-09 00:00
Description: Guidelines for consistent repositories under AI_Repos_Integration


This repository contains a collection of experimental projects used for machine learning, data processing, and automation prototypes. Each folder is a standalone project maintained independently.

## Notable directories

- **api_server** – Sample FastAPI server.
- **etl_framework** – Reusable ETL utilities.
- **master_etl_final** – Consolidated ETL pipeline.
- **scripts/** – Automation scripts. See `scripts/` for details.

## Qwen Context Documentation

For AI agent development and repository management guidelines, see [QWEN_CONTEXT.md](QWEN_CONTEXT.md) which provides comprehensive documentation on:
- Prototyping guidelines for AI agents
- Repository audit criteria
- Folder standardization processes
- Validation tools and best practices

For comprehensive repository guidelines and the original long-form documentation, see [docs/repository_guidelines.md](docs/repository_guidelines.md).

## Auditing duplicate files

Run `scripts/find_duplicate_files.py` to identify files sharing the same name across the repository and preview their differences:

```bash
python scripts/find_duplicate_files.py --ext py
```

Use `--ext` to filter by extension.
