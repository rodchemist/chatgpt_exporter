Language: Markdown
Lines of Code: 71
File: README.md
Version: 1.1.0
Project: AI_CryptoTrader
Repository: AI_CryptoTrader
Author: Rod Sanchez
Created: 2024-07-12 00:00
Last Edited: 2025-07-12 06:31


# RodChem Crypto Predictor Synthetic Data

This repository contains multiple model testing scripts that expect a dataset named `comprehensive_tempering_data.csv` under `data/sample/`.

The provided script `src/utils/generate_synthetic_data.py` creates this dataset with synthetic temperature sensor values so that all tests can run without needing real data.

To generate the synthetic dataset run:

```bash
python src/utils/generate_synthetic_data.py
```

The generated CSV includes the columns `timestamp_utc`, `unique_tagpath_id` and `combined_value` for nine sensor ids used by the model preprocessing utilities.

To verify all files include the required headers run:

```bash
python universal_file_validator.py
```

## Pip Requirements

The `env` directory contains Conda environment files. To create equivalent pip requirements files run:

```bash
python scripts/convert_conda_to_pip.py
```


This generates `.txt` files with the same names that can be installed via
`pip install -r env/<name>.txt` on systems without Conda.


## Coin List Synchronization

Run the following command to update the local list of cryptocurrency symbols:

```bash
python src/utils/update_coin_list.py
```

This stores the complete symbol list in `data/coins_list.csv` and updates the
SQLite database `data/cache/crypto_cache.db` with any new coins.


## Environment Setup

Use the helper script to install all pip environments into separate virtualenvs:

```bash
bash scripts/setup_all_envs.sh
```

## Generating Data and Running Tests

Execute the next script to create the synthetic dataset and run all unit tests:

```bash
bash scripts/generate_data_and_test.sh
```
