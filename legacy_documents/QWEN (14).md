# Qwen Context Documentation - Cognex Vision Tools

## Project Overview
This directory contains a collection of Python scripts for interacting with Cognex vision systems, primarily used in industrial settings. The tools are designed for reading data from Cognex cameras and merging production data. Each script originated as an isolated experiment and has been preserved for reference.

## Key Components

### Data Processing Scripts
1. **01_Cognex_stats.py** - Interactive script that:
   - Loads CSV data exported from vision systems
   - Groups data by timestamp and lane
   - Calculates derived metrics (volume in grams, weight, cylinder volume)
   - Outputs results to a new CSV file

2. **02_OPC_UA_Cognex.py** - Minimal example that:
   - Uses `CognexNativePy` library
   - Logs into In-Sight cameras
   - Captures images and reads/writes cell values

3. **03_Cognex_OPC.py** - OPC UA integration:
   - Uses `opcua` client library
   - Connects to Cognex cameras via OPC UA
   - Browses available nodes
   - Handles common connection errors

4. **04_CVognex.py** - Camera triggering:
   - Demonstrates sending trigger commands
   - Uses `CognexNativePy` interface

5. **Mallow_Data_processing.py** - Large ETL script that:
   - Queries multiple OCS_AI database tables
   - Merges work order data
   - Pivots results
   - Writes back to other tables
   - Logs progress
   - Processes data in chunks using process pools

## Important Notes
- All Python files in `src` have identical counterparts in `all_organized_scripts/DATA_PROCESSING`
- No functional differences exist between the copies in both locations
- The versions here are kept for reference and can be used interchangeably