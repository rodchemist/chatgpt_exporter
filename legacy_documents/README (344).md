# MashMallow Tools

This folder contains a small collection of scripts used for reading data from Cognex cameras and for merging production data. Each script started life as an isolated experiment and has been preserved in the `src` directory.

The same scripts also appear under `all_organized_scripts/DATA_PROCESSING`. Checksums confirm both locations contain identical code. The versions here are kept for reference and can be used interchangeably.

## Directory layout

```
04_MashMallow/
└── src/
    ├── 01_Cognex_stats.py
    ├── 02_OPC_UA_Cognex.py
    ├── 03_Cognex_OPC.py
    ├── 04_CVognex.py
    └── Mallow_Data_processing.py
```

## Script overview

### `01_Cognex_stats.py`
Interactive script that loads a CSV exported from the vision system, groups the data by timestamp and lane, and calculates derived metrics including volume in grams, weight and cylinder volume. Output is saved to a new CSV.

### `02_OPC_UA_Cognex.py`
Minimal example that uses `CognexNativePy` to log in to an In-Sight camera, capture the current image and read or write cell values.

### `03_Cognex_OPC.py`
Uses the `opcua` client library to connect to a Cognex camera via OPC UA and browse the available nodes. Handles common connection errors.

### `04_CVognex.py`
Demonstrates how to send a trigger command to a camera through the `CognexNativePy` interface.

### `Mallow_Data_processing.py`
Large ETL style script that queries several OCS_AI database tables, merges work order data, pivots the results and writes them back to other tables. It logs progress and processes the data in chunks using a process pool.

## Identical copies

Every Python file in `src` has an identical counterpart in `all_organized_scripts/DATA_PROCESSING`. No functional differences were found when comparing these files.
