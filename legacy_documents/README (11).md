# AI Predicting Chocolate

This folder contains scripts and utilities used during early experiments on predicting chocolate production metrics. The files were originally scattered across various folders with duplicate versions. They have been consolidated here for easier reference.

## Structure

- `scripts/` – Python scripts used for data extraction, preprocessing and exploratory modeling.
- `config/` – Configuration files such as database connectors.
- `data/` – Placeholder for raw datasets.
- `output/` – Placeholder for generated results.

## Duplicated Scripts

Many scripts in this folder also exist in the `all_organized_scripts` directory. Most copies are identical. The main difference is in `db_config.py`:

- **ai_predicting_chocolate/config/db_config.py** – Uses SQLAlchemy to optionally return a `Session` object via `connect_MSSQL_sqlalchemy` and expects credentials in `D:\00_Working_area\01_dare_ai\db_credentials.json`.
- **all_organized_scripts/** variations – Either wrap the logic in a `DBConfig` class or omit the SQLAlchemy helper and use a different credentials path (`System_variables/00_DB_variables`).

The extraction scripts (`01_extract_data.py`, `02_complete_index.py`, etc.) are otherwise the same as their counterparts in `all_organized_scripts`.

