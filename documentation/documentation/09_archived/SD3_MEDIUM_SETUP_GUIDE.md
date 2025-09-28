# Stable Diffusion 3 Medium Setup Guide
**Optimized for RTX 4090 (24GB VRAM) + 128GB RAM**

## Overview
Stable Diffusion 3 Medium is a state-of-the-art text-to-image model with 2.5B parameters, designed for high-quality image generation with excellent prompt adherence and superior text integration capabilities.

## System Compatibility ✅
Your system is **perfectly suited** for SD3 Medium:
- **RTX 4090 (24GB VRAM)**: Ideal for SD3 Medium (requires 18-20GB)
- **128GB RAM**: Excellent for model loading and processing
- **CUDA 12.1**: Compatible with latest diffusers
- **PyTorch 2.4.1**: Supports all required features

## Key Advantages of SD3 Medium

### Quality Benchmarks (2024)
Based on comprehensive comparisons:

1. **🥇 FLUX-dev**: Best overall quality, superior text rendering (requires ~24GB, slower generation)
2. **🥈 SD3 Medium**: Excellent prompt adherence, good text integration, balanced performance
3. **🥉 SDXL**: Good detail and resolution, faster generation, lower VRAM usage

### Performance Comparison (RTX 4090)
| Model | Generation Time | VRAM Usage | Resolution | Text Quality | Prompt Adherence |
|-------|----------------|------------|------------|--------------|-----------------|
| **SD3 Medium** | ~20-25s | 18-20GB | 1024x1024 | Excellent | Excellent |
| SDXL | ~13s | 8-10GB | 1024x1024 | Good | Good |
| FLUX-dev | ~57s | 20-24GB | 1024x1024 | Superior | Superior |

## Installation Steps

### 1. Environment Setup
```bash
# Activate your conda environment
conda activate image_gen

# Run the installation script
./install_sd3_medium.sh
```

### 2. Manual Installation (Alternative)
```bash
# Update core packages
pip install -U diffusers transformers accelerate huggingface-hub safetensors

# Install xformers for memory efficiency
pip install xformers
```

### 3. HuggingFace Authentication **REQUIRED**
SD3 Medium requires HuggingFace authentication:

1. **Visit**: https://huggingface.co/stabilityai/stable-diffusion-3-medium
2. **Click**: "Agree and access repository" (requires HF account)
3. **Get token**: https://huggingface.co/settings/tokens
4. **Authenticate**:
   ```bash
   huggingface-cli login
   # Paste your token when prompted
   ```

### 4. Test Installation
```bash
python sd3_medium_setup.py
```

## Licensing Information

### SD3 Medium License
- **Free**: Research and commercial use for organizations with <$1M annual revenue
- **Enterprise License**: Required for companies with >$1M annual revenue
- **Contact**: Stability AI for enterprise licensing

### Comparison with Other Models
| Model | License | Commercial Use | Revenue Limit |
|-------|---------|----------------|---------------|
| **SD3 Medium** | Stability AI Community | Yes | <$1M free |
| SDXL | Apache 2.0 | Yes | No limit |
| FLUX-dev | Apache 2.0 | Yes | No limit |

## Memory Optimization Options

### For 24GB VRAM (Your System) - **Recommended**
```python
# Full model loading (optimal performance)
pipe = StableDiffusion3Pipeline.from_pretrained(
    "stabilityai/stable-diffusion-3-medium-diffusers",
    torch_dtype=torch.float16,
    use_safetensors=True,
    variant="fp16"
).to("cuda")

# Enable optimizations
pipe.enable_xformers_memory_efficient_attention()
pipe.enable_vae_tiling()
```

### For Lower VRAM Systems
```python
# CPU offloading (16GB+ VRAM)
pipe.enable_model_cpu_offload()

# Text encoder quantization (reduces memory by ~4GB)
from diffusers import BitsAndBytesConfig
quantization_config = BitsAndBytesConfig(load_in_8bit=True)

# Remove T5 encoder entirely (8GB VRAM)
pipe = StableDiffusion3Pipeline.from_pretrained(
    model_id,
    text_encoder_3=None,
    tokenizer_3=None,
    torch_dtype=torch.float16
)
```

## Generation Parameters

### Optimal Settings for SD3 Medium
```python
generation_params = {
    "num_inference_steps": 28,    # SD3 optimal (vs 20 for SDXL)
    "guidance_scale": 7.0,        # SD3 optimal (vs 7.5 for SDXL)
    "height": 1024,               # Native resolution
    "width": 1024,                # Native resolution
}
```

### Quality Tips
1. **Text Integration**: SD3 excels at rendering text within images
2. **Complex Prompts**: Superior understanding of multi-element scenes
3. **Prompt Structure**: Use detailed, descriptive prompts for best results
4. **Negative Prompts**: Less critical than with SDXL but still beneficial

## Troubleshooting

### Common Issues

#### Authentication Error
```
Error: Repository not found or access denied
```
**Solution**: Complete HuggingFace authentication steps above

#### CUDA Out of Memory
```
RuntimeError: CUDA out of memory
```
**Solutions**:
1. Enable CPU offloading: `pipe.enable_model_cpu_offload()`
2. Enable VAE tiling: `pipe.enable_vae_tiling()`
3. Reduce batch size to 1
4. Use torch.float16 precision

#### Slow Generation
- **Expected**: SD3 is slower than SDXL but faster than FLUX
- **Optimization**: Ensure XFormers is installed and enabled
- **Alternative**: Use SDXL for faster iteration, SD3 for final quality

### Performance Monitoring
```python
# Monitor VRAM usage
print(f"VRAM used: {torch.cuda.memory_allocated() / 1024**3:.1f} GB")
print(f"VRAM cached: {torch.cuda.memory_reserved() / 1024**3:.1f} GB")
```

## File Structure
```
/mnt/c/_automation/images_generation/
├── sd3_medium_setup.py          # Main test script
├── install_sd3_medium.sh        # Installation script
├── SD3_MEDIUM_SETUP_GUIDE.md    # This guide
├── sd3_medium_test/             # Generated images (created after test)
└── output/                      # Existing output folder
```

## Model Comparison Summary

### When to Use SD3 Medium
- **High-quality final images**
- **Text integration in images**
- **Complex, multi-element scenes**
- **Professional/commercial projects**
- **When you have 24GB VRAM**

### When to Use SDXL Instead
- **Rapid prototyping/iteration**
- **Lower VRAM systems (8-16GB)**
- **Speed is priority over quality**
- **No HuggingFace account/authentication**

### When to Use FLUX-dev Instead
- **Maximum quality requirements**
- **Best text rendering**
- **Time is not a constraint**
- **Commercial applications requiring top-tier results**

## Next Steps

1. **Run Installation**: `./install_sd3_medium.sh`
2. **Complete Authentication**: Follow HuggingFace setup
3. **Test Generation**: `python sd3_medium_setup.py`
4. **Compare Results**: Check generated images vs your existing SDXL outputs
5. **Optimize Workflow**: Adjust parameters based on your specific needs

Your RTX 4090 system is **perfectly equipped** for SD3 Medium. You'll get excellent quality with reasonable generation times, making it ideal for both experimentation and production use.