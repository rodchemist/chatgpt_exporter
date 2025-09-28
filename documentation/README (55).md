# AI Image Generation Model Comparison Framework

A comprehensive testing and comparison framework for evaluating multiple AI image generation models including Stable Diffusion 1.5, SDXL, FLUX.1, and Stable Diffusion 3.

## Features

- **Unified Testing Interface**: Test multiple models with a single script
- **Standardized Prompts**: Fair comparison across different model architectures
- **Performance Monitoring**: VRAM usage, generation time, and throughput metrics
- **Side-by-Side Comparisons**: Automated generation of comparison grids
- **Comprehensive Reporting**: Detailed performance analysis and recommendations
- **Memory Management**: Automatic model loading/unloading to prevent OOM errors
- **Quality Assessment**: Standardized test prompts across different categories

## Supported Models

| Model | Version | Resolution | Memory Req. | Strengths |
|-------|---------|------------|-------------|-----------|
| Stable Diffusion 1.5 | runwayml/stable-diffusion-v1-5 | 512x512 | 4GB | Fast, lightweight, reliable |
| Stable Diffusion XL | stabilityai/stable-diffusion-xl-base-1.0 | 1024x1024 | 8GB | High resolution, detailed |
| FLUX.1 Schnell | black-forest-labs/FLUX.1-schnell | 1024x1024 | 12GB | State-of-the-art quality, 4 steps |
| Stable Diffusion 3 | stabilityai/stable-diffusion-3-medium-diffusers | 1024x1024 | 10GB | Latest architecture, improved text |

## Test Categories

### 1. Realistic Photography
- Professional portraits with natural lighting
- Landscape photography with detailed environments

### 2. Cartoon/Anime Style
- Pixar-style 3D characters with expressive features
- Anime illustrations with detailed art style

### 3. Artistic/Painting Style
- Oil paintings with visible brush strokes
- Watercolor paintings with soft, transparent layers

### 4. Complex Scenes
- Multi-element scenes with detailed environments
- Fantasy landscapes with multiple objects

### 5. Text Rendering
- Signs and typography rendering capabilities
- Book covers and design elements

## Installation

### Prerequisites
- Python 3.8+
- CUDA-compatible GPU (4GB+ VRAM recommended)
- conda environment (recommended)

### Setup Environment
```bash
# Create and activate conda environment
conda create -n image_gen python=3.10
conda activate image_gen

# Install dependencies
pip install -r requirements.txt

# Optional: Install XFormers for memory optimization
pip install xformers
```

### GPU Requirements
- **Minimum**: 4GB VRAM (SD 1.5 only)
- **Recommended**: 8GB VRAM (SD 1.5 + SDXL)
- **Optimal**: 12GB+ VRAM (All models)

## Usage

### Quick Start
```bash
# Run with recommended models based on your GPU memory
python ai_model_comparison_framework.py
```

### Custom Testing
```python
from ai_model_comparison_framework import ModelComparison

# Initialize framework
framework = ModelComparison(output_base_dir="my_comparison")

# Check system capabilities
system_info = framework.check_system_requirements()

# Test specific models
models_to_test = ["sd15", "sdxl"]  # Only test these models
framework.run_comprehensive_test(models_to_test=models_to_test)

# Test specific prompts
prompt_names = ["portrait_photography", "pixar_character"]
framework.run_comprehensive_test(prompts_to_test=prompt_names)
```

### Advanced Usage
```python
# Generate single image with custom parameters
framework = ModelComparison()
prompt = framework.test_prompts[0]  # First test prompt

custom_params = {
    "num_inference_steps": 50,
    "guidance_scale": 8.0,
    "height": 768,
    "width": 768
}

result = framework.generate_image(prompt, "sdxl", custom_params)
```

## Output Structure

