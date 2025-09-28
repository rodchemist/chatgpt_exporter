# Comprehensive Time Series Models Implementation Guide

## PyTorch-Based Models (12 models)

| Model | Repository/Installation | Performance Gains | Complexity | Special Installation | Best Use Case |
|-------|------------------------|-------------------|------------|---------------------|---------------|
| **iTransformer** | `git clone https://github.com/thuml/iTransformer`<br/>Also in TSLib | SOTA multivariate<br/>Variable-wise attention | O(D²L) where D=variables | Standard PyTorch | Multivariate correlations |
| **TimeMixer** | Available through TSLib<br/>`git clone https://github.com/thuml/Time-Series-Library` | Consistent SOTA<br/>38-65% improvement | O(L) linear | Standard PyTorch | General purpose, efficiency |
| **PatchTST** | `git clone https://github.com/yuqinie98/PatchTST` | 21% MSE reduction<br/>2-3X memory efficiency | O(N²) where N=patches | Standard PyTorch | Long sequences |
| **Mamba4Cast** | `git clone https://github.com/automl/Mamba4Cast`<br/>`pip install mamba-ssm` | Competitive with foundations<br/>27M vs billions params | O(L) linear | **Requires mamba-ssm**<br/>`pip install causal-conv1d>=1.0.0`<br/>`pip install mamba-ssm` | Zero-shot, efficiency |
| **MTGNN** | `git clone https://github.com/nnzhan/MTGNN` | 9.4% MAE improvement<br/>Auto graph learning | O(L × D²) | **Requires PyTorch Geometric**<br/>`pip install torch-geometric` | Complex variable relationships |
| **FourierGNN** | `git clone https://github.com/aikunyi/FourierGNN` | 9.4% MAE, 10.9% RMSE<br/>Unified spatiotemporal | O(L log L) | **Requires PyTorch Geometric**<br/>`pip install torch-geometric`<br/>`pip install scipy` | Spatiotemporal patterns |
| **StemGNN** | `git clone https://github.com/microsoft/StemGNN` | SOTA on traffic/energy<br/>Spectral efficiency | O(L log L) | **Requires spectral packages**<br/>`pip install scipy`<br/>`pip install networkx` | Frequency domain patterns |
| **TimeGrad** | Multiple implementations<br/>`pip install pytorch-lightning` | 40-65% over probabilistic<br/>Superior uncertainty | O(L × T) diffusion steps | **Requires diffusion libs**<br/>`pip install diffusers`<br/>`pip install pytorch-lightning` | Uncertainty quantification |
| **Neural ODEs** | `pip install torchdiffeq` | Superior extrapolation<br/>Continuous time | Adaptive (solver dependent) | **Requires ODE solvers**<br/>`pip install torchdiffeq`<br/>`pip install scipy` | Irregular sampling |
| **TCN** | `pip install pytorch-tcn`<br/>Or custom implementation | Competitive with RNNs<br/>Parallelizable | O(L) with dilations | Standard PyTorch | Real-time applications |
| **TimeVAE** | Custom implementations<br/>Various repositories | Good probabilistic<br/>Interpretable latent | O(L × latent_dim) | Standard PyTorch | Probabilistic forecasting |
| **Echo State Networks** | `pip install reservoirpy` | Fast training<br/>Good for chaotic | O(L × reservoir_size) | **Requires reservoir libraries**<br/>`pip install reservoirpy`<br/>or `pip install pyESN` | Real-time, chaotic series |

## Transformer-Based Models (5 models)

| Model | Repository/Installation | Performance Gains | Complexity | Special Installation | Best Use Case |
|-------|------------------------|-------------------|------------|---------------------|---------------|
| **Autoformer** | `git clone https://github.com/thuml/Autoformer`<br/>Also in TSLib | 38% relative improvement<br/>Auto-correlation | O(L log L) | Standard PyTorch | Periodic patterns |
| **FEDformer** | `git clone https://github.com/MAZiqing/FEDformer` | 14.8% & 22.6% reduction<br/>Frequency domain | O(L) linear | **Requires frequency libs**<br/>`pip install scipy`<br/>`pip install PyWavelets` | Long sequences |
| **Temporal Fusion Transformer** | `pip install pytorch-forecasting`<br/>`pip install pytorch-lightning` | SOTA interpretability<br/>M5 competition winner | O(L²) attention | **Requires full stack**<br/>`pip install pytorch-forecasting`<br/>`pip install pytorch-lightning`<br/>`pip install optuna` | Interpretable forecasting |
| **Crossformer** | `git clone https://github.com/Thinklab-SJTU/Crossformer` | Superior multivariate<br/>Cross-dimension modeling | O(L² + D²) | Standard PyTorch | Multivariate relationships |
| **Informer** | `git clone https://github.com/zhouhaoyi/Informer2020` | AAAI 2021 Best Paper<br/>ProbSparse attention | O(L log L) | Standard PyTorch | Long-term forecasting |

## TensorFlow-Based Models (3 models)

