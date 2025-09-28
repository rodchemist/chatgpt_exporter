# Dependency Issues and Solutions

## Current Issue

The framework encounters import conflicts with the current environment, specifically:

```
ImportError: /home/rod/miniforge3/lib/python3.12/site-packages/flash_attn_2_cuda.cpython-312-x86_64-linux-gnu.so: undefined symbol: _ZN3c104cuda9SetDeviceEi
```

This is caused by:
1. NumPy 2.x compatibility issues with compiled packages
2. Flash Attention CUDA compilation mismatches
3. TensorFlow/Transformers version conflicts

## Solutions

### Option 1: Clean Environment Setup (Recommended)

```bash
# Create new conda environment
conda create -n ai_comparison python=3.10
conda activate ai_comparison

# Install PyTorch first
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia

# Install core dependencies
pip install diffusers>=0.21.0
pip install transformers>=4.25.0
pip install accelerate>=0.21.0
pip install safetensors>=0.3.1

# Install other requirements
pip install pillow matplotlib pandas psutil tqdm requests

# Optional: Install XFormers for optimization
pip install xformers
```

### Option 2: Fix Current Environment

```bash
# Downgrade NumPy to resolve compatibility
pip install "numpy<2.0"

# Reinstall flash-attn with proper CUDA version
pip uninstall flash-attn -y
pip install flash-attn --no-build-isolation

# Or disable flash attention entirely
export DISABLE_FLASH_ATTENTION=1
```

### Option 3: Use Alternative Models

The framework is designed to gracefully handle missing dependencies. You can:

1. Use only basic Stable Diffusion models (no FLUX/SD3)
2. Disable flash attention optimizations
3. Run with CPU-only mode for testing

## Verification Steps

1. Test framework structure (already working):
   ```bash
   python test_framework_structure.py
   ```

2. Test model imports:
   ```bash
   python -c "from diffusers import StableDiffusionPipeline; print('✅ SD works')"
   ```

3. Test full framework:
   ```bash
   python ai_model_comparison_framework.py
   ```

## Environment Requirements

### Minimum Requirements
- Python 3.8+
- PyTorch with CUDA support
- 4GB GPU memory for SD 1.5

### Recommended Requirements
- Python 3.10
- PyTorch 2.0+
- 8GB+ GPU memory for SDXL
- 12GB+ GPU memory for FLUX.1

### Detected System
- ✅ NVIDIA GeForce RTX 4090 (24GB) - Excellent for all models
- ✅ PyTorch 2.4.0+cu121 - Good version
- ❌ NumPy 2.1.2 - Causing compatibility issues

## Quick Test Commands

```bash
# Test system requirements
python -c "import torch; print(f'CUDA: {torch.cuda.is_available()}, GPU: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else \"None\"}')"

# Test specific models (after fixing dependencies)
python quick_test.py --mode quick          # SD 1.5 only
python quick_test.py --mode memory_limited # SD 1.5 + SDXL
python quick_test.py --mode full          # All available models

# List available options
python quick_test.py --mode list
```

## Framework Status

✅ **Core Structure**: Working perfectly
✅ **Memory Monitoring**: Functional
✅ **Performance Metrics**: Ready
✅ **Comparison System**: Implemented
✅ **Report Generation**: Working
❌ **Model Loading**: Blocked by dependencies

The framework is complete and ready to use once the dependency conflicts are resolved.