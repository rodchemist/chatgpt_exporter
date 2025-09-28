# FLUX.1 Installation Guide for RTX 4090 with FP8 Quantization

## System Requirements
- **GPU**: NVIDIA RTX 4090 (24GB VRAM) - Confirmed working
- **RAM**: 128GB system RAM
- **CUDA**: 12.1+ (12.1 confirmed working)
- **Python**: 3.11+

## Installation Commands

### 1. Environment Setup
```bash
# Activate your conda environment
source ~/miniforge3/etc/profile.d/conda.sh
conda activate image_gen
```

### 2. Core Dependencies
```bash
# PyTorch with CUDA 12.1 (already installed)
pip install torch==2.4.1+cu121 --index-url https://download.pytorch.org/whl/cu121

# Essential libraries
pip install diffusers==0.35.1
pip install transformers==4.56.1
pip install optimum-quanto==0.2.5
pip install accelerate
pip install huggingface_hub
```

### 3. Hugging Face Authentication
```bash
# Method 1: CLI login (recommended)
pip install huggingface_hub[cli]
huggingface-cli login

# Method 2: Set environment variable
export HF_TOKEN="your_token_here"

# Method 3: Use the setup script
python setup_huggingface_auth.py
```

### 4. Request Model Access
Visit these URLs and request access:
- [FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev)
- [FLUX.1-schnell](https://huggingface.co/black-forest-labs/FLUX.1-schnell)

## Verification

### Quick Validation
```bash
python flux_installation_validator.py
```

### Full Performance Test
```bash
python flux_fp8_test.py
```

## Performance Expectations

### FLUX.1 Dev with FP8 Quantization
- **VRAM Usage**: ~12-16GB (down from ~24GB)
- **Generation Time**: 15-25 seconds (1024x1024, 20 steps)
- **Quality**: Minimal degradation from FP16

### FLUX.1 Schnell with FP8 Quantization
- **VRAM Usage**: ~8-12GB
- **Generation Time**: 3-6 seconds (1024x1024, 4 steps)
- **Quality**: Good quality, faster inference

## Optimization Settings

### FP8 Quantization Configuration
```python
from optimum.quanto import freeze, qfloat8, quantize

# Quantize transformer (main component)
quantize(pipe.transformer, weights=qfloat8)
freeze(pipe.transformer)

# Quantize text encoder for additional memory savings
quantize(pipe.text_encoder_2, weights=qfloat8)
freeze(pipe.text_encoder_2)
```

### Memory Optimization
```python
# Enable CPU offloading
pipe.enable_model_cpu_offload()

# Clear memory between generations
torch.cuda.empty_cache()
```

## Troubleshooting

### Common Issues

1. **Authentication Error**
   ```
   Solution: Run python setup_huggingface_auth.py
   ```

2. **Out of Memory**
   ```
   Solution: Ensure FP8 quantization is enabled
   Try reducing batch size or image resolution
   ```

3. **Slow Performance**
   ```
   Solution: Check GPU utilization with nvidia-smi
   Ensure CUDA 12.1+ is properly installed
   ```

### Alternative Models

If you can't access official FLUX.1 models, try these FP8 variants:
- `Kijai/flux-fp8` - Pre-quantized FLUX.1
- `XLabs-AI/flux-RealismLora` - FLUX.1 with realism LoRA

## Generated Files

The scripts will create:
- `output/` - Generated images
- `flux_validation_test.png` - Quick test image
- Performance logs with timing and memory usage

## Hardware-Specific Notes

### RTX 4090 Optimizations
- Use `torch.bfloat16` for best performance
- Enable Tensor Core operations
- FP8 reduces memory by ~40% with minimal quality loss

### Memory Distribution
- **FP16 FLUX.1 Dev**: ~24GB VRAM (uses full capacity)
- **FP8 FLUX.1 Dev**: ~14-16GB VRAM (comfortable headroom)
- **FP8 FLUX.1 Schnell**: ~8-12GB VRAM (very efficient)

## Next Steps

1. Run `python setup_huggingface_auth.py` to authenticate
2. Run `python flux_installation_validator.py` to verify setup
3. Run `python flux_fp8_test.py` for comprehensive testing
4. Check `output/` directory for generated images

## Support

If you encounter issues:
1. Check CUDA installation: `nvidia-smi`
2. Verify PyTorch CUDA: `python -c "import torch; print(torch.cuda.is_available())"`
3. Test authentication: `python setup_huggingface_auth.py`
4. Review error logs in the script outputs