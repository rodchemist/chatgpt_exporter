# Unified Tempering Project

This directory consolidates three prior tempering-related projects into a single location. The existing directories were:

- `tempering_data_prediction` – scripts for analyzing and predicting chocolate tempering data.
- `tempering_prediction_final` – an Electron-based FTP management application for tempering data.
- `tempering_prediction-fork` – a fork of the FTP manager which used Docker for builds.

The fork has been removed after merging its changes into `ftp_manager`. The remaining projects are organized as:

- `data_prediction/` – all files from `tempering_data_prediction`.
- `ftp_manager/` – files from `tempering_prediction_final`, adjusted to work without conflicts.

See each subdirectory for usage details.
