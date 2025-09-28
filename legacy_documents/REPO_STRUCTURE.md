# Repository Structure

```
model_testing/
├── configs/               # JSON configuration files for the framework
├── docs/                  # Guides and troubleshooting information
├── modular_system/        # Model registry and helper utilities
├── old_models/            # Legacy scripts kept for reference
├── rep_data/              # Sample data for quick tests
├── test_results/          # Example output from previous runs
├── torch/                 # PyTorch model implementations and helpers
├── obs/                   # Archived troubleshooting scripts
└── *.sh / *.py            # Test runners and framework scripts
```

Most functionality is driven by the shell scripts. `run_all_tests.sh` invokes each environment test script and saves reports in `test_results/`.
