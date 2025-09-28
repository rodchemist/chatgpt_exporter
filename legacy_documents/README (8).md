# Tempering Data Prediction

This repository contains various scripts for exporting chocolate tempering sensor
data, exploring the resulting time‑series and training machine‑learning models.
Most of the interactive tools live under the [`trainer visualizer`](trainer%20visualizer/README.md)
directory.

## Main components

- **Data Exporter** – scripts such as `tempering_exporter_with_exclussions.py` and
  `trainer visualizer/dare_tempering_exporter.py` retrieve sensor data from
  SQL Server databases or generate demo data.
- **Data Explorer** – `trainer visualizer/data_explorer.py` provides a Plotly
  based web interface for time‑series inspection.
- **Training Dashboard** – `trainer visualizer/run_training.py` and
  `training_visualizer.py` train deep‑learning models (LSTM, GRU, CNN,
  Transformer) with real‑time charts.
- **Integrated launcher** – `trainer visualizer/launch_chocolate_suite.py` ties
  exporter, explorer and training tools together.

## Setup

1. Ensure Python 3.7+ is installed.
2. Install the required packages:
   ```bash
   pip install -r "trainer visualizer/requirements.txt"
   ```
3. Optionally run `trainer visualizer/setup.py` to perform environment checks and
   create sample data.

## Usage

Run the individual tools or launch the entire suite:

```bash
# Export data only
python "trainer visualizer/dare_tempering_exporter.py"

# Explore CSV/Parquet files
python "trainer visualizer/data_explorer.py"

# Train models with a dashboard
python "trainer visualizer/run_training.py" --data_file <path to csv>

# All-in-one launcher
python "trainer visualizer/launch_chocolate_suite.py"
```

The default ports are 5003 for the exporter, 5002 for the explorer and 5001 for
training.

See the [trainer visualizer README](trainer%20visualizer/README.md) for detailed
instructions, advanced options and screenshots.
