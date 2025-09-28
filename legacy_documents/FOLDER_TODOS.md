# Folder TODOs (PR-Ready Checklist)

This checklist captures actionable tasks per folder to bring structure and consistency. Use sections as PR descriptions or split by area.

## 00_Machine_Learning
- [ ] Add README with purpose and usage
- [ ] Move reusable code into `src/` and add `tests/`

## 00_general_use
- [ ] Add README summarizing utilities
- [ ] Add minimal tests for public utilities

## 01_Retrieve Data
- [ ] Ensure each subfolder has a README
- [ ] Standardize data locations; avoid committing large binaries

## 03_Data_Analysis
- [ ] Add README and usage examples
- [ ] Add tests for core analysis utilities

## 03_Tempering_Unit
- [ ] Add `src/` structure (modularize scripts)
- [ ] Add tests for calculations and plotting utilities

## 03_data_collection_v6
- [ ] Add `tests/` and quick-start instructions
- [ ] Document data directories and sample data policy

## 04_MashMallow
- [ ] Add tests and run instructions

## 04_Specs_Cookies_TL
- [ ] Add README explaining notebooks and environment
- [ ] Exclude large binaries or move to external storage

## 05_ML_TU
- [ ] Add tests and wire into CI

## 06_ML_mondotherm
- [ ] Verify tests run in CI and add requirements if needed

## 07_Waste_Mallow
- [ ] Separate raw data; add README for notebooks
- [ ] Add tests where feasible

## Example_Notebooks
- [ ] Add README and consider moving under `docs/`

## File_Scanner
- [ ] Add README with usage examples
- [ ] Add tests for core functions

## File_Scanner_Integrated
- [ ] Add README with Electron dev/build instructions
- [ ] Add JS tests (Jest/Playwright) and linting

## File_Scanner_Lightweight
- [ ] Ensure CI runs tests; consider fixing `requirements.txt` formatting

## Instructions_GPT
- [ ] Add index/README or link from root docs

## Meging_Tempering_projects
- [ ] Clarify purpose; remove if obsolete

## docs
- [ ] Add index of available documents

## etl_framework
- [ ] Keep as reference style/tests; expand examples if needed

## ftp_txt_processing
- [ ] Add JS tests and linting; clarify Docker workflows

## hmi_visor_local
- [ ] Add structure or move to docs if informational

## last_rejected_local
- [ ] Add `src/` and tests; document usage

## local_execution_by_os
- [ ] Document OS differences and safety notes

## logs
- [ ] Keep out of Git or add `.gitkeep` with README

## rd_File_Scanner
- [ ] Add README/tests; clarify relationship to other scanners

## repo_template
- [ ] Keep updated and marked as reference

## rs_code-watermark
- [ ] Document usage; add tests if active

## scripts
- [ ] Add README and examples for each script

## security_scanning
- [ ] Add tests; document scan targets and configs

## work_in_progress
- [ ] Add README; promote finished work into structured projects