| Model | Repository/Installation | Performance Gains | Complexity | Special Installation | Best Use Case |
|-------|------------------------|-------------------|------------|---------------------|---------------|
| **N-BEATS** | `pip install darts`<br/>TensorFlow official | M4 competition strong<br/>Interpretable blocks | O(L × blocks) | **Multi-framework support**<br/>`pip install darts[torch]`<br/>or TensorFlow implementation | Interpretable forecasting |
| **WaveNet** | TensorFlow official<br/>`pip install tensorflow` | Strong sequential<br/>Dilated convolutions | O(L) with dilations | Standard TensorFlow | Audio-like temporal patterns |
| **DeepAR** | `pip install gluonts[torch]`<br/>AWS SageMaker | Production-proven<br/>Handles thousands of series | O(L × series_count) | **Requires GluonTS**<br/>`pip install gluonts[torch]`<br/>or `pip install gluonts[mx]` | Multiple related series |

## Comprehensive Libraries & Frameworks

| Library | Installation | Models Included | Special Requirements |
|---------|-------------|-----------------|---------------------|
| **TSLib (Time-Series-Library)** | `git clone https://github.com/thuml/Time-Series-Library` | 24+ models: TimeMixer, iTransformer, PatchTST, Autoformer, Informer, etc. | Standard PyTorch |
| **PyTorch Forecasting** | `pip install pytorch-forecasting` | TFT, DeepAR, N-HiTS, NBeats variants | `pip install pytorch-lightning optuna` |
| **GluonTS** | `pip install gluonts[torch]` | 15+ models: DeepAR, WaveNet, Transformer variants | Choose backend: `[torch]` or `[mx]` |
| **Darts** | `pip install darts[torch]` | 40+ models across frameworks | `pip install darts[all]` for full features |

## Installation Instructions for Complex Dependencies

### For Graph Neural Network Models (MTGNN, FourierGNN, StemGNN)

```bash
# PyTorch Geometric installation (choose based on your CUDA version)
pip install torch-geometric
# OR for specific CUDA version:
pip install pyg-lib torch-scatter torch-sparse torch-cluster torch-spline-conv torch-geometric -f https://data.pyg.org/whl/torch-2.1.0+cu118.html

# Additional graph dependencies
pip install networkx scipy
```

### For State Space Models (Mamba4Cast, Time-SSM)

```bash
# Mamba dependencies
pip install causal-conv1d>=1.0.0
pip install mamba-ssm

# Alternative state space implementations
pip install s4-pytorch  # For S4 models
```

### For Diffusion Models (TimeGrad, CSDI)

```bash
# Diffusion libraries
pip install diffusers
pip install pytorch-lightning
pip install hydra-core  # For configuration management

# Optional: For advanced diffusion implementations
pip install accelerate transformers
```

### For Neural ODE Models

```bash
# ODE solvers
pip install torchdiffeq
pip install scipy

# Alternative Julia-based (more advanced)
# Requires Julia installation first
pip install diffeqpy
# Then in Julia: using Pkg; Pkg.add("DifferentialEquations")
```

### For Frequency Domain Models (FEDformer, spectral methods)

```bash
# Frequency analysis libraries
pip install scipy
pip install PyWavelets
pip install librosa  # For advanced spectral analysis
```

### For Production Deployment

```bash
# Full production stack
pip install pytorch-forecasting pytorch-lightning
pip install optuna  # Hyperparameter optimization
pip install wandb   # Experiment tracking
pip install mlflow  # Model versioning

# For serving
pip install fastapi uvicorn
pip install onnx onnxruntime  # Model optimization
```

## Quick Start for Your Chocolate Tempering System

### Option 1: TSLib (Recommended - Most Models)
```bash
git clone https://github.com/thuml/Time-Series-Library
cd Time-Series-Library
pip install -r requirements.txt

# Test with your data
python run.py --task_name long_term_forecast --is_training 1 --root_path ./dataset/your_data/ --data_path tempering_data.csv --model_id your_test --model TimeMixer --data custom --features M --seq_len 96 --label_len 48 --pred_len 96 --e_layers 2 --d_layers 1 --factor 3 --enc_in 7 --dec_in 7 --c_out 7 --des 'Exp' --itr 1
```

### Option 2: Individual High-Performance Models
```bash
# iTransformer (best for multivariate)
git clone https://github.com/thuml/iTransformer
cd iTransformer
pip install -r requirements.txt

# Mamba4Cast (best efficiency)
git clone https://github.com/automl/Mamba4Cast
cd Mamba4Cast
pip install -e .
pip install mamba-ssm causal-conv1d
```

### Option 3: Production-Ready Framework
```bash
pip install pytorch-forecasting pytorch-lightning
# Use TFT or NBeats for interpretable production forecasting
```

## Performance Summary for Chocolate Tempering Application

| Priority | Model | Why Choose | Installation Complexity |
|----------|-------|------------|-------------------------|
| **High** | TimeMixer | Best overall performance, linear complexity | Low (TSLib) |
| **High** | iTransformer | Superior multivariate handling | Low (TSLib) |
| **High** | PatchTST | Memory efficient for long sequences | Low |
| **Medium** | Mamba4Cast | Zero-shot capabilities, ultra-efficient | Medium (mamba-ssm) |
| **Medium** | TFT | Production-ready with interpretability | Medium (full stack) |
| **Low** | MTGNN | If complex temperature relationships | High (PyG) |

Choose based on your priorities: TimeMixer/iTransformer for immediate performance gains with easy installation, Mamba4Cast for cutting-edge efficiency, or TFT for production deployment with interpretability.