# crypto-ts-gpu

GPU-ready time‑series training for minute‑level crypto (or any OHLCV + TA). Targets **+15 min** horizon with:
- **CUDA XGBoost** (strong tabular baseline), and
- **PyTorch Lightning LSTM** (sequence model with long lookback, bf16 mixed precision).

> Tested shape: 182 features (incl. TA), 172,800 rows (≈120 days). Works fine on a **RTX 4090 (24 GB)** with lookback **L=1,024–2,048** and batch **256**.

## Quickstart

This project provides a pipeline for preparing OHLCV data and generating TA-Lib features, followed by machine learning model training.

```bash
# 1) Create environment
#    (adjust pytorch-cuda version in env/environment.yml to your driver if needed)
mamba env create -f env/environment.yml
mamba activate env_talib

# 2) Prepare data and generate TA-Lib features
#    (replace path to your raw OHLCV CSV)
#    This will output a _talib.csv file in the data/ directory.
bash shell/run_talib_pipeline.sh --csv data/Binance_BTCUSDC_2022_minute.csv

# 3) Run baseline and LSTM models
#    (use the _talib.csv generated in the previous step)
#    Example:
#    python -m src.train_xgb --csv data/Binance_BTCUSDC_2022_minute_talib.csv --h 15
#    python -m src.train_lstm --csv data/Binance_BTCUSDC_2022_minute_talib.csv --L 1024 --epochs 30 --h 15
```

### Minimal CSV requirements
- A timestamp column named **`date`** (ISO datetime or epoch) — changeable via CLI.
- A price column **`close`**.
- Other columns are treated as features (e.g., TA indicators).

### Data Preparation and Feature Generation

The pipeline uses the following scripts to prepare raw OHLCV data and generate TA-Lib indicators:

-   **`src/pipeline/pre_talib_prepare.py`**: This script takes a raw OHLCV CSV file, performs necessary data cleaning (e.g., timestamp conversion, type casting, sorting, de-duplication), and outputs a prepared CSV. This step ensures the data is in a consistent format suitable for TA-Lib.
-   **`src/pipeline/talib_all_features.py`**: This script takes the prepared CSV from the previous step and computes a comprehensive set of technical analysis indicators using the TA-Lib Abstract API. The output is a new CSV file containing the original OHLCV data augmented with all the calculated TA features.

These two scripts are orchestrated by `shell/run_talib_pipeline.sh`.

### Horizon, Lookback, Splits
- Forecast **+15 min**: `--h 15`.
- Lookback (sequence models): start with **L=1,024**; if VRAM permits, try **2,048**.
- Default splits: 70% train / 15% val / 15% test (by time).

## Commands

### CUDA XGBoost baseline
```bash
python -m src.train_xgb --csv data/Binance_BTCUSDC_2022_minute_talib.csv --h 15
```
Flags: `--timestamp-col`, `--price-col`, `--seed`, `--outdir`, `--mlflow`.

### Lightning LSTM (bf16)
```bash
python -m src.train_lstm --csv data/Binance_BTCUSDC_2022_minute_talib.csv --L 1024 --epochs 30 --h 15
```
Flags include `--batch`, `--hidden`, `--layers`, `--precision bf16-mixed|16-mixed`, `--accumulate` (grad accumulation).

### Probe GPU capacity
```bash
python tools/probe_lstm_capacity.py --features 182 --hidden 256 --layers 2 --batch 256 --start 512
```

## Logging & Caching
- Standardized logging to `logs/` and console.
- Feature matrices cached to `cache/` keyed by CSV path + params for fast re-runs.
- Optional MLflow logging (`--mlflow` to enable).

## Notes
- Ensure your rolling/TA features are **right-aligned** (no future leakage).
- If your driver/CUDA differs, edit `env/environment.yml` (`pytorch-cuda` version).

## License
MIT
