# Contribution Summary: tempering_data_prediction to ai_timeseries_framework

## Overview
The `tempering_data_prediction` folder contains a comprehensive suite of tools for working with chocolate tempering data, including data export, exploration, and deep learning model training with a web-based dashboard.

## Key Contributions

1.  **Data Export**: Scripts to pull tempering sensor data from SQL Server databases or generate demo data.
2.  **Data Exploration**: An interactive Plotly-based web interface for time-series exploration and quality checks.
3.  **Model Training**: Deep learning training interface with real-time charts for several model types (LSTM, GRU, CNN, Transformer).
4.  **Integrated Launcher**: A script that ties the exporter, explorer, and training tools together.

## Selected Components for Integration

1.  **Data Export**: The data export logic in `tempering_exporter_with_exclussions.py` and `trainer visualizer/dare_tempering_exporter.py` could be adapted for retrieving time series data from various databases.
2.  **Data Exploration**: The interactive data exploration interface in `trainer visualizer/data_explorer.py` could be integrated as a visualization tool in the framework.
3.  **Model Training**: The deep learning model training scripts in `trainer visualizer/training_visualizer.py` and `trainer visualizer/run_training.py` could be integrated as new model types or training utilities.
4.  **Integrated Launcher**: The integrated launcher concept in `trainer visualizer/launch_chocolate_suite.py` could be adapted for launching different components of the `ai_timeseries_framework`.

## Integration Plan

1.  Adapt the selected scripts to align with the `ai_timeseries_framework`'s coding standards and directory structure.
2.  Integrate the adapted components into the framework's data ingestion, visualization, model training, and launcher modules.
3.  Update the framework's documentation to include the new data export, visualization, model training, and launcher capabilities.