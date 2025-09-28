# 🔧 Troubleshooting Guide

## Common Issues

### 1. Environment Not Found
```bash
# Error: environment "env_tslib" not found
conda env list  # Check available environments
# Solution: Run installation script first
./deep_learning_conda.sh
```

### 2. Import Errors
```bash
# Error: ModuleNotFoundError: No module named 'torch'
conda activate env_base_torch
conda list torch  # Check if installed
# Solution: Reinstall environment
conda env remove -n env_base_torch
# Re-run installation
```

### 3. CUDA Issues
```bash
# Error: CUDA out of memory
# Solutions:
# 1. Reduce batch size
# 2. Use CPU instead
# 3. Clear CUDA cache
export CUDA_VISIBLE_DEVICES=""  # Force CPU
```

### 4. Data File Not Found
```bash
# Error: FileNotFoundError: CSV file not found
# Check data path in config
ls rep_data/sampling/unified_sample/
# If missing, framework creates synthetic data
```

### 5. Permission Errors
```bash
# Error: Permission denied
# Fix permissions
chmod +x *.sh
chmod -R u+w test_results/
```

### 6. Mamba Installation Fails
```bash
# Common with mamba-ssm compilation
conda activate env_mamba
# Install build dependencies
conda install -c conda-forge ninja build-essential
pip install packaging
# Try manual installation
pip install --no-build-isolation causal-conv1d==1.4.0
pip install --no-build-isolation mamba-ssm
```

### 7. TSLib Models Not Found
```bash
# Check TSLib installation
ls ~/ai_repos/time_series_models/pytorch_models/Time-Series-Library/
# If missing, clone manually
cd ~/ai_repos/time_series_models/pytorch_models/
git clone https://github.com/thuml/Time-Series-Library.git
```

### 8. Tests Hang or Timeout
```bash
# Kill hanging processes
pkill -f "python.*test_.*models.py"
# Reduce epochs in config
# Use smaller models
```

### 9. Memory Issues
```bash
# Monitor memory usage
htop
# Solutions:
# 1. Reduce sequence_length
# 2. Smaller batch_size
# 3. Test fewer models
# 4. Use swap space
sudo swapon -s
```

### 10. Results Not Generated
```bash
# Check test results directory
ls -la test_results/
# Check logs for errors
tail -n 50 logs/master_test_run_*.log
# Verify permissions
chmod -R u+w test_results/
```

## Performance Optimization

### GPU Optimization
```bash
# Check GPU memory
nvidia-smi
# Set memory growth
export TF_FORCE_GPU_ALLOW_GROWTH=true
# Use mixed precision
# (enabled by default in configs)
```

### CPU Optimization
```bash
# Set thread count
export OMP_NUM_THREADS=4
export MKL_NUM_THREADS=4
# Use CPU device
sed -i 's/"device": "auto"/"device": "cpu"/' configs/test_config.json
```

### Disk Space
```bash
# Check disk space
df -h
# Clean old results
rm -rf test_results/old_*
# Disable model saving
sed -i 's/"save_models": true/"save_models": false/' configs/test_config.json
```

## Environment-Specific Issues

### env_mamba
- **Issue**: Compilation errors
- **Solution**: Use fallback implementations
- **Workaround**: Skip if installation fails

### env_geometric
- **Issue**: PyTorch Geometric version conflicts
- **Solution**: Use conda-forge channel
- **Command**: `conda install pyg -c pyg`

### env_tensorflow
- **Issue**: GPU configuration
- **Solution**: Set TF_CPP_MIN_LOG_LEVEL=2
- **Alternative**: Use CPU-only TensorFlow

### env_unified
- **Issue**: Darts dependencies
- **Solution**: Install from conda-forge
- **Command**: `conda install darts -c conda-forge`

## Recovery Procedures

### Complete Reset
```bash
# Remove all environments
for env in env_base_torch env_tslib env_geometric env_mamba env_transformers env_tensorflow env_unified; do
    conda env remove -n $env -y
done

# Re-run installation
./deep_learning_conda.sh
```

### Partial Reset
```bash
# Reset specific environment
conda env remove -n env_tslib -y
conda create -n env_tslib --clone env_base_torch -y
conda activate env_tslib
# Install specific packages...
```

### Clean Results
```bash
# Backup important results
cp -r test_results test_results_backup_$(date +%Y%m%d)

# Clean results directory
rm -rf test_results/*
mkdir -p test_results/model_artifacts
```

## Getting Help

1. **Check Logs**: Always check the detailed logs first
2. **Environment Info**: Include conda environment info in issues
3. **System Info**: Include OS, Python, CUDA versions
4. **Error Messages**: Include full error traceback
5. **Configuration**: Share your test_config.json

## Performance Benchmarks

Expected performance on different systems:

### High-End Workstation (RTX 4090, 64GB RAM)
- **Total Time**: 2-4 hours
- **Per Environment**: 20-40 minutes
- **Best Models**: R² > 0.85

### Mid-Range System (GTX 1080, 16GB RAM)
- **Total Time**: 4-8 hours
- **Per Environment**: 30-60 minutes
- **Best Models**: R² > 0.80

### CPU-Only System
- **Total Time**: 8-16 hours
- **Per Environment**: 1-2 hours
- **Best Models**: R² > 0.75

Remember: Results depend heavily on data quality and chocolate tempering process complexity! 🍫
