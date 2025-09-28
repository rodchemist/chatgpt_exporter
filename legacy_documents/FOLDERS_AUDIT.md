# Repository Folder Audit

This report reviews each top-level folder for project structure, language, and readiness. Signals checked: presence of `README`, `src/`, `tests/`, `pyproject.toml`, `requirements.txt`, `package.json`, and common assets.

## Summary
- Folders scanned: 30
- READMEs present: 16; `src/`: 8; `tests/`: 4
- Tech mix: Python-heavy with some Electron/React apps. CI enforces Black, Flake8, PyTest for `etl_framework`.

## Per-Folder Findings
- 00_Machine_Learning: Python scripts only; no README/tests. Recommendation: add README and group modules under `src/` with tests.
- 00_general_use: Utility Python scripts; no README/tests. Recommendation: document purpose and add minimal tests.
- 01_Retrieve Data: Mixed subprojects with README; many .py and some notebooks. Recommendation: standardize subfolder READMEs and data locations.
- 03_Data_Analysis: Python analysis scripts; no README/tests. Recommendation: add README and tests for key functions.
- 03_Tempering_Unit: Has README; scripts only. Recommendation: modularize into `src/` and add tests.
- 03_data_collection_v6: README + `pyproject.toml`; data and main scripts present. Recommendation: add `tests/` and usage instructions.
- 04_MashMallow: README + `src/`; appears structured. Recommendation: add tests and clarify run commands.
- 04_Specs_Cookies_TL: Primarily notebooks/assets; no README. Recommendation: add README explaining notebooks and expected environment.
- 05_ML_TU: README + `src/` + `requirements.txt`; Python project. Recommendation: add tests and CI coverage.
- 06_ML_mondotherm: README + `src/` + `tests/` + `docs/`; Python + simple web. Recommendation: ensure tests run in CI and add requirements.
- 07_Waste_Mallow: README + `src/`; many notebooks and `data/`. Recommendation: separate raw data; add README for notebooks and add tests where possible.
- Example_Notebooks: Notebooks only. Recommendation: add README and move to `docs/` or a dedicated examples area.
- File_Scanner: Python scripts. Recommendation: add README, describe usage, and tests.
- File_Scanner_Integrated: Electron app with `src/` and `tests/` dirs; `package.json` present, no README. Recommendation: add README and Node instructions; consider enabling JS tests.
- File_Scanner_Lightweight: Well-structured Python+web with README, `src/`, `tests/`, `docs/`. Recommendation: integrate with CI.
- Instructions_GPT: Instruction docs. Recommendation: add README or link from root docs.
- Meging_Tempering_projects: Empty/placeholder. Recommendation: remove or document purpose.
- docs: Documentation hub. Recommendation: index what lives here.
- etl_framework: Python library with README and tests; covered by CI. Recommendation: keep as the reference for style/tests.
- ftp_txt_processing: Electron + React app (`package.json`, Docker) with README. Recommendation: JS/TS tests and linting; clarify Docker usage.
- hmi_visor_local: README only; unclear structure. Recommendation: add source layout or move to `docs/` if purely descriptive.
- last_rejected_local: README + `requirements.txt`; Python scripts only. Recommendation: add `src/` and tests.
- local_execution_by_os: README; helper scripts. Recommendation: document OS-specific behaviors.
- logs: Runtime logs; keep out of Git or add `.gitkeep` with README.
- rd_File_Scanner: `src/` present; no README/tests. Recommendation: add README and tests; clarify relation to other scanner projects.
- repo_template: README + docs; serves as template. Recommendation: mark as reference and keep updated.
- rs_code-watermark: README; minimal code. Recommendation: document usage and add tests if active.
- scripts: Utility scripts; no README/tests. Recommendation: add README and usage examples.
- security_scanning: README + `requirements.txt`; Python scripts. Recommendation: add tests and document scan targets.
- work_in_progress: Staging area of Python scripts. Recommendation: add README; move finished work into structured projects.

## Cross-Cutting Recommendations
- Adopt consistent prototype layout per `PROTOTYPING_GUIDELINES.md` for new folders: `README.md`, `src/`, and a runnable entry (`main.py` or `index.html`).
- Add minimal `tests/` for active Python projects and include them in CI beyond `etl_framework`.
- Avoid committing large binaries and logs; prefer `data/` in `.gitignore` with sampled data under `data/sample/`.
- For Electron/React apps, add `README`, `npm scripts`, and basic tests (Jest/Playwright) with linting.
