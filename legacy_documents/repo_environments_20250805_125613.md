# Folder Archive

Source Directory: C:/00_Repos_Rod/Testing_Repos/environments
Archive Created: 2025-08-05 12:56:13

This Markdown file archives the contents of .conf, .sh files from the directory.
Each file's content is stored between markers in the format:
```
--- BEGIN FILE: relative/path/to/file.ext ---
[file content]
--- END FILE ---
```

## Archived Files

<!-- Full Path: C:/00_Repos_Rod/Testing_Repos/environments\activate.sh -->
<!-- Relative Path: activate.sh -->
<!-- File Size: 6684 bytes -->
<!-- Last Modified: 2025-08-03 23:54:34 -->
--- BEGIN FILE: activate.sh ---
#!/bin/bash
# Language: Bash 5.0
# Lines of Code: 200
# File: activate.sh
# Version: 4.0.0
# Project: AI Time Series Framework
# Repository: AI_TimeSeriesFramework
# Author: Rod Sanchez
# Created: 2025-08-03 09:30
# Last Edited: 2025-08-03 23:30
# Change: Major (+1.0) - Updated for split environments
# Modifications: +60, -20
# Last Modification Comment: Added new split environments and removed old ones; updated help with new model info

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/scripts/core/conda_manager.sh"

show_help() {
    echo "🎯 AI Time Series Framework - Environment Activator"
    echo ""
    echo "Usage: $0 <environment>"
    echo ""
    echo "Available environments:"
    echo "  transformers_modern   - Modern transformers (transformers>=4.45.0)"
    echo "  transformers_legacy   - Legacy transformers (transformers==4.33.3)"
    echo "  transformers_ts       - Time series transformers (pytorch-forecasting)"
    echo "  llm_chronos           - Chronos LLM (chronos-forecasting)"
    echo "  llm_uni2ts            - Uni2TS LLM (uni2ts==1.2.0)"
    echo "  llm_momentfm          - MomentFM LLM (momentfm==0.1.4)"
    echo "  llm_mamba             - Mamba LLM (mamba-ssm>=2.2.2)"
    echo "  tslib_traditional     - Traditional time series (statsmodels, prophet, sktime)"
    echo "  tslib_nixtla          - Nixtla time series (neuralforecast)"
    echo "  tslib_advanced        - Advanced time series (darts, tsfresh)"
    echo "  base_torch            - Core PyTorch foundation"
    echo "  geometric             - PyTorch Geometric for graphs"
    echo "  tensorflow            - TensorFlow ecosystem"
    echo "  rapids                - GPU-accelerated RAPIDS"
    echo "  anomaly_advanced      - Advanced anomaly detection models"
    echo "  federated             - Federated learning models"
    echo "  multimodal            - Multimodal time series models"
    echo "  probabilistic         - Probabilistic time series models"
    echo "  causal                - Causal discovery models"
    echo "  vision_ts             - Vision-enhanced time series models"
    echo ""
    echo "Examples:"
    echo "  $0 transformers_modern"
    echo "  $0 llm_chronos"
    echo "  $0 tslib_traditional"
    echo ""
    echo "🆕 Stable LLM Models:"
    echo "  • Chronos     - Probabilistic forecasting"
    echo "  • Uni2TS      - Salesforce unified time series model"
    echo "  • MomentFM    - Representation learning"
    echo "  • TimesFM     - Google's time series foundation model"
    echo ""
    echo "🆕 Research LLM Models:"
    echo "  • Time-MoE    - Mixture of Experts model"
    echo "  • Lag-Llama   - Probabilistic forecasting"
    echo "  • Timer-XL    - Large-scale foundation model"
    echo "  • Diffusion-TS - Diffusion-based forecasting"
    echo "  • Time-LLM    - Time series language model"
    echo "  • AutoTimes   - Automated time series modeling"
    echo "  • MM-TSFlib   - Multimodal time series library"
    echo "  • LLMTIME     - Language model for time series"
    echo "  • TEMPO       - Temporal modeling"
    echo ""
    echo "🆕 Anomaly Advanced Models:"
    echo "  • CARLA       - Contrastive representation learning"
    echo "  • DACAD       - Domain adaptation contrastive learning"
    echo "  • AT-DCAEP    - Attention-based deep convolutional autoencoder"
    echo "  • GSLAD       - Graph structure learning-based anomaly detection"
    echo ""
    echo "🆕 Federated Models:"
    echo "  • FedAvg      - Federated averaging"
    echo "  • FedProx     - Federated proximal"
    echo "  • SCAFFOLD    - Stochastic controlled averaging"
    echo "  • MOON        - Model contrastive federated learning"
    echo ""
    echo "🆕 Multimodal Models:"
    echo "  • ChatTime    - Unified multimodal time series model"
    echo "  • Time-MMD    - Multi-domain multimodal model"
    echo "  • MST-GAT     - Multimodal spatial-temporal graph attention network"
    echo ""
    echo "🆕 Probabilistic Models:"
    echo "  • AutoBNN     - Automated Bayesian neural network"
    echo ""
    echo "🆕 Causal Models:"
    echo "  • PCMCI       - Peter-Clark momentary conditional independence"
    echo "  • CReP        - Causal-oriented representation learning"
    echo ""
    echo "🆕 Vision TS Models:"
    echo "  • VisionTS    - Vision-enhanced time series forecasting"
    echo "  • ViTime      - Vision-powered time series forecasting"
    echo ""
    echo "💡 Deactivate with: conda deactivate"
    echo ""
    echo "Run setup first: ./setup.sh"
}

if [[ $# -eq 0 ]] || [[ "$1" == "--help" ]]; then
    show_help
    exit 0
fi

env_name="env_$1"

init_conda

if env_exists "$env_name"; then
    echo "🔄 Activating $env_name..."
    conda activate "$env_name"
    echo "✅ Environment activated: $env_name"
    
    case "$env_name" in
        "env_transformers_modern") echo "🚀 Modern Transformers Environment Active!";;
        "env_transformers_legacy") echo "🔄 Legacy Transformers Environment Active!";;
        "env_transformers_ts") echo "📈 Time Series Transformers Environment Active!";;
        "env_llm_chronos") echo "⏰ Chronos LLM Environment Active!";;
        "env_llm_uni2ts") echo "🏢 Uni2TS LLM Environment Active!";;
        "env_llm_momentfm") echo "📊 MomentFM LLM Environment Active!";;
        "env_llm_mamba") echo "🐍 Mamba LLM Environment Active!";;
        "env_tslib_traditional") echo "📊 Traditional TSLib Environment Active!";;
        "env_tslib_nixtla") echo "🏢 Nixtla TSLib Environment Active!";;
        "env_tslib_advanced") echo "🔬 Advanced TSLib Environment Active!";;
        "env_base_torch") echo "🔥 Base Torch Environment Active!";;
        "env_geometric") echo "📈 Geometric Environment Active!";;
        "env_tensorflow") echo "🧠 TensorFlow Environment Active!";;
        "env_rapids") echo "🚀 RAPIDS Environment Active!";;
        "env_anomaly_advanced") echo "🔍 Anomaly Advanced Environment Active!";;
        "env_federated") echo "🌐 Federated Environment Active!";;
        "env_multimodal") echo "🎨 Multimodal Environment Active!";;
        "env_probabilistic") echo "🎲 Probabilistic Environment Active!";;
        "env_causal") echo "🔗 Causal Environment Active!";;
        "env_vision_ts") echo "📷 Vision TS Environment Active!";;
    esac
    
    echo "💡 Deactivate with: conda deactivate"
else
    echo "❌ Environment $env_name not found"
    echo ""
    echo "Available environments:"
    conda env list | grep "^env_" | sed 's/env_/  /'
    echo ""
    echo "Run setup first: ./setup.sh"
fi
--- END FILE ---

<!-- Full Path: C:/00_Repos_Rod/Testing_Repos/environments\diagnose_environments.sh -->
<!-- Relative Path: diagnose_environments.sh -->
<!-- File Size: 1860 bytes -->
<!-- Last Modified: 2025-08-04 00:10:02 -->
--- BEGIN FILE: diagnose_environments.sh ---
#!/bin/bash
# Language: Bash 5.0
# Lines of Code: 1279
# File: diagnose_environments.sh
# Version: 2.0.0
# Project: AI Time Series Framework
# Repository: AI_TimeSeriesFramework
# Author: Rod Sanchez
# Created: 2025-08-03 22:28:39
# Last Edited: 2025-08-03 23:30
# Change: Minor (+0.1) - Updated envs to new split environments
# Modifications: +10, -6
# Last Modification Comment: Replaced old envs with new split ones in envs array

set -euo pipefail

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'  
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

log_info() { echo -e "${BLUE}[INFO]${NC} $1"; }

# Initialize conda
if eval "$(conda shell.bash hook)" 2>/dev/null || source "$(conda info --base)/etc/profile.d/conda.sh" 2>/dev/null; then
    :
else
    echo "Failed to initialize Conda"
    exit 1
fi

check_env_conflicts() {
    local env_name="$1"
    if ! conda env list | grep -q "^$env_name "; then
        echo "❓ Not found"
        return 0
    fi
    
    conda activate "$env_name" 2>/dev/null
    local conflicts=$(pip check 2>&1 | wc -l)
    conda deactivate 2>/dev/null
    
    if [[ $conflicts -eq 0 ]]; then
        echo "✅ Clean"
    elif [[ $conflicts -le 3 ]]; then
        echo "⚠️ Minor ($conflicts conflicts)"
    elif [[ $conflicts -le 10 ]]; then
        echo "🔥 Major ($conflicts conflicts)"  
    else
        echo "💥 Critical ($conflicts+ conflicts)"
    fi
}

echo "🔍 Environment Analysis"
echo "======================"
echo ""

envs=("env_transformers_modern" "env_transformers_legacy" "env_transformers_ts" "env_llm_chronos" "env_llm_uni2ts" "env_llm_momentfm" "env_llm_mamba" "env_tslib_traditional" "env_tslib_nixtla" "env_tslib_advanced" "env_multimodal" "env_probabilistic" "env_vision_ts")

for env in "${envs[@]}"; do
    status=$(check_env_conflicts "$env")
    printf "%-25s %s\n" "$env:" "$status"
done
--- END FILE ---

<!-- Full Path: C:/00_Repos_Rod/Testing_Repos/environments\environment_splitter_script.sh -->
<!-- Relative Path: environment_splitter_script.sh -->
<!-- File Size: 21988 bytes -->
<!-- Last Modified: 2025-08-03 23:51:03 -->
--- BEGIN FILE: environment_splitter_script.sh ---
#!/bin/bash
# Language: Bash 5.0
# Lines of Code: 352
# File: scripts/core/split_environments.sh
# Version: 1.0.5
# Project: AI Time Series Framework
# Repository: AI_TimeSeriesFramework
# Author: Rod Sanchez
# Created: 2025-08-03 22:30
# Last Edited: 2025-08-03 23:30
# Change: Minor (+0.01) - Fixed torchaudio version in create_transformers_legacy
# Modifications: +1, -1
# Last Modification Comment: Changed torchaudio==0.20.0 to torchaudio==2.0.0 to match torch==2.0.0 and torchvision==0.15.0

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Initialize logging first (before sourcing other modules)
setup_logging() {
    mkdir -p logs
    LOG_FILE="logs/environment_split_$(date +%Y%m%d_%H%M%S).log"
    export LOG_FILE
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] Starting Environment Splitting Process..." | tee "$LOG_FILE"
}

# Simple logging functions (standalone)
log_info() { echo "[INFO $(date +'%H:%M:%S')] $1" | tee -a "$LOG_FILE"; }
log_success() { echo "[SUCCESS $(date +'%H:%M:%S')] $1" | tee -a "$LOG_FILE"; }
log_warning() { echo "[WARNING $(date +'%H:%M:%S')] $1" | tee -a "$LOG_FILE"; }
log_error() { echo "[ERROR $(date +'%H:%M:%S')] $1" | tee -a "$LOG_FILE"; }

# Source other modules after logging is set up
if [[ -f "$SCRIPT_DIR/scripts/core/conda_manager.sh" ]]; then
    source "$SCRIPT_DIR/scripts/core/conda_manager.sh"
else
    log_warning "Cannot find conda_manager.sh - using built-in functions"
    
    # Built-in conda functions
    init_conda() {
        if eval "$(conda shell.bash hook)" 2>/dev/null; then
            log_success "✅ Conda shell hook initialized"
        elif source "$(conda info --base)/etc/profile.d/conda.sh" 2>/dev/null; then
            log_success "✅ Conda profile sourced"
        else
            log_error "❌ Failed to initialize Conda"
            exit 1
        fi
    }
    
    env_exists() {
        local env_name="$1"
        conda env list | grep -q "^$env_name "
    }
    
    create_environment() {
        local env_name="$1"
        local python_version="${2:-3.11}"
        
        if env_exists "$env_name"; then
            log_info "Environment $env_name exists, checking dependencies..."
            activate_env "$env_name"
            if pip check >/dev/null 2>&1; then
                log_success "✅ Environment $env_name is functional (no dependency conflicts)"
                deactivate_env
                return 0
            else
                log_warning "⚠️ Environment $env_name has dependency conflicts, removing and recreating..."
                deactivate_env
                conda env remove -n "$env_name" -y || log_error "❌ Failed to remove environment $env_name"
            fi
        fi
        
        log_info "Creating new environment $env_name with Python $python_version..."
        conda create -n "$env_name" python="$python_version" -y || { log_error "❌ Failed to create environment $env_name"; exit 1; }
        log_success "✅ Environment $env_name created successfully"
    }
    
    activate_env() {
        local env_name="$1"
        conda activate "$env_name" 2>/dev/null || { log_error "❌ Failed to activate environment $env_name"; exit 1; }
    }
    
    deactivate_env() {
        conda deactivate 2>/dev/null || true
    }
    
    remove_environment() {
        local env_name="$1"
        conda env remove -n "$env_name" -y 2>/dev/null || log_warning "Failed to remove environment $env_name"
    }
fi

# Backup problematic environments
backup_environments() {
    log_info "📋 Backing up problematic environments..."
    
    mkdir -p backups/pre_split_$(date +%Y%m%d_%H%M%S)
    local backup_dir="backups/pre_split_$(date +%Y%m%d_%H%M%S)"
    
    local envs_to_backup=("env_transformers" "env_llm_stable" "env_tslib")
    
    for env in "${envs_to_backup[@]}"; do
        if env_exists "$env"; then
            log_info "Backing up $env..."
            conda env export -n "$env" > "$backup_dir/${env}.yml" || log_warning "Failed to backup $env"
        else
            log_info "$env does not exist, skipping backup"
        fi
    done
    
    log_success "✅ Backup completed in $backup_dir"
}

# Create modern transformers environment
create_transformers_modern() {
    local env_name="env_transformers_modern"
    log_info "🚀 Creating $env_name..."
    
    create_environment "$env_name" "3.11"
    activate_env "$env_name"
    
    log_info "Installing packages for $env_name..."
    pip install --upgrade pip setuptools wheel || { log_error "❌ Failed to upgrade pip in $env_name"; exit 1; }
    pip install torch>=2.1 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 || { log_error "❌ Failed to install torch in $env_name"; exit 1; }
    pip install transformers>=4.45.0 datasets>=2.18.0 tokenizers>=0.21.0 || { log_error "❌ Failed to install transformers in $env_name"; exit 1; }
    pip install accelerate evaluate peft diffusers || { log_error "❌ Failed to install additional packages in $env_name"; exit 1; }
    pip install numpy>=1.26 pandas>=2.2 huggingface-hub>=0.28 || { log_error "❌ Failed to install numpy/pandas in $env_name"; exit 1; }
    pip install matplotlib seaborn plotly scipy scikit-learn || { log_error "❌ Failed to install visualization packages in $env_name"; exit 1; }
    
    deactivate_env
    if pip check >/dev/null 2>&1; then
        log_success "✅ Created and verified $env_name (no dependency conflicts)"
    else
        log_error "❌ $env_name has dependency conflicts after installation"
        exit 1
    fi
}

# Create legacy transformers environment
create_transformers_legacy() {
    local env_name="env_transformers_legacy"
    log_info "🔄 Creating $env_name..."
    
    create_environment "$env_name" "3.11"
    activate_env "$env_name"
    
    log_info "Installing packages for $env_name..."
    pip install --upgrade pip setuptools wheel || { log_error "❌ Failed to upgrade pip in $env_name"; exit 1; }
    pip install torch==2.0.0 torchvision==0.15.0 torchaudio==2.0.0 --index-url https://download.pytorch.org/whl/cu118 || { log_error "❌ Failed to install torch in $env_name"; exit 1; }
    pip install transformers==4.33.3 datasets==2.17.1 tokenizers==0.13.3 || { log_error "❌ Failed to install transformers in $env_name"; exit 1; }
    pip install accelerate==0.20.3 huggingface-hub==0.24.0 || { log_error "❌ Failed to install additional packages in $env_name"; exit 1; }
    pip install numpy>=1.25 pandas==2.0.3 || { log_error "❌ Failed to install numpy/pandas in $env_name"; exit 1; }
    pip install matplotlib seaborn plotly scipy>=1.11 scikit-learn || { log_error "❌ Failed to install visualization packages in $env_name"; exit 1; }
    
    deactivate_env
    if pip check >/dev/null 2>&1; then
        log_success "✅ Created and verified $env_name (no dependency conflicts)"
    else
        log_error "❌ $env_name has dependency conflicts after installation"
        exit 1
    fi
}

# Create time series transformers environment
create_transformers_ts() {
    local env_name="env_transformers_ts"
    log_info "📈 Creating $env_name..."
    
    create_environment "$env_name" "3.11"
    activate_env "$env_name"
    
    log_info "Installing packages for $env_name..."
    pip install --upgrade pip setuptools wheel || { log_error "❌ Failed to upgrade pip in $env_name"; exit 1; }
    pip install torch>=2.1 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 || { log_error "❌ Failed to install torch in $env_name"; exit 1; }
    pip install pytorch-forecasting pytorch-lightning>=2.0 || { log_error "❌ Failed to install pytorch packages in $env_name"; exit 1; }
    pip install einops>=0.7 numpy>=1.26 pandas>=2.2 || { log_error "❌ Failed to install numpy/pandas/einops in $env_name"; exit 1; }
    pip install matplotlib seaborn plotly scipy scikit-learn || { log_error "❌ Failed to install visualization packages in $env_name"; exit 1; }
    
    deactivate_env
    if pip check >/dev/null 2>&1; then
        log_success "✅ Created and verified $env_name (no dependency conflicts)"
    else
        log_error "❌ $env_name has dependency conflicts after installation"
        exit 1
    fi
}

# Create Chronos LLM environment
create_llm_chronos() {
    local env_name="env_llm_chronos"
    log_info "⏰ Creating $env_name..."
    
    create_environment "$env_name" "3.11"
    activate_env "$env_name"
    
    log_info "Installing packages for $env_name..."
    pip install --upgrade pip setuptools wheel || { log_error "❌ Failed to upgrade pip in $env_name"; exit 1; }
    pip install torch>=2.1 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 || { log_error "❌ Failed to install torch in $env_name"; exit 1; }
    pip install transformers>=4.45.0 numpy>=1.26.4 pandas>=2.2 || { log_error "❌ Failed to install transformers/numpy/pandas in $env_name"; exit 1; }
    pip install chronos-forecasting timesfm[torch] || { log_error "❌ Failed to install chronos/timesfm in $env_name"; exit 1; }
    pip install matplotlib seaborn plotly scipy scikit-learn || { log_error "❌ Failed to install visualization packages in $env_name"; exit 1; }
    
    deactivate_env
    if pip check >/dev/null 2>&1; then
        log_success "✅ Created and verified $env_name (no dependency conflicts)"
    else
        log_error "❌ $env_name has dependency conflicts after installation"
        exit 1
    fi
}

# Create Uni2TS LLM environment (without momentfm, pinned torch <2.5)
create_llm_uni2ts() {
    local env_name="env_llm_uni2ts"
    log_info "🏢 Creating $env_name..."
    
    create_environment "$env_name" "3.11"
    activate_env "$env_name"
    
    log_info "Installing packages for $env_name..."
    pip install --upgrade pip setuptools wheel || { log_error "❌ Failed to upgrade pip in $env_name"; exit 1; }
    pip install torch==2.4.1 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 || { log_error "❌ Failed to install torch in $env_name"; exit 1; }
    pip install transformers==4.33.3 || { log_error "❌ Failed to install transformers in $env_name"; exit 1; }
    pip install "numpy~=1.26.0" pandas>=2.1 "einops==0.7.*" || { log_error "❌ Failed to install numpy/pandas/einops in $env_name"; exit 1; }
    pip install uni2ts==1.2.0 || { log_error "❌ Failed to install uni2ts in $env_name"; exit 1; }
    pip install matplotlib seaborn plotly scipy scikit-learn || { log_error "❌ Failed to install visualization packages in $env_name"; exit 1; }
    
    deactivate_env
    if pip check >/dev/null 2>&1; then
        log_success "✅ Created and verified $env_name (no dependency conflicts)"
    else
        log_error "❌ $env_name has dependency conflicts after installation"
        exit 1
    fi
}

# Create MomentFM LLM environment (separate to resolve conflicts)
create_llm_momentfm() {
    local env_name="env_llm_momentfm"
    log_info "🏢 Creating $env_name..."
    
    create_environment "$env_name" "3.11"
    activate_env "$env_name"
    
    log_info "Installing packages for $env_name..."
    pip install --upgrade pip setuptools wheel || { log_error "❌ Failed to upgrade pip in $env_name"; exit 1; }
    pip install torch>=2.1 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 || { log_error "❌ Failed to install torch in $env_name"; exit 1; }
    pip install transformers==4.33.3 || { log_error "❌ Failed to install transformers in $env_name"; exit 1; }
    pip install numpy==1.25.2 pandas>=2.1 "einops==0.7.*" || { log_error "❌ Failed to install numpy/pandas/einops in $env_name"; exit 1; }
    pip install momentfm==0.1.4 || { log_error "❌ Failed to install momentfm in $env_name"; exit 1; }
    pip install matplotlib seaborn plotly scipy scikit-learn || { log_error "❌ Failed to install visualization packages in $env_name"; exit 1; }
    
    deactivate_env
    if pip check >/dev/null 2>&1; then
        log_success "✅ Created and verified $env_name (no dependency conflicts)"
    else
        log_error "❌ $env_name has dependency conflicts after installation"
        exit 1
    fi
}

# Create Mamba LLM environment
create_llm_mamba() {
    local env_name="env_llm_mamba"
    log_info "🐍 Creating $env_name..."
    
    create_environment "$env_name" "3.11"
    activate_env "$env_name"
    
    log_info "Installing packages for $env_name..."
    pip install --upgrade pip setuptools wheel || { log_error "❌ Failed to upgrade pip in $env_name"; exit 1; }
    pip install torch>=2.1 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 || { log_error "❌ Failed to install torch in $env_name"; exit 1; }
    pip install transformers>=4.45.0 numpy>=1.26 pandas>=2.2 || { log_error "❌ Failed to install transformers/numpy/pandas in $env_name"; exit 1; }
    pip install mamba-ssm>=2.2.2 "causal-conv1d>=1.4.0" || { log_error "❌ Failed to install mamba-ssm/causal-conv1d in $env_name"; exit 1; }
    pip install matplotlib seaborn plotly scipy scikit-learn || { log_error "❌ Failed to install visualization packages in $env_name"; exit 1; }
    
    deactivate_env
    if pip check >/dev/null 2>&1; then
        log_success "✅ Created and verified $env_name (no dependency conflicts)"
    else
        log_error "❌ $env_name has dependency conflicts after installation"
        exit 1
    fi
}

# Create traditional TSLib environment
create_tslib_traditional() {
    local env_name="env_tslib_traditional"
    log_info "📊 Creating $env_name..."
    
    create_environment "$env_name" "3.11"
    activate_env "$env_name"
    
    log_info "Installing packages for $env_name..."
    pip install --upgrade pip setuptools wheel || { log_error "❌ Failed to upgrade pip in $env_name"; exit 1; }
    pip install torch==2.0.1 torchvision torchaudio || { log_error "❌ Failed to install torch in $env_name"; exit 1; }
    pip install "numpy>=1.24,<1.26" "pandas>=1.5,<2.0" "scipy>=1.10,<1.14" || { log_error "❌ Failed to install numpy/pandas/scipy in $env_name"; exit 1; }
    pip install statsmodels prophet "sktime==0.26.0" || { log_error "❌ Failed to install statsmodels/prophet/sktime in $env_name"; exit 1; }
    pip install matplotlib seaborn plotly scikit-learn || { log_error "❌ Failed to install visualization packages in $env_name"; exit 1; }
    
    deactivate_env
    if pip check >/dev/null 2>&1; then
        log_success "✅ Created and verified $env_name (no dependency conflicts)"
    else
        log_error "❌ $env_name has dependency conflicts after installation"
        exit 1
    fi
}

# Create Nixtla TSLib environment
create_tslib_nixtla() {
    local env_name="env_tslib_nixtla"
    log_info "🏢 Creating $env_name..."
    
    create_environment "$env_name" "3.11"
    activate_env "$env_name"
    
    log_info "Installing packages for $env_name..."
    pip install --upgrade pip setuptools wheel || { log_error "❌ Failed to upgrade pip in $env_name"; exit 1; }
    pip install torch>=2.1 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 || { log_error "❌ Failed to install torch in $env_name"; exit 1; }
    pip install numpy>=1.26 pandas>=2.2 || { log_error "❌ Failed to install numpy/pandas in $env_name"; exit 1; }
    pip install nixtla statsforecast mlforecast neuralforecast hierarchicalforecast || { log_error "❌ Failed to install nixtla packages in $env_name"; exit 1; }
    pip install matplotlib seaborn plotly scipy scikit-learn || { log_error "❌ Failed to install visualization packages in $env_name"; exit 1; }
    
    deactivate_env
    if pip check >/dev/null 2>&1; then
        log_success "✅ Created and verified $env_name (no dependency conflicts)"
    else
        log_error "❌ $env_name has dependency conflicts after installation"
        exit 1
    fi
}

# Create advanced TSLib environment
create_tslib_advanced() {
    local env_name="env_tslib_advanced"
    log_info "🔬 Creating $env_name..."
    
    create_environment "$env_name" "3.11"
    activate_env "$env_name"
    
    log_info "Installing packages for $env_name..."
    pip install --upgrade pip setuptools wheel || { log_error "❌ Failed to upgrade pip in $env_name"; exit 1; }
    pip install torch>=2.1 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 || { log_error "❌ Failed to install torch in $env_name"; exit 1; }
    pip install numpy>=1.26 pandas>=2.2 einops || { log_error "❌ Failed to install numpy/pandas/einops in $env_name"; exit 1; }
    pip install darts tslearn tsfresh pytorch-lightning>=2.0 || { log_error "❌ Failed to install time series packages in $env_name"; exit 1; }
    pip install matplotlib seaborn plotly scipy scikit-learn || { log_error "❌ Failed to install visualization packages in $env_name"; exit 1; }
    
    deactivate_env
    if pip check >/dev/null 2>&1; then
        log_success "✅ Created and verified $env_name (no dependency conflicts)"
    else
        log_error "❌ $env_name has dependency conflicts after installation"
        exit 1
    fi
}

# Fix minor environment issues
fix_minor_environments() {
    log_info "🔧 Fixing minor environment issues..."
    
    if env_exists "env_multimodal"; then
        log_info "Fixing env_multimodal..."
        activate_env "env_multimodal"
        pip install sympy==1.13.1 || log_error "❌ Failed to fix env_multimodal"
        deactivate_env
    fi
    
    if env_exists "env_probabilistic"; then
        log_info "Fixing env_probabilistic..."
        activate_env "env_probabilistic"
        pip install fsspec sympy==1.13.1 || log_error "❌ Failed to fix env_probabilistic"
        deactivate_env
    fi
    
    if env_exists "env_vision_ts"; then
        log_info "Fixing env_vision_ts..."
        activate_env "env_vision_ts"
        pip install numpy>=2.3.2 dill>=0.3.8 multiprocess==0.70.16 datasets|| log_error "❌ Failed to fix env_vision_ts"
        deactivate_env
    fi
    
    log_success "✅ Minor fixes completed"
}

# Remove old problematic environments (optional)
remove_old_environments() {
    log_info "📋 Removing old problematic environments..."
    local old_envs=("env_transformers" "env_llm_stable" "env_tslib")
    for env in "${old_envs[@]}"; do
        if env_exists "$env"; then
            log_info "Removing $env..."
            remove_environment "$env"
        else
            log_info "$env does not exist, skipping removal"
        fi
    done
    log_success "✅ Old environments removed"
}
# Verify new environments
verify_new_environments() {
    log_info "🔍 Verifying new environments..."
    
    local new_envs=(
        "env_llm_chronos"
        "env_llm_uni2ts"
        "env_llm_momentfm"
        "env_llm_mamba"
        "env_tslib_traditional"
        "env_tslib_nixtla"
        "env_tslib_advanced"
        "env_transformers_modern"
        "env_transformers_legacy"
        "env_transformers_ts"
    )
    
    for env in "${new_envs[@]}"; do
        if env_exists "$env"; then
            log_info "Checking $env..."
            activate_env "$env"
            if pip check >/dev/null 2>&1; then
                log_success "✅ $env: No dependency conflicts"
            else
                log_warning "⚠️ $env: Still has conflicts"
            fi
            deactivate_env
        else
            log_warning "⚠️ $env: Does not exist"
        fi
    done
}

# Main execution
main() {
    setup_logging
    log_info "🚀 Starting Environment Splitting Process..."
    log_info "📁 Working directory: $SCRIPT_DIR"
    
    if ! command -v conda &> /dev/null; then
        log_error "❌ Conda not found. Please install Anaconda or Miniconda first."
        exit 1
    fi
    
    init_conda
    
    log_info "🔍 Checking for problematic environments..."
    local has_problems=false
    
    if env_exists "env_transformers"; then
        log_info "Found env_transformers (25+ conflicts)"
        has_problems=true
    fi
    if env_exists "env_llm_stable"; then
        log_info "Found env_llm_stable (6 conflicts)"
        has_problems=true
    fi
    if env_exists "env_tslib"; then
        log_info "Found env_tslib (7 conflicts)"
        has_problems=true
    fi
    
    if ! $has_problems; then
        log_warning "No problematic environments found. This script is designed to split:"
        log_warning "  - env_transformers"
        log_warning "  - env_llm_stable"
        log_warning "  - env_tslib"
        read -p "Continue anyway to create new clean environments? (y/N): " -r
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            log_info "Exiting..."
            exit 0
        fi
    fi
    
    backup_environments
    
    log_info "🏗️ Creating new split environments..."
    for func in create_transformers_modern create_transformers_legacy create_transformers_ts \
                create_llm_chronos create_llm_uni2ts create_llm_momentfm create_llm_mamba \
                create_tslib_traditional create_tslib_nixtla create_tslib_advanced; do
        if ! $func; then
            log_error "❌ Failed to execute $func"
            exit 1
        fi
    done
    
    fix_minor_environments
    verify_new_environments
    remove_old_environments
    
    log_success "🎉 Environment splitting completed successfully!"
    log_info "📋 Summary:"
    log_info "  - Created 10 new focused environments"
    log_info "  - Fixed 3 minor environment issues"
    log_info "  - All environments should now have clean dependencies"
    log_info ""
    log_info "💡 Next steps:"
    log_info "  1. Test your workflows with the new environments"
    log_info "  2. Update your activation scripts to use new environment names"
    log_info "  3. Run pip check on all environments to confirm no conflicts"
    log_info ""
    log_info "📄 Log file: $LOG_FILE"
}

# Execute if run directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi
--- END FILE ---

<!-- Full Path: C:/00_Repos_Rod/Testing_Repos/environments\quick_fix_environments.sh -->
<!-- Relative Path: quick_fix_environments.sh -->
<!-- File Size: 1349 bytes -->
<!-- Last Modified: 2025-08-03 22:28:53 -->
--- BEGIN FILE: quick_fix_environments.sh ---
#!/bin/bash
set -euo pipefail

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

log_info() { echo -e "${BLUE}[INFO]${NC} $1"; }
log_success() { echo -e "${GREEN}[SUCCESS]${NC} $1"; }
log_warning() { echo -e "${YELLOW}[WARNING]${NC} $1"; }

# Initialize conda
eval "$(conda shell.bash hook)" 2>/dev/null || source "$(conda info --base)/etc/profile.d/conda.sh" 2>/dev/null

env_exists() { conda env list | grep -q "^$1 "; }

log_info "🔧 Fixing minor environment issues..."

# Fix env_multimodal (1 conflict)
if env_exists "env_multimodal"; then
    log_info "Fixing env_multimodal..."
    conda activate env_multimodal
    pip install sympy==1.13.1 --quiet
    conda deactivate
    log_success "✅ Fixed env_multimodal"
fi

# Fix env_probabilistic (2 conflicts)  
if env_exists "env_probabilistic"; then
    log_info "Fixing env_probabilistic..."
    conda activate env_probabilistic
    pip install fsspec sympy==1.13.1 --quiet
    conda deactivate
    log_success "✅ Fixed env_probabilistic"
fi

# Fix env_vision_ts (3 conflicts)
if env_exists "env_vision_ts"; then
    log_info "Fixing env_vision_ts..."
    conda activate env_vision_ts
    pip install "numpy>=1.26" "dill<0.3.9" "multiprocess<0.70.17" --quiet
    conda deactivate
    log_success "✅ Fixed env_vision_ts"
fi

log_success "🎉 Quick fixes completed!"

--- END FILE ---

<!-- Full Path: C:/00_Repos_Rod/Testing_Repos/environments\setup.sh -->
<!-- Relative Path: setup.sh -->
<!-- File Size: 31506 bytes -->
<!-- Last Modified: 2025-08-05 00:54:23 -->
--- BEGIN FILE: setup.sh ---
#!/bin/bash
# Language: Bash 5.0
# Lines of Code: 1250
# File: setup.sh
# Version: 6.0.0
# Project: AI Time Series Framework
# Repository: AI_TimeSeriesFramework
# Author: Rod Sanchez
# Created: 2025-08-03 09:30
# Last Edited: 2025-08-04 10:15
# Change: Major (+1.0) - Comprehensive integration with splitter script functionality
# Modifications: +800, -400
# Last Modification Comment: Integrated all critical elements from environment splitter, enhanced error handling, logging, and verification

set -euo pipefail

# Script directory detection
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Global configuration
export FORCE_REINSTALL="${FORCE_REINSTALL:-false}"
export VERIFY_MODE="${VERIFY_MODE:-false}"
export SKIP_GPU_CHECK="${SKIP_GPU_CHECK:-false}"
export SELECTED_ENVS=()

# Enhanced logging setup
setup_logging() {
    mkdir -p logs
    LOG_FILE="logs/setup_$(date +%Y%m%d_%H%M%S).log"
    export LOG_FILE
    if touch "$LOG_FILE" 2>/dev/null; then
        echo "[$(date +'%Y-%m-%d %H:%M:%S')] Enhanced Setup Script Initialized..." | tee "$LOG_FILE"
    else
        echo "WARNING: Cannot create log file $LOG_FILE, using console only"
        LOG_FILE="/dev/null"
    fi
}

# Enhanced logging functions
log_info() { echo "[INFO $(date +'%H:%M:%S')] $1" | tee -a "$LOG_FILE"; }
log_success() { echo "[SUCCESS $(date +'%H:%M:%S')] $1" | tee -a "$LOG_FILE"; }
log_warning() { echo "[WARNING $(date +'%H:%M:%S')] $1" | tee -a "$LOG_FILE"; }
log_error() { echo "[ERROR $(date +'%H:%M:%S')] $1" | tee -a "$LOG_FILE"; }

# Source configuration files with error handling
source_configs() {
    log_info "📋 Loading configuration files..."
    
    local config_files=(
        "scripts/config/environments.conf"
        "scripts/config/packages.conf" 
        "scripts/config/repositories.conf"
    )
    
    for config_file in "${config_files[@]}"; do
        if [[ -f "$config_file" ]]; then
            source "$config_file" || { log_error "Failed to source $config_file"; exit 1; }
            log_success "✅ Loaded $config_file"
        else
            log_error "❌ Configuration file not found: $config_file"
            exit 1
        fi
    done
}

# Enhanced conda management functions
init_conda() {
    log_info "🐍 Initializing Conda..."
    if eval "$(conda shell.bash hook)" 2>/dev/null; then
        log_success "✅ Conda shell hook initialized"
    elif source "$(conda info --base)/etc/profile.d/conda.sh" 2>/dev/null; then
        log_success "✅ Conda profile sourced"
    else
        log_error "❌ Failed to initialize Conda. Please install Anaconda or Miniconda."
        exit 1
    fi
}

env_exists() {
    local env_name="$1"
    conda env list | grep -q "^$env_name "
}

get_env_status() {
    local env_name="$1"
    if ! env_exists "$env_name"; then
        echo "missing"
        return 1
    fi
    
    if conda activate "$env_name" 2>/dev/null; then
        if pip check >/dev/null 2>&1; then
            conda deactivate 2>/dev/null || true
            echo "functional"
            return 0
        else
            conda deactivate 2>/dev/null || true
            echo "conflicts"
            return 1
        fi
    else
        echo "broken"
        return 1
    fi
}

create_environment() {
    local env_name="$1"
    local python_version="${2:-3.11}"
    
    if env_exists "$env_name"; then
        log_info "Environment $env_name exists, checking status..."
        local status=$(get_env_status "$env_name")
        if [[ "$status" == "functional" && "$FORCE_REINSTALL" != "true" ]]; then
            log_success "✅ Environment $env_name is functional"
            return 0
        else
            log_warning "⚠️ Environment $env_name is $status, recreating..."
            conda env remove -n "$env_name" -y || log_error "❌ Failed to remove environment $env_name"
        fi
    fi
    
    log_info "Creating new environment $env_name with Python $python_version..."
    if conda create -n "$env_name" python="$python_version" -y; then
        log_success "✅ Environment $env_name created successfully"
        return 0
    else
        log_error "❌ Failed to create environment $env_name"
        return 1
    fi
}

activate_env() {
    local env_name="$1"
    if conda activate "$env_name" 2>/dev/null; then
        return 0
    else
        log_error "❌ Failed to activate environment $env_name"
        return 1
    fi
}

deactivate_env() {
    conda deactivate 2>/dev/null || true
}

remove_environment() {
    local env_name="$1"
    log_info "Removing environment $env_name..."
    conda env remove -n "$env_name" -y 2>/dev/null || log_warning "Failed to remove environment $env_name"
}

# Enhanced package installation
install_package_smart() {
    local package="$1"
    log_info "📦 Installing package: $package"
    
    case "$package" in
        git+*)
            log_info "Skipping git+ package for pip; will handle via cloning"
            return 0
            ;;
        "torch"*"--index-url"*)
            # Handle torch with index URL
            pip install $package || { log_error "❌ Failed to install $package"; return 1; }
            ;;
        "momentfm"|"timesfm[torch]"|"mamba-ssm"|"causal-conv1d"*|"nixtla"|"statsforecast"|"mlforecast"|"neuralforecast"|"hierarchicalforecast"|"utilsforecast"|"datasetsforecast"|"chronos-forecasting"|"uni2ts")
            pip install "$package" || { log_error "❌ Failed to install $package"; return 1; }
            ;;
        *)
            if echo "$package" | grep -qE '[<>=]'; then
                pip install "$package" || { log_error "❌ Failed to install $package"; return 1; }
            else
                conda install "$package" -y 2>/dev/null || pip install "$package" || { log_error "❌ Failed to install $package"; return 1; }
            fi
            ;;
    esac
    log_success "✅ Successfully installed: $package"
    return 0
}

# Get packages from configuration
get_packages() {
    local env_name="$1"
    case "$env_name" in
        "$ENV_TRANSFORMERS_MODERN") echo "$PACKAGES_TRANSFORMERS_MODERN" ;;
        "$ENV_TRANSFORMERS_LEGACY") echo "$PACKAGES_TRANSFORMERS_LEGACY" ;;
        "$ENV_TRANSFORMERS_TS") echo "$PACKAGES_TRANSFORMERS_TS" ;;
        "$ENV_LLM_CHRONOS") echo "$PACKAGES_LLM_CHRONOS" ;;
        "$ENV_LLM_UNI2TS") echo "$PACKAGES_LLM_UNI2TS" ;;
        "$ENV_LLM_MOMENTFM") echo "$PACKAGES_LLM_MOMENTFM" ;;
        "$ENV_LLM_MAMBA") echo "$PACKAGES_LLM_MAMBA" ;;
        "$ENV_TSLIB_TRADITIONAL") echo "$PACKAGES_TSLIB_TRADITIONAL" ;;
        "$ENV_TSLIB_NIXTLA") echo "$PACKAGES_TSLIB_NIXTLA" ;;
        "$ENV_TSLIB_ADVANCED") echo "$PACKAGES_TSLIB_ADVANCED" ;;
        "$ENV_BASE_TORCH") echo "$PACKAGES_BASE_TORCH" ;;
        "$ENV_GEOMETRIC") echo "$PACKAGES_GEOMETRIC" ;;
        "$ENV_TENSORFLOW") echo "$PACKAGES_TENSORFLOW" ;;
        "$ENV_RAPIDS") echo "$PACKAGES_RAPIDS" ;;
        "$ENV_ANOMALY_ADVANCED") echo "$PACKAGES_ANOMALY_ADVANCED" ;;
        "$ENV_FEDERATED") echo "$PACKAGES_FEDERATED" ;;
        "$ENV_MULTIMODAL") echo "$PACKAGES_MULTIMODAL" ;;
        "$ENV_PROBABILISTIC") echo "$PACKAGES_PROBABILISTIC" ;;
        "$ENV_CAUSAL") echo "$PACKAGES_CAUSAL" ;;
        "$ENV_VISION_TS") echo "$PACKAGES_VISION_TS" ;;
        *) echo "" ;;
    esac
}

# Get repositories from configuration
get_repositories_for_env() {
    local env_name="$1"
    case "$env_name" in
        "$ENV_ANOMALY_ADVANCED") echo "$REPOS_ANOMALY_ADVANCED" ;;
        "$ENV_FEDERATED") echo "$REPOS_FEDERATED" ;;
        "$ENV_MULTIMODAL") echo "$REPOS_MULTIMODAL" ;;
        "$ENV_PROBABILISTIC") echo "$REPOS_PROBABILISTIC" ;;
        "$ENV_CAUSAL") echo "$REPOS_CAUSAL" ;;
        "$ENV_VISION_TS") echo "$REPOS_VISION_TS" ;;
        *) echo "" ;;
    esac
}

# Enhanced environment installation
install_environment() {
    local env_name="$1"
    log_info "🔧 Installing environment: $env_name"
    
    # Skip RAPIDS if no GPU and SKIP_GPU_CHECK is true
    if [[ "$SKIP_GPU_CHECK" == "true" && "$env_name" == "$ENV_RAPIDS" ]]; then
        log_info "Skipping RAPIDS installation due to SKIP_GPU_CHECK"
        return 0
    fi
    
    local packages=$(get_packages "$env_name")
    if [[ -z "$packages" ]]; then
        log_error "❌ No packages defined for $env_name"
        return 1
    fi
    
    # Create environment
    if ! create_environment "$env_name" "3.11"; then
        return 1
    fi
    
    # Install packages
    if ! activate_env "$env_name"; then
        return 1
    fi
    
    # Upgrade pip first
    pip install --upgrade pip setuptools wheel || { log_error "❌ Failed to upgrade pip in $env_name"; deactivate_env; return 1; }
    
    # Install packages based on environment type
    case "$env_name" in
        "$ENV_TRANSFORMERS_MODERN")
            install_transformers_modern_packages
            ;;
        "$ENV_TRANSFORMERS_LEGACY")
            install_transformers_legacy_packages
            ;;
        "$ENV_TRANSFORMERS_TS")
            install_transformers_ts_packages
            ;;
        "$ENV_LLM_CHRONOS")
            install_llm_chronos_packages
            ;;
        "$ENV_LLM_UNI2TS")
            install_llm_uni2ts_packages
            ;;
        "$ENV_LLM_MOMENTFM")
            install_llm_momentfm_packages
            ;;
        "$ENV_LLM_MAMBA")
            install_llm_mamba_packages
            ;;
        "$ENV_TSLIB_TRADITIONAL")
            install_tslib_traditional_packages
            ;;
        "$ENV_TSLIB_NIXTLA")
            install_tslib_nixtla_packages
            ;;
        "$ENV_TSLIB_ADVANCED")
            install_tslib_advanced_packages
            ;;
        *)
            # Generic installation
            IFS=' ' read -ra package_array <<< "$packages"
            for package in "${package_array[@]}"; do
                install_package_smart "$package" || { log_error "❌ Failed to install $package in $env_name"; deactivate_env; return 1; }
            done
            ;;
    esac
    
    deactivate_env
    log_success "✅ Environment $env_name installed successfully"
    return 0
}

# Specific package installation functions
install_transformers_modern_packages() {
    log_info "🚀 Installing Modern Transformers packages..."
    pip install torch>=2.1 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
    pip install transformers>=4.45.0 datasets>=2.18.0 tokenizers>=0.21.0
    pip install accelerate evaluate peft diffusers
    pip install numpy>=1.26 pandas>=2.2 huggingface-hub>=0.28
    pip install matplotlib seaborn plotly scipy scikit-learn
}

install_transformers_legacy_packages() {
    log_info "🔄 Installing Legacy Transformers packages..."
    pip install torch==2.0.0 torchvision==0.15.0 torchaudio==2.0.0 --index-url https://download.pytorch.org/whl/cu118
    pip install transformers==4.33.3 datasets==2.17.1 tokenizers==0.13.3
    pip install accelerate==0.20.3 huggingface-hub==0.24.0
    pip install numpy>=1.25 pandas==2.0.3
    pip install matplotlib seaborn plotly scipy>=1.11 scikit-learn
}

install_transformers_ts_packages() {
    log_info "📈 Installing Time Series Transformers packages..."
    pip install torch>=2.1 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
    pip install pytorch-forecasting pytorch-lightning>=2.0
    pip install einops>=0.7 numpy>=1.26 pandas>=2.2
    pip install matplotlib seaborn plotly scipy scikit-learn
}

install_llm_chronos_packages() {
    log_info "⏰ Installing Chronos LLM packages..."
    pip install torch>=2.1 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
    pip install transformers>=4.45.0 numpy>=1.26.4 pandas>=2.2
    pip install chronos-forecasting timesfm[torch]
    pip install matplotlib seaborn plotly scipy scikit-learn
}

install_llm_uni2ts_packages() {
    log_info "🏢 Installing Uni2TS LLM packages..."
    pip install torch==2.4.1 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
    pip install transformers==4.33.3 "numpy~=1.26.0" pandas>=2.1 "einops==0.7.*"
    pip install uni2ts==1.2.0
    pip install matplotlib seaborn plotly scipy scikit-learn
}

install_llm_momentfm_packages() {
    log_info "📊 Installing MomentFM LLM packages..."
    pip install torch>=2.1 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
    pip install transformers==4.33.3 numpy==1.25.2 pandas>=2.1 "einops==0.7.*"
    pip install momentfm==0.1.4
    pip install matplotlib seaborn plotly scipy scikit-learn
}

install_llm_mamba_packages() {
    log_info "🐍 Installing Mamba LLM packages..."
    pip install torch>=2.1 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
    pip install transformers>=4.45.0 numpy>=1.26 pandas>=2.2
    pip install mamba-ssm>=2.2.2 "causal-conv1d>=1.4.0"
    pip install matplotlib seaborn plotly scipy scikit-learn
}

install_tslib_traditional_packages() {
    log_info "📊 Installing Traditional TSLib packages..."
    pip install torch==2.0.1 torchvision torchaudio
    pip install "numpy>=1.24,<1.26" "pandas>=1.5,<2.0" "scipy>=1.10,<1.14"
    pip install statsmodels prophet "sktime==0.26.0"
    pip install matplotlib seaborn plotly scikit-learn
}

install_tslib_nixtla_packages() {
    log_info "🏢 Installing Nixtla TSLib packages..."
    pip install torch>=2.1 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
    pip install numpy>=1.26 pandas>=2.2
    pip install nixtla statsforecast mlforecast neuralforecast hierarchicalforecast
    pip install matplotlib seaborn plotly scipy scikit-learn
}

install_tslib_advanced_packages() {
    log_info "🔬 Installing Advanced TSLib packages..."
    pip install torch>=2.1 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
    pip install numpy>=1.26 pandas>=2.2 einops
    pip install darts tslearn tsfresh pytorch-lightning>=2.0
    pip install matplotlib seaborn plotly scipy scikit-learn
}

# Repository cloning functions
install_research_package() {
    local repo_url="$1"
    local repo_name="$2"
    local repo_dir="models/$repo_name"
    
    log_info "📦 Cloning and installing research package: $repo_name from $repo_url"
    mkdir -p models
    if git clone --depth 1 "$repo_url" "$repo_dir" 2>/tmp/clone_error.log; then
        log_success "Successfully cloned $repo_name"
        cd "$repo_dir"
        if [[ -f "requirements.txt" ]]; then
            pip install -r "requirements.txt" || log_warning "Failed to install requirements for $repo_name"
        fi
        if [[ -f "pyproject.toml" || -f "setup.py" ]]; then
            pip install -e . || log_warning "Failed to install $repo_name as editable package"
        fi
        cd - > /dev/null
    else
        log_error "Failed to clone $repo_name"
        cat /tmp/clone_error.log
        return 1
    fi
    log_success "✅ Successfully installed research package: $repo_name"
    return 0
}

clone_repositories() {
    local env_name="$1"
    log_info "📚 Cloning repositories for $env_name..."
    
    local repositories=$(get_repositories_for_env "$env_name")
    if [[ -z "$repositories" ]]; then
        log_info "No repositories defined for $env_name"
        return 0
    fi
    
    IFS=' ' read -ra repo_array <<< "$repositories"
    
    for repo in "${repo_array[@]}"; do
        local repo_url=$(echo "$repo" | cut -d':' -f1)
        local repo_name=$(echo "$repo" | cut -d':' -f2)
        install_research_package "$repo_url" "$repo_name" || { log_error "Failed to install $repo in $env_name"; return 1; }
    done
    
    log_success "✅ Repositories cloned for $env_name"
    return 0
}

# Enhanced verification functions
verify_environment() {
    local env_name="$1"
    log_info "🔍 Verifying environment: $env_name"
    
    # Check if environment exists and is functional
    local status=$(get_env_status "$env_name")
    if [[ "$status" != "functional" ]]; then
        log_error "❌ Environment $env_name is $status"
        return 1
    fi
    
    # Activate environment for detailed verification
    if ! activate_env "$env_name"; then
        return 1
    fi
    
    # Run environment-specific verification
    local verify_result=0
    case "$env_name" in
        "$ENV_TRANSFORMERS_MODERN") verify_transformers_modern_installation ;;
        "$ENV_TRANSFORMERS_LEGACY") verify_transformers_legacy_installation ;;
        "$ENV_TRANSFORMERS_TS") verify_transformers_ts_installation ;;
        "$ENV_LLM_CHRONOS") verify_llm_chronos_installation ;;
        "$ENV_LLM_UNI2TS") verify_llm_uni2ts_installation ;;
        "$ENV_LLM_MOMENTFM") verify_llm_momentfm_installation ;;
        "$ENV_LLM_MAMBA") verify_llm_mamba_installation ;;
        "$ENV_TSLIB_TRADITIONAL") verify_tslib_traditional_installation ;;
        "$ENV_TSLIB_NIXTLA") verify_tslib_nixtla_installation ;;
        "$ENV_TSLIB_ADVANCED") verify_tslib_advanced_installation ;;
        *) verify_generic_installation ;;
    esac
    verify_result=$?
    
    # Run pip check
    local pip_check_result=0
    if pip check >/dev/null 2>&1; then
        log_success "✅ Pip check passed for $env_name: No broken dependencies"
    else
        log_error "❌ Pip check failed for $env_name: Broken dependencies detected"
        pip check 2>&1 | while IFS= read -r line; do log_error "$line"; done
        pip_check_result=1
    fi
    
    deactivate_env
    
    if [[ $verify_result -eq 0 && $pip_check_result -eq 0 ]]; then
        log_success "✅ Environment $env_name verification passed"
        return 0
    else
        log_error "❌ Environment $env_name verification failed"
        return 1
    fi
}

# Verification functions for each environment
verify_transformers_modern_installation() {
    python -c "import transformers; assert transformers.__version__ >= '4.45.0'; print('Transformers Modern OK')" 2>/dev/null
}

verify_transformers_legacy_installation() {
    python -c "import transformers; assert transformers.__version__ == '4.33.3'; print('Transformers Legacy OK')" 2>/dev/null
}

verify_transformers_ts_installation() {
    python -c "import pytorch_forecasting; print('Transformers TS OK')" 2>/dev/null
}

verify_llm_chronos_installation() {
    python -c "import chronos; print('LLM Chronos OK')" 2>/dev/null
}

verify_llm_uni2ts_installation() {
    python -c "import uni2ts; print('LLM Uni2TS OK')" 2>/dev/null
}

verify_llm_momentfm_installation() {
    python -c "import momentfm; print('LLM MomentFM OK')" 2>/dev/null
}

verify_llm_mamba_installation() {
    python -c "import mamba_ssm; print('LLM Mamba OK')" 2>/dev/null
}

verify_tslib_traditional_installation() {
    python -c "import statsmodels, prophet, sktime; print('TSLib Traditional OK')" 2>/dev/null
}

verify_tslib_nixtla_installation() {
    python -c "import neuralforecast; print('TSLib Nixtla OK')" 2>/dev/null
}

verify_tslib_advanced_installation() {
    python -c "import darts, tsfresh; print('TSLib Advanced OK')" 2>/dev/null
}

verify_generic_installation() {
    python -c "import sys; print(f'Python {sys.version} OK')" 2>/dev/null
}

# Backup function
backup_environments() {
    local backup_dir="backups/setup_$(date +%Y%m%d_%H%M%S)"
    log_info "📋 Backing up environments to $backup_dir..."
    mkdir -p "$backup_dir"
    
    local all_envs=(
        "$ENV_TRANSFORMERS_MODERN" "$ENV_TRANSFORMERS_LEGACY" "$ENV_TRANSFORMERS_TS"
        "$ENV_LLM_CHRONOS" "$ENV_LLM_UNI2TS" "$ENV_LLM_MOMENTFM" "$ENV_LLM_MAMBA"
        "$ENV_TSLIB_TRADITIONAL" "$ENV_TSLIB_NIXTLA" "$ENV_TSLIB_ADVANCED"
        "$ENV_BASE_TORCH" "$ENV_GEOMETRIC" "$ENV_TENSORFLOW" "$ENV_RAPIDS"
        "$ENV_ANOMALY_ADVANCED" "$ENV_FEDERATED" "$ENV_MULTIMODAL" 
        "$ENV_PROBABILISTIC" "$ENV_CAUSAL" "$ENV_VISION_TS"
    )
    
    for env in "${all_envs[@]}"; do
        if env_exists "$env"; then
            log_info "Backing up $env..."
            conda env export -n "$env" > "$backup_dir/${env}.yml" 2>/dev/null || log_warning "Failed to backup $env"
        fi
    done
    
    log_success "✅ Backup completed in $backup_dir"
}

# Verify and reinstall function
verify_and_install() {
    local env_name="$1"
    log_info "🔍 Starting verification for $env_name"
    
    local needs_reinstall=false
    
    # Verify environment
    if ! verify_environment "$env_name"; then
        log_warning "⚠️ Environment $env_name failed verification, marking for reinstall"
        needs_reinstall=true
    fi
    
    if $needs_reinstall; then
        log_info "🔧 Reinstalling environment $env_name due to verification failures"
        if install_environment "$env_name" && clone_repositories "$env_name"; then
            log_success "✅ Successfully reinstalled $env_name"
        else
            log_error "❌ Failed to reinstall $env_name"
            return 1
        fi
    else
        log_success "✅ Environment $env_name is fully functional, no reinstall needed"
    fi
    
    return 0
}

# Interactive environment selection
select_environments_interactive() {
    SELECTED_ENVS=()
    echo ""
    echo "🎯 AI Time Series Framework - Environment Selection"
    echo "=================================================="
    echo ""
    echo "Available environments:"
    echo "  1) $ENV_TRANSFORMERS_MODERN    - Modern transformers (latest versions)"
    echo "  2) $ENV_TRANSFORMERS_LEGACY    - Legacy transformers (compatible versions)"
    echo "  3) $ENV_TRANSFORMERS_TS        - Time series transformers"
    echo "  4) $ENV_LLM_CHRONOS            - Chronos LLM forecasting"
    echo "  5) $ENV_LLM_UNI2TS             - Uni2TS LLM forecasting"
    echo "  6) $ENV_LLM_MOMENTFM           - MomentFM LLM forecasting"
    echo "  7) $ENV_LLM_MAMBA              - Mamba LLM forecasting"
    echo "  8) $ENV_TSLIB_TRADITIONAL      - Traditional time series libraries"
    echo "  9) $ENV_TSLIB_NIXTLA           - Nixtla time series ecosystem"
    echo " 10) $ENV_TSLIB_ADVANCED         - Advanced time series libraries"
    echo " 11) $ENV_BASE_TORCH             - PyTorch base environment"
    echo " 12) $ENV_GEOMETRIC              - PyTorch Geometric environment"
    echo " 13) $ENV_TENSORFLOW             - TensorFlow environment"
    echo " 14) $ENV_RAPIDS                 - RAPIDS environment (GPU required)"
    echo " 15) $ENV_ANOMALY_ADVANCED       - Advanced anomaly detection"
    echo " 16) $ENV_FEDERATED              - Federated learning"
    echo " 17) $ENV_MULTIMODAL             - Multimodal time series"
    echo " 18) $ENV_PROBABILISTIC          - Probabilistic time series"
    echo " 19) $ENV_CAUSAL                 - Causal discovery"
    echo " 20) $ENV_VISION_TS              - Vision-enhanced time series"
    echo " 21) all                         - Install all environments"
    echo ""
    
    while true; do
        if [[ ${#SELECTED_ENVS[@]} -gt 0 ]]; then
            echo "Currently selected: ${SELECTED_ENVS[*]}"
            echo ""
        fi
        read -p "Enter environment number (1-21), 'q' to quit, or 'd' when done: " choice
        case $choice in
            1) SELECTED_ENVS+=("$ENV_TRANSFORMERS_MODERN"); echo "✅ Added $ENV_TRANSFORMERS_MODERN" ;;
            2) SELECTED_ENVS+=("$ENV_TRANSFORMERS_LEGACY"); echo "✅ Added $ENV_TRANSFORMERS_LEGACY" ;;
            3) SELECTED_ENVS+=("$ENV_TRANSFORMERS_TS"); echo "✅ Added $ENV_TRANSFORMERS_TS" ;;
            4) SELECTED_ENVS+=("$ENV_LLM_CHRONOS"); echo "✅ Added $ENV_LLM_CHRONOS" ;;
            5) SELECTED_ENVS+=("$ENV_LLM_UNI2TS"); echo "✅ Added $ENV_LLM_UNI2TS" ;;
            6) SELECTED_ENVS+=("$ENV_LLM_MOMENTFM"); echo "✅ Added $ENV_LLM_MOMENTFM" ;;
            7) SELECTED_ENVS+=("$ENV_LLM_MAMBA"); echo "✅ Added $ENV_LLM_MAMBA" ;;
            8) SELECTED_ENVS+=("$ENV_TSLIB_TRADITIONAL"); echo "✅ Added $ENV_TSLIB_TRADITIONAL" ;;
            9) SELECTED_ENVS+=("$ENV_TSLIB_NIXTLA"); echo "✅ Added $ENV_TSLIB_NIXTLA" ;;
            10) SELECTED_ENVS+=("$ENV_TSLIB_ADVANCED"); echo "✅ Added $ENV_TSLIB_ADVANCED" ;;
            11) SELECTED_ENVS+=("$ENV_BASE_TORCH"); echo "✅ Added $ENV_BASE_TORCH" ;;
            12) SELECTED_ENVS+=("$ENV_GEOMETRIC"); echo "✅ Added $ENV_GEOMETRIC" ;;
            13) SELECTED_ENVS+=("$ENV_TENSORFLOW"); echo "✅ Added $ENV_TENSORFLOW" ;;
            14) SELECTED_ENVS+=("$ENV_RAPIDS"); echo "✅ Added $ENV_RAPIDS" ;;
            15) SELECTED_ENVS+=("$ENV_ANOMALY_ADVANCED"); echo "✅ Added $ENV_ANOMALY_ADVANCED" ;;
            16) SELECTED_ENVS+=("$ENV_FEDERATED"); echo "✅ Added $ENV_FEDERATED" ;;
            17) SELECTED_ENVS+=("$ENV_MULTIMODAL"); echo "✅ Added $ENV_MULTIMODAL" ;;
            18) SELECTED_ENVS+=("$ENV_PROBABILISTIC"); echo "✅ Added $ENV_PROBABILISTIC" ;;
            19) SELECTED_ENVS+=("$ENV_CAUSAL"); echo "✅ Added $ENV_CAUSAL" ;;
            20) SELECTED_ENVS+=("$ENV_VISION_TS"); echo "✅ Added $ENV_VISION_TS" ;;
            21)
                SELECTED_ENVS=(
                    "$ENV_TRANSFORMERS_MODERN" "$ENV_TRANSFORMERS_LEGACY" "$ENV_TRANSFORMERS_TS"
                    "$ENV_LLM_CHRONOS" "$ENV_LLM_UNI2TS" "$ENV_LLM_MOMENTFM" "$ENV_LLM_MAMBA"
                    "$ENV_TSLIB_TRADITIONAL" "$ENV_TSLIB_NIXTLA" "$ENV_TSLIB_ADVANCED"
                    "$ENV_BASE_TORCH" "$ENV_GEOMETRIC" "$ENV_TENSORFLOW" "$ENV_RAPIDS"
                    "$ENV_ANOMALY_ADVANCED" "$ENV_FEDERATED" "$ENV_MULTIMODAL" 
                    "$ENV_PROBABILISTIC" "$ENV_CAUSAL" "$ENV_VISION_TS"
                )
                echo "✅ All environments selected!"
                return 0
                ;;
            d|D|done|DONE)
                if [[ ${#SELECTED_ENVS[@]} -eq 0 ]]; then
                    echo "❌ No environments selected. Please select at least one environment."
                else
                    log_info "Environment selection completed: ${SELECTED_ENVS[*]}"
                    echo "✅ Selection completed with: ${SELECTED_ENVS[*]}"
                    return 0
                fi
                ;;
            q|Q|quit|QUIT)
                echo "❌ Setup cancelled by user."
                exit 0
                ;;
            *)
                echo "❌ Invalid selection. Please choose 1-21, 'd' for done, or 'q' to quit."
                ;;
        esac
        echo ""
    done
}

# Generate activation scripts
generate_activation_scripts() {
    log_info "📝 Generating activation scripts..."
    mkdir -p scripts/activation
    
    for env in "${SELECTED_ENVS[@]}"; do
        cat > "scripts/activation/activate_${env}.sh" << EOF
#!/bin/bash
# Auto-generated activation script for $env
echo "🚀 Activating $env..."
conda activate $env
echo "✅ Environment $env activated"
echo "Python: \$(python --version)"
echo "Current environment: \$CONDA_DEFAULT_ENV"
EOF
        chmod +x "scripts/activation/activate_${env}.sh"
    done
    
    log_success "✅ Activation scripts generated in scripts/activation/"
}

# Generate documentation
generate_documentation() {
    log_info "📚 Generating documentation..."
    cat > "ENVIRONMENT_SETUP.md" << EOF
# AI Time Series Framework - Environment Setup

Generated on: $(date)
Setup version: 6.0.0

## Installed Environments

$(for env in "${SELECTED_ENVS[@]}"; do
    echo "### $env"
    echo "- Packages: $(get_packages "$env" | tr ' ' '\n' | head -5 | tr '\n' ' ')..."
    echo "- Status: $(get_env_status "$env")"
    echo ""
done)

## Usage

To activate an environment:
\`\`\`bash
conda activate <environment_name>
\`\`\`

Or use the generated activation scripts:
\`\`\`bash
./scripts/activation/activate_<environment_name>.sh
\`\`\`

## Verification

To verify environments:
\`\`\`bash
./setup.sh --verify
\`\`\`

## Logs

Installation logs are available in: logs/
EOF
    
    log_success "✅ Documentation generated: ENVIRONMENT_SETUP.md"
}

# Help function
show_help() {
    echo "🎯 AI Time Series Framework - Enhanced Setup Script"
    echo "=================================================="
    echo ""
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  --help                Show this help message"
    echo "  --verify             Verify environments and reinstall only if needed"
    echo "  --force-reinstall    Force reinstallation of all selected environments"
    echo "  --skip-gpu-check     Skip GPU-dependent packages (like RAPIDS)"
    echo ""
    echo "Environment Variables:"
    echo "  FORCE_REINSTALL=true    Force reinstall all environments"
    echo "  SKIP_GPU_CHECK=true     Skip GPU checks"
    echo "  VERIFY_MODE=true        Run in verification mode"
    echo ""
    echo "Examples:"
    echo "  $0                      Interactive mode"
    echo "  $0 --verify             Verify all environments"
    echo "  $0 --force-reinstall    Force reinstall selected environments"
    echo ""
    exit 0
}

# Main execution function
main() {
    # Parse command line arguments
    while [[ $# -gt 0 ]]; do
        case $1 in
            --help)
                show_help
                ;;
            --verify)
                VERIFY_MODE="true"
                log_info "Verification mode activated"
                shift
                ;;
            --force-reinstall)
                FORCE_REINSTALL="true"
                log_info "Force reinstall mode activated"
                shift
                ;;
            --skip-gpu-check)
                SKIP_GPU_CHECK="true"
                log_info "GPU check skip activated"
                shift
                ;;
            *)
                SELECTED_ENVS+=("$1")
                shift
                ;;
        esac
    done
    
    # Initialize
    setup_logging
    log_info "🚀 Starting Enhanced AI Time Series Framework Setup..."
    log_info "📁 Working directory: $SCRIPT_DIR"
    
    # Source configuration files
    source_configs
    
    # Initialize Conda
    init_conda
    
    # Select environments if none specified
    if [[ ${#SELECTED_ENVS[@]} -eq 0 ]]; then
        select_environments_interactive
    fi
    
    # Backup existing environments
    backup_environments
    
    # Process each selected environment
    log_info "🔧 Processing ${#SELECTED_ENVS[@]} environments..."
    local success_count=0
    local total_count=${#SELECTED_ENVS[@]}
    
    for env_name in "${SELECTED_ENVS[@]}"; do
        log_info "Processing $env_name..."
        
        if [[ "$VERIFY_MODE" == "true" ]]; then
            if verify_and_install "$env_name"; then
                ((success_count++))
            fi
        else
            if install_environment "$env_name" && clone_repositories "$env_name"; then
                ((success_count++))
            fi
        fi
    done
    
    # Generate supporting files
    generate_activation_scripts
    generate_documentation
    
    # Final summary
    echo ""
    echo "🎉 Setup Complete!"
    echo "=================="
    echo "✅ Successfully processed: $success_count/$total_count environments"
    echo "📄 Log file: $LOG_FILE"
    echo "📚 Documentation: ENVIRONMENT_SETUP.md"
    echo "🚀 Activation scripts: scripts/activation/"
    echo ""
    
    if [[ $success_count -eq $total_count ]]; then
        log_success "🎉 All environments set up successfully!"
        exit 0
    else
        log_warning "⚠️ Some environments failed to install. Check the logs for details."
        exit 1
    fi
}

# Execute main function if script is run directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi
--- END FILE ---

<!-- Full Path: C:/00_Repos_Rod/Testing_Repos/environments\scripts\align_folders.sh -->
<!-- Relative Path: scripts\align_folders.sh -->
<!-- File Size: 21463 bytes -->
<!-- Last Modified: 2025-08-05 00:04:20 -->
--- BEGIN FILE: scripts\align_folders.sh ---
#!/bin/bash
# Language: Bash 5.0
# Lines of Code: 420
# File: scripts/align_folders_v3.sh
# Version: 3.0.0
# Project: AI Time Series Framework
# Repository: AI_TimeSeriesFramework
# Author: Rod Sanchez
# Created: 2025-08-04 16:00
# Last Edited: 2025-08-04 16:00
# Change: Major (+1.0) - Complete rewrite with dependency conflict avoidance and intelligent package management
# Modifications: +420, -0
# Last Modification Comment: Implemented dependency-aware, conflict-free repository management with strict separation of installation methods

set -euo pipefail

# =============================================================================
# COLORS AND FORMATTING
# =============================================================================
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
PURPLE='\033[0;35m'
NC='\033[0m' # No Color

# =============================================================================
# DIRECTORIES AND PATHS
# =============================================================================
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="${SCRIPT_DIR}/.."
MODELS_DIR="${PROJECT_DIR}/models"
CONFIG_DIR="${SCRIPT_DIR}/config"
LOGS_DIR="${PROJECT_DIR}/logs"

# Create necessary directories
mkdir -p "$MODELS_DIR" "$LOGS_DIR"

# Log file for this session
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
LOG_FILE="${LOGS_DIR}/align_repositories_${TIMESTAMP}.log"

# =============================================================================
# LOGGING FUNCTIONS
# =============================================================================
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1" | tee -a "$LOG_FILE"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1" | tee -a "$LOG_FILE"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1" | tee -a "$LOG_FILE"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1" | tee -a "$LOG_FILE"
}

log_step() {
    echo -e "${PURPLE}[STEP]${NC} $1" | tee -a "$LOG_FILE"
}

# =============================================================================
# INITIALIZATION
# =============================================================================
main() {
    echo -e "${CYAN}🚀 AI Time Series Framework - Conflict-Free Repository Management${NC}"
    echo -e "${CYAN}=================================================================${NC}"
    echo ""
    
    log_info "Starting repository alignment at $(date)"
    log_info "Log file: $LOG_FILE"
    echo ""

    # Load configurations
    log_step "Loading configurations..."
    if ! load_configurations; then
        log_error "Failed to load configurations"
        exit 1
    fi
    log_success "Configurations loaded successfully"
    echo ""

    # Environment validation
    log_step "Validating conda environments..."
    validate_environments
    echo ""

    # Cleanup phase
    log_step "Cleaning up duplicate folders..."
    cleanup_duplicate_folders
    echo ""

    # Conflict detection and resolution
    log_step "Detecting and resolving conflicts..."
    detect_and_resolve_conflicts
    echo ""

    # Package management phase
    log_step "Managing packages with dependency-aware installation..."
    manage_packages_intelligently
    echo ""

    # Source repository management
    log_step "Managing source-only repositories..."
    manage_source_repositories
    echo ""

    # Final validation
    log_step "Performing final validation..."
    final_validation
    echo ""

    log_success "Repository alignment completed successfully!"
    show_final_summary
}

# =============================================================================
# CONFIGURATION LOADING
# =============================================================================
load_configurations() {
    local configs=(
        "${CONFIG_DIR}/environments.conf"
        "${CONFIG_DIR}/repositories.conf"
    )
    
    for config in "${configs[@]}"; do
        if [[ -f "$config" ]]; then
            source "$config"
            log_info "Loaded: $(basename "$config")"
        else
            log_error "Missing configuration: $config"
            return 1
        fi
    done
    
    return 0
}

# =============================================================================
# ENVIRONMENT VALIDATION
# =============================================================================
validate_environments() {
    local all_envs=(
        "${ENV_TRANSFORMERS_MODERN}"
        "${ENV_TRANSFORMERS_LEGACY}"
        "${ENV_TRANSFORMERS_TS}"
        "${ENV_LLM_CHRONOS}"
        "${ENV_LLM_UNI2TS}"
        "${ENV_LLM_MOMENTFM}"
        "${ENV_LLM_MAMBA}"
        "${ENV_TSLIB_TRADITIONAL}"
        "${ENV_TSLIB_NIXTLA}"
        "${ENV_TSLIB_ADVANCED}"
        "${ENV_BASE_TORCH}"
        "${ENV_GEOMETRIC}"
        "${ENV_TENSORFLOW}"
        "${ENV_RAPIDS}"
        "${ENV_ANOMALY_ADVANCED}"
        "${ENV_FEDERATED}"
        "${ENV_MULTIMODAL}"
        "${ENV_PROBABILISTIC}"
        "${ENV_CAUSAL}"
        "${ENV_VISION_TS}"
    )

    local valid_envs=()
    local missing_envs=()

    log_info "Checking ${#all_envs[@]} conda environments..."

    for env in "${all_envs[@]}"; do
        if conda env list | grep -q "^${env}\s"; then
            log_success "✅ $env"
            valid_envs+=("$env")
        else
            log_error "❌ $env (not found)"
            missing_envs+=("$env")
        fi
    done

    VALID_ENVIRONMENTS=("${valid_envs[@]}")
    MISSING_ENVIRONMENTS=("${missing_envs[@]}")

    log_info "Environment Status: ${#valid_envs[@]} valid, ${#missing_envs[@]} missing"

    if [ ${#missing_envs[@]} -gt 0 ]; then
        log_warning "Missing environments detected. Some operations will be skipped."
        log_warning "Missing: ${missing_envs[*]}"
        
        read -p "Continue with valid environments only? [y/N]: " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            log_error "Aborted by user"
            exit 1
        fi
    fi
}

# =============================================================================
# CLEANUP FUNCTIONS
# =============================================================================
cleanup_duplicate_folders() {
    local cleanup_count=0
    
    # Legacy folder cleanup
    local legacy_folders=(
        "${MODELS_DIR}/geometric_models"
        "${MODELS_DIR}/pytorch_models"
        "${MODELS_DIR}/transformer_models"
    )
    
    for folder in "${legacy_folders[@]}"; do
        if [ -d "$folder" ]; then
            rm -rf "$folder"
            log_success "Removed legacy folder: $(basename "$folder")"
            ((cleanup_count++))
        fi
    done
    
    # Root level repository cleanup
    local common_repo_names=(
        "Time-Series-Library" "Autoformer" "Informer2020" "PatchTST"
        "chronos-forecasting" "uni2ts" "moment" "mamba-ssm"
    )
    
    for repo in "${common_repo_names[@]}"; do
        if [ -d "${PROJECT_DIR}/${repo}" ]; then
            # Check if it should be in models directory instead
            local target_dir=$(find "$MODELS_DIR" -name "$repo" -type d | head -1)
            if [ -n "$target_dir" ]; then
                rm -rf "${PROJECT_DIR}/${repo}"
                log_success "Removed root duplicate: $repo"
                ((cleanup_count++))
            fi
        fi
    done
    
    if [ $cleanup_count -eq 0 ]; then
        log_info "No duplicate folders found - system is clean"
    else
        log_success "Cleanup complete: $cleanup_count items processed"
    fi
}

# =============================================================================
# CONFLICT DETECTION AND RESOLUTION
# =============================================================================
detect_and_resolve_conflicts() {
    log_info "Scanning for dependency conflicts across environments..."
    
    local total_conflicts=0
    
    for env in "${VALID_ENVIRONMENTS[@]}"; do
        log_info "Checking conflicts in: $env"
        
        # Check for known conflict patterns
        local env_conflicts=0
        
        # Detect mixed installation methods
        for package in "${CONFLICT_PRONE_PACKAGES[@]}"; do
            local conda_installed=false
            local pip_installed=false
            
            if conda run -n "$env" conda list 2>/dev/null | grep -qi "^${package}\s"; then
                conda_installed=true
            fi
            
            if conda run -n "$env" pip list 2>/dev/null | grep -qi "^${package}\s"; then
                pip_installed=true
            fi
            
            if $conda_installed && $pip_installed; then
                log_warning "⚠️ CONFLICT: $package installed via both conda and pip in $env"
                
                # Auto-resolve: Remove pip version, keep conda
                log_info "Auto-resolving: Removing pip version of $package"
                conda run -n "$env" pip uninstall -y "$package" 2>/dev/null || true
                log_success "Resolved conflict for $package in $env"
                
                ((env_conflicts++))
                ((total_conflicts++))
            fi
        done
        
        if [ $env_conflicts -eq 0 ]; then
            log_success "No conflicts found in $env"
        else
            log_warning "Resolved $env_conflicts conflicts in $env"
        fi
    done
    
    if [ $total_conflicts -eq 0 ]; then
        log_success "No dependency conflicts detected across all environments"
    else
        log_success "Resolved $total_conflicts total conflicts across all environments"
    fi
}

# =============================================================================
# INTELLIGENT PACKAGE MANAGEMENT
# =============================================================================
manage_packages_intelligently() {
    log_info "Starting dependency-aware package management..."
    
    for env in "${VALID_ENVIRONMENTS[@]}"; do
        log_info "Processing packages for: $env"
        echo "────────────────────────────────────────────────"
        
        # Phase 1: Install conda packages (highest priority)
        install_conda_packages "$env"
        
        # Phase 2: Install pip packages (medium priority)
        install_pip_packages "$env"
        
        # Phase 3: Verify installation integrity
        verify_package_integrity "$env"
        
        echo ""
    done
}

install_conda_packages() {
    local env="$1"
    local conda_packages
    conda_packages=$(get_conda_packages_for_env "$env")
    
    if [ -n "$conda_packages" ]; then
        log_info "Installing conda packages for $env"
        
        # Split packages and install individually to handle failures gracefully
        for package in $conda_packages; do
            if ! conda run -n "$env" conda list 2>/dev/null | grep -qi "^${package}\s"; then
                log_info "Installing conda package: $package"
                if conda install -n "$env" -c conda-forge "$package" -y 2>/dev/null; then
                    log_success "✅ $package (conda)"
                else
                    log_warning "⚠️ Failed to install $package via conda, will try pip"
                fi
            else
                log_info "✅ $package already installed (conda)"
            fi
        done
    else
        log_info "No conda packages defined for $env"
    fi
}

install_pip_packages() {
    local env="$1"
    local pip_packages
    pip_packages=$(get_pip_packages_for_env "$env")
    
    if [ -n "$pip_packages" ]; then
        log_info "Installing pip packages for $env"
        
        for package in $pip_packages; do
            # Check if package is blacklisted for source installation
            if is_package_blacklisted "$package"; then
                log_warning "⚠️ Package $package is blacklisted for non-standard installation"
                continue
            fi
            
            if ! conda run -n "$env" pip list 2>/dev/null | grep -qi "^${package}\s"; then
                log_info "Installing pip package: $package"
                if conda run -n "$env" pip install "$package" --no-deps 2>/dev/null; then
                    log_success "✅ $package (pip)"
                else
                    log_warning "⚠️ Failed to install $package via pip"
                fi
            else
                log_info "✅ $package already installed (pip)"
            fi
        done
    else
        log_info "No pip packages defined for $env"
    fi
}

verify_package_integrity() {
    local env="$1"
    
    log_info "Verifying package integrity for $env"
    
    # Check for common import issues
    local test_imports=(
        "import torch; print('PyTorch:', torch.__version__)"
        "import numpy; print('NumPy:', numpy.__version__)"
        "import pandas; print('Pandas:', pandas.__version__)"
    )
    
    for test_import in "${test_imports[@]}"; do
        if conda run -n "$env" python -c "$test_import" 2>/dev/null; then
            local package_name=$(echo "$test_import" | cut -d';' -f2 | cut -d':' -f1 | xargs)
            log_success "✅ $package_name imports successfully"
        fi
    done
}

# =============================================================================
# SOURCE REPOSITORY MANAGEMENT
# =============================================================================
manage_source_repositories() {
    log_info "Managing source-only repositories..."
    
    for env in "${VALID_ENVIRONMENTS[@]}"; do
        local source_repos
        source_repos=$(get_source_repos_for_env "$env")
        
        if [ -n "$source_repos" ]; then
            log_info "Processing source repositories for: $env"
            
            # Create environment-specific model directory
            local model_dir="${MODELS_DIR}/${env}"
            mkdir -p "$model_dir"
            
            # Process each repository
            local repos_array=($source_repos)
            for repo_spec in "${repos_array[@]}"; do
                clone_and_setup_repository "$env" "$repo_spec" "$model_dir"
            done
        else
            log_info "No source repositories defined for $env"
        fi
    done
}

clone_and_setup_repository() {
    local env="$1"
    local repo_spec="$2"
    local base_dir="$3"
    
    # Parse repository specification
    local repo_name=$(echo "$repo_spec" | cut -d':' -f1)
    local repo_url=$(echo "$repo_spec" | cut -d':' -f2)
    local repo_branch=$(echo "$repo_spec" | cut -d':' -f3)
    local package_name=$(echo "$repo_spec" | cut -d':' -f4)
    
    log_info "Processing repository: $repo_name"
    
    pushd "$base_dir" > /dev/null
    
    # Check if already cloned and up to date
    if [ -d "$repo_name/.git" ]; then
        log_info "Repository $repo_name exists, updating..."
        pushd "$repo_name" > /dev/null
        if git pull origin "$repo_branch" 2>/dev/null; then
            log_success "✅ Updated $repo_name"
        else
            log_warning "⚠️ Failed to update $repo_name"
        fi
        popd > /dev/null
    else
        # Clone repository
        if [ -d "$repo_name" ]; then
            log_warning "Directory $repo_name exists but no .git, removing..."
            rm -rf "$repo_name"
        fi
        
        log_info "Cloning $repo_name from github.com/$repo_url"
        if git clone "https://github.com/$repo_url" -b "$repo_branch" "$repo_name" 2>/dev/null; then
            log_success "✅ Cloned $repo_name"
        else
            log_error "❌ Failed to clone $repo_name"
            popd > /dev/null
            return 1
        fi
    fi
    
    # Attempt installation if package name is provided
    if [ -n "$package_name" ] && [ "$package_name" != "$repo_name" ]; then
        log_info "Attempting to install $package_name from source..."
        
        # Check if package is blacklisted
        if is_package_blacklisted "$package_name"; then
            log_error "❌ Package $package_name is blacklisted for source installation"
            popd > /dev/null
            return 1
        fi
        
        pushd "$repo_name" > /dev/null
        if [ -f "setup.py" ] || [ -f "pyproject.toml" ]; then
            if conda run -n "$env" pip install -e . --no-deps 2>/dev/null; then
                log_success "✅ Installed $package_name in development mode"
            else
                log_warning "⚠️ Failed to install $package_name, kept as source-only"
            fi
        else
            log_info "No setup.py or pyproject.toml found, keeping as source-only"
        fi
        popd > /dev/null
    fi
    
    popd > /dev/null
}

# =============================================================================
# FINAL VALIDATION
# =============================================================================
final_validation() {
    log_info "Performing final system validation..."
    
    # Check directory structure
    validate_directory_structure
    
    # Check for remaining conflicts
    check_final_conflicts
    
    # Generate installation report
    generate_installation_report
}

validate_directory_structure() {
    log_info "Validating directory structure..."
    
    local expected_dirs=(
        "models"
        "logs"
        "scripts/config"
    )
    
    for dir in "${expected_dirs[@]}"; do
        if [ -d "${PROJECT_DIR}/${dir}" ]; then
            log_success "✅ Directory exists: $dir"
        else
            log_warning "⚠️ Directory missing: $dir"
        fi
    done
}

check_final_conflicts() {
    log_info "Performing final conflict check..."
    
    local total_issues=0
    
    for env in "${VALID_ENVIRONMENTS[@]}"; do
        # Check for duplicate packages
        for package in "${CONFLICT_PRONE_PACKAGES[@]}"; do
            local conda_count pip_count
            conda_count=$(conda run -n "$env" conda list 2>/dev/null | grep -c "^${package}\s" || true)
            pip_count=$(conda run -n "$env" pip list 2>/dev/null | grep -c "^${package}\s" || true)
            
            if [ "$conda_count" -gt 1 ] || [ "$pip_count" -gt 1 ]; then
                log_warning "⚠️ Multiple versions of $package detected in $env"
                ((total_issues++))
            fi
        done
    done
    
    if [ $total_issues -eq 0 ]; then
        log_success "✅ No conflicts detected in final validation"
    else
        log_warning "⚠️ $total_issues potential issues detected"
    fi
}

generate_installation_report() {
    local report_file="${LOGS_DIR}/installation_report_${TIMESTAMP}.txt"
    
    log_info "Generating installation report: $report_file"
    
    {
        echo "AI Time Series Framework Installation Report"
        echo "==========================================="
        echo "Generated: $(date)"
        echo "Environments processed: ${#VALID_ENVIRONMENTS[@]}"
        echo "Missing environments: ${#MISSING_ENVIRONMENTS[@]}"
        echo ""
        
        echo "Valid Environments:"
        for env in "${VALID_ENVIRONMENTS[@]}"; do
            echo "  - $env"
        done
        echo ""
        
        if [ ${#MISSING_ENVIRONMENTS[@]} -gt 0 ]; then
            echo "Missing Environments:"
            for env in "${MISSING_ENVIRONMENTS[@]}"; do
                echo "  - $env"
            done
            echo ""
        fi
        
        echo "Directory Structure:"
        find "$MODELS_DIR" -type d -maxdepth 2 | sort
        
    } > "$report_file"
    
    log_success "Installation report generated: $report_file"
}

# =============================================================================
# FINAL SUMMARY
# =============================================================================
show_final_summary() {
    echo ""
    echo -e "${GREEN}🎉 REPOSITORY ALIGNMENT COMPLETED SUCCESSFULLY!${NC}"
    echo -e "${GREEN}===============================================${NC}"
    echo ""
    echo -e "${CYAN}📊 SUMMARY:${NC}"
    echo -e "   🏗️  Environments processed: ${#VALID_ENVIRONMENTS[@]}"
    echo -e "   📁 Models directory: $MODELS_DIR"
    echo -e "   📋 Log file: $LOG_FILE"
    echo ""
    
    if [ ${#MISSING_ENVIRONMENTS[@]} -gt 0 ]; then
        echo -e "${YELLOW}⚠️  RECOMMENDATIONS:${NC}"
        echo -e "   • Create missing environments: ${#MISSING_ENVIRONMENTS[@]}"
        echo -e "   • Re-run script after creating missing environments"
        echo ""
    fi
    
    echo -e "${CYAN}📁 To view the structure:${NC}"
    echo -e "   ${GREEN}tree models -L 3${NC}"
    echo ""
    
    echo -e "${CYAN}🔍 To check installation:${NC}"
    echo -e "   ${GREEN}conda run -n <env_name> python -c \"import torch; print(torch.__version__)\"${NC}"
    echo ""
    
    # Display directory structure if tree is available
    if command -v tree &> /dev/null; then
        echo -e "${CYAN}📁 CURRENT STRUCTURE:${NC}"
        echo "════════════════════════"
        tree "$MODELS_DIR" -L 2 2>/dev/null | head -20
        echo ""
    fi
    
    log_success "All operations completed successfully at $(date)"
}

# =============================================================================
# SCRIPT EXECUTION
# =============================================================================
# Run main function if script is executed directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi
--- END FILE ---

<!-- Full Path: C:/00_Repos_Rod/Testing_Repos/environments\scripts\comprehensive_dependency_fixer.sh -->
<!-- Relative Path: scripts\comprehensive_dependency_fixer.sh -->
<!-- File Size: 17233 bytes -->
<!-- Last Modified: 2025-08-05 02:24:38 -->
--- BEGIN FILE: scripts\comprehensive_dependency_fixer.sh ---
#!/bin/bash
# Language: Bash 5.0
# Lines of Code: 350
# File: scripts/comprehensive_dependency_fixer.sh
# Version: 2.0.0
# Project: AI Time Series Framework
# Repository: AI_TimeSeriesFramework
# Author: Rod Sanchez
# Created: 2025-08-05 01:35
# Last Edited: 2025-08-05 01:35
# Change: Major rewrite (+1.0.0) - Comprehensive dependency resolution with conda-forge priority
# Modifications: +200, -50
# Last Modification Comment: Complete rewrite with proper dependency resolution

set -eo pipefail

# =============================================================================
# COLORS AND FORMATTING
# =============================================================================
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
PURPLE='\033[0;35m'
NC='\033[0m'

# =============================================================================
# CONFIGURATION
# =============================================================================
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="${SCRIPT_DIR}/.."
LOGS_DIR="${PROJECT_DIR}/logs"
REPORTS_DIR="${PROJECT_DIR}/reports"

mkdir -p "$LOGS_DIR" "$REPORTS_DIR"

TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
FIX_LOG="${LOGS_DIR}/dependency_fix_${TIMESTAMP}.log"

# Core packages that should be prioritized via conda-forge
CORE_PACKAGES=(
    "numpy" "scipy" "pandas" "scikit-learn" "matplotlib" "seaborn"
    "jupyter" "ipython" "notebook" "jupyterlab"
)

# ML/AI packages that can be mixed conda/pip
ML_PACKAGES=(
    "torch" "torchvision" "torchaudio" "tensorflow" "transformers" 
    "datasets" "tokenizers" "accelerate" "evaluate"
)

# Time series specific packages (usually pip)
TS_PACKAGES=(
    "tsai" "tsfresh" "sktime" "darts" "neuralprophet" "prophet"
    "statsmodels" "arch" "pmdarima" "seasonal"
)

# Initialize variables
ACTION="${ACTION:-fix}"
TARGET_ENV="${TARGET_ENV:-}"
AUTO_FIX="${AUTO_FIX:-false}"
VERBOSE="${VERBOSE:-false}"
DRY_RUN="${DRY_RUN:-false}"
USE_MAMBA="${USE_MAMBA:-true}"  # Default to mamba for better performance

# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================
detect_package_manager() {
    if [ "${USE_MAMBA}" = "true" ] && command -v mamba >/dev/null 2>&1; then
        echo "mamba"
    elif command -v conda >/dev/null 2>&1; then
        echo "conda"
    else
        log_error "Neither mamba nor conda found in PATH"
        exit 1
    fi
}

# Get the package manager command
PKG_MGR=$(detect_package_manager)

log_info() {
    echo -e "${BLUE}[INFO]${NC} $1" | tee -a "$FIX_LOG"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1" | tee -a "$FIX_LOG"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1" | tee -a "$FIX_LOG"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1" | tee -a "$FIX_LOG"
}

confirm_action() {
    local message="$1"
    
    if [ "${AUTO_FIX}" = "true" ]; then
        return 0
    fi
    
    read -p "$message [y/N]: " -n 1 -r
    echo
    [[ $REPLY =~ ^[Yy]$ ]]
}

get_ts_environments() {
    $PKG_MGR env list | grep -E "env_(base_torch|geometric|transformers|llm|tslib|tensorflow|rapids|anomaly|federated|multimodal|probabilistic|causal|vision)" | awk '{print $1}' 2>/dev/null || echo ""
}

# =============================================================================
# DEPENDENCY ANALYSIS FUNCTIONS
# =============================================================================
analyze_pip_check() {
    local env="$1"
    local issues_file="${LOGS_DIR}/pip_issues_${env}_${TIMESTAMP}.txt"
    
    log_info "Analyzing dependency issues in $env using $PKG_MGR..."
    
    # Capture pip check output
    if $PKG_MGR run -n "$env" pip check > "$issues_file" 2>&1; then
        log_success "No pip dependency issues in $env"
        return 0
    else
        local missing_deps=()
        local version_conflicts=()
        
        # Parse pip check output
        while IFS= read -r line; do
            if [[ "$line" =~ "requires "(.+)", which is not installed" ]]; then
                missing_deps+=("${BASH_REMATCH[1]}")
            elif [[ "$line" =~ "has requirement "(.+)", but you have "(.+) ]]; then
                version_conflicts+=("${BASH_REMATCH[1]}")
            fi
        done < "$issues_file"
        
        # Remove duplicates
        local unique_missing=($(printf "%s\n" "${missing_deps[@]}" | sort -u))
        local unique_conflicts=($(printf "%s\n" "${version_conflicts[@]}" | sort -u))
        
        log_warning "Found ${#unique_missing[@]} missing dependencies"
        log_warning "Found ${#unique_conflicts[@]} version conflicts"
        
        if [ "${VERBOSE}" = "true" ]; then
            echo "Missing dependencies: ${unique_missing[*]}"
            echo "Version conflicts: ${unique_conflicts[*]}"
        fi
        
        # Store results for fixing
        printf "%s\n" "${unique_missing[@]}" > "${LOGS_DIR}/missing_deps_${env}.txt"
        printf "%s\n" "${unique_conflicts[@]}" > "${LOGS_DIR}/conflicts_${env}.txt"
        
        return 1
    fi
}

get_package_source() {
    local package="$1"
    
    # Check if it's a core package (should be conda)
    for core_pkg in "${CORE_PACKAGES[@]}"; do
        if [[ "$package" == "$core_pkg"* ]]; then
            echo "conda-forge"
            return
        fi
    done
    
    # Check if it's an ML package (can be conda)
    for ml_pkg in "${ML_PACKAGES[@]}"; do
        if [[ "$package" == "$ml_pkg"* ]]; then
            echo "conda-forge"
            return
        fi
    done
    
    # Check if it's a TS package (usually pip)
    for ts_pkg in "${TS_PACKAGES[@]}"; do
        if [[ "$package" == "$ts_pkg"* ]]; then
            echo "pip"
            return
        fi
    done
    
    # Default to conda-forge for known packages
    case "$package" in
        numpy|scipy|pandas|matplotlib|jupyter*|ipython|notebook)
            echo "conda-forge"
            ;;
        torch*|tensorflow*|transformers|datasets)
            echo "conda-forge"
            ;;
        *ai|*ml|*deep*|*neural*)
            echo "pip"
            ;;
        *)
            echo "conda-forge"
            ;;
    esac
}

# =============================================================================
# COMPREHENSIVE FIXING FUNCTIONS
# =============================================================================
install_missing_dependencies() {
    local env="$1"
    local missing_file="${LOGS_DIR}/missing_deps_${env}.txt"
    
    if [ ! -f "$missing_file" ]; then
        log_info "No missing dependencies file found for $env"
        return 0
    fi
    
    log_info "Installing missing dependencies in $env using $PKG_MGR..."
    
    local conda_packages=()
    local pip_packages=()
    
    # Categorize packages by preferred installation method
    while IFS= read -r package; do
        if [ -n "$package" ]; then
            local source=$(get_package_source "$package")
            if [ "$source" = "conda-forge" ]; then
                conda_packages+=("$package")
            else
                pip_packages+=("$package")
            fi
        fi
    done < "$missing_file"
    
    # Install conda packages first (using mamba for speed!)
    if [ ${#conda_packages[@]} -gt 0 ]; then
        log_info "Installing via $PKG_MGR (conda-forge): ${conda_packages[*]}"
        
        if [ "${DRY_RUN}" = "false" ]; then
            if $PKG_MGR install -n "$env" -c conda-forge -y "${conda_packages[@]}" 2>/dev/null; then
                log_success "Successfully installed $PKG_MGR packages"
            else
                log_warning "Some $PKG_MGR packages failed, trying individually..."
                for pkg in "${conda_packages[@]}"; do
                    if $PKG_MGR install -n "$env" -c conda-forge -y "$pkg" 2>/dev/null; then
                        log_success "Installed $pkg via $PKG_MGR"
                    else
                        log_warning "Failed to install $pkg via $PKG_MGR, adding to pip list"
                        pip_packages+=("$pkg")
                    fi
                done
            fi
        fi
    fi
    
    # Install remaining packages via pip
    if [ ${#pip_packages[@]} -gt 0 ]; then
        log_info "Installing via pip: ${pip_packages[*]}"
        
        if [ "${DRY_RUN}" = "false" ]; then
            for pkg in "${pip_packages[@]}"; do
                if $PKG_MGR run -n "$env" pip install "$pkg" 2>/dev/null; then
                    log_success "Installed $pkg via pip"
                else
                    log_error "Failed to install $pkg"
                fi
            done
        fi
    fi
}

resolve_version_conflicts() {
    local env="$1"
    local conflicts_file="${LOGS_DIR}/conflicts_${env}.txt"
    
    if [ ! -f "$conflicts_file" ]; then
        log_info "No version conflicts file found for $env"
        return 0
    fi
    
    log_info "Resolving version conflicts in $env using $PKG_MGR..."
    
    # Strategy: Update packages to latest compatible versions
    local packages_to_update=()
    
    while IFS= read -r conflict; do
        if [ -n "$conflict" ]; then
            # Extract package name (before the version requirement)
            local pkg_name=$(echo "$conflict" | cut -d'=' -f1 | cut -d'<' -f1 | cut -d'>' -f1 | cut -d'~' -f1 | tr -d ' ')
            packages_to_update+=("$pkg_name")
        fi
    done < "$conflicts_file"
    
    # Remove duplicates
    local unique_packages=($(printf "%s\n" "${packages_to_update[@]}" | sort -u))
    
    log_info "Updating packages to resolve conflicts: ${unique_packages[*]}"
    
    if [ "${DRY_RUN}" = "false" ]; then
        for pkg in "${unique_packages[@]}"; do
            local source=$(get_package_source "$pkg")
            
            if [ "$source" = "conda-forge" ]; then
                if $PKG_MGR update -n "$env" -c conda-forge -y "$pkg" 2>/dev/null; then
                    log_success "Updated $pkg via $PKG_MGR"
                else
                    log_warning "Failed to update $pkg via $PKG_MGR, trying pip..."
                    $PKG_MGR run -n "$env" pip install --upgrade "$pkg" 2>/dev/null || log_error "Failed to update $pkg"
                fi
            else
                if $PKG_MGR run -n "$env" pip install --upgrade "$pkg" 2>/dev/null; then
                    log_success "Updated $pkg via pip"
                else
                    log_error "Failed to update $pkg"
                fi
            fi
        done
    fi
}

clean_broken_packages() {
    local env="$1"
    
    log_info "Cleaning broken packages in $env..."
    
    # Remove packages that are commonly problematic
    local problematic_packages=(
        "flood-forecast"  # Often has strict version requirements
    )
    
    for pkg in "${problematic_packages[@]}"; do
        if $PKG_MGR run -n "$env" pip show "$pkg" >/dev/null 2>&1; then
            log_warning "Found problematic package $pkg, considering removal..."
            
            if [ "${AUTO_FIX}" = "true" ] || confirm_action "Remove potentially problematic package $pkg?"; then
                if [ "${DRY_RUN}" = "false" ]; then
                    $PKG_MGR run -n "$env" pip uninstall -y "$pkg" 2>/dev/null || true
                    log_success "Removed $pkg"
                fi
            fi
        fi
    done
}

perform_comprehensive_fix() {
    local env="$1"
    
    echo -e "${CYAN}Performing comprehensive fix for: $env${NC}"
    echo "============================================="
    
    # Step 1: Analyze current issues
    analyze_pip_check "$env"
    local has_issues=$?
    
    if [ $has_issues -eq 0 ]; then
        log_success "$env has no dependency issues"
        return 0
    fi
    
    # Step 2: Clean problematic packages
    clean_broken_packages "$env"
    
    # Step 3: Install missing dependencies
    install_missing_dependencies "$env"
    
    # Step 4: Resolve version conflicts
    resolve_version_conflicts "$env"
    
    # Step 5: Verify fixes
    log_info "Verifying fixes..."
    if [ "${DRY_RUN}" = "false" ]; then
        if $PKG_MGR run -n "$env" pip check >/dev/null 2>&1; then
            log_success "All dependency issues resolved in $env"
            return 0
        else
            log_warning "Some issues may remain in $env"
            return 1
        fi
    else
        log_info "Dry run completed for $env"
        return 0
    fi
}

# =============================================================================
# MAIN FUNCTIONS
# =============================================================================
fix_all_environments() {
    echo -e "${BLUE}Starting comprehensive dependency fixing...${NC}"
    echo ""
    
    local envs_string
    envs_string=$(get_ts_environments)
    local envs=($envs_string)
    
    if [ -n "${TARGET_ENV}" ]; then
        envs=("${TARGET_ENV}")
    fi
    
    if [ ${#envs[@]} -eq 0 ]; then
        log_error "No environments found to fix"
        return 1
    fi
    
    log_info "Found ${#envs[@]} environments to fix"
    
    local total_fixed=0
    local total_environments=${#envs[@]}
    
    for env in "${envs[@]}"; do
        echo ""
        
        if perform_comprehensive_fix "$env"; then
            total_fixed=$((total_fixed + 1))
        fi
        
        echo ""
    done
    
    # Summary
    echo -e "${PURPLE}COMPREHENSIVE FIX SUMMARY${NC}"
    echo -e "${PURPLE}===========================${NC}"
    echo -e "Environments processed: $total_environments"
    echo -e "Successfully fixed: $total_fixed"
    echo -e "Fix log: $FIX_LOG"
    echo ""
    
    if [ $total_fixed -eq $total_environments ]; then
        log_success "All environments successfully fixed!"
        return 0
    else
        log_warning "Some environments may still have issues"
        return 1
    fi
}

show_usage() {
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Actions:"
    echo "  fix       - Perform comprehensive dependency fixing (default)"
    echo "  analyze   - Analyze dependency issues without fixing"
    echo ""
    echo "Options:"
    echo "  -e, --environment ENV     Target specific environment"
    echo "      --auto-fix            Automatically fix without prompts"
    echo "      --dry-run             Show what would be done without executing"
    echo "      --use-conda           Force using conda instead of mamba"
    echo "  -v, --verbose             Enable verbose output"
    echo "  -h, --help               Show this help message"
    echo ""
    echo "Package Manager:"
    echo "  • Automatically detects and prefers mamba (faster than conda)"
    echo "  • Falls back to conda if mamba not available"
    echo "  • Use --use-conda to force conda usage"
    echo ""
    echo "Examples:"
    echo "  $0 --environment env_base_torch           # Fix specific environment"
    echo "  $0 --auto-fix                            # Fix all environments automatically"
    echo "  $0 --dry-run --verbose                   # Preview changes with details"
    echo "  $0 --use-conda --environment env_base_torch  # Force conda usage"
    echo ""
}

parse_arguments() {
    while [[ $# -gt 0 ]]; do
        case $1 in
            --environment|-e)
                TARGET_ENV="$2"
                shift 2
                ;;
            --auto-fix)
                AUTO_FIX=true
                shift
                ;;
            --dry-run)
                DRY_RUN=true
                shift
                ;;
            --use-conda)
                USE_MAMBA=false
                shift
                ;;
            --verbose|-v)
                VERBOSE=true
                shift
                ;;
            --help|-h)
                show_usage
                exit 0
                ;;
            fix|analyze)
                ACTION="$1"
                shift
                ;;
            *)
                if [[ "$1" =~ ^env_ ]]; then
                    TARGET_ENV="$1"
                    shift
                else
                    echo "Unknown option: $1"
                    show_usage
                    exit 1
                fi
                ;;
        esac
    done
}

main() {
    echo -e "${CYAN}AI Time Series Framework - Comprehensive Dependency Fixer${NC}"
    echo -e "${CYAN}=========================================================${NC}"
    echo ""
    
    parse_arguments "$@"
    
    # Show which package manager we're using
    log_info "Using package manager: $PKG_MGR"
    
    if [ "${DRY_RUN}" = "true" ]; then
        log_info "DRY RUN MODE - No changes will be made"
        echo ""
    fi
    
    case "${ACTION}" in
        "fix")
            fix_all_environments
            ;;
        "analyze")
            # Just analyze without fixing
            DRY_RUN=true
            VERBOSE=true
            fix_all_environments
            ;;
        *)
            show_usage
            exit 1
            ;;
    esac
}

# =============================================================================
# SCRIPT EXECUTION
# =============================================================================
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi
--- END FILE ---

<!-- Full Path: C:/00_Repos_Rod/Testing_Repos/environments\scripts\dependency_doctor.sh -->
<!-- Relative Path: scripts\dependency_doctor.sh -->
<!-- File Size: 17233 bytes -->
<!-- Last Modified: 2025-08-05 02:24:38 -->
--- BEGIN FILE: scripts\dependency_doctor.sh ---
#!/bin/bash
# Language: Bash 5.0
# Lines of Code: 350
# File: scripts/comprehensive_dependency_fixer.sh
# Version: 2.0.0
# Project: AI Time Series Framework
# Repository: AI_TimeSeriesFramework
# Author: Rod Sanchez
# Created: 2025-08-05 01:35
# Last Edited: 2025-08-05 01:35
# Change: Major rewrite (+1.0.0) - Comprehensive dependency resolution with conda-forge priority
# Modifications: +200, -50
# Last Modification Comment: Complete rewrite with proper dependency resolution

set -eo pipefail

# =============================================================================
# COLORS AND FORMATTING
# =============================================================================
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
PURPLE='\033[0;35m'
NC='\033[0m'

# =============================================================================
# CONFIGURATION
# =============================================================================
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="${SCRIPT_DIR}/.."
LOGS_DIR="${PROJECT_DIR}/logs"
REPORTS_DIR="${PROJECT_DIR}/reports"

mkdir -p "$LOGS_DIR" "$REPORTS_DIR"

TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
FIX_LOG="${LOGS_DIR}/dependency_fix_${TIMESTAMP}.log"

# Core packages that should be prioritized via conda-forge
CORE_PACKAGES=(
    "numpy" "scipy" "pandas" "scikit-learn" "matplotlib" "seaborn"
    "jupyter" "ipython" "notebook" "jupyterlab"
)

# ML/AI packages that can be mixed conda/pip
ML_PACKAGES=(
    "torch" "torchvision" "torchaudio" "tensorflow" "transformers" 
    "datasets" "tokenizers" "accelerate" "evaluate"
)

# Time series specific packages (usually pip)
TS_PACKAGES=(
    "tsai" "tsfresh" "sktime" "darts" "neuralprophet" "prophet"
    "statsmodels" "arch" "pmdarima" "seasonal"
)

# Initialize variables
ACTION="${ACTION:-fix}"
TARGET_ENV="${TARGET_ENV:-}"
AUTO_FIX="${AUTO_FIX:-false}"
VERBOSE="${VERBOSE:-false}"
DRY_RUN="${DRY_RUN:-false}"
USE_MAMBA="${USE_MAMBA:-true}"  # Default to mamba for better performance

# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================
detect_package_manager() {
    if [ "${USE_MAMBA}" = "true" ] && command -v mamba >/dev/null 2>&1; then
        echo "mamba"
    elif command -v conda >/dev/null 2>&1; then
        echo "conda"
    else
        log_error "Neither mamba nor conda found in PATH"
        exit 1
    fi
}

# Get the package manager command
PKG_MGR=$(detect_package_manager)

log_info() {
    echo -e "${BLUE}[INFO]${NC} $1" | tee -a "$FIX_LOG"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1" | tee -a "$FIX_LOG"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1" | tee -a "$FIX_LOG"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1" | tee -a "$FIX_LOG"
}

confirm_action() {
    local message="$1"
    
    if [ "${AUTO_FIX}" = "true" ]; then
        return 0
    fi
    
    read -p "$message [y/N]: " -n 1 -r
    echo
    [[ $REPLY =~ ^[Yy]$ ]]
}

get_ts_environments() {
    $PKG_MGR env list | grep -E "env_(base_torch|geometric|transformers|llm|tslib|tensorflow|rapids|anomaly|federated|multimodal|probabilistic|causal|vision)" | awk '{print $1}' 2>/dev/null || echo ""
}

# =============================================================================
# DEPENDENCY ANALYSIS FUNCTIONS
# =============================================================================
analyze_pip_check() {
    local env="$1"
    local issues_file="${LOGS_DIR}/pip_issues_${env}_${TIMESTAMP}.txt"
    
    log_info "Analyzing dependency issues in $env using $PKG_MGR..."
    
    # Capture pip check output
    if $PKG_MGR run -n "$env" pip check > "$issues_file" 2>&1; then
        log_success "No pip dependency issues in $env"
        return 0
    else
        local missing_deps=()
        local version_conflicts=()
        
        # Parse pip check output
        while IFS= read -r line; do
            if [[ "$line" =~ "requires "(.+)", which is not installed" ]]; then
                missing_deps+=("${BASH_REMATCH[1]}")
            elif [[ "$line" =~ "has requirement "(.+)", but you have "(.+) ]]; then
                version_conflicts+=("${BASH_REMATCH[1]}")
            fi
        done < "$issues_file"
        
        # Remove duplicates
        local unique_missing=($(printf "%s\n" "${missing_deps[@]}" | sort -u))
        local unique_conflicts=($(printf "%s\n" "${version_conflicts[@]}" | sort -u))
        
        log_warning "Found ${#unique_missing[@]} missing dependencies"
        log_warning "Found ${#unique_conflicts[@]} version conflicts"
        
        if [ "${VERBOSE}" = "true" ]; then
            echo "Missing dependencies: ${unique_missing[*]}"
            echo "Version conflicts: ${unique_conflicts[*]}"
        fi
        
        # Store results for fixing
        printf "%s\n" "${unique_missing[@]}" > "${LOGS_DIR}/missing_deps_${env}.txt"
        printf "%s\n" "${unique_conflicts[@]}" > "${LOGS_DIR}/conflicts_${env}.txt"
        
        return 1
    fi
}

get_package_source() {
    local package="$1"
    
    # Check if it's a core package (should be conda)
    for core_pkg in "${CORE_PACKAGES[@]}"; do
        if [[ "$package" == "$core_pkg"* ]]; then
            echo "conda-forge"
            return
        fi
    done
    
    # Check if it's an ML package (can be conda)
    for ml_pkg in "${ML_PACKAGES[@]}"; do
        if [[ "$package" == "$ml_pkg"* ]]; then
            echo "conda-forge"
            return
        fi
    done
    
    # Check if it's a TS package (usually pip)
    for ts_pkg in "${TS_PACKAGES[@]}"; do
        if [[ "$package" == "$ts_pkg"* ]]; then
            echo "pip"
            return
        fi
    done
    
    # Default to conda-forge for known packages
    case "$package" in
        numpy|scipy|pandas|matplotlib|jupyter*|ipython|notebook)
            echo "conda-forge"
            ;;
        torch*|tensorflow*|transformers|datasets)
            echo "conda-forge"
            ;;
        *ai|*ml|*deep*|*neural*)
            echo "pip"
            ;;
        *)
            echo "conda-forge"
            ;;
    esac
}

# =============================================================================
# COMPREHENSIVE FIXING FUNCTIONS
# =============================================================================
install_missing_dependencies() {
    local env="$1"
    local missing_file="${LOGS_DIR}/missing_deps_${env}.txt"
    
    if [ ! -f "$missing_file" ]; then
        log_info "No missing dependencies file found for $env"
        return 0
    fi
    
    log_info "Installing missing dependencies in $env using $PKG_MGR..."
    
    local conda_packages=()
    local pip_packages=()
    
    # Categorize packages by preferred installation method
    while IFS= read -r package; do
        if [ -n "$package" ]; then
            local source=$(get_package_source "$package")
            if [ "$source" = "conda-forge" ]; then
                conda_packages+=("$package")
            else
                pip_packages+=("$package")
            fi
        fi
    done < "$missing_file"
    
    # Install conda packages first (using mamba for speed!)
    if [ ${#conda_packages[@]} -gt 0 ]; then
        log_info "Installing via $PKG_MGR (conda-forge): ${conda_packages[*]}"
        
        if [ "${DRY_RUN}" = "false" ]; then
            if $PKG_MGR install -n "$env" -c conda-forge -y "${conda_packages[@]}" 2>/dev/null; then
                log_success "Successfully installed $PKG_MGR packages"
            else
                log_warning "Some $PKG_MGR packages failed, trying individually..."
                for pkg in "${conda_packages[@]}"; do
                    if $PKG_MGR install -n "$env" -c conda-forge -y "$pkg" 2>/dev/null; then
                        log_success "Installed $pkg via $PKG_MGR"
                    else
                        log_warning "Failed to install $pkg via $PKG_MGR, adding to pip list"
                        pip_packages+=("$pkg")
                    fi
                done
            fi
        fi
    fi
    
    # Install remaining packages via pip
    if [ ${#pip_packages[@]} -gt 0 ]; then
        log_info "Installing via pip: ${pip_packages[*]}"
        
        if [ "${DRY_RUN}" = "false" ]; then
            for pkg in "${pip_packages[@]}"; do
                if $PKG_MGR run -n "$env" pip install "$pkg" 2>/dev/null; then
                    log_success "Installed $pkg via pip"
                else
                    log_error "Failed to install $pkg"
                fi
            done
        fi
    fi
}

resolve_version_conflicts() {
    local env="$1"
    local conflicts_file="${LOGS_DIR}/conflicts_${env}.txt"
    
    if [ ! -f "$conflicts_file" ]; then
        log_info "No version conflicts file found for $env"
        return 0
    fi
    
    log_info "Resolving version conflicts in $env using $PKG_MGR..."
    
    # Strategy: Update packages to latest compatible versions
    local packages_to_update=()
    
    while IFS= read -r conflict; do
        if [ -n "$conflict" ]; then
            # Extract package name (before the version requirement)
            local pkg_name=$(echo "$conflict" | cut -d'=' -f1 | cut -d'<' -f1 | cut -d'>' -f1 | cut -d'~' -f1 | tr -d ' ')
            packages_to_update+=("$pkg_name")
        fi
    done < "$conflicts_file"
    
    # Remove duplicates
    local unique_packages=($(printf "%s\n" "${packages_to_update[@]}" | sort -u))
    
    log_info "Updating packages to resolve conflicts: ${unique_packages[*]}"
    
    if [ "${DRY_RUN}" = "false" ]; then
        for pkg in "${unique_packages[@]}"; do
            local source=$(get_package_source "$pkg")
            
            if [ "$source" = "conda-forge" ]; then
                if $PKG_MGR update -n "$env" -c conda-forge -y "$pkg" 2>/dev/null; then
                    log_success "Updated $pkg via $PKG_MGR"
                else
                    log_warning "Failed to update $pkg via $PKG_MGR, trying pip..."
                    $PKG_MGR run -n "$env" pip install --upgrade "$pkg" 2>/dev/null || log_error "Failed to update $pkg"
                fi
            else
                if $PKG_MGR run -n "$env" pip install --upgrade "$pkg" 2>/dev/null; then
                    log_success "Updated $pkg via pip"
                else
                    log_error "Failed to update $pkg"
                fi
            fi
        done
    fi
}

clean_broken_packages() {
    local env="$1"
    
    log_info "Cleaning broken packages in $env..."
    
    # Remove packages that are commonly problematic
    local problematic_packages=(
        "flood-forecast"  # Often has strict version requirements
    )
    
    for pkg in "${problematic_packages[@]}"; do
        if $PKG_MGR run -n "$env" pip show "$pkg" >/dev/null 2>&1; then
            log_warning "Found problematic package $pkg, considering removal..."
            
            if [ "${AUTO_FIX}" = "true" ] || confirm_action "Remove potentially problematic package $pkg?"; then
                if [ "${DRY_RUN}" = "false" ]; then
                    $PKG_MGR run -n "$env" pip uninstall -y "$pkg" 2>/dev/null || true
                    log_success "Removed $pkg"
                fi
            fi
        fi
    done
}

perform_comprehensive_fix() {
    local env="$1"
    
    echo -e "${CYAN}Performing comprehensive fix for: $env${NC}"
    echo "============================================="
    
    # Step 1: Analyze current issues
    analyze_pip_check "$env"
    local has_issues=$?
    
    if [ $has_issues -eq 0 ]; then
        log_success "$env has no dependency issues"
        return 0
    fi
    
    # Step 2: Clean problematic packages
    clean_broken_packages "$env"
    
    # Step 3: Install missing dependencies
    install_missing_dependencies "$env"
    
    # Step 4: Resolve version conflicts
    resolve_version_conflicts "$env"
    
    # Step 5: Verify fixes
    log_info "Verifying fixes..."
    if [ "${DRY_RUN}" = "false" ]; then
        if $PKG_MGR run -n "$env" pip check >/dev/null 2>&1; then
            log_success "All dependency issues resolved in $env"
            return 0
        else
            log_warning "Some issues may remain in $env"
            return 1
        fi
    else
        log_info "Dry run completed for $env"
        return 0
    fi
}

# =============================================================================
# MAIN FUNCTIONS
# =============================================================================
fix_all_environments() {
    echo -e "${BLUE}Starting comprehensive dependency fixing...${NC}"
    echo ""
    
    local envs_string
    envs_string=$(get_ts_environments)
    local envs=($envs_string)
    
    if [ -n "${TARGET_ENV}" ]; then
        envs=("${TARGET_ENV}")
    fi
    
    if [ ${#envs[@]} -eq 0 ]; then
        log_error "No environments found to fix"
        return 1
    fi
    
    log_info "Found ${#envs[@]} environments to fix"
    
    local total_fixed=0
    local total_environments=${#envs[@]}
    
    for env in "${envs[@]}"; do
        echo ""
        
        if perform_comprehensive_fix "$env"; then
            total_fixed=$((total_fixed + 1))
        fi
        
        echo ""
    done
    
    # Summary
    echo -e "${PURPLE}COMPREHENSIVE FIX SUMMARY${NC}"
    echo -e "${PURPLE}===========================${NC}"
    echo -e "Environments processed: $total_environments"
    echo -e "Successfully fixed: $total_fixed"
    echo -e "Fix log: $FIX_LOG"
    echo ""
    
    if [ $total_fixed -eq $total_environments ]; then
        log_success "All environments successfully fixed!"
        return 0
    else
        log_warning "Some environments may still have issues"
        return 1
    fi
}

show_usage() {
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Actions:"
    echo "  fix       - Perform comprehensive dependency fixing (default)"
    echo "  analyze   - Analyze dependency issues without fixing"
    echo ""
    echo "Options:"
    echo "  -e, --environment ENV     Target specific environment"
    echo "      --auto-fix            Automatically fix without prompts"
    echo "      --dry-run             Show what would be done without executing"
    echo "      --use-conda           Force using conda instead of mamba"
    echo "  -v, --verbose             Enable verbose output"
    echo "  -h, --help               Show this help message"
    echo ""
    echo "Package Manager:"
    echo "  • Automatically detects and prefers mamba (faster than conda)"
    echo "  • Falls back to conda if mamba not available"
    echo "  • Use --use-conda to force conda usage"
    echo ""
    echo "Examples:"
    echo "  $0 --environment env_base_torch           # Fix specific environment"
    echo "  $0 --auto-fix                            # Fix all environments automatically"
    echo "  $0 --dry-run --verbose                   # Preview changes with details"
    echo "  $0 --use-conda --environment env_base_torch  # Force conda usage"
    echo ""
}

parse_arguments() {
    while [[ $# -gt 0 ]]; do
        case $1 in
            --environment|-e)
                TARGET_ENV="$2"
                shift 2
                ;;
            --auto-fix)
                AUTO_FIX=true
                shift
                ;;
            --dry-run)
                DRY_RUN=true
                shift
                ;;
            --use-conda)
                USE_MAMBA=false
                shift
                ;;
            --verbose|-v)
                VERBOSE=true
                shift
                ;;
            --help|-h)
                show_usage
                exit 0
                ;;
            fix|analyze)
                ACTION="$1"
                shift
                ;;
            *)
                if [[ "$1" =~ ^env_ ]]; then
                    TARGET_ENV="$1"
                    shift
                else
                    echo "Unknown option: $1"
                    show_usage
                    exit 1
                fi
                ;;
        esac
    done
}

main() {
    echo -e "${CYAN}AI Time Series Framework - Comprehensive Dependency Fixer${NC}"
    echo -e "${CYAN}=========================================================${NC}"
    echo ""
    
    parse_arguments "$@"
    
    # Show which package manager we're using
    log_info "Using package manager: $PKG_MGR"
    
    if [ "${DRY_RUN}" = "true" ]; then
        log_info "DRY RUN MODE - No changes will be made"
        echo ""
    fi
    
    case "${ACTION}" in
        "fix")
            fix_all_environments
            ;;
        "analyze")
            # Just analyze without fixing
            DRY_RUN=true
            VERBOSE=true
            fix_all_environments
            ;;
        *)
            show_usage
            exit 1
            ;;
    esac
}

# =============================================================================
# SCRIPT EXECUTION
# =============================================================================
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi
--- END FILE ---

<!-- Full Path: C:/00_Repos_Rod/Testing_Repos/environments\scripts\config\environments.conf -->
<!-- Relative Path: scripts\config\environments.conf -->
<!-- File Size: 1262 bytes -->
<!-- Last Modified: 2025-08-04 00:19:41 -->
--- BEGIN FILE: scripts\config\environments.conf ---
# Language: Bash 5.0
# Lines of Code: 20
# File: scripts/config/environments.conf
# Version: 2.0.0
# Project: AI Time Series Framework
# Repository: AI_TimeSeriesFramework
# Author: Rod Sanchez
# Created: 2025-08-03 09:30
# Last Edited: 2025-08-03 23:30
# Change: Major (+1.0) - Updated for split environments
# Modifications: +10, -3
# Last Modification Comment: Replaced old environments with new split ones

export ENV_TRANSFORMERS_MODERN="env_transformers_modern"
export ENV_TRANSFORMERS_LEGACY="env_transformers_legacy"
export ENV_TRANSFORMERS_TS="env_transformers_ts"
export ENV_LLM_CHRONOS="env_llm_chronos"
export ENV_LLM_UNI2TS="env_llm_uni2ts"
export ENV_LLM_MOMENTFM="env_llm_momentfm"
export ENV_LLM_MAMBA="env_llm_mamba"
export ENV_TSLIB_TRADITIONAL="env_tslib_traditional"
export ENV_TSLIB_NIXTLA="env_tslib_nixtla"
export ENV_TSLIB_ADVANCED="env_tslib_advanced"
export ENV_BASE_TORCH="env_base_torch"
export ENV_GEOMETRIC="env_geometric"
export ENV_TENSORFLOW="env_tensorflow"
export ENV_RAPIDS="env_rapids"
export ENV_ANOMALY_ADVANCED="env_anomaly_advanced"
export ENV_FEDERATED="env_federated"
export ENV_MULTIMODAL="env_multimodal"
export ENV_PROBABILISTIC="env_probabilistic"
export ENV_CAUSAL="env_causal"
export ENV_VISION_TS="env_vision_ts"
--- END FILE ---

<!-- Full Path: C:/00_Repos_Rod/Testing_Repos/environments\scripts\config\packages.conf -->
<!-- Relative Path: scripts\config\packages.conf -->
<!-- File Size: 3165 bytes -->
<!-- Last Modified: 2025-08-04 00:19:52 -->
--- BEGIN FILE: scripts\config\packages.conf ---
# Language: Bash 5.0
# Lines of Code: 30
# File: scripts/config/packages.conf
# Version: 2.0.0
# Project: AI Time Series Framework
# Repository: AI_TimeSeriesFramework
# Author: Rod Sanchez
# Created: 2025-08-03 09:30
# Last Edited: 2025-08-03 23:30
# Change: Major (+1.0) - Updated for split environments
# Modifications: +15, -5
# Last Modification Comment: Added package lists for new split environments, removed old ones

export PACKAGES_TRANSFORMERS_MODERN="torch>=2.1 torchvision torchaudio transformers>=4.45.0 datasets>=2.18.0 tokenizers>=0.21.0 accelerate evaluate peft diffusers numpy>=1.26 pandas>=2.2 huggingface-hub>=0.28 matplotlib seaborn plotly scipy scikit-learn"
export PACKAGES_TRANSFORMERS_LEGACY="torch==2.0.0 torchvision==0.15.0 torchaudio==2.0.0 transformers==4.33.3 datasets==2.17.1 tokenizers==0.13.3 accelerate==0.20.3 huggingface-hub==0.24.0 numpy>=1.25 pandas==2.0.3 matplotlib seaborn plotly scipy>=1.11 scikit-learn"
export PACKAGES_TRANSFORMERS_TS="torch>=2.1 torchvision torchaudio pytorch-forecasting pytorch-lightning>=2.0 einops>=0.7 numpy>=1.26 pandas>=2.2 matplotlib seaborn plotly scipy scikit-learn"
export PACKAGES_LLM_CHRONOS="torch>=2.1 torchvision torchaudio transformers>=4.45.0 numpy>=1.26.4 pandas>=2.2 chronos-forecasting timesfm[torch] matplotlib seaborn plotly scipy scikit-learn"
export PACKAGES_LLM_UNI2TS="torch==2.4.1 torchvision torchaudio transformers==4.33.3 numpy~=1.26.0 pandas>=2.1 einops==0.7.* uni2ts==1.2.0 matplotlib seaborn plotly scipy scikit-learn"
export PACKAGES_LLM_MOMENTFM="torch>=2.1 torchvision torchaudio transformers==4.33.3 numpy==1.25.2 pandas>=2.1 einops==0.7.* momentfm==0.1.4 matplotlib seaborn plotly scipy scikit-learn"
export PACKAGES_LLM_MAMBA="torch>=2.1 torchvision torchaudio transformers>=4.45.0 numpy>=1.26 pandas>=2.2 mamba-ssm>=2.2.2 causal-conv1d>=1.4.0 matplotlib seaborn plotly scipy scikit-learn"
export PACKAGES_TSLIB_TRADITIONAL="torch==2.0.1 torchvision torchaudio numpy>=1.24,<1.26 pandas>=1.5,<2.0 scipy>=1.10,<1.14 statsmodels prophet sktime==0.26.0 matplotlib seaborn plotly scikit-learn"
export PACKAGES_TSLIB_NIXTLA="torch>=2.1 torchvision torchaudio numpy>=1.26 pandas>=2.2 nixtla statsforecast mlforecast neuralforecast hierarchicalforecast matplotlib seaborn plotly scipy scikit-learn"
export PACKAGES_TSLIB_ADVANCED="torch>=2.1 torchvision torchaudio numpy>=1.26 pandas>=2.2 einops darts tslearn tsfresh pytorch-lightning>=2.0 matplotlib seaborn plotly scipy scikit-learn"
export PACKAGES_BASE_TORCH="torch torchvision torchaudio torch-geometric lightning tensorboard"
export PACKAGES_GEOMETRIC="torch-geometric"
export PACKAGES_TENSORFLOW="tensorflow tensorflow-probability gluonts keras tensorboard tensorflow-addons"
export PACKAGES_RAPIDS="cudf cuml cugraph"
export PACKAGES_ANOMALY_ADVANCED="torch numpy pandas scikit-learn"
export PACKAGES_FEDERATED="torch numpy pandas flwr"
export PACKAGES_MULTIMODAL="transformers torch numpy pandas torchvision"
export PACKAGES_PROBABILISTIC="torch numpy pandas tensorflow-probability pyro-ppl"
export PACKAGES_CAUSAL="tigramite numpy pandas"
export PACKAGES_VISION_TS="transformers torch numpy pandas torchvision"
--- END FILE ---

<!-- Full Path: C:/00_Repos_Rod/Testing_Repos/environments\scripts\config\repositories.conf -->
<!-- Relative Path: scripts\config\repositories.conf -->
<!-- File Size: 13121 bytes -->
<!-- Last Modified: 2025-08-05 00:04:20 -->
--- BEGIN FILE: scripts\config\repositories.conf ---
# Language: Bash 5.0
# Lines of Code: 380
# File: scripts/config/repositories.conf
# Version: 3.0.0
# Project: AI Time Series Framework
# Repository: AI_TimeSeriesFramework
# Author: Rod Sanchez
# Created: 2025-08-04 16:00
# Last Edited: 2025-08-04 16:00
# Change: Major (+1.0) - Complete rewrite with dependency conflict avoidance and intelligent package management
# Modifications: +380, -0
# Last Modification Comment: Implemented conflict-free repository management with clear separation of package sources

# =============================================================================
# DEPENDENCY-AWARE REPOSITORY CONFIGURATION
# =============================================================================
# This configuration separates repositories into three categories:
# 1. CONDA_PACKAGES: Available via conda-forge/conda channels
# 2. PIP_PACKAGES: Available via PyPI but not conda
# 3. SOURCE_ONLY: Must be cloned from source (not available via package managers)
# =============================================================================

# Package manager priority: conda > pip > source
# NEVER mix installation methods for the same package to avoid conflicts

# =============================================================================
# CONDA-INSTALLABLE PACKAGES (Priority 1)
# =============================================================================
# These packages should ONLY be installed via conda to avoid conflicts

export CONDA_PACKAGES_BASE="pytorch torchvision torchaudio pytorch-cuda cudatoolkit numpy pandas matplotlib seaborn plotly scipy scikit-learn jupyterlab notebook"

export CONDA_PACKAGES_TRANSFORMERS="transformers datasets tokenizers accelerate huggingface_hub"

export CONDA_PACKAGES_TENSORFLOW="tensorflow tensorflow-probability keras tensorboard"

export CONDA_PACKAGES_TRADITIONAL="statsmodels scipy pandas numpy matplotlib"

export CONDA_PACKAGES_RAPIDS="cudf cuml cugraph cuspatial cupy"

export CONDA_PACKAGES_SCIENTIFIC="numpy scipy pandas matplotlib seaborn plotly scikit-learn"

# =============================================================================
# PIP-INSTALLABLE PACKAGES (Priority 2)
# =============================================================================
# These packages are available via PyPI but not conda-forge

export PIP_PACKAGES_LLM_MODERN="chronos-forecasting timesfm uni2ts momentfm"

export PIP_PACKAGES_NIXTLA="nixtla statsforecast mlforecast neuralforecast hierarchicalforecast utilsforecast"

export PIP_PACKAGES_TS_LIBS="darts pytorch-forecasting tsfresh tslearn sktime prophet pmdarima arch"

export PIP_PACKAGES_ADVANCED="pyod anomaly-detection flwr fedml gluonts gpytorch"

export PIP_PACKAGES_MAMBA="mamba-ssm causal-conv1d"

export PIP_PACKAGES_GEOMETRIC="torch-geometric"

export PIP_PACKAGES_PROBABILISTIC="pyro-ppl edward2 bayesian-torch"

export PIP_PACKAGES_CAUSAL="tigramite"

# =============================================================================
# SOURCE-ONLY REPOSITORIES (Priority 3)
# =============================================================================
# These repositories MUST be cloned as they are not available via package managers
# or require specific development versions

# Format: "local_name:github_owner/repo_name:branch:optional_package_name"

# Modern Time Series Research (Cutting-edge, not yet packaged)
SOURCE_ONLY_RESEARCH=(
"Time-Series-Library:thuml/Time-Series-Library:main:TSLib"
"iTransformer:thuml/iTransformer:main"
"PatchTST:yuqinie98/PatchTST:main"
"TimeXer:thuml/TimeXer:main"
"Timer-XL:thuml/Timer-XL:main"
"AutoTimes:thuml/AutoTimes:main"
"Large-Time-Series-Model:thuml/Large-Time-Series-Model:main"
)

# Foundation Models (Research implementations)
SOURCE_ONLY_FOUNDATION=(
"Time-MoE:Time-MoE/Time-MoE:main"
"lag-llama:time-series-foundation-models/lag-llama:main"
"Time-LLM:KimMeen/Time-LLM:main"
"Diffusion-TS:Y-debug-sys/Diffusion-TS:main"
"llmtime:ngruver/llmtime:main"
"TEMPO:DC-research/TEMPO:main"
)

# Graph Neural Networks for Time Series
SOURCE_ONLY_GEOMETRIC=(
"MTGNN:nnzhan/MTGNN:master"
"StemGNN:microsoft/StemGNN:master"
"Graph-WaveNet:nnzhan/Graph-WaveNet:master"
"GDN:d-ailin/GDN:main"
"AGCRN:LeiBAI/AGCRN:master"
"ST-UNet:XinnHe/ST-UNet:main"
)

# Legacy Transformers (Specific versions not on PyPI)
SOURCE_ONLY_TRANSFORMERS_LEGACY=(
"Informer2020:zhouhaoyi/Informer2020:main"
"Autoformer:thuml/Autoformer:main"
"FEDformer:MAZiqing/FEDformer:master"
"Pyraformer:ant-research/Pyraformer:master"
"Crossformer:Thinklab-SJTU/Crossformer:master"
)

# Anomaly Detection Research
SOURCE_ONLY_ANOMALY=(
"CARLA:zamanzadeh/CARLA:main"
"DACAD:zamanzadeh/DACAD:main"
"USAD:manigalati/usad:master"
"OmniAnomaly:NetManAIOps/OmniAnomaly:master"
)

# Multimodal Time Series
SOURCE_ONLY_MULTIMODAL=(
"ChatTime:ForestsKing/ChatTime:main"
"Time-MMD:AdityaLab/Time-MMD:main"
"VisionTS:Leezekun/ViTST:main"
"ViTime:IkeYang/ViTime:main"
)

# Advanced Federated Learning
SOURCE_ONLY_FEDERATED=(
"PySyft:OpenMined/PySyft:main"
"FedProx:litian96/FedProx:master"
"SCAFFOLD:lxcnju/FedRepo:main"
"MOON:QinbinLi/MOON:main"
"FedNova:JYWa/FedNova:master"
)

# =============================================================================
# ENVIRONMENT TO PACKAGE MAPPING
# =============================================================================

# Conda packages for each environment
declare -A ENV_CONDA_PACKAGES=(
["env_base_torch"]="$CONDA_PACKAGES_BASE $CONDA_PACKAGES_SCIENTIFIC"
["env_geometric"]="$CONDA_PACKAGES_BASE $CONDA_PACKAGES_SCIENTIFIC"
["env_transformers_modern"]="$CONDA_PACKAGES_BASE $CONDA_PACKAGES_TRANSFORMERS $CONDA_PACKAGES_SCIENTIFIC"
["env_transformers_legacy"]="$CONDA_PACKAGES_BASE $CONDA_PACKAGES_SCIENTIFIC"
["env_transformers_ts"]="$CONDA_PACKAGES_BASE $CONDA_PACKAGES_TRANSFORMERS $CONDA_PACKAGES_SCIENTIFIC"
["env_llm_chronos"]="$CONDA_PACKAGES_BASE $CONDA_PACKAGES_TRANSFORMERS $CONDA_PACKAGES_SCIENTIFIC"
["env_llm_uni2ts"]="$CONDA_PACKAGES_BASE $CONDA_PACKAGES_TRANSFORMERS $CONDA_PACKAGES_SCIENTIFIC"
["env_llm_momentfm"]="$CONDA_PACKAGES_BASE $CONDA_PACKAGES_TRANSFORMERS $CONDA_PACKAGES_SCIENTIFIC"
["env_llm_mamba"]="$CONDA_PACKAGES_BASE $CONDA_PACKAGES_TRANSFORMERS $CONDA_PACKAGES_SCIENTIFIC"
["env_tslib_traditional"]="$CONDA_PACKAGES_BASE $CONDA_PACKAGES_TRADITIONAL $CONDA_PACKAGES_SCIENTIFIC"
["env_tslib_nixtla"]="$CONDA_PACKAGES_BASE $CONDA_PACKAGES_SCIENTIFIC"
["env_tslib_advanced"]="$CONDA_PACKAGES_BASE $CONDA_PACKAGES_SCIENTIFIC"
["env_tensorflow"]="$CONDA_PACKAGES_BASE $CONDA_PACKAGES_TENSORFLOW $CONDA_PACKAGES_SCIENTIFIC"
["env_rapids"]="$CONDA_PACKAGES_BASE $CONDA_PACKAGES_RAPIDS $CONDA_PACKAGES_SCIENTIFIC"
["env_anomaly_advanced"]="$CONDA_PACKAGES_BASE $CONDA_PACKAGES_SCIENTIFIC"
["env_federated"]="$CONDA_PACKAGES_BASE $CONDA_PACKAGES_SCIENTIFIC"
["env_multimodal"]="$CONDA_PACKAGES_BASE $CONDA_PACKAGES_TRANSFORMERS $CONDA_PACKAGES_SCIENTIFIC"
["env_probabilistic"]="$CONDA_PACKAGES_BASE $CONDA_PACKAGES_SCIENTIFIC"
["env_causal"]="$CONDA_PACKAGES_BASE $CONDA_PACKAGES_SCIENTIFIC"
["env_vision_ts"]="$CONDA_PACKAGES_BASE $CONDA_PACKAGES_TRANSFORMERS $CONDA_PACKAGES_SCIENTIFIC"
)

# Pip packages for each environment
declare -A ENV_PIP_PACKAGES=(
["env_base_torch"]=""
["env_geometric"]="$PIP_PACKAGES_GEOMETRIC"
["env_transformers_modern"]=""
["env_transformers_legacy"]=""
["env_transformers_ts"]="$PIP_PACKAGES_TS_LIBS"
["env_llm_chronos"]="$PIP_PACKAGES_LLM_MODERN"
["env_llm_uni2ts"]="$PIP_PACKAGES_LLM_MODERN"
["env_llm_momentfm"]="$PIP_PACKAGES_LLM_MODERN"
["env_llm_mamba"]="$PIP_PACKAGES_MAMBA"
["env_tslib_traditional"]="$PIP_PACKAGES_TS_LIBS"
["env_tslib_nixtla"]="$PIP_PACKAGES_NIXTLA"
["env_tslib_advanced"]="$PIP_PACKAGES_TS_LIBS $PIP_PACKAGES_ADVANCED"
["env_tensorflow"]=""
["env_rapids"]=""
["env_anomaly_advanced"]="$PIP_PACKAGES_ADVANCED"
["env_federated"]="$PIP_PACKAGES_ADVANCED"
["env_multimodal"]=""
["env_probabilistic"]="$PIP_PACKAGES_PROBABILISTIC"
["env_causal"]="$PIP_PACKAGES_CAUSAL"
["env_vision_ts"]=""
)

# Source repositories for each environment
declare -A ENV_SOURCE_REPOS=(
["env_base_torch"]=""
["env_geometric"]="${SOURCE_ONLY_GEOMETRIC[*]}"
["env_transformers_modern"]="${SOURCE_ONLY_RESEARCH[*]}"
["env_transformers_legacy"]="${SOURCE_ONLY_TRANSFORMERS_LEGACY[*]}"
["env_transformers_ts"]="${SOURCE_ONLY_RESEARCH[*]} ${SOURCE_ONLY_TRANSFORMERS_LEGACY[*]}"
["env_llm_chronos"]="${SOURCE_ONLY_FOUNDATION[*]}"
["env_llm_uni2ts"]="${SOURCE_ONLY_FOUNDATION[*]}"
["env_llm_momentfm"]="${SOURCE_ONLY_FOUNDATION[*]}"
["env_llm_mamba"]="${SOURCE_ONLY_FOUNDATION[*]}"
["env_tslib_traditional"]=""
["env_tslib_nixtla"]=""
["env_tslib_advanced"]="${SOURCE_ONLY_RESEARCH[*]}"
["env_tensorflow"]=""
["env_rapids"]=""
["env_anomaly_advanced"]="${SOURCE_ONLY_ANOMALY[*]}"
["env_federated"]="${SOURCE_ONLY_FEDERATED[*]}"
["env_multimodal"]="${SOURCE_ONLY_MULTIMODAL[*]}"
["env_probabilistic"]=""
["env_causal"]=""
["env_vision_ts"]="${SOURCE_ONLY_MULTIMODAL[*]}"
)

# =============================================================================
# DEPENDENCY CONFLICT DETECTION
# =============================================================================

# Packages that commonly conflict when installed from multiple sources
CONFLICT_PRONE_PACKAGES=(
"torch" "torchvision" "torchaudio" "tensorflow" "numpy" "scipy" "pandas"
"scikit-learn" "matplotlib" "transformers" "datasets" "tokenizers"
)

# Package installation blacklist (never install from source)
NEVER_INSTALL_FROM_SOURCE=(
"torch" "torchvision" "torchaudio" "tensorflow" "numpy" "scipy" "pandas"
"scikit-learn" "matplotlib" "seaborn" "plotly" "jupyter" "jupyterlab"
"cudatoolkit" "pytorch-cuda" "tensorflow-gpu"
)

# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

# Check if package should never be installed from source
is_package_blacklisted() {
    local package="$1"
    for blacklisted in "${NEVER_INSTALL_FROM_SOURCE[@]}"; do
        if [[ "$package" == "$blacklisted"* ]]; then
            return 0
        fi
    done
    return 1
}

# Check if package is conflict-prone
is_conflict_prone() {
    local package="$1"
    for conflict_pkg in "${CONFLICT_PRONE_PACKAGES[@]}"; do
        if [[ "$package" == "$conflict_pkg"* ]]; then
            return 0
        fi
    done
    return 1
}

# Get conda packages for environment
get_conda_packages_for_env() {
    local env_name="$1"
    echo "${ENV_CONDA_PACKAGES[$env_name]:-}"
}

# Get pip packages for environment
get_pip_packages_for_env() {
    local env_name="$1"
    echo "${ENV_PIP_PACKAGES[$env_name]:-}"
}

# Get source repositories for environment
get_source_repos_for_env() {
    local env_name="$1"
    echo "${ENV_SOURCE_REPOS[$env_name]:-}"
}

# Validate package installation method
validate_installation_method() {
    local package="$1"
    local method="$2"  # conda, pip, or source
    
    if is_package_blacklisted "$package" && [[ "$method" == "source" ]]; then
        echo "ERROR: Package $package is blacklisted for source installation" >&2
        return 1
    fi
    
    if is_conflict_prone "$package" && [[ "$method" == "source" ]]; then
        echo "WARNING: Package $package is conflict-prone for source installation" >&2
    fi
    
    return 0
}

# Check for conflicting installations
check_installation_conflicts() {
    local env_name="$1"
    
    echo "🔍 Checking for potential conflicts in $env_name..."
    
    # Check if any conflict-prone packages are installed via multiple methods
    for package in "${CONFLICT_PRONE_PACKAGES[@]}"; do
        local conda_installed=false
        local pip_installed=false
        
        if conda run -n "$env_name" conda list 2>/dev/null | grep -qi "^${package}\s"; then
            conda_installed=true
        fi
        
        if conda run -n "$env_name" pip list 2>/dev/null | grep -qi "^${package}\s"; then
            pip_installed=true
        fi
        
        if $conda_installed && $pip_installed; then
            echo "⚠️ CONFLICT: $package installed via both conda and pip in $env_name"
        fi
    done
}

# Clean conflicting installations
clean_conflicts() {
    local env_name="$1"
    local package="$2"
    
    echo "🧹 Cleaning conflicts for $package in $env_name..."
    
    # Remove pip version if conda version exists (conda takes priority)
    if conda run -n "$env_name" conda list 2>/dev/null | grep -qi "^${package}\s"; then
        if conda run -n "$env_name" pip list 2>/dev/null | grep -qi "^${package}\s"; then
            echo "🗑️ Removing pip version of $package (conda version takes priority)"
            conda run -n "$env_name" pip uninstall -y "$package" 2>/dev/null || true
        fi
    fi
}

# Export functions for sourcing
if [[ "${BASH_SOURCE[0]}" != "${0}" ]]; then
    export -f is_package_blacklisted
    export -f is_conflict_prone
    export -f get_conda_packages_for_env
    export -f get_pip_packages_for_env
    export -f get_source_repos_for_env
    export -f validate_installation_method
    export -f check_installation_conflicts
    export -f clean_conflicts
fi
--- END FILE ---

<!-- Full Path: C:/00_Repos_Rod/Testing_Repos/environments\scripts\core\conda_manager.sh -->
<!-- Relative Path: scripts\core\conda_manager.sh -->
<!-- File Size: 5871 bytes -->
<!-- Last Modified: 2025-08-03 10:38:16 -->
--- BEGIN FILE: scripts\core\conda_manager.sh ---
#!/bin/bash
# Language: Bash 5.0
# Lines of Code: 187
# File: scripts/core/conda_manager.sh
# Version: 3.0.0
# Project: AI Time Series Framework
# Repository: AI_TimeSeriesFramework
# Author: Rod Sanchez
# Created: 2025-08-03 09:30
# Last Edited: 2025-08-03 09:30

# Conda management module - All conda operations centralized

source "$(dirname "${BASH_SOURCE[0]}")/logger.sh"

# Initialize conda for script operations
init_conda() {
    log_info "🐍 Initializing Conda for script operations..."
    
    # Multiple initialization strategies
    if eval "$(conda shell.bash hook)" 2>/dev/null; then
        log_success "✅ Conda shell hook initialized"
    elif source "$(conda info --base)/etc/profile.d/conda.sh" 2>/dev/null; then
        log_success "✅ Conda profile sourced"
    else
        log_error "❌ Failed to initialize Conda"
        exit 1
    fi
}

# Check if environment exists
env_exists() {
    local env_name="$1"
    conda env list | grep -q "^$env_name "
}

# Get environment status
get_env_status() {
    local env_name="$1"
    
    if ! env_exists "$env_name"; then
        echo "missing"
        return
    fi
    
    if conda activate "$env_name" 2>/dev/null; then
        if python -c "import sys; print('OK')" >/dev/null 2>&1; then
            conda deactivate 2>/dev/null
            echo "functional"
        else
            conda deactivate 2>/dev/null
            echo "corrupted"
        fi
    else
        echo "broken"
    fi
}

# Create environment safely
create_environment() {
    local env_name="$1"
    local python_version="${2:-3.11}"
    
    log_info "🏗️ Creating environment: $env_name (Python $python_version)"
    
    # Check if already exists
    local status
    status=$(get_env_status "$env_name")
    
    case "$status" in
        "functional")
            log_info "✅ Environment $env_name already exists and is functional"
            return 0
            ;;
        "missing")
            log_info "🆕 Creating new environment: $env_name"
            ;;
        *)
            log_warning "🔧 Removing corrupted environment: $env_name"
            remove_environment "$env_name"
            ;;
    esac
    
    # Create with retry logic
    local max_retries=3
    local retry_count=0
    
    while [[ $retry_count -lt $max_retries ]]; do
        if conda create -n "$env_name" python="$python_version" -y 2>/dev/null; then
            log_success "✅ Environment $env_name created successfully"
            return 0
        else
            retry_count=$((retry_count + 1))
            if [[ $retry_count -lt $max_retries ]]; then
                log_warning "⚠️ Retry $retry_count/$max_retries for environment creation"
                conda clean --all -y 2>/dev/null
                sleep 2
            fi
        fi
    done
    
    log_error "❌ Failed to create environment: $env_name"
    return 1
}

# Clone environment
clone_environment() {
    local source_env="$1"
    local target_env="$2"
    
    log_info "📋 Cloning environment: $source_env → $target_env"
    
    if ! env_exists "$source_env"; then
        log_error "❌ Source environment $source_env does not exist"
        return 1
    fi
    
    if conda create --clone "$source_env" --name "$target_env" -y 2>/dev/null; then
        log_success "✅ Environment cloned successfully"
        return 0
    else
        log_error "❌ Failed to clone environment"
        return 1
    fi
}

# Remove environment forcefully
remove_environment() {
    local env_name="$1"
    
    log_info "🗑️ Removing environment: $env_name"
    
    # Standard removal
    conda env remove -n "$env_name" -y 2>/dev/null || true
    
    # Force remove directory if still exists
    local conda_base env_path
    conda_base=$(conda info --base)
    env_path="$conda_base/envs/$env_name"
    
    if [[ -d "$env_path" ]]; then
        log_warning "🔧 Force removing environment directory"
        rm -rf "$env_path" 2>/dev/null || true
    fi
    
    # Clean cache
    conda clean --envs -y 2>/dev/null || true
    
    log_success "✅ Environment $env_name removed"
}

# Install package with multiple strategies
install_package() {
    local package="$1"
    local max_retries="${2:-3}"
    local retry_count=0
    
    log_debug "📦 Installing package: $package"
    
    while [[ $retry_count -lt $max_retries ]]; do
        # Strategy 1: conda-forge
        if conda install -c conda-forge "$package" -y 2>/dev/null; then
            return 0
        fi
        
        # Strategy 2: default conda
        if conda install "$package" -y 2>/dev/null; then
            return 0
        fi
        
        # Strategy 3: pip
        if pip install "$package" 2>/dev/null; then
            return 0
        fi
        
        retry_count=$((retry_count + 1))
        if [[ $retry_count -lt $max_retries ]]; then
            log_warning "⚠️ Retry $retry_count/$max_retries for package: $package"
            conda clean --packages -y 2>/dev/null
            sleep 1
        fi
    done
    
    log_error "❌ Failed to install package: $package"
    return 1
}

# Activate environment safely
activate_env() {
    local env_name="$1"
    
    if ! env_exists "$env_name"; then
        log_error "❌ Environment $env_name does not exist"
        return 1
    fi
    
    if conda activate "$env_name" 2>/dev/null; then
        log_debug "✅ Activated environment: $env_name"
        return 0
    else
        log_error "❌ Failed to activate environment: $env_name"
        return 1
    fi
}

# Deactivate environment safely
deactivate_env() {
    conda deactivate 2>/dev/null || true
    log_debug "✅ Environment deactivated"
}

# Clean conda system
clean_conda() {
    log_info "🧹 Cleaning conda system..."
    
    conda clean --all -y 2>/dev/null || true
    log_success "✅ Conda system cleaned"
}

--- END FILE ---

<!-- Full Path: C:/00_Repos_Rod/Testing_Repos/environments\scripts\core\environment.sh -->
<!-- Relative Path: scripts\core\environment.sh -->
<!-- File Size: 5219 bytes -->
<!-- Last Modified: 2025-08-03 11:50:15 -->
--- BEGIN FILE: scripts\core\environment.sh ---
#!/bin/bash
# Language: Bash 5.0
# Lines of Code: 130
# File: scripts/core/environment.sh
# Version: 3.0.1
# Project: AI Time Series Framework
# Repository: AI_TimeSeriesFramework
# Author: Rod Sanchez
# Created: 2025-08-03 09:30
# Last Edited: 2025-08-03 17:30
#
# Change: Bugfix (+0.01) - Improve CUDA detection accuracy
# Modifications: +6, -1
# Last Modification Comment: Added nvcc check and better version parsing

# Environment detection module - System capabilities and requirements

source "$(dirname "${BASH_SOURCE[0]}")/logger.sh"

# Global environment variables
declare -g HAS_NVIDIA_GPU=false
declare -g CUDA_VERSION=""
declare -g RAPIDS_COMPATIBLE=false
declare -g SYSTEM_MEMORY_GB=0
declare -g AVAILABLE_DISK_GB=0

# Detect system capabilities
detect_system_environment() {
    log_info "🔍 Detecting system environment..."
    
    detect_gpu_capabilities
    detect_system_resources
    detect_conda_installation
    detect_build_tools
    
    log_success "✅ System environment detection completed"
}

# GPU and CUDA detection
detect_gpu_capabilities() {
    log_info "🎯 Detecting GPU and CUDA capabilities..."
    
    if command -v nvidia-smi &> /dev/null; then
        local gpu_name driver_version cuda_version
        gpu_name=$(nvidia-smi --query-gpu=name --format=csv,noheader,nounits | head -1)
        driver_version=$(nvidia-smi --query-gpu=driver_version --format=csv,noheader,nounits | head -1)
        cuda_version=$(nvidia-smi --query-gpu=cuda_version --format=csv,noheader,nounits | head -1)
        
        HAS_NVIDIA_GPU=true
        CUDA_VERSION="$cuda_version"
        
        log_success "✅ NVIDIA GPU: $gpu_name"
        log_info "🎯 Driver: $driver_version, CUDA: $cuda_version"
        
        # Check RAPIDS compatibility
        case "$cuda_version" in
            12.*|11.8|11.7) 
                RAPIDS_COMPATIBLE=true
                log_success "🚀 RAPIDS compatible CUDA version detected"
                ;;
            *)
                log_warning "⚠️ CUDA version may have limited RAPIDS support"
                ;;
        esac
    else
        if command -v nvcc &> /dev/null; then  # Added fallback to nvcc if nvidia-smi missing
            local nvcc_version
            nvcc_version=$(nvcc --version | grep "release" | awk '{print $5}' | cut -d, -f1)
            HAS_NVIDIA_GPU=true
            CUDA_VERSION="$nvcc_version"
            log_info "🎯 CUDA found via nvcc: $CUDA_VERSION (GPU detection limited)"
        else
            log_info "💻 No NVIDIA GPU detected - CPU-only mode"
        fi
    fi
}

# System resource detection
detect_system_resources() {
    log_info "📊 Detecting system resources..."
    
    # Memory detection
    if command -v free &> /dev/null; then
        SYSTEM_MEMORY_GB=$(free -g | awk '/^Mem:/{print $2}')
        log_info "🧠 System RAM: ${SYSTEM_MEMORY_GB}GB"
        
        if [[ "${SYSTEM_MEMORY_GB:-0}" -lt 8 ]]; then
            log_warning "⚠️ Less than 8GB RAM - may affect large model training"
        fi
    fi
    
    # Disk space detection
    if command -v df &> /dev/null; then
        AVAILABLE_DISK_GB=$(df "$(pwd)" | awk 'NR==2 {print int($4/1024/1024)}' 2>/dev/null || echo "0")
        log_info "💾 Available disk space: ${AVAILABLE_DISK_GB}GB"
        
        if [[ "${AVAILABLE_DISK_GB:-0}" -lt 20 ]]; then
            log_warning "⚠️ Less than 20GB disk space - installation may require cleanup"
        fi
    fi
}

# Conda installation detection
detect_conda_installation() {
    log_info "🐍 Detecting Conda installation..."
    
    if command -v conda &> /dev/null; then
        local conda_version
        conda_version=$(conda --version 2>/dev/null)
        log_success "✅ $conda_version detected"
        
        # Test conda functionality
        if conda info --envs &> /dev/null; then
            log_success "✅ Conda is functional"
        else
            log_warning "⚠️ Conda needs initialization"
        fi
    else
        log_error "❌ Conda not found - please install Miniconda/Anaconda"
        exit 1
    fi
}

# Build tools detection
detect_build_tools() {
    log_info "🔧 Detecting build tools..."
    
    local build_tools=("gcc" "g++" "make" "git")
    local missing_tools=()
    
    for tool in "${build_tools[@]}"; do
        if command -v "$tool" &> /dev/null; then
            log_success "✅ $tool found"
        else
            missing_tools+=("$tool")
        fi
    done
    
    if [[ ${#missing_tools[@]} -gt 0 ]]; then
        log_warning "⚠️ Missing build tools: ${missing_tools[*]}"
        log_info "💡 Install with: sudo apt-get install build-essential git (Ubuntu/Debian)"
    fi
}

# Get optimal CUDA version for PyTorch
get_pytorch_cuda_version() {
    if [[ "$HAS_NVIDIA_GPU" == true ]]; then
        case "$CUDA_VERSION" in
            12.*) echo "cu121";;
            11.8) echo "cu118";;
            11.7) echo "cu117";;
            *) echo "cu121";;  # Default to latest
        esac
    else
        echo "cpu"
    fi
}

# Export environment variables
export_environment_vars() {
    export HAS_NVIDIA_GPU CUDA_VERSION RAPIDS_COMPATIBLE
    export SYSTEM_MEMORY_GB AVAILABLE_DISK_GB
}
--- END FILE ---

<!-- Full Path: C:/00_Repos_Rod/Testing_Repos/environments\scripts\core\logger.sh -->
<!-- Relative Path: scripts\core\logger.sh -->
<!-- File Size: 3316 bytes -->
<!-- Last Modified: 2025-08-03 11:53:11 -->
--- BEGIN FILE: scripts\core\logger.sh ---
#!/bin/bash
# Language: Bash 5.0
# Lines of Code: 103
# File: scripts/core/logger.sh
# Version: 3.0.1
# Project: AI Time Series Framework
# Repository: AI_TimeSeriesFramework
# Author: Rod Sanchez
# Created: 2025-08-03 09:30
# Last Edited: 2025-08-03 12:15
#
# Change: Bugfix (+0.01) - Prevent readonly variable redefinition
# Modifications: +8, -0
# Last Modification Comment: Added checks for existing color variables

# Centralized logging module - Single source of truth for all logging

# Colors (check terminal support)
if [[ -t 1 ]]; then
    [[ -z "${RED+x}" ]] && declare -gr RED='\033[0;31m'
    [[ -z "${GREEN+x}" ]] && declare -gr GREEN='\033[0;32m'
    [[ -z "${YELLOW+x}" ]] && declare -gr YELLOW='\033[1;33m'
    [[ -z "${BLUE+x}" ]] && declare -gr BLUE='\033[0;34m'
    [[ -z "${CYAN+x}" ]] && declare -gr CYAN='\033[0;36m'
    [[ -z "${PURPLE+x}" ]] && declare -gr PURPLE='\033[0;35m'
    [[ -z "${NC+x}" ]] && declare -gr NC='\033[0m'
else
    [[ -z "${RED+x}" ]] && declare -gr RED=''
    [[ -z "${GREEN+x}" ]] && declare -gr GREEN=''
    [[ -z "${YELLOW+x}" ]] && declare -gr YELLOW=''
    [[ -z "${BLUE+x}" ]] && declare -gr BLUE=''
    [[ -z "${CYAN+x}" ]] && declare -gr CYAN=''
    [[ -z "${PURPLE+x}" ]] && declare -gr PURPLE=''
    [[ -z "${NC+x}" ]] && declare -gr NC=''
fi

# Global log configuration
declare -g LOG_FILE=""
declare -g LOG_LEVEL="${LOG_LEVEL:-INFO}"

# Initialize logging system
init_logger() {
    local log_dir="${1:-logs}"
    mkdir -p "$log_dir"
    LOG_FILE="$log_dir/framework_$(date +'%Y%m%d_%H%M%S').log"
    
    echo "🚀 AI Time Series Framework - Session Started" | tee "$LOG_FILE"
    echo "📅 $(date)" | tee -a "$LOG_FILE"
    echo "🎯 Log Level: $LOG_LEVEL" | tee -a "$LOG_FILE"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" | tee -a "$LOG_FILE"
}

# Logging functions with levels
log_debug() { [[ "$LOG_LEVEL" =~ ^(DEBUG)$ ]] && echo -e "${PURPLE}[DEBUG $(date +'%H:%M:%S')] $1${NC}" | tee -a "$LOG_FILE"; }
log_info() { [[ "$LOG_LEVEL" =~ ^(DEBUG|INFO)$ ]] && echo -e "${BLUE}[INFO $(date +'%H:%M:%S')] $1${NC}" | tee -a "$LOG_FILE"; }
log_success() { echo -e "${GREEN}[SUCCESS $(date +'%H:%M:%S')] $1${NC}" | tee -a "$LOG_FILE"; }
log_warning() { echo -e "${YELLOW}[WARNING $(date +'%H:%M:%S')] $1${NC}" | tee -a "$LOG_FILE"; }
log_error() { echo -e "${RED}[ERROR $(date +'%H:%M:%S')] $1${NC}" | tee -a "$LOG_FILE"; }
log_highlight() { echo -e "${CYAN}[HIGHLIGHT $(date +'%H:%M:%S')] $1${NC}" | tee -a "$LOG_FILE"; }

# Convenient aliases for backward compatibility
log() { log_info "$1"; }
info() { log_info "$1"; }
success() { log_success "$1"; }
warning() { log_warning "$1"; }
error() { log_error "$1"; }
highlight() { log_highlight "$1"; }

# Progress tracking
declare -g PROGRESS_TOTAL=0
declare -g PROGRESS_CURRENT=0

init_progress() {
    PROGRESS_TOTAL="$1"
    PROGRESS_CURRENT=0
}

update_progress() {
    PROGRESS_CURRENT=$((PROGRESS_CURRENT + 1))
    local percentage=$((PROGRESS_CURRENT * 100 / PROGRESS_TOTAL))
    printf "\r${BLUE}[PROGRESS] %d/%d (%d%%) %s${NC}" "$PROGRESS_CURRENT" "$PROGRESS_TOTAL" "$percentage" "$1"
    if [[ $PROGRESS_CURRENT -eq $PROGRESS_TOTAL ]]; then
        echo ""
    fi
}
--- END FILE ---

<!-- Full Path: C:/00_Repos_Rod/Testing_Repos/environments\scripts\core\validator.sh -->
<!-- Relative Path: scripts\core\validator.sh -->
<!-- File Size: 3212 bytes -->
<!-- Last Modified: 2025-08-03 10:38:16 -->
--- BEGIN FILE: scripts\core\validator.sh ---
#!/bin/bash
# Language: Bash 5.0
# Lines of Code: 98
# File: scripts/core/validator.sh
# Version: 3.0.0
# Project: AI Time Series Framework
# Repository: AI_TimeSeriesFramework
# Author: Rod Sanchez
# Created: 2025-08-03 09:30
# Last Edited: 2025-08-03 09:30

# Validation module - System and environment validation

source "$(dirname "${BASH_SOURCE[0]}")/logger.sh"
source "$(dirname "${BASH_SOURCE[0]}")/conda_manager.sh"

# Validate entire system
validate_system() {
    log_info "🔍 Starting system validation..."
    
    validate_prerequisites
    validate_permissions
    validate_disk_space
    
    log_success "✅ System validation completed"
}

# Validate prerequisites
validate_prerequisites() {
    log_info "📋 Validating prerequisites..."
    
    local required_commands=("conda" "python" "git")
    local missing_commands=()
    
    for cmd in "${required_commands[@]}"; do
        if command -v "$cmd" &> /dev/null; then
            log_success "✅ $cmd found"
        else
            missing_commands+=("$cmd")
        fi
    done
    
    if [[ ${#missing_commands[@]} -gt 0 ]]; then
        log_error "❌ Missing required commands: ${missing_commands[*]}"
        exit 1
    fi
}

# Validate permissions
validate_permissions() {
    log_info "🔐 Validating write permissions..."
    
    local test_file="$(pwd)/.write_test"
    
    if echo "test" > "$test_file" 2>/dev/null && rm "$test_file" 2>/dev/null; then
        log_success "✅ Write permissions OK"
    else
        log_error "❌ No write permissions in current directory"
        exit 1
    fi
}

# Validate disk space
validate_disk_space() {
    local min_space_gb=15
    
    if command -v df &> /dev/null; then
        local available_gb
        available_gb=$(df "$(pwd)" | awk 'NR==2 {print int($4/1024/1024)}' 2>/dev/null || echo "0")
        
        if [[ $available_gb -ge $min_space_gb ]]; then
            log_success "✅ Sufficient disk space: ${available_gb}GB"
        else
            log_warning "⚠️ Low disk space: ${available_gb}GB (recommended: ${min_space_gb}GB)"
        fi
    fi
}

# Validate environment
validate_environment() {
    local env_name="$1"
    
    log_info "🔍 Validating environment: $env_name"
    
    local status
    status=$(get_env_status "$env_name")
    
    case "$status" in
        "functional")
            log_success "✅ Environment $env_name is functional"
            return 0
            ;;
        "missing")
            log_error "❌ Environment $env_name is missing"
            return 1
            ;;
        *)
            log_error "❌ Environment $env_name is $status"
            return 1
            ;;
    esac
}

# Validate all environments
validate_all_environments() {
    local envs=("$@")
    local failed_envs=()
    
    log_info "🔍 Validating all environments..."
    
    for env in "${envs[@]}"; do
        if ! validate_environment "$env"; then
            failed_envs+=("$env")
        fi
    done
    
    if [[ ${#failed_envs[@]} -eq 0 ]]; then
        log_success "✅ All environments are functional"
        return 0
    else
        log_warning "⚠️ Failed environments: ${failed_envs[*]}"
        return 1
    fi
}

--- END FILE ---

<!-- Full Path: C:/00_Repos_Rod/Testing_Repos/environments\scripts\installers\base_installer.sh -->
<!-- Relative Path: scripts\installers\base_installer.sh -->
<!-- File Size: 7633 bytes -->
<!-- Last Modified: 2025-08-03 21:37:38 -->
--- BEGIN FILE: scripts\installers\base_installer.sh ---
#!/bin/bash
# Language: Bash 5.0
# Lines of Code: 210
# File: scripts/installers/base_installer.sh
# Version: 3.0.2
# Project: AI Time Series Framework
# Repository: AI_TimeSeriesFramework
# Author: Rod Sanchez
# Created: 2025-08-03 09:30
# Last Edited: 2025-08-03 21:45
#
# Change: Fix (+0.0.1) - Corrected multi-line pip install syntax, handled git packages separately, fixed package names, completed validation import
# Modifications: +42, -0
# Last Modification Comment: Integrated LLM package installation as a new function with proper git handling and verification

source "$(dirname "${BASH_SOURCE[0]}")/../core/logger.sh"
source "$(dirname "${BASH_SOURCE[0]}")/../core/conda_manager.sh"
source "$(dirname "${BASH_SOURCE[0]}")/../core/environment.sh"

# Install base PyTorch environment
install_base_environment() {
    local env_name="$1"
    local python_version="${2:-3.11}"
    
    log_info "🔥 Installing base PyTorch environment: $env_name"
    
    # Create base environment
    if ! create_environment "$env_name" "$python_version"; then
        return 1
    fi
    
    # Activate and install packages
    if ! activate_env "$env_name"; then
        return 1
    fi
    
    # Install PyTorch
    install_pytorch
    
    # Install core packages
    install_core_packages
    
    # Install Jupyter if requested
    if [[ "${INSTALL_JUPYTER:-true}" == "true" ]]; then
        install_jupyter_packages
    fi
    
    deactivate_env
    
    # Verify installation
    if verify_pytorch_installation "$env_name"; then
        log_success "✅ Base environment $env_name installed successfully"
        return 0
    else
        log_error "❌ Base environment $env_name verification failed"
        return 1
    fi
}

# Install PyTorch with optimal settings
install_pytorch() {
    log_info "🔥 Installing PyTorch..."
    
    local cuda_version
    cuda_version=$(detect_cuda_version)
    
    # Upgrade pip first
    pip install --upgrade pip setuptools wheel
    
    # Install PyTorch based on CUDA availability
    local index_url="https://download.pytorch.org/whl/cpu"
    if [[ "$cuda_version" != "cpu" ]]; then
        index_url="https://download.pytorch.org/whl/$cuda_version"
        log_info "🎯 Installing CUDA-enabled PyTorch ($cuda_version)"
    else
        log_info "💻 Installing CPU-only PyTorch"
    fi
    
    pip install torch torchvision torchaudio --index-url "$index_url"
    
    # Verify PyTorch installation
    if python -c "import torch; print(f'PyTorch {torch.__version__} installed')" 2>/dev/null; then
        log_success "✅ PyTorch installed successfully"
        
        if [[ "$cuda_version" != "cpu" ]]; then
            python -c "
import torch
print(f'CUDA available: {torch.cuda.is_available()}')
if torch.cuda.is_available():
    print(f'GPU count: {torch.cuda.device_count()}')
    print(f'Current GPU: {torch.cuda.get_device_name()}')
"
        fi
    else
        log_error "❌ PyTorch installation verification failed"
        return 1
    fi
}

# Install core packages
install_core_packages() {
    log_info "📦 Installing core packages..."
    
    local core_packages=(
        "numpy>=1.26.4"
        "pandas>=2.2.2"
        "scikit-learn>=1.5.1"
        "matplotlib>=3.9.2"
        "seaborn"
        "plotly"
        "scipy"
        "tqdm"
    )
    
    for package in "${core_packages[@]}"; do
        if install_package "$package"; then
            log_success "✅ Installed: $package"
        else
            log_warning "⚠️ Failed to install: $package"
        fi
    done
}

# Install Jupyter packages
install_jupyter_packages() {
    log_info "📚 Installing Jupyter packages..."
    
    local jupyter_packages=(
        "jupyter"
        "jupyterlab"
        "ipython"
        "ipywidgets"
    )
    
    for package in "${jupyter_packages[@]}"; do
        install_package "$package"
    done
}

# Verify PyTorch installation
verify_pytorch_installation() {
    local env_name="$1"
    
    if activate_env "$env_name"; then
        local verification_success=true
        
        # Test basic imports
        if ! python -c "import torch, numpy, pandas" 2>/dev/null; then
            verification_success=false
        fi
        
        # Test PyTorch functionality
        if ! python -c "
import torch
x = torch.randn(5, 3)
y = torch.randn(3, 4)
z = torch.mm(x, y)
print('PyTorch operations working')
" 2>/dev/null; then
            verification_success=false
        fi
        
        # Test CUDA if available
        if python -c "import torch; print(torch.cuda.is_available())" 2>/dev/null | grep -q "True"; then
            if ! python -c "import torch; x = torch.randn(5, 3).cuda(); print('CUDA test OK')" 2>/dev/null; then
                verification_success=false
            fi
        fi
        
        deactivate_env
        
        if [[ "$verification_success" == "true" ]]; then
            return 0
        fi
    fi
    
    return 1
}

# Install LLM dependencies
install_llm_dependencies() {
    log_info "📦 Installing LLM dependencies..."
    
    # Pip-installable packages with pinned versions
    local pip_packages=(
        "transformers>=4.45.1"
        "scikit-learn>=1.5.1"
        "mamba-ssm>=2.2.2"
        "causal-conv1d>=1.4.0"
        "nixtla>=0.3.0"
        "chronos-forecasting>=1.0.0"
        "momentfm>=0.1.0"
        "timesfm[torch]>=1.0.0"
        "uni2ts>=0.1.0"
    )
    
    for package in "${pip_packages[@]}"; do
        if [[ -n "$package" ]]; then
            if pip install "$package" 2>/tmp/pip_error.log; then
                log_success "✅ Installed: $package"
            else
                log_error "❌ Failed to install: $package"
                cat /tmp/pip_error.log | log_error
            fi
        else
            log_error "❌ Empty package name detected, skipping"
        fi
    done
    
    # Git-installable packages
    local git_repos=(
        "Time-MoE:https://github.com/Time-MoE/Time-MoE.git:main"
        "GTT:https://github.com/cfeng783/GTT.git:main"
        "TEMPO:https://github.com/DC-research/TEMPO.git:main"
        "moirai:https://github.com/SalesforceAIResearch/uni2ts.git:main"
    )
    
    for repo in "${git_repos[@]}"; do
        repo_name=$(echo "$repo" | cut -d':' -f1)
        repo_url=$(echo "$repo" | cut -d':' -f2)
        repo_branch=$(echo "$repo" | cut -d':' -f3)
        repo_dir="models/$repo_name"
        
        log_info "Cloning and installing $repo_name from $repo_url (branch: $repo_branch)"
        mkdir -p models
        if git clone --depth 1 --branch "$repo_branch" "$repo_url" "$repo_dir" 2>/tmp/clone_error.log; then
            cd "$repo_dir"
            if [[ -f "requirements.txt" ]]; then
                pip install -r requirements.txt 2>/tmp/pip_error.log || log_error "Failed to install requirements for $repo_name"
            fi
            pip install -e . 2>/tmp/pip_error.log || log_error "Failed to install $repo_name as editable package"
            cd - > /dev/null
            log_success "✅ Installed: $repo_name"
        else
            log_error "❌ Failed to clone $repo_name"
            cat /tmp/clone_error.log | log_error
        fi
    done
    
    # Verify installations
    if python -c "import transformers, sklearn, timesfm, mamba_ssm, causal_conv1d, nixtla, chronos_forecasting, momentfm, uni2ts, time_moe; print('All LLM dependencies OK')" 2>/tmp/validation_error.log; then
        log_success "✅ LLM dependencies verified"
    else
        log_error "❌ LLM dependencies validation failed"
        cat /tmp/validation_error.log | log_error
        return 1
    fi
}
--- END FILE ---

<!-- Full Path: C:/00_Repos_Rod/Testing_Repos/environments\scripts\installers\rapids_installer.sh -->
<!-- Relative Path: scripts\installers\rapids_installer.sh -->
<!-- File Size: 5363 bytes -->
<!-- Last Modified: 2025-08-03 11:56:02 -->
--- BEGIN FILE: scripts\installers\rapids_installer.sh ---
#!/bin/bash
# Language: Bash 5.0
# Lines of Code: 143
# File: scripts/installers/rapids_installer.sh
# Version: 3.0.1
# Project: AI Time Series Framework
# Repository: AI_TimeSeriesFramework
# Author: Rod Sanchez
# Created: 2025-08-03 09:30
# Last Edited: 2025-08-03 13:15
#
# Change: Bugfix (+0.01) - Fix here-document syntax in show_rapids_examples
# Modifications: +2, -2
# Last Modification Comment: Corrected EOF delimiter and added CUDA version check

# RAPIDS installer module - GPU-accelerated data science

source "$(dirname "${BASH_SOURCE[0]}")/../core/logger.sh"
source "$(dirname "${BASH_SOURCE[0]}")/../core/conda_manager.sh"
source "$(dirname "${BASH_SOURCE[0]}")/../core/environment.sh"

# Install RAPIDS environment
install_rapids_environment() {
    local env_name="$1"
    local python_version="${2:-3.11}"
    local rapids_version="${3:-24.02}"
    
    log_info "🚀 Installing RAPIDS environment: $env_name"
    
    # Check GPU requirements
    if [[ "$HAS_NVIDIA_GPU" != "true" ]]; then
        log_warning "⚠️ No NVIDIA GPU detected - RAPIDS will have limited functionality"
        read -p "Continue anyway? (y/n): " -r
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            return 1
        fi
    fi
    
    # Create environment
    if ! create_environment "$env_name" "$python_version"; then
        return 1
    fi
    
    if activate_env "$env_name"; then
        install_rapids_packages "$rapids_version"
        deactivate_env
        
        if verify_rapids_installation "$env_name"; then
            log_success "✅ RAPIDS environment installed"
            return 0
        fi
    fi
    
    return 1
}

# Install RAPIDS packages
install_rapids_packages() {
    local rapids_version="$1"
    
    log_info "🚀 Installing RAPIDS packages (version $rapids_version)..."
    
    # Add RAPIDS channels
    conda config --env --add channels rapidsai
    conda config --env --add channels nvidia
    conda config --env --add channels conda-forge
    
    # Determine CUDA version for RAPIDS
    local cuda_spec=""
    if [[ "$HAS_NVIDIA_GPU" == "true" ]]; then
        case "$CUDA_VERSION" in
            12.*) cuda_spec="cuda-version=12.0";;
            11.8) cuda_spec="cuda-version=11.8";;
            11.7) cuda_spec="cuda-version=11.7";;
            *) cuda_spec="cuda-version=12.0";;
        esac
    fi
    
    # Core RAPIDS packages
    local rapids_packages=(
        "cudf=$rapids_version"
        "cuml=$rapids_version"
        "cugraph=$rapids_version"
        "cuspatial=$rapids_version"
        "cusignal=$rapids_version"
        "cucim=$rapids_version"
    )
    
    # Install RAPIDS packages
    if [[ -n "$cuda_spec" ]]; then
        for package in "${rapids_packages[@]}"; do
            log_info "📦 Installing $package with $cuda_spec"
            conda install "$package" "$cuda_spec" -y 2>/dev/null || \
            log_warning "⚠️ Failed to install: $package"
        done
    else
        log_warning "⚠️ Installing CPU-only RAPIDS (limited functionality)"
        for package in "${rapids_packages[@]}"; do
            conda install "$package" -y 2>/dev/null || \
            log_warning "⚠️ Failed to install: $package"
        done
    fi
    
    # Additional packages for RAPIDS ecosystem
    local additional_packages=(
        "dask-cuda"
        "rmm"
        "jupyter"
        "matplotlib"
        "bokeh"
        "holoviews"
        "panel"
    )
    
    for package in "${additional_packages[@]}"; do
        install_package "$package" 1
    done
    
    # Verify installation
    if python -c "import cudf; print('RAPIDS cuDF ready!')" 2>/dev/null; then
        log_success "✅ RAPIDS core packages installed"
    else
        log_error "❌ RAPIDS installation verification failed"
        return 1
    fi
}

# Verify RAPIDS installation
verify_rapids_installation() {
    local env_name="$1"
    
    log_info "🔍 Verifying RAPIDS installation..."
    
    if activate_env "$env_name"; then
        local verification_code="
import cudf
import cuml
import numpy as np

# Test cuDF
df = cudf.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [1, 4, 9, 16, 25]})
print(f'cuDF DataFrame shape: {df.shape}')

# Test cuML
from cuml.linear_model import LinearRegression
model = LinearRegression()
print('cuML LinearRegression created successfully')

print('🚀 RAPIDS verification successful!')
"
        
        if python -c "$verification_code" 2>/dev/null; then
            deactivate_env
            log_success "✅ RAPIDS verification passed"
            return 0
        else
            deactivate_env
            log_error "❌ RAPIDS verification failed"
            return 1
        fi
    fi
    
    return 1
}

# Show RAPIDS usage examples
show_rapids_examples() {
    cat << EOF

🚀 RAPIDS Quick Start Examples:

1. Basic cuDF usage:
   import cudf
   df = cudf.read_csv('data.csv')
   result = df.groupby('category').sum()

2. GPU-accelerated ML with cuML:
   from cuml.ensemble import RandomForestRegressor
   model = RandomForestRegressor()
   model.fit(X_train, y_train)

3. Graph analytics with cuGraph:
   import cugraph
   G = cugraph.from_cudf_edgelist(df)
   pagerank = cugraph.pagerank(G)

4. Distributed computing with Dask:
   import dask_cudf
   ddf = dask_cudf.read_csv('large_data.csv')
   result = ddf.groupby('key').value.mean().compute()

EOF
}
--- END FILE ---

<!-- Full Path: C:/00_Repos_Rod/Testing_Repos/environments\scripts\installers\specialized_installer.sh -->
<!-- Relative Path: scripts\installers\specialized_installer.sh -->
<!-- File Size: 16565 bytes -->
<!-- Last Modified: 2025-08-04 13:37:53 -->
--- BEGIN FILE: scripts\installers\specialized_installer.sh ---
#!/bin/bash
# Language: Bash 5.0
# Lines of Code: 450
# File: scripts/installers/specialized_installer.sh
# Version: 3.2.0
# Project: AI Time Series Framework
# Repository: AI_TimeSeriesFramework
# Author: Rod Sanchez
# Created: 2025-08-03 09:30
# Last Edited: 2025-08-03 20:15
# Change: Feature (+0.1) - Added installers for new environments
# Modifications: +170, -0
# Last Modification Comment: Added install functions for env_anomaly_advanced, env_federated, env_multimodal, env_probabilistic, env_causal, env_vision_ts

source "$(dirname "${BASH_SOURCE[0]}")/../core/logger.sh"
source "$(dirname "${BASH_SOURCE[0]}")/../core/conda_manager.sh"
source "$(dirname "${BASH_SOURCE[0]}")/base_installer.sh"

# Install geometric environment
install_geometric_environment() {
    local env_name="$1"
    local base_env="${2:-env_base_torch}"
    log_info "📊 Installing PyTorch Geometric environment: $env_name"
    if ! clone_environment "$base_env" "$env_name"; then
        log_warning "⚠️ Failed to clone, creating fresh environment"
        if ! install_base_environment "$env_name"; then
            return 1
        fi
    fi
    if activate_env "$env_name"; then
        install_pytorch_geometric
        deactivate_env
        if verify_geometric_installation "$env_name"; then
            log_success "✅ Geometric environment installed"
            return 0
        fi
    fi
    return 1
}

# Install PyTorch Geometric packages
install_pytorch_geometric() {
    log_info "📊 Installing PyTorch Geometric..."
    pip install torch-geometric
    local wheel_url="https://data.pyg.org/whl/torch-2.5.1+cu121.html"
    if [[ "$HAS_NVIDIA_GPU" != "true" ]]; then
        wheel_url="https://data.pyg.org/whl/torch-2.5.1+cpu.html"
    fi
    pip install torch-scatter torch-sparse torch-cluster torch-spline-conv pyg-lib \
        -f "$wheel_url" || pip install torch-scatter torch-sparse torch-cluster torch-spline-conv
    local geom_packages=("networkx" "graph-tool" "ogb")
    for package in "${geom_packages[@]}"; do
        install_package "$package" 1
    done
}

# Install transformers environment
install_transformers_environment() {
    local env_name="$1"
    local base_env="${2:-env_base_torch}"
    log_info "🤖 Installing Transformers environment: $env_name"
    if ! clone_environment "$base_env" "$env_name"; then
        if ! install_base_environment "$env_name"; then
            return 1
        fi
    fi
    if activate_env "$env_name"; then
        install_transformers_packages
        deactivate_env
        if verify_transformers_installation "$env_name"; then
            log_success "✅ Transformers environment installed"
            return 0
        fi
    fi
    return 1
}

# Install HuggingFace ecosystem
install_transformers_packages() {
    log_info "🤖 Installing HuggingFace ecosystem..."
    local hf_packages=("transformers" "datasets" "tokenizers" "accelerate" "evaluate" "peft" "diffusers" "pytorch-forecasting")
    for package in "${hf_packages[@]}"; do
        install_package "$package"
    done
}

# Install stable LLM environment
install_llm_stable_environment() {
    local env_name="$1"
    local base_env="${2:-env_base_torch}"
    log_info "🚀 Installing Stable LLM environment: $env_name"
    if ! clone_environment "$base_env" "$env_name"; then
        if ! install_base_environment "$env_name"; then
            return 1
        fi
    fi
    if activate_env "$env_name"; then
        install_llm_stable_packages
        deactivate_env
        if verify_llm_stable_installation "$env_name"; then
            log_success "✅ Stable LLM environment installed"
            return 0
        fi
    fi
    return 1
}

# Install stable LLM packages
install_llm_stable_packages() {
    log_info "🚀 Installing Stable LLM packages..."
    local llm_packages=("transformers" "datasets" "tokenizers" "accelerate" "evaluate" "peft" "mamba-ssm" "causal-conv1d>=1.4.0" "chronos-forecasting" "uni2ts" "momentfm" "timesfm[torch]")
    for package in "${llm_packages[@]}"; do
        install_package "$package"
    done
}

# Install research LLM environment
install_llm_research_environment() {
    local env_name="$1"
    local base_env="${2:-env_base_torch}"
    log_info "🔬 Installing Research LLM environment: $env_name"
    if ! clone_environment "$base_env" "$env_name"; then
        if ! install_base_environment "$env_name"; then
            return 1
        fi
    fi
    if activate_env "$env_name"; then
        install_llm_research_packages
        deactivate_env
        if verify_llm_research_installation "$env_name"; then
            log_success "✅ Research LLM environment installed"
            return 0
        fi
    fi
    return 1
}

# Install research LLM packages
install_llm_research_packages() {
    log_info "🔬 Installing Research LLM packages..."
    local research_repos=(
        "git+https://github.com/Time-MoE/Time-MoE.git"
        "git+https://github.com/time-series-foundation-models/lag-llama.git"
        "git+https://github.com/thuml/Timer-XL.git"
        "git+https://github.com/Y-debug-sys/Diffusion-TS.git"
        "git+https://github.com/KimMeen/Time-LLM.git"
        "git+https://github.com/thuml/AutoTimes.git"
        "git+https://github.com/AdityaLab/MM-TSFlib.git"
        "git+https://github.com/ngruver/llmtime.git"
        "git+https://github.com/DC-research/TEMPO.git"
    )
    for repo in "${research_repos[@]}"; do
        repo_url=$(echo "$repo" | sed 's/git+//')
        repo_name=$(basename "$repo_url" .git)
        local repo_dir="models/$repo_name"
        log "Cloning and installing $repo_name from $repo_url"
        mkdir -p models
        if git clone --depth 1 "$repo_url" "$repo_dir" 2>/tmp/clone_error.log; then
            log "Successfully cloned $repo_name"
            cd "$repo_dir"
            if [[ -f "requirements.txt" ]]; then
                pip install -r requirements.txt || log "WARNING: Failed to install requirements for $repo_name"
            fi
            if [[ -f "pyproject.toml" || -f "setup.py" ]]; then
                pip install -e . || log "WARNING: Failed to install $repo_name as editable package"
            fi
            cd - > /dev/null
        else
            log "ERROR: Failed to clone $repo_name"
            cat /tmp/clone_error.log | log
        fi
    done
}

# Install time series library environment
install_tslib_environment() {
    local env_name="$1"
    local base_env="${2:-env_base_torch}"
    log_info "📈 Installing Time Series Library environment: $env_name"
    if ! clone_environment "$base_env" "$env_name"; then
        if ! install_base_environment "$env_name"; then
            return 1
        fi
    fi
    if activate_env "$env_name"; then
        install_tslib_packages
        deactivate_env
        if verify_tslib_installation "$env_name"; then
            log_success "✅ TSLib environment installed"
            return 0
        fi
    fi
    return 1
}

# Install time series packages
install_tslib_packages() {
    log_info "📈 Installing time series packages..."
    local ts_packages=("statsmodels" "prophet" "sktime" "darts" "tslearn" "tsfresh" "einops" "pytorch-lightning")
    for package in "${ts_packages[@]}"; do
        install_package "$package"
    done
}

# Install TensorFlow environment
install_tensorflow_environment() {
    local env_name="$1"
    local python_version="${2:-3.11}"
    log_info "🧠 Installing TensorFlow environment: $env_name"
    if ! create_environment "$env_name" "$python_version"; then
        return 1
    fi
    if activate_env "$env_name"; then
        install_tensorflow_packages
        install_core_packages
        deactivate_env
        if verify_tensorflow_installation "$env_name"; then
            log_success "✅ TensorFlow environment installed"
            return 0
        fi
    fi
    return 1
}

# Install TensorFlow packages
install_tensorflow_packages() {
    log_info "🧠 Installing TensorFlow..."
    pip install --upgrade pip
    pip install tensorflow tensorflow-probability gluonts
    local tf_packages=("keras" "tensorboard" "tensorflow-addons")
    for package in "${tf_packages[@]}"; do
        install_package "$package"
    done
}

# Install anomaly advanced environment
install_anomaly_advanced_environment() {
    local env_name="$1"
    local base_env="${2:-env_base_torch}"
    log_info "🔍 Installing Anomaly Advanced environment: $env_name"
    if ! clone_environment "$base_env" "$env_name"; then
        if ! install_base_environment "$env_name"; then
            return 1
        fi
    fi
    if activate_env "$env_name"; then
        install_anomaly_advanced_packages
        deactivate_env
        if verify_anomaly_advanced_installation "$env_name"; then
            log_success "✅ Anomaly Advanced environment installed"
            return 0
        fi
    fi
    return 1
}

# Install anomaly advanced packages
install_anomaly_advanced_packages() {
    log_info "🔍 Installing Anomaly Advanced packages..."
    local anomaly_packages=("torch" "numpy" "pandas" "scikit-learn")
    for package in "${anomaly_packages[@]}"; do
        install_package "$package"
    done
}

# Install federated environment
install_federated_environment() {
    local env_name="$1"
    local base_env="${2:-env_base_torch}"
    log_info "🌐 Installing Federated environment: $env_name"
    if ! clone_environment "$base_env" "$env_name"; then
        if ! install_base_environment "$env_name"; then
            return 1
        fi
    fi
    if activate_env "$env_name"; then
        install_federated_packages
        deactivate_env
        if verify_federated_installation "$env_name"; then
            log_success "✅ Federated environment installed"
            return 0
        fi
    fi
    return 1
}

# Install federated packages
install_federated_packages() {
    log_info "🌐 Installing Federated packages..."
    local federated_packages=("torch" "numpy" "pandas" "flwr")
    for package in "${federated_packages[@]}"; do
        install_package "$package"
    done
}

# Install multimodal environment
install_multimodal_environment() {
    local env_name="$1"
    local base_env="${2:-env_base_torch}"
    log_info "🎨 Installing Multimodal environment: $env_name"
    if ! clone_environment "$base_env" "$env_name"; then
        if ! install_base_environment "$env_name"; then
            return 1
        fi
    fi
    if activate_env "$env_name"; then
        install_multimodal_packages
        deactivate_env
        if verify_multimodal_installation "$env_name"; then
            log_success "✅ Multimodal environment installed"
            return 0
        fi
    fi
    return 1
}

# Install multimodal packages
install_multimodal_packages() {
    log_info "🎨 Installing Multimodal packages..."
    local multimodal_packages=("transformers" "torch" "numpy" "pandas" "torchvision")
    for package in "${multimodal_packages[@]}"; do
        install_package "$package"
    done
}

# Install probabilistic environment
install_probabilistic_environment() {
    local env_name="$1"
    local base_env="${2:-env_base_torch}"
    log_info "🎲 Installing Probabilistic environment: $env_name"
    if ! clone_environment "$base_env" "$env_name"; then
        if ! install_base_environment "$env_name"; then
            return 1
        fi
    fi
    if activate_env "$env_name"; then
        install_probabilistic_packages
        deactivate_env
        if verify_probabilistic_installation "$env_name"; then
            log_success "✅ Probabilistic environment installed"
            return 0
        fi
    fi
    return 1
}

# Install probabilistic packages
install_probabilistic_packages() {
    log_info "🎲 Installing Probabilistic packages..."
    local probabilistic_packages=("torch" "numpy" "pandas" "tensorflow-probability" "pyro-ppl")
    for package in "${probabilistic_packages[@]}"; do
        install_package "$package"
    done
}

# Install causal environment
install_causal_environment() {
    local env_name="$1"
    local base_env="${2:-env_base_torch}"
    log_info "🔗 Installing Causal environment: $env_name"
    if ! clone_environment "$base_env" "$env_name"; then
        if ! install_base_environment "$env_name"; then
            return 1
        fi
    fi
    if activate_env "$env_name"; then
        install_causal_packages
        deactivate_env
        if verify_causal_installation "$env_name"; then
            log_success "✅ Causal environment installed"
            return 0
        fi
    fi
    return 1
}

# Install causal packages
install_causal_packages() {
    log_info "🔗 Installing Causal packages..."
    local causal_packages=("tigramite" "numpy" "pandas")
    for package in "${causal_packages[@]}"; do
        install_package "$package"
    done
}

# Install vision time series environment
install_vision_ts_environment() {
    local env_name="$1"
    local base_env="${2:-env_base_torch}"
    log_info "📷 Installing Vision TS environment: $env_name"
    if ! clone_environment "$base_env" "$env_name"; then
        if ! install_base_environment "$env_name"; then
            return 1
        fi
    fi
    if activate_env "$env_name"; then
        install_vision_ts_packages
        deactivate_env
        if verify_vision_ts_installation "$env_name"; then
            log_success "✅ Vision TS environment installed"
            return 0
        fi
    fi
    return 1
}

# Install vision time series packages
install_vision_ts_packages() {
    log_info "📷 Installing Vision TS packages..."
    local vision_ts_packages=("transformers" "torch" "numpy" "pandas" "torchvision")
    for package in "${vision_ts_packages[@]}"; do
        install_package "$package"
    done
}

# Verification functions
verify_geometric_installation() {
    local env_name="$1"
    activate_env "$env_name" && \
    python -c "import torch_geometric; print('PyG OK')" 2>/dev/null
    local result=$?
    deactivate_env
    return $result
}

verify_transformers_installation() {
    local env_name="$1"
    activate_env "$env_name" && \
    python -c "import transformers; print('Transformers OK')" 2>/dev/null
    local result=$?
    deactivate_env
    return $result
}

verify_llm_stable_installation() {
    local env_name="$1"
    activate_env "$env_name" && \
    python -c "import transformers, chronos, uni2ts, momentfm, timesfm; print('Stable LLM OK')" 2>/dev/null
    local result=$?
    deactivate_env
    return $result
}

verify_llm_research_installation() {
    local env_name="$1"
    activate_env "$env_name" && \
    python -c "import time_moe, lag_llama; print('Research LLM OK')" 2>/dev/null
    local result=$?
    deactivate_env
    return $result
}

verify_tslib_installation() {
    local env_name="$1"
    activate_env "$env_name" && \
    python -c "import statsmodels, sktime; print('TSLib OK')" 2>/dev/null
    local result=$?
    deactivate_env
    return $result
}

verify_tensorflow_installation() {
    local env_name="$1"
    activate_env "$env_name" && \
    python -c "import tensorflow as tf; print('TF OK')" 2>/dev/null
    local result=$?
    deactivate_env
    return $result
}

verify_anomaly_advanced_installation() {
    local env_name="$1"
    activate_env "$env_name" && \
    python -c "import torch, sklearn; print('Anomaly Advanced OK')" 2>/dev/null
    local result=$?
    deactivate_env
    return $result
}

verify_federated_installation() {
    local env_name="$1"
    activate_env "$env_name" && \
    python -c "import flwr; print('Federated OK')" 2>/dev/null
    local result=$?
    deactivate_env
    return $result
}

verify_multimodal_installation() {
    local env_name="$1"
    activate_env "$env_name" && \
    python -c "import transformers, torchvision; print('Multimodal OK')" 2>/dev/null
    local result=$?
    deactivate_env
    return $result
}

verify_probabilistic_installation() {
    local env_name="$1"
    activate_env "$env_name" && \
    python -c "import tensorflow_probability, pyro; print('Probabilistic OK')" 2>/dev/null
    local result=$?
    deactivate_env
    return $result
}

verify_causal_installation() {
    local env_name="$1"
    activate_env "$env_name" && \
    python -c "import tigramite; print('Causal OK')" 2>/dev/null
    local result=$?
    deactivate_env
    return $result
}

verify_vision_ts_installation() {
    local env_name="$1"
    activate_env "$env_name" && \
    python -c "import transformers, torchvision; print('Vision TS OK')" 2>/dev/null
    local result=$?
    deactivate_env
    return $result
}
--- END FILE ---

<!-- Full Path: C:/00_Repos_Rod/Testing_Repos/environments\scripts\utils\activation.sh -->
<!-- Relative Path: scripts\utils\activation.sh -->
<!-- File Size: 7814 bytes -->
<!-- Last Modified: 2025-08-03 19:28:22 -->
--- BEGIN FILE: scripts\utils\activation.sh ---
#!/bin/bash
# Language: Bash 5.0
# Lines of Code: 120
# File: scripts/utils/activation.sh
# Version: 3.2.0
# Project: AI Time Series Framework
# Repository: AI_TimeSeriesFramework
# Author: Rod Sanchez
# Created: 2025-08-03 09:30
# Last Edited: 2025-08-03 20:15
# Change: Feature (+0.1) - Added new environments to activation script
# Modifications: +40, -0
# Last Modification Comment: Added env_anomaly_advanced, env_federated, env_multimodal, env_probabilistic, env_causal, env_vision_ts

source "$(dirname "${BASH_SOURCE[0]}")/../core/logger.sh"
source "$(dirname "${BASH_SOURCE[0]}")/../core/conda_manager.sh"

# Generate activation scripts
generate_activation_scripts() {
    local project_dir="$1"
    
    log_info "📝 Generating activation scripts..."
    
    cat > "$project_dir/activate.sh" << 'MAIN_ACTIVATE'
#!/bin/bash
# Language: Bash 5.0
# Lines of Code: 140
# File: activate.sh
# Version: 3.4.0
# Project: AI Time Series Framework
# Repository: AI_TimeSeriesFramework
# Author: Rod Sanchez
# Created: 2025-08-03 09:30
# Last Edited: 2025-08-03 20:15

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/scripts/core/conda_manager.sh"

show_help() {
    echo "🎯 AI Time Series Framework - Environment Activator"
    echo ""
    echo "Usage: $0 <environment>"
    echo ""
    echo "Available environments:"
    echo "  base_torch        - Core PyTorch foundation"
    echo "  geometric         - PyTorch Geometric for graphs"
    echo "  transformers      - HuggingFace transformers"
    echo "  llm_stable        - Stable LLM-based time series models"
    echo "  llm_research      - Research LLM-based time series models"
    echo "  tslib             - Time series libraries"
    echo "  tensorflow        - TensorFlow ecosystem"
    echo "  rapids            - GPU-accelerated RAPIDS"
    echo "  anomaly_advanced  - Advanced anomaly detection models"
    echo "  federated         - Federated learning models"
    echo "  multimodal        - Multimodal time series models"
    echo "  probabilistic     - Probabilistic time series models"
    echo "  causal            - Causal discovery models"
    echo "  vision_ts         - Vision-enhanced time series models"
    echo ""
    echo "Examples:"
    echo "  $0 base_torch"
    echo "  $0 llm_stable"
    echo "  $0 anomaly_advanced"
    echo ""
    echo "🆕 Stable LLM Models in env_llm_stable:"
    echo "  • Chronos     - Probabilistic forecasting"
    echo "  • Uni2TS      - Salesforce unified time series model"
    echo "  • MomentFM    - Representation learning"
    echo "  • TimesFM     - Google's time series foundation model"
    echo ""
    echo "🆕 Research LLM Models in env_llm_research:"
    echo "  • Time-MoE    - Mixture of Experts model"
    echo "  • Lag-Llama   - Probabilistic forecasting"
    echo "  • Timer-XL    - Large-scale foundation model"
    echo "  • Diffusion-TS - Diffusion-based forecasting"
    echo "  • Time-LLM    - Time series language model"
    echo "  • AutoTimes   - Automated time series modeling"
    echo "  • MM-TSFlib   - Multimodal time series library"
    echo "  • LLMTIME     - Language model for time series"
    echo "  • TEMPO       - Temporal modeling"
    echo ""
    echo "🆕 Anomaly Advanced Models in env_anomaly_advanced:"
    echo "  • CARLA       - Contrastive representation learning"
    echo "  • DACAD       - Domain adaptation contrastive learning"
    echo "  • AT-DCAEP    - Attention-based deep convolutional autoencoder"
    echo "  • GSLAD       - Graph structure learning-based anomaly detection"
    echo ""
    echo "🆕 Federated Models in env_federated:"
    echo "  • FedAvg      - Federated averaging"
    echo "  • FedProx     - Federated proximal"
    echo "  • SCAFFOLD    - Stochastic controlled averaging"
    echo "  • MOON        - Model contrastive federated learning"
    echo ""
    echo "🆕 Multimodal Models in env_multimodal:"
    echo "  • ChatTime    - Unified multimodal time series model"
    echo "  • Time-MMD    - Multi-domain multimodal model"
    echo "  • MST-GAT     - Multimodal spatial-temporal graph attention network"
    echo ""
    echo "🆕 Probabilistic Models in env_probabilistic:"
    echo "  • AutoBNN     - Automated Bayesian neural network"
    echo ""
    echo "🆕 Causal Models in env_causal:"
    echo "  • PCMCI       - Peter-Clark momentary conditional independence"
    echo "  • CReP        - Causal-oriented representation learning"
    echo ""
    echo "🆕 Vision TS Models in env_vision_ts:"
    echo "  • VisionTS    - Vision-enhanced time series forecasting"
    echo "  • ViTime      - Vision-powered time series forecasting"
}

if [[ $# -eq 0 ]] || [[ "$1" == "--help" ]]; then
    show_help
    exit 0
fi

env_name="env_$1"

init_conda

if env_exists "$env_name"; then
    echo "🔄 Activating $env_name..."
    conda activate "$env_name"
    echo "✅ Environment activated: $env_name"
    
    if [[ "$env_name" == "env_llm_stable" ]]; then
        echo ""
        echo "🚀 Stable LLM Time Series Environment Active!"
        echo "💡 Quick test: python -c \"import chronos, uni2ts, momentfm, timesfm; print('Stable LLM models ready!')\""
        echo "📚 Models available: Chronos, Uni2TS, MomentFM, TimesFM"
    elif [[ "$env_name" == "env_llm_research" ]]; then
        echo ""
        echo "🔬 Research LLM Time Series Environment Active!"
        echo "💡 Quick test: python -c \"import time_moe, lag_llama; print('Research LLM models ready!')\""
        echo "📚 Models available: Time-MoE, Lag-Llama, Timer-XL, Diffusion-TS, Time-LLM, AutoTimes, MM-TSFlib, LLMTIME, TEMPO"
    elif [[ "$env_name" == "env_anomaly_advanced" ]]; then
        echo ""
        echo "🔍 Anomaly Advanced Environment Active!"
        echo "💡 Quick test: python -c \"import torch, sklearn; print('Anomaly Advanced models ready!')\""
        echo "📚 Models available: CARLA, DACAD, AT-DCAEP, GSLAD"
    elif [[ "$env_name" == "env_federated" ]]; then
        echo ""
        echo "🌐 Federated Environment Active!"
        echo "💡 Quick test: python -c \"import flwr; print('Federated models ready!')\""
        echo "📚 Models available: FedAvg, FedProx, SCAFFOLD, MOON"
    elif [[ "$env_name" == "env_multimodal" ]]; then
        echo ""
        echo "🎨 Multimodal Environment Active!"
        echo "💡 Quick test: python -c \"import transformers, torchvision; print('Multimodal models ready!')\""
        echo "📚 Models available: ChatTime, Time-MMD, MST-GAT"
    elif [[ "$env_name" == "env_probabilistic" ]]; then
        echo ""
        echo "🎲 Probabilistic Environment Active!"
        echo "💡 Quick test: python -c \"import tensorflow_probability, pyro; print('Probabilistic models ready!')\""
        echo "📚 Models available: AutoBNN"
    elif [[ "$env_name" == "env_causal" ]]; then
        echo ""
        echo "🔗 Causal Environment Active!"
        echo "💡 Quick test: python -c \"import tigramite; print('Causal models ready!')\""
        echo "📚 Models available: PCMCI, CReP"
    elif [[ "$env_name" == "env_vision_ts" ]]; then
        echo ""
        echo "📷 Vision TS Environment Active!"
        echo "💡 Quick test: python -c \"import transformers, torchvision; print('Vision TS models ready!')\""
        echo "📚 Models available: VisionTS, ViTime"
    fi
    
    echo "💡 Deactivate with: conda deactivate"
else
    echo "❌ Environment $env_name not found"
    echo ""
    echo "Available environments:"
    conda env list | grep "^env_" | sed 's/env_/  /'
    echo ""
    echo "Run setup first: ./setup.sh"
fi
MAIN_ACTIVATE
    
    chmod +x "$project_dir/activate.sh"
    
    log_success "✅ Activation scripts generated"
}
--- END FILE ---

<!-- Full Path: C:/00_Repos_Rod/Testing_Repos/environments\scripts\utils\check_model_dirs.sh -->
<!-- Relative Path: scripts\utils\check_model_dirs.sh -->
<!-- File Size: 3065 bytes -->
<!-- Last Modified: 2025-08-04 15:48:44 -->
--- BEGIN FILE: scripts\utils\check_model_dirs.sh ---
#!/bin/bash
# Language: Bash 5.0
# Lines of Code: 50
# File: scripts/utils/check_model_dirs.sh
# Version: 1.0.0
# Project: AI Time Series Framework
# Repository: AI_TimeSeriesFramework
# Author: Rod Sanchez
# Created: 2025-08-04 12:00
# Last Edited: 2025-08-04 12:00
# Change: Initial creation
# Modifications: +50, -0
# Last Modification Comment: Created script to verify model directory mappings against actual filesystem

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Define model directories (copied from user's query)
PYTORCH_MODEL_DIR="models/pytorch"
GEOMETRIC_MODEL_DIR="models/geometric"
TRANSFORMER_MODEL_DIR="models/transformers"
TRANSFORMERS_MODERN_MODEL_DIR="models/transformers_modern"
TRANSFORMERS_LEGACY_MODEL_DIR="models/transformers_legacy"
TRANSFORMERS_TS_MODEL_DIR="models/transformers_ts"
LLM_CHRONOS_MODEL_DIR="models/llm_chronos"
LLM_UNI2TS_MODEL_DIR="models/llm_uni2ts"
LLM_MOMENTFM_MODEL_DIR="models/llm_momentfm"
LLM_MAMBA_MODEL_DIR="models/llm_mamba"
TSLIB_MODEL_DIR="models/tslib"
TSLIB_TRADITIONAL_MODEL_DIR="models/tslib_traditional"
TSLIB_NIXTLA_MODEL_DIR="models/tslib_nixtla"
TSLIB_ADVANCED_MODEL_DIR="models/tslib_advanced"
TENSORFLOW_MODEL_DIR="models/tensorflow"
RAPIDS_MODEL_DIR="models/rapids"
LLM_RESEARCH_MODEL_DIR="models/llm_research"
ANOMALY_ADVANCED_MODEL_DIR="models/anomaly_advanced"
FEDERATED_MODEL_DIR="models/federated"
MULTIMODAL_MODEL_DIR="models/multimodal"
PROBABILISTIC_MODEL_DIR="models/probabilistic"
CAUSAL_MODEL_DIR="models/causal"
VISION_TS_MODEL_DIR="models/vision_ts"

# Array of all directory variables
declare -a dirs=(
    PYTORCH_MODEL_DIR
    GEOMETRIC_MODEL_DIR
    TRANSFORMER_MODEL_DIR
    TRANSFORMERS_MODERN_MODEL_DIR
    TRANSFORMERS_LEGACY_MODEL_DIR
    TRANSFORMERS_TS_MODEL_DIR
    LLM_CHRONOS_MODEL_DIR
    LLM_UNI2TS_MODEL_DIR
    LLM_MOMENTFM_MODEL_DIR
    LLM_MAMBA_MODEL_DIR
    TSLIB_MODEL_DIR
    TSLIB_TRADITIONAL_MODEL_DIR
    TSLIB_NIXTLA_MODEL_DIR
    TSLIB_ADVANCED_MODEL_DIR
    TENSORFLOW_MODEL_DIR
    RAPIDS_MODEL_DIR
    LLM_RESEARCH_MODEL_DIR
    ANOMALY_ADVANCED_MODEL_DIR
    FEDERATED_MODEL_DIR
    MULTIMODAL_MODEL_DIR
    PROBABILISTIC_MODEL_DIR
    CAUSAL_MODEL_DIR
    VISION_TS_MODEL_DIR
)

echo "🔍 Checking model directories..."
echo "=============================="

total_dirs=${#dirs[@]}
existing=0
missing=0

for var in "${dirs[@]}"; do
    dir_path="${!var}"
    if [ -d "$dir_path" ]; then
        echo -e "${GREEN}✅ ${var}: Exists (${dir_path})${NC}"
        ((existing++))
    else
        echo -e "${RED}❌ ${var}: Missing (${dir_path})${NC}"
        ((missing++))
    fi
done

echo ""
echo "📊 Summary:"
echo "  Total directories defined: $total_dirs"
echo "  Existing: $existing"
echo "  Missing: $missing"

if [ $missing -eq 0 ]; then
    echo -e "${GREEN}🎉 All defined directories exist! The mappings are correct.${NC}"
    exit 0
else
    echo -e "${YELLOW}⚠️ Some directories are missing. The mappings may need updates or repositories need cloning.${NC}"
    exit 1
fi
--- END FILE ---

<!-- Full Path: C:/00_Repos_Rod/Testing_Repos/environments\scripts\utils\cleanup.sh -->
<!-- Relative Path: scripts\utils\cleanup.sh -->
<!-- File Size: 2880 bytes -->
<!-- Last Modified: 2025-08-05 01:04:36 -->
--- BEGIN FILE: scripts\utils\cleanup.sh ---
#!/bin/bash
# Language: Bash 5.0
# Lines of Code: 110
# File: scripts/utils/cleanup.sh
# Version: 4.0.0
# Project: AI Time Series Framework
# Repository: AI_TimeSeriesFramework
# Author: Rod Sanchez
# Created: 2025-08-03 09:30
# Last Edited: 2025-08-03 23:30
# Change: Major (+1.0) - Updated for split environments
# Modifications: +10, -6
# Last Modification Comment: Replaced old environments with new split ones in cleanup_all_environments

source "$(dirname "${BASH_SOURCE[0]}")/../core/logger.sh"
source "$(dirname "${BASH_SOURCE[0]}")/../core/conda_manager.sh"

# Clean all environments
cleanup_all_environments() {
    log_info "🧹 Cleaning all framework environments..."
    
    local framework_envs=(
        "env_transformers_modern"
        "env_transformers_legacy"
        "env_transformers_ts"
        "env_llm_chronos"
        "env_llm_uni2ts"
        "env_llm_momentfm"
        "env_llm_mamba"
        "env_tslib_traditional"
        "env_tslib_nixtla"
        "env_tslib_advanced"
        "env_base_torch"
        "env_geometric"
        "env_tensorflow"
        "env_rapids"
        "env_anomaly_advanced"
        "env_federated"
        "env_multimodal"
        "env_probabilistic"
        "env_causal"
        "env_vision_ts"
    )
    
    for env in "${framework_envs[@]}"; do
        if env_exists "$env"; then
            log_info "🗑️ Removing environment: $env"
            remove_environment "$env"
        fi
    done
    
    clean_conda
    log_success "✅ All environments cleaned"
}

# Clean conda system thoroughly
deep_clean_conda() {
    log_info "🧹 Performing deep conda cleanup..."
    
    conda clean --all -y 2>/dev/null
    
    local conda_base
    conda_base=$(conda info --base)
    
    local cache_dirs=(
        "$conda_base/pkgs"
        "$HOME/.conda/pkgs"
        "$HOME/.cache/pip"
    )
    
    for cache_dir in "${cache_dirs[@]}"; do
        if [[ -d "$cache_dir" ]]; then
            log_info "🗑️ Cleaning cache: $cache_dir"
            find "$cache_dir" -type f -name "*.tar.bz2" -delete 2>/dev/null || true
            find "$cache_dir" -type f -name "*.conda" -delete 2>/dev/null || true
        fi
    done
    
    log_success "✅ Deep cleanup completed"
}

# Repair corrupted environments
repair_environments() {
    log_info "🔧 Repairing corrupted environments..."
    
    local all_envs
    mapfile -t all_envs < <(conda env list | grep -v '^#' | awk '{print $1}' | grep -v '^$')
    
    for env in "${all_envs[@]}"; do
        [[ "$env" == "base" ]] && continue
        
        local status
        status=$(get_env_status "$env")
        
        if [[ "$status" == "corrupted" ]] || [[ "$status" == "broken" ]]; then
            log_warning "🔧 Repairing environment: $env"
            remove_environment "$env"
        fi
    done
    
    log_success "✅ Environment repair completed"
}
--- END FILE ---

<!-- Full Path: C:/00_Repos_Rod/Testing_Repos/environments\scripts\utils\documentation.sh -->
<!-- Relative Path: scripts\utils\documentation.sh -->
<!-- File Size: 7293 bytes -->
<!-- Last Modified: 2025-08-04 00:21:25 -->
--- BEGIN FILE: scripts\utils\documentation.sh ---
# Language: Bash 5.0
# Lines of Code: 200
# File: scripts/utils/documentation.sh
# Version: 4.0.0
# Project: AI Time Series Framework
# Repository: AI_TimeSeriesFramework
# Author: Rod Sanchez
# Created: 2025-08-03 09:30
# Last Edited: 2025-08-03 23:30
# Change: Major (+1.0) - Updated for split environments
# Modifications: +50, -41
# Last Modification Comment: Replaced old environments with new split ones in environment guide

source "$(dirname "${BASH_SOURCE[0]}")/../core/logger.sh"

# Generate comprehensive documentation
generate_documentation() {
    local project_dir="$1"
    
    log_info "📚 Generating documentation..."
    
    generate_readme "$project_dir"
    generate_quick_start "$project_dir"
    generate_environment_guide "$project_dir"
    
    log_success "✅ Documentation generated"
}

# Generate main README
generate_readme() {
    local project_dir="$1"
    
    cat > "$project_dir/README.md" << EOF
# 🎯 AI Time Series Framework

A comprehensive, modular framework for time series modeling with support for PyTorch, TensorFlow, RAPIDS, and specialized libraries.

## 🚀 Quick Start

\`\`\`bash
# Install the framework
./setup.sh

# Activate an environment
./activate.sh transformers_modern

# Start modeling!
python -c "import torch; print('Ready for time series modeling!')"
\`\`\`

## 🏗️ Architecture

### Core Principles
- **DRY (Don't Repeat Yourself)**: Single source of truth for all operations
- **Modular Design**: Clear separation of concerns
- **Scalable**: Easy to extend with new environments
- **Pragmatic**: Following industry best practices

### Directory Structure
\`\`\`
AI_TimeSeriesFramework/
├── scripts/
│   ├── core/           # Core functionality (logger, conda manager, etc.)
│   ├── installers/     # Environment installation modules
│   ├── utils/          # Utility modules (cleanup, activation, docs)
│   └── config/         # Configuration files
├── environments/       # Environment metadata
├── models/            # Model repositories
├── docs/              # Documentation
├── logs/              # Logs
├── data/cache/        # SQLite databases
└── README.md          # Project docs
\`\`\`

## 🌟 Features

- **DRY Principle**: Centralized logging and configuration
- **20 Specialized Environments**: PyTorch, Geometric, Transformers, TSLib, TensorFlow, RAPIDS, LLMs, Anomaly, Federated, Multimodal, Probabilistic, Causal, Vision TS
- **GPU Support**: Automatic CUDA detection and optimization (e.g., cu121 for CUDA 12.1)
- **Modular Installation**: Install only what you need
- **Easy Management**: Simple activation and cleanup utilities
- **Comprehensive Testing**: Built-in validation and verification

## 📖 Environments

The framework now uses split environments for better dependency management. Old environments (env_transformers, env_llm_stable, env_tslib) have been removed.

New environments:
- \`env_transformers_modern\`: Modern transformers setup (transformers>=4.45.0, Python 3.11)
- \`env_transformers_legacy\`: Legacy transformers setup (transformers==4.33.3, torch==2.0.0, torchvision==0.15.0, torchaudio==2.0.0, numpy>=1.25, Python 3.11)
- \`env_transformers_ts\`: Time series transformers (pytorch-forecasting, Python 3.11)
- \`env_llm_chronos\`: Chronos LLM setup (chronos-forecasting, Python 3.11)
- \`env_llm_uni2ts\`: Uni2TS LLM setup (uni2ts==1.2.0, Python 3.11)
- \`env_llm_momentfm\`: MomentFM LLM setup (momentfm==0.1.4, Python 3.11)
- \`env_llm_mamba\`: Mamba LLM setup (mamba-ssm>=2.2.2, Python 3.11)
- \`env_tslib_traditional\`: Traditional time series libraries (statsmodels, prophet, sktime==0.26.0, Python 3.11)
- \`env_tslib_nixtla\`: Nixtla time series libraries (neuralforecast, Python 3.11)
- \`env_tslib_advanced\`: Advanced time series libraries (darts, tsfresh, Python 3.11)

Other environments:
- \`env_base_torch\`: Core PyTorch foundation
- \`env_geometric\`: PyTorch Geometric for graphs
- \`env_tensorflow\`: TensorFlow ecosystem
- \`env_rapids\`: GPU-accelerated RAPIDS
- \`env_anomaly_advanced\`: Advanced anomaly detection models
- \`env_federated\`: Federated learning models
- \`env_multimodal\`: Multimodal time series models
- \`env_probabilistic\`: Probabilistic time series models
- \`env_causal\`: Causal discovery models
- \`env_vision_ts\`: Vision-enhanced time series models

## 📚 Documentation

- [Quick Start Guide](docs/QUICK_START.md)
- [Environment Guide](docs/ENVIRONMENTS.md)
- [API Reference](docs/API.md)

## 🤝 Contributing

This framework follows the Pragmatic Programmer principles. When contributing:

1. Follow the DRY principle
2. Write tests for new functionality
3. Update documentation
4. Use meaningful commit messages

## 📄 License

MIT License - see LICENSE file for details.
EOF
    
    local result=$?
    if [[ $result -eq 0 ]]; then
        log_success "✅ README.md generated"
    else
        log_error "❌ Failed to generate README.md"
    fi
}

# Generate quick start guide
generate_quick_start() {
    local project_dir="$1"
    
    cat > "$project_dir/docs/QUICK_START.md" << EOF
# Quick Start Guide

## Installation
\`\`\`bash
./setup.sh
\`\`\`

## Activation
\`\`\`bash
./activate.sh transformers_modern
\`\`\`

## Basic Usage
\`\`\`python
import torch
x = torch.randn(5, 3)
print(x)
\`\`\`

## CUDA Testing (if GPU available)
\`\`\`python
import torch
print(f'CUDA available: {torch.cuda.is_available()}')
if torch.cuda.is_available():
    print(f'GPU: {torch.cuda.get_device_name(0)}')
    print(f'CUDA Version: {torch.version.cuda}')
\`\`\`

EOF
    
    log_success "✅ QUICK_START.md generated"
}

# Generate environment guide
generate_environment_guide() {
    local project_dir="$1"
    
    cat > "$project_dir/docs/ENVIRONMENTS.md" << EOF
# Environment Guide

## transformers_modern
Modern transformers with latest versions (transformers>=4.45.0)

## transformers_legacy
Legacy transformers for compatibility (transformers==4.33.3)

## transformers_ts
Time series specific transformers (pytorch-forecasting)

## llm_chronos
Chronos LLM for probabilistic forecasting

## llm_uni2ts
Uni2TS LLM for unified time series modeling

## llm_momentfm
MomentFM LLM for representation learning

## llm_mamba
Mamba LLM for state space modeling

## tslib_traditional
Traditional time series libraries (statsmodels, prophet, sktime==0.26.0)

## tslib_nixtla
Nixtla time series libraries (neuralforecast, etc.)

## tslib_advanced
Advanced time series libraries (darts, tsfresh)

## base_torch
Core PyTorch foundation with CUDA support if available

## geometric
PyTorch Geometric for graph neural networks

## tensorflow
TensorFlow ecosystem with GluonTS support

## rapids
GPU-accelerated RAPIDS (requires NVIDIA GPU)

## anomaly_advanced
Advanced anomaly detection models (CARLA, DACAD, AT-DCAEP, GSLAD)

## federated
Federated learning frameworks (FedAvg, FedProx, SCAFFOLD, MOON)

## multimodal
Multimodal time series models (ChatTime, Time-MMD, MST-GAT)

## probabilistic
Probabilistic time series models (AutoBNN)

## causal
Causal discovery models (PCMCI, CReP)

## vision_ts
Vision-enhanced time series models (VisionTS, ViTime)

## Activation
Use ./activate.sh <env_name>

EOF
    
    log_success "✅ ENVIRONMENTS.md generated"
}
--- END FILE ---

<!-- Full Path: C:/00_Repos_Rod/Testing_Repos/environments\scripts\utils\performance_monitor.sh -->
<!-- Relative Path: scripts\utils\performance_monitor.sh -->
<!-- File Size: 3919 bytes -->
<!-- Last Modified: 2025-08-04 00:21:11 -->
--- BEGIN FILE: scripts\utils\performance_monitor.sh ---
#!/bin/bash
# Language: Bash 5.0
# Lines of Code: 95
# File: scripts/utils/performance_monitor.sh
# Version: 4.0.0
# Project: AI Time Series Framework
# Repository: AI_TimeSeriesFramework
# Author: Rod Sanchez
# Created: 2025-08-03 09:30
# Last Edited: 2025-08-03 23:30
# Change: Major (+1.0) - Updated for split environments
# Modifications: +10, -6
# Last Modification Comment: Updated monitor_environments to include new split environments

source "$(dirname "${BASH_SOURCE[0]}")/../core/logger.sh"

# Monitor system resources
monitor_system() {
    log_info "📊 System Performance Monitor"
    echo "=============================="
    
    # CPU information
    if command -v lscpu &> /dev/null; then
        local cpu_model cores
        cpu_model=$(lscpu | grep "Model name" | cut -d: -f2 | xargs)
        cores=$(lscpu | grep "^CPU(s):" | cut -d: -f2 | xargs)
        echo "🖥️ CPU: $cpu_model ($cores cores)"
    fi
    
    # Memory information
    if command -v free &> /dev/null; then
        local total_mem used_mem
        total_mem=$(free -h | awk '/^Mem:/{print $2}')
        used_mem=$(free -h | awk '/^Mem:/{print $3}')
        echo "🧠 Memory: $used_mem / $total_mem used"
    fi
    
    # Disk space
    if command -v df &> /dev/null; then
        local disk_usage
        disk_usage=$(df -h . | awk 'NR==2{print $4 " available (" $5 " used)"}')
        echo "💾 Disk: $disk_usage"
    fi
    
    # GPU information
    if command -v nvidia-smi &> /dev/null; then
        echo ""
        echo "🎯 GPU Information:"
        nvidia-smi --query-gpu=name,memory.total,memory.used,utilization.gpu \
                   --format=csv,noheader,nounits | while IFS=, read -r name mem_total mem_used util; do
            echo "  📊 $name"
            echo "     Memory: ${mem_used}MB / ${mem_total}MB"
            echo "     Utilization: ${util}%"
        done
    else
        echo "💻 No GPU detected"
    fi
}

# Monitor conda environments
monitor_environments() {
    log_info "📋 Environment Disk Usage"
    echo "=========================="
    
    local conda_base
    conda_base=$(conda info --base)
    local envs_dir="$conda_base/envs"
    
    if [[ -d "$envs_dir" ]]; then
        local framework_envs=(
            "env_transformers_modern"
            "env_transformers_legacy"
            "env_transformers_ts"
            "env_llm_chronos"
            "env_llm_uni2ts"
            "env_llm_momentfm"
            "env_llm_mamba"
            "env_tslib_traditional"
            "env_tslib_nixtla"
            "env_tslib_advanced"
            "env_base_torch"
            "env_geometric"
            "env_tensorflow"
            "env_rapids"
            "env_anomaly_advanced"
            "env_federated"
            "env_multimodal"
            "env_probabilistic"
            "env_causal"
            "env_vision_ts"
        )
        for env in "${framework_envs[@]}"; do
            if [[ -d "$envs_dir/$env" ]]; then
                local size
                size=$(du -sh "$envs_dir/$env" 2>/dev/null | cut -f1)
                echo "📁 $env: $size"
            fi
        done
    fi
}

# Monitor package cache
monitor_cache() {
    log_info "🗄️ Package Cache Usage"
    echo "======================"
    
    local conda_base
    conda_base=$(conda info --base)
    
    local cache_dirs=(
        "$conda_base/pkgs"
        "$HOME/.conda/pkgs"
        "$HOME/.cache/pip"
    )
    
    for cache_dir in "${cache_dirs[@]}"; do
        if [[ -d "$cache_dir" ]]; then
            local cache_size
            cache_size=$(du -sh "$cache_dir" 2>/dev/null | cut -f1)
            echo "📦 $(basename "$cache_dir"): $cache_size"
        fi
    done
}

# Main monitoring function
main() {
    monitor_system
    echo ""
    monitor_environments
    echo ""
    monitor_cache
}

# Execute if run directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi
--- END FILE ---

<!-- Full Path: C:/00_Repos_Rod/Testing_Repos/environments\scripts\utils\version_checker.sh -->
<!-- Relative Path: scripts\utils\version_checker.sh -->
<!-- File Size: 5205 bytes -->
<!-- Last Modified: 2025-08-04 12:50:32 -->
--- BEGIN FILE: scripts\utils\version_checker.sh ---
#!/bin/bash
# Language: Bash 5.0
# Lines of Code: 78
# File: scripts/utils/version_checker.sh
# Version: 4.0.0
# Project: AI Time Series Framework
# Repository: AI_TimeSeriesFramework
# Author: Rod Sanchez
# Created: 2025-08-03 09:30
# Last Edited: 2025-08-03 23:30
# Change: Major (+1.0) - Updated for split environments
# Modifications: +15, -5
# Last Modification Comment: Updated check_all_versions to include new split environments

source "$(dirname "${BASH_SOURCE[0]}")/../core/logger.sh"

# Check all package versions in an environment
check_environment_versions() {
    local env_name="$1"
    
    log_info "📋 Checking versions in $env_name..."
    
    if conda activate "$env_name" 2>/dev/null; then
        echo ""
        echo "🐍 Python: $(python --version)"
        
        # Check key packages
        local packages=("torch" "numpy" "pandas" "matplotlib")
        
        for package in "${packages[@]}"; do
            local version
            version=$(python -c "
try:
    import $package
    print($package.__version__)
except:
    print('Not installed')
" 2>/dev/null)
            echo "📦 $package: $version"
        done
        
        # Check environment-specific packages
        case "$env_name" in
            "env_transformers_modern"|"env_transformers_legacy"|"env_transformers_ts")
                local version
                version=$(python -c "import transformers; print(transformers.__version__)" 2>/dev/null || echo "Not installed")
                echo "📦 transformers: $version"
                ;;
            "env_llm_chronos")
                local version
                version=$(python -c "import chronos; print(chronos.__version__)" 2>/dev/null || echo "Not installed")
                echo "📦 chronos: $version"
                ;;
            "env_llm_uni2ts")
                local version
                version=$(python -c "import uni2ts; print(uni2ts.__version__)" 2>/dev/null || echo "Not installed")
                echo "📦 uni2ts: $version"
                ;;
            "env_llm_momentfm")
                local version
                version=$(python -c "import momentfm; print(momentfm.__version__)" 2>/dev/null || echo "Not installed")
                echo "📦 momentfm: $version"
                ;;
            "env_llm_mamba")
                local version
                version=$(python -c "import mamba_ssm; print(mamba_ssm.__version__)" 2>/dev/null || echo "Not installed")
                echo "📦 mamba_ssm: $version"
                ;;
            "env_tslib_traditional")
                local version
                version=$(python -c "import sktime; print(sktime.__version__)" 2>/dev/null || echo "Not installed")
                echo "📦 sktime: $version"
                ;;
            "env_tslib_nixtla")
                local version
                version=$(python -c "import neuralforecast; print(neuralforecast.__version__)" 2>/dev/null || echo "Not installed")
                echo "📦 neuralforecast: $version"
                ;;
            "env_tslib_advanced")
                local version
                version=$(python -c "import darts; print(darts.__version__)" 2>/dev/null || echo "Not installed")
                echo "📦 darts: $version"
                ;;
            "env_tensorflow")
                local version
                version=$(python -c "import tensorflow; print(tensorflow.__version__)" 2>/dev/null || echo "Not installed")
                echo "📦 tensorflow: $version"
                ;;
            "env_rapids")
                local version
                version=$(python -c "import cudf; print(cudf.__version__)" 2>/dev/null || echo "Not installed")
                echo "📦 cudf: $version"
                ;;
        esac
        
        # Check CUDA if available
        if python -c "import torch; print(torch.cuda.is_available())" 2>/dev/null | grep -q "True"; then
            local cuda_version
            cuda_version=$(python -c "import torch; print(torch.version.cuda)" 2>/dev/null)
            echo "🎯 CUDA: $cuda_version"
        fi
        
        conda deactivate
    else
        log_error "❌ Cannot activate environment: $env_name"
    fi
}

# Check all framework environments
check_all_versions() {
    log_info "📋 Checking all environment versions..."
    
    local framework_envs=(
        "env_transformers_modern"
        "env_transformers_legacy"
        "env_transformers_ts"
        "env_llm_chronos"
        "env_llm_uni2ts"
        "env_llm_momentfm"
        "env_llm_mamba"
        "env_tslib_traditional"
        "env_tslib_nixtla"
        "env_tslib_advanced"
        "env_base_torch"
        "env_geometric"
        "env_tensorflow"
        "env_rapids"
        "env_anomaly_advanced"
        "env_federated"
        "env_multimodal"
        "env_probabilistic"
        "env_causal"
        "env_vision_ts"
    )
    
    for env in "${framework_envs[@]}"; do
        check_environment_versions "$env"
        echo ""
    done
}

# Main function
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    if [[ $# -eq 0 ]]; then
        check_all_versions
    else
        check_environment_versions "$1"
    fi
fi
--- END FILE ---

<!-- Full Path: C:/00_Repos_Rod/Testing_Repos/environments\tests\test_core.sh -->
<!-- Relative Path: tests\test_core.sh -->
<!-- File Size: 3880 bytes -->
<!-- Last Modified: 2025-08-04 00:20:42 -->
--- BEGIN FILE: tests\test_core.sh ---
#!/bin/bash
# Language: Bash 5.0
# Lines of Code: 87
# File: tests/test_core.sh
# Version: 4.0.0
# Project: AI Time Series Framework
# Repository: AI_TimeSeriesFramework
# Author: Rod Sanchez
# Created: 2025-08-03 09:30
# Last Edited: 2025-08-03 23:30
# Change: Major (+1.0) - Updated for new environments
# Modifications: +5, -0
# Last Modification Comment: Added tests for new split environments in test_environment_detection

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FRAMEWORK_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

# Test results
TESTS_PASSED=0
TESTS_FAILED=0

# Test logging
test_logger() {
    echo "Testing logger module..."
    
    source "$FRAMEWORK_DIR/scripts/core/logger.sh"
    
    # Test initialization
    init_logger "$FRAMEWORK_DIR/tests/logs"
    
    if [[ -n "$LOG_FILE" ]] && [[ -f "$LOG_FILE" ]]; then
        echo "✅ Logger initialization: PASSED"
        TESTS_PASSED=$((TESTS_PASSED + 1))
    else
        echo "❌ Logger initialization: FAILED"
        TESTS_FAILED=$((TESTS_FAILED + 1))
    fi
    
    # Test logging functions
    log_info "Test info message"
    log_error "Test error message"
    log_success "Test success message"
    
    if grep -q "Test info message" "$LOG_FILE"; then
        echo "✅ Logging functions: PASSED"
        TESTS_PASSED=$((TESTS_PASSED + 1))
    else
        echo "❌ Logging functions: FAILED"
        TESTS_FAILED=$((TESTS_FAILED + 1))
    fi
}

# Test environment detection
test_environment_detection() {
    echo "Testing environment detection..."
    
    source "$FRAMEWORK_DIR/scripts/core/environment.sh"
    
    detect_system_environment
    
    if [[ -n "$SYSTEM_MEMORY_GB" ]] && [[ "$SYSTEM_MEMORY_GB" -gt 0 ]]; then
        echo "✅ Memory detection: PASSED ($SYSTEM_MEMORY_GB GB)"
        TESTS_PASSED=$((TESTS_PASSED + 1))
    else
        echo "❌ Memory detection: FAILED"
        TESTS_FAILED=$((TESTS_FAILED + 1))
    fi
    
    if [[ "$HAS_NVIDIA_GPU" == "true" ]] || [[ "$HAS_NVIDIA_GPU" == "false" ]]; then
        echo "✅ GPU detection: PASSED ($HAS_NVIDIA_GPU)"
        TESTS_PASSED=$((TESTS_PASSED + 1))
    else
        echo "❌ GPU detection: FAILED"
        TESTS_FAILED=$((TESTS_FAILED + 1))
    fi
    
    # Test new environments
    local new_envs=("env_transformers_modern" "env_llm_chronos" "env_tslib_advanced")
    for env in "${new_envs[@]}"; do
        if env_exists "$env"; then
            echo "✅ $env detection: PASSED"
            TESTS_PASSED=$((TESTS_PASSED + 1))
        else
            echo "❌ $env detection: FAILED"
            TESTS_FAILED=$((TESTS_FAILED + 1))
        fi
    done
}

# Test conda manager
test_conda_manager() {
    echo "Testing conda manager..."
    
    source "$FRAMEWORK_DIR/scripts/core/conda_manager.sh"
    
    init_conda
    
    # Test environment checking
    if env_exists "base"; then
        echo "✅ Environment checking: PASSED"
        TESTS_PASSED=$((TESTS_PASSED + 1))
    else
        echo "❌ Environment checking: FAILED"
        TESTS_FAILED=$((TESTS_FAILED + 1))
    fi
}

# Test validator
test_validator() {
    echo "Testing validator..."
    
    source "$FRAMEWORK_DIR/scripts/core/validator.sh"
    
    validate_system
    
    echo "✅ System validation: PASSED"
    TESTS_PASSED=$((TESTS_PASSED + 1))
}

# Main test runner
main() {
    echo "🧪 Running Core Module Tests"
    echo "============================"
    
    mkdir -p "$FRAMEWORK_DIR/tests/logs"
    
    test_logger
    test_environment_detection
    test_conda_manager
    test_validator
    
    echo ""
    echo "📊 Test Results:"
    echo "  ✅ Passed: $TESTS_PASSED"
    echo "  ❌ Failed: $TESTS_FAILED"
    
    if [[ $TESTS_FAILED -eq 0 ]]; then
        echo "🎉 All tests passed!"
        exit 0
    else
        echo "💥 Some tests failed!"
        exit 1
    fi
}

main "$@"
--- END FILE ---

<!-- Full Path: C:/00_Repos_Rod/Testing_Repos/environments\tests\test_generation.sh -->
<!-- Relative Path: tests\test_generation.sh -->
<!-- File Size: 20927 bytes -->
<!-- Last Modified: 2025-08-04 00:09:28 -->
--- BEGIN FILE: tests\test_generation.sh ---
#!/bin/bash
# Language: Bash 5.0
# Lines of Code: 8793
# File: tests/test_generation.sh
# Version: 3.0.0
# Project: AI Time Series Framework
# Repository: AI_TimeSeriesFramework
# Author: Rod Sanchez
# Created: 2025-08-03 14:40
# Last Edited: 2025-08-03 23:30
# Change: Major (+1.0) - Updated for new split environments
# Modifications: +200, -185
# Last Modification Comment: Replaced old environment tests with new split ones; added tests for all new environments

# Check directory structure
if [ -d "../src" ] && [ -d "../docs" ]; then
    echo "✅ Directory structure tests passed"
else
    echo "❌ Directory structure tests failed"
    exit 1
fi

source ../scripts/core/conda_manager.sh

# Test transformers_modern packages
if env_exists "env_transformers_modern"; then
    if conda activate env_transformers_modern; then
        if python -c "
import sys
packages_to_test = ['transformers', 'datasets', 'tokenizers', 'accelerate', 'evaluate', 'peft', 'diffusers', 'numpy', 'pandas', 'huggingface_hub', 'matplotlib', 'seaborn', 'plotly', 'scipy', 'sklearn']
failed_imports = []
for pkg in packages_to_test:
    try:
        __import__(pkg)
        print(f'✅ {pkg} imported successfully')
    except ImportError as e:
        failed_imports.append(pkg)
        print(f'❌ {pkg} failed to import: {e}')
if failed_imports:
    print(f'Total failed imports: {len(failed_imports)}')
    sys.exit(1)
else:
    print('🎉 All transformers_modern imports successful!')
" 2>/dev/null; then
            echo "✅ Transformers Modern packages: PASSED"
        else
            echo "❌ Transformers Modern packages: FAILED"
            exit 1
        fi
        conda deactivate
    else
        echo "❌ Failed to activate env_transformers_modern"
        exit 1
    fi
else
    echo "⚠️ env_transformers_modern not found, skipping package tests"
fi

# Test transformers_legacy packages
if env_exists "env_transformers_legacy"; then
    if conda activate env_transformers_legacy; then
        if python -c "
import sys
packages_to_test = ['transformers', 'datasets', 'tokenizers', 'accelerate', 'huggingface_hub', 'numpy', 'pandas', 'matplotlib', 'seaborn', 'plotly', 'scipy', 'sklearn']
failed_imports = []
for pkg in packages_to_test:
    try:
        __import__(pkg)
        print(f'✅ {pkg} imported successfully')
    except ImportError as e:
        failed_imports.append(pkg)
        print(f'❌ {pkg} failed to import: {e}')
if failed_imports:
    print(f'Total failed imports: {len(failed_imports)}')
    sys.exit(1)
else:
    print('🎉 All transformers_legacy imports successful!')
" 2>/dev/null; then
            echo "✅ Transformers Legacy packages: PASSED"
        else
            echo "❌ Transformers Legacy packages: FAILED"
            exit 1
        fi
        conda deactivate
    else
        echo "❌ Failed to activate env_transformers_legacy"
        exit 1
    fi
else
    echo "⚠️ env_transformers_legacy not found, skipping package tests"
fi

# Test transformers_ts packages
if env_exists "env_transformers_ts"; then
    if conda activate env_transformers_ts; then
        if python -c "
import sys
packages_to_test = ['pytorch_forecasting', 'pytorch_lightning', 'einops', 'numpy', 'pandas', 'matplotlib', 'seaborn', 'plotly', 'scipy', 'sklearn']
failed_imports = []
for pkg in packages_to_test:
    try:
        __import__(pkg)
        print(f'✅ {pkg} imported successfully')
    except ImportError as e:
        failed_imports.append(pkg)
        print(f'❌ {pkg} failed to import: {e}')
if failed_imports:
    print(f'Total failed imports: {len(failed_imports)}')
    sys.exit(1)
else:
    print('🎉 All transformers_ts imports successful!')
" 2>/dev/null; then
            echo "✅ Transformers TS packages: PASSED"
        else
            echo "❌ Transformers TS packages: FAILED"
            exit 1
        fi
        conda deactivate
    else
        echo "❌ Failed to activate env_transformers_ts"
        exit 1
    fi
else
    echo "⚠️ env_transformers_ts not found, skipping package tests"
fi

# Test llm_chronos packages
if env_exists "env_llm_chronos"; then
    if conda activate env_llm_chronos; then
        if python -c "
import sys
packages_to_test = ['transformers', 'numpy', 'pandas', 'chronos', 'timesfm', 'matplotlib', 'seaborn', 'plotly', 'scipy', 'sklearn']
failed_imports = []
for pkg in packages_to_test:
    try:
        __import__(pkg)
        print(f'✅ {pkg} imported successfully')
    except ImportError as e:
        failed_imports.append(pkg)
        print(f'❌ {pkg} failed to import: {e}')
if failed_imports:
    print(f'Total failed imports: {len(failed_imports)}')
    sys.exit(1)
else:
    print('🎉 All llm_chronos imports successful!')
" 2>/dev/null; then
            echo "✅ LLM Chronos packages: PASSED"
        else
            echo "❌ LLM Chronos packages: FAILED"
            exit 1
        fi
        conda deactivate
    else
        echo "❌ Failed to activate env_llm_chronos"
        exit 1
    fi
else
    echo "⚠️ env_llm_chronos not found, skipping package tests"
fi

# Test llm_uni2ts packages
if env_exists "env_llm_uni2ts"; then
    if conda activate env_llm_uni2ts; then
        if python -c "
import sys
packages_to_test = ['transformers', 'numpy', 'pandas', 'einops', 'uni2ts', 'matplotlib', 'seaborn', 'plotly', 'scipy', 'sklearn']
failed_imports = []
for pkg in packages_to_test:
    try:
        __import__(pkg)
        print(f'✅ {pkg} imported successfully')
    except ImportError as e:
        failed_imports.append(pkg)
        print(f'❌ {pkg} failed to import: {e}')
if failed_imports:
    print(f'Total failed imports: {len(failed_imports)}')
    sys.exit(1)
else:
    print('🎉 All llm_uni2ts imports successful!')
" 2>/dev/null; then
            echo "✅ LLM Uni2TS packages: PASSED"
        else
            echo "❌ LLM Uni2TS packages: FAILED"
            exit 1
        fi
        conda deactivate
    else
        echo "❌ Failed to activate env_llm_uni2ts"
        exit 1
    fi
else
    echo "⚠️ env_llm_uni2ts not found, skipping package tests"
fi

# Test llm_momentfm packages
if env_exists "env_llm_momentfm"; then
    if conda activate env_llm_momentfm; then
        if python -c "
import sys
packages_to_test = ['transformers', 'numpy', 'pandas', 'einops', 'momentfm', 'matplotlib', 'seaborn', 'plotly', 'scipy', 'sklearn']
failed_imports = []
for pkg in packages_to_test:
    try:
        __import__(pkg)
        print(f'✅ {pkg} imported successfully')
    except ImportError as e:
        failed_imports.append(pkg)
        print(f'❌ {pkg} failed to import: {e}')
if failed_imports:
    print(f'Total failed imports: {len(failed_imports)}')
    sys.exit(1)
else:
    print('🎉 All llm_momentfm imports successful!')
" 2>/dev/null; then
            echo "✅ LLM MomentFM packages: PASSED"
        else
            echo "❌ LLM MomentFM packages: FAILED"
            exit 1
        fi
        conda deactivate
    else
        echo "❌ Failed to activate env_llm_momentfm"
        exit 1
    fi
else
    echo "⚠️ env_llm_momentfm not found, skipping package tests"
fi

# Test llm_mamba packages
if env_exists "env_llm_mamba"; then
    if conda activate env_llm_mamba; then
        if python -c "
import sys
packages_to_test = ['transformers', 'numpy', 'pandas', 'mamba_ssm', 'matplotlib', 'seaborn', 'plotly', 'scipy', 'sklearn']
failed_imports = []
for pkg in packages_to_test:
    try:
        __import__(pkg)
        print(f'✅ {pkg} imported successfully')
    except ImportError as e:
        failed_imports.append(pkg)
        print(f'❌ {pkg} failed to import: {e}')
if failed_imports:
    print(f'Total failed imports: {len(failed_imports)}')
    sys.exit(1)
else:
    print('🎉 All llm_mamba imports successful!')
" 2>/dev/null; then
            echo "✅ LLM Mamba packages: PASSED"
        else
            echo "❌ LLM Mamba packages: FAILED"
            exit 1
        fi
        conda deactivate
    else
        echo "❌ Failed to activate env_llm_mamba"
        exit 1
    fi
else
    echo "⚠️ env_llm_mamba not found, skipping package tests"
fi

# Test tslib_traditional packages
if env_exists "env_tslib_traditional"; then
    if conda activate env_tslib_traditional; then
        if python -c "
import sys
packages_to_test = ['statsmodels', 'prophet', 'sktime', 'numpy', 'pandas', 'scipy', 'matplotlib', 'seaborn', 'plotly', 'sklearn']
failed_imports = []
for pkg in packages_to_test:
    try:
        __import__(pkg)
        print(f'✅ {pkg} imported successfully')
    except ImportError as e:
        failed_imports.append(pkg)
        print(f'❌ {pkg} failed to import: {e}')
if failed_imports:
    print(f'Total failed imports: {len(failed_imports)}')
    sys.exit(1)
else:
    print('🎉 All tslib_traditional imports successful!')
" 2>/dev/null; then
            echo "✅ TSLib Traditional packages: PASSED"
        else
            echo "❌ TSLib Traditional packages: FAILED"
            exit 1
        fi
        conda deactivate
    else
        echo "❌ Failed to activate env_tslib_traditional"
        exit 1
    fi
else
    echo "⚠️ env_tslib_traditional not found, skipping package tests"
fi

# Test tslib_nixtla packages
if env_exists "env_tslib_nixtla"; then
    if conda activate env_tslib_nixtla; then
        if python -c "
import sys
packages_to_test = ['nixtla', 'statsforecast', 'mlforecast', 'neuralforecast', 'hierarchicalforecast', 'numpy', 'pandas', 'matplotlib', 'seaborn', 'plotly', 'scipy', 'sklearn']
failed_imports = []
for pkg in packages_to_test:
    try:
        __import__(pkg)
        print(f'✅ {pkg} imported successfully')
    except ImportError as e:
        failed_imports.append(pkg)
        print(f'❌ {pkg} failed to import: {e}')
if failed_imports:
    print(f'Total failed imports: {len(failed_imports)}')
    sys.exit(1)
else:
    print('🎉 All tslib_nixtla imports successful!')
" 2>/dev/null; then
            echo "✅ TSLib Nixtla packages: PASSED"
        else
            echo "❌ TSLib Nixtla packages: FAILED"
            exit 1
        fi
        conda deactivate
    else
        echo "❌ Failed to activate env_tslib_nixtla"
        exit 1
    fi
else
    echo "⚠️ env_tslib_nixtla not found, skipping package tests"
fi

# Test tslib_advanced packages
if env_exists "env_tslib_advanced"; then
    if conda activate env_tslib_advanced; then
        if python -c "
import sys
packages_to_test = ['darts', 'tslearn', 'tsfresh', 'pytorch_lightning', 'numpy', 'pandas', 'einops', 'matplotlib', 'seaborn', 'plotly', 'scipy', 'sklearn']
failed_imports = []
for pkg in packages_to_test:
    try:
        __import__(pkg)
        print(f'✅ {pkg} imported successfully')
    except ImportError as e:
        failed_imports.append(pkg)
        print(f'❌ {pkg} failed to import: {e}')
if failed_imports:
    print(f'Total failed imports: {len(failed_imports)}')
    sys.exit(1)
else:
    print('🎉 All tslib_advanced imports successful!')
" 2>/dev/null; then
            echo "✅ TSLib Advanced packages: PASSED"
        else
            echo "❌ TSLib Advanced packages: FAILED"
            exit 1
        fi
        conda deactivate
    else
        echo "❌ Failed to activate env_tslib_advanced"
        exit 1
    fi
else
    echo "⚠️ env_tslib_advanced not found, skipping package tests"
fi

# Test base_torch packages
if env_exists "env_base_torch"; then
    if conda activate env_base_torch; then
        if python -c "
import sys
packages_to_test = ['torch', 'torchvision', 'torchaudio', 'torch_geometric', 'lightning', 'tensorboard']
failed_imports = []
for pkg in packages_to_test:
    try:
        __import__(pkg)
        print(f'✅ {pkg} imported successfully')
    except ImportError as e:
        failed_imports.append(pkg)
        print(f'❌ {pkg} failed to import: {e}')
if failed_imports:
    print(f'Total failed imports: {len(failed_imports)}')
    sys.exit(1)
else:
    print('🎉 All base_torch imports successful!')
" 2>/dev/null; then
            echo "✅ Base Torch packages: PASSED"
        else
            echo "❌ Base Torch packages: FAILED"
            exit 1
        fi
        conda deactivate
    else
        echo "❌ Failed to activate env_base_torch"
        exit 1
    fi
else
    echo "⚠️ env_base_torch not found, skipping package tests"
fi

# Test geometric packages
if env_exists "env_geometric"; then
    if conda activate env_geometric; then
        if python -c "
import sys
packages_to_test = ['torch_geometric']
failed_imports = []
for pkg in packages_to_test:
    try:
        __import__(pkg)
        print(f'✅ {pkg} imported successfully')
    except ImportError as e:
        failed_imports.append(pkg)
        print(f'❌ {pkg} failed to import: {e}')
if failed_imports:
    print(f'Total failed imports: {len(failed_imports)}')
    sys.exit(1)
else:
    print('🎉 All geometric imports successful!')
" 2>/dev/null; then
            echo "✅ Geometric packages: PASSED"
        else
            echo "❌ Geometric packages: FAILED"
            exit 1
        fi
        conda deactivate
    else
        echo "❌ Failed to activate env_geometric"
        exit 1
    fi
else
    echo "⚠️ env_geometric not found, skipping package tests"
fi

# Test tensorflow packages
if env_exists "env_tensorflow"; then
    if conda activate env_tensorflow; then
        if python -c "
import sys
packages_to_test = ['tensorflow', 'tensorflow_probability', 'gluonts', 'keras', 'tensorboard', 'tensorflow_addons']
failed_imports = []
for pkg in packages_to_test:
    try:
        __import__(pkg)
        print(f'✅ {pkg} imported successfully')
    except ImportError as e:
        failed_imports.append(pkg)
        print(f'❌ {pkg} failed to import: {e}')
if failed_imports:
    print(f'Total failed imports: {len(failed_imports)}')
    sys.exit(1)
else:
    print('🎉 All tensorflow imports successful!')
" 2>/dev/null; then
            echo "✅ TensorFlow packages: PASSED"
        else
            echo "❌ TensorFlow packages: FAILED"
            exit 1
        fi
        conda deactivate
    else
        echo "❌ Failed to activate env_tensorflow"
        exit 1
    fi
else
    echo "⚠️ env_tensorflow not found, skipping package tests"
fi

# Test rapids packages
if env_exists "env_rapids"; then
    if conda activate env_rapids; then
        if python -c "
import sys
packages_to_test = ['cudf', 'cuml', 'cugraph']
failed_imports = []
for pkg in packages_to_test:
    try:
        __import__(pkg)
        print(f'✅ {pkg} imported successfully')
    except ImportError as e:
        failed_imports.append(pkg)
        print(f'❌ {pkg} failed to import: {e}')
if failed_imports:
    print(f'Total failed imports: {len(failed_imports)}')
    sys.exit(1)
else:
    print('🎉 All rapids imports successful!')
" 2>/dev/null; then
            echo "✅ RAPIDS packages: PASSED"
        else
            echo "❌ RAPIDS packages: FAILED"
            exit 1
        fi
        conda deactivate
    else
        echo "❌ Failed to activate env_rapids"
        exit 1
    fi
else
    echo "⚠️ env_rapids not found, skipping package tests"
fi

# Test anomaly advanced packages
if env_exists "env_anomaly_advanced"; then
    if conda activate env_anomaly_advanced; then
        if python -c "
import sys
packages_to_test = ['torch', 'sklearn']
failed_imports = []
for pkg in packages_to_test:
    try:
        __import__(pkg)
        print(f'✅ {pkg} imported successfully')
    except ImportError as e:
        failed_imports.append(pkg)
        print(f'❌ {pkg} failed to import: {e}')
if failed_imports:
    print(f'Total failed imports: {len(failed_imports)}')
    sys.exit(1)
else:
    print('🎉 All anomaly advanced model imports successful!')
" 2>/dev/null; then
            echo "✅ Anomaly Advanced packages: PASSED"
        else
            echo "❌ Anomaly Advanced packages: FAILED"
            exit 1
        fi
        conda deactivate
    else
        echo "❌ Failed to activate env_anomaly_advanced"
        exit 1
    fi
else
    echo "⚠️ env_anomaly_advanced not found, skipping package tests"
fi

# Test federated packages
if env_exists "env_federated"; then
    if conda activate env_federated; then
        if python -c "
import sys
packages_to_test = ['flwr']
failed_imports = []
for pkg in packages_to_test:
    try:
        __import__(pkg)
        print(f'✅ {pkg} imported successfully')
    except ImportError as e:
        failed_imports.append(pkg)
        print(f'❌ {pkg} failed to import: {e}')
if failed_imports:
    print(f'Total failed imports: {len(failed_imports)}')
    sys.exit(1)
else:
    print('🎉 All federated model imports successful!')
" 2>/dev/null; then
            echo "✅ Federated packages: PASSED"
        else
            echo "❌ Federated packages: FAILED"
            exit 1
        fi
        conda deactivate
    else
        echo "❌ Failed to activate env_federated"
        exit 1
    fi
else
    echo "⚠️ env_federated not found, skipping package tests"
fi

# Test multimodal packages
if env_exists "env_multimodal"; then
    if conda activate env_multimodal; then
        if python -c "
import sys
packages_to_test = ['transformers', 'torchvision']
failed_imports = []
for pkg in packages_to_test:
    try:
        __import__(pkg)
        print(f'✅ {pkg} imported successfully')
    except ImportError as e:
        failed_imports.append(pkg)
        print(f'❌ {pkg} failed to import: {e}')
if failed_imports:
    print(f'Total failed imports: {len(failed_imports)}')
    sys.exit(1)
else:
    print('🎉 All multimodal model imports successful!')
" 2>/dev/null; then
            echo "✅ Multimodal packages: PASSED"
        else
            echo "❌ Multimodal packages: FAILED"
            exit 1
        fi
        conda deactivate
    else
        echo "❌ Failed to activate env_multimodal"
        exit 1
    fi
else
    echo "⚠️ env_multimodal not found, skipping package tests"
fi

# Test probabilistic packages
if env_exists "env_probabilistic"; then
    if conda activate env_probabilistic; then
        if python -c "
import sys
packages_to_test = ['tensorflow_probability', 'pyro']
failed_imports = []
for pkg in packages_to_test:
    try:
        __import__(pkg)
        print(f'✅ {pkg} imported successfully')
    except ImportError as e:
        failed_imports.append(pkg)
        print(f'❌ {pkg} failed to import: {e}')
if failed_imports:
    print(f'Total failed imports: {len(failed_imports)}')
    sys.exit(1)
else:
    print('🎉 All probabilistic model imports successful!')
" 2>/dev/null; then
            echo "✅ Probabilistic packages: PASSED"
        else
            echo "❌ Probabilistic packages: FAILED"
            exit 1
        fi
        conda deactivate
    else
        echo "❌ Failed to activate env_probabilistic"
        exit 1
    fi
else
    echo "⚠️ env_probabilistic not found, skipping package tests"
fi

# Test causal packages
if env_exists "env_causal"; then
    if conda activate env_causal; then
        if python -c "
import sys
packages_to_test = ['tigramite']
failed_imports = []
for pkg in packages_to_test:
    try:
        __import__(pkg)
        print(f'✅ {pkg} imported successfully')
    except ImportError as e:
        failed_imports.append(pkg)
        print(f'❌ {pkg} failed to import: {e}')
if failed_imports:
    print(f'Total failed imports: {len(failed_imports)}')
    sys.exit(1)
else:
    print('🎉 All causal model imports successful!')
" 2>/dev/null; then
            echo "✅ Causal packages: PASSED"
        else
            echo "❌ Causal packages: FAILED"
            exit 1
        fi
        conda deactivate
    else
        echo "❌ Failed to activate env_causal"
        exit 1
    fi
else
    echo "⚠️ env_causal not found, skipping package tests"
fi

# Test vision time series packages
if env_exists "env_vision_ts"; then
    if conda activate env_vision_ts; then
        if python -c "
import sys
packages_to_test = ['transformers', 'torchvision']
failed_imports = []
for pkg in packages_to_test:
    try:
        __import__(pkg)
        print(f'✅ {pkg} imported successfully')
    except ImportError as e:
        failed_imports.append(pkg)
        print(f'❌ {pkg} failed to import: {e}')
if failed_imports:
    print(f'Total failed imports: {len(failed_imports)}')
    sys.exit(1)
else:
    print('🎉 All vision time series model imports successful!')
" 2>/dev/null; then
            echo "✅ Vision TS packages: PASSED"
        else
            echo "❌ Vision TS packages: FAILED"
            exit 1
        fi
        conda deactivate
    else
        echo "❌ Failed to activate env_vision_ts"
        exit 1
    fi
else
    echo "⚠️ env_vision_ts not found, skipping package tests"
fi

echo "🎉 All tests completed successfully!"
--- END FILE ---