```
model_comparison/
└── session_20250915_143022/
    ├── images/                     # Generated images
    │   ├── sd15_realistic_portrait_photography_20250915_143022.png
    │   ├── sdxl_realistic_portrait_photography_20250915_143022.png
    │   └── ...
    ├── comparisons/                # Side-by-side grids
    │   ├── realistic_portrait_photography_comparison.png
    │   ├── cartoon_pixar_character_comparison.png
    │   └── ...
    ├── reports/                    # Performance reports
    │   ├── comparison_report.txt
    │   └── performance_chart.png
    ├── system_info.json           # Hardware information
    ├── detailed_results.json      # Raw generation data
    └── performance_metrics.json   # Calculated metrics
```

## Performance Metrics

The framework tracks and reports:
- **Generation Time**: Average and total time per model
- **Memory Usage**: Peak and average VRAM consumption
- **Success Rate**: Percentage of successful generations
- **Throughput**: Images generated per minute
- **Quality Indicators**: Category-specific performance

## Model Selection Guide

### Choose SD 1.5 if:
- Limited GPU memory (4-6GB)
- Fast iteration and prototyping
- Basic image generation needs

### Choose SDXL if:
- Need high resolution (1024x1024)
- Better prompt understanding required
- Good balance of quality and speed

### Choose FLUX.1 if:
- Maximum quality is priority
- Have sufficient GPU memory (12GB+)
- Need state-of-the-art results

### Choose SD3 if:
- Latest architecture benefits needed
- Improved text rendering required
- Advanced prompt following

## Troubleshooting

### Common Issues

#### Out of Memory (OOM) Errors
```bash
# Solution 1: Test fewer models
python ai_model_comparison_framework.py  # Uses recommended models only

# Solution 2: Enable CPU offloading (automatically enabled)
# Framework automatically uses memory optimizations
```

#### Model Download Issues
```bash
# Ensure you have access to model repositories
# Some models may require Hugging Face authentication
pip install huggingface_hub
huggingface-cli login
```

#### Slow Generation
- Enable XFormers: `pip install xformers`
- Use lower resolution for testing
- Reduce number of inference steps

### Performance Optimization

```python
# Custom optimization settings
framework = ModelComparison()

# Use half precision for all models (done automatically)
# Enable gradient checkpointing for memory savings
# Use CPU offloading for large models (done automatically)
```

## Extending the Framework

### Adding New Models
```python
# Add to model_configs in _initialize_model_configs()
"my_model": ModelConfig(
    name="My Custom Model",
    model_id="organization/model-name",
    pipeline_class=StableDiffusionPipeline,
    torch_dtype=torch.float16,
    default_steps=30,
    default_guidance=7.5,
    native_resolution=(512, 512),
    supports_negative_prompt=True,
    supports_guidance=True,
    memory_requirements_gb=6.0,
    special_params={}
)
```

### Adding New Test Prompts
```python
# Add to test_prompts in _initialize_test_prompts()
TestPrompt(
    category="my_category",
    name="my_test",
    prompt="Your detailed prompt here",
    negative_prompt="What to avoid",
    description="Test description",
    expected_elements=["element1", "element2"]
)
```

## Results Interpretation

### Performance Chart
- **Success Rate**: Higher is better (aim for >90%)
- **Generation Time**: Lower is better for speed
- **Memory Usage**: Lower is better for efficiency
- **Images/Minute**: Higher is better for throughput

### Comparison Grids
- Visual quality comparison across models
- Consistency in style and prompt following
- Detail level and resolution differences

### Detailed Reports
- Category-specific performance analysis
- Model recommendations based on use case
- Memory and time optimization suggestions

## Contributing

To contribute improvements:
1. Fork the repository
2. Create feature branch
3. Add tests for new functionality
4. Submit pull request with detailed description

## License

This framework is provided for research and educational purposes. Please respect the individual model licenses from their respective creators.

## Acknowledgments

- Stability AI for Stable Diffusion models
- Black Forest Labs for FLUX.1
- Hugging Face for the diffusers library
- The open-source AI community for continued innovation