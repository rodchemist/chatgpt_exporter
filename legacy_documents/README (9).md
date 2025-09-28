# Chocolate Tempering Analysis Suite

This folder contains an integrated set of tools for working with chocolate tempering data. It bundles three main components:

- **Data Exporter** – pulls tempering sensor data from multiple SQL Server databases or generates demo data.
- **Data Explorer** – interactive Plotly based web interface for time‑series exploration and quality checks.
- **Training Dashboard** – deep‑learning training interface with real‑time charts for several model types (LSTM, GRU, CNN, Transformer).

`launch_chocolate_suite.py` ties everything together so that you can export, explore and train from one command.

## Setup

1. Ensure Python 3.7+ is installed.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run `setup.py` for optional environment checks and demo data creation.

## Quick start

Launch the interactive suite using the convenience scripts:

```bash
# Linux/macOS
bash bash_script.sh

# Windows
batch_script.bat
```

Or manually run:

```bash
python launch_chocolate_suite.py
```

The default ports are:
- Data Exporter: http://localhost:5003
- Data Explorer: http://localhost:5002
- Training Dashboard: http://localhost:5001

## Individual components

- **`dare_tempering_exporter.py`** – Web service for exporting or generating tempering data.
- **`data_explorer.py`** – Web server for visualising CSV files and computing statistics.
- **`training_visualizer.py`** – Training script with a Flask/SocketIO dashboard.
- **`run_training.py`** – Simple wrapper around `training_visualizer.py` providing presets.
- **`integrated_launcher.py`** – Smaller launcher for explorer and training only.

Saved models are stored in `saved_models/` and sample exported data is placed under `rep_data/sampling/`.

## Example

To train models on the provided sample CSV and view progress:

```bash
python run_training.py --data_file rep_data/sampling/unified_sample/tempering_unified_sample_comprehensive.csv
```
Then open [http://localhost:5002](http://localhost:5002) in your browser.

## License

This repository is provided for demonstration purposes and does not include production database credentials.
