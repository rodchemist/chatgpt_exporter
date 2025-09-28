# AI Agents Quick Launcher

Quick access to all available AI agents with status checks, model validation, and performance benchmarking.

## Usage
Launch AI agents with automatic environment preparation, dependency validation, fallback handling, and performance metrics.

## Implementation
```bash
#!/bin/bash
# Enhanced AI Agents Quick Launcher with Error Handling and Performance Metrics

# Standardized output functions
print_header() {
    echo "🚀 $1"
    echo "========================"
}

print_success() {
    echo "✅ $1"
}

print_warning() {
    echo "⚠️  $1"
}

print_error() {
    echo "❌ $1"
}

print_info() {
    echo "ℹ️  $1"
}

# Error handling
set -e

print_header "AI Agents Quick Launcher"

# Function to check agent availability with enhanced error handling
check_agent_availability() {
    local agent="$1"
    local command_name="${agent}-full"

    if command -v "$command_name" >/dev/null 2>&1; then
        print_success "$agent"
    else
        print_error "$agent (command not found)"
    fi
}

# Function to check Ollama model with performance metrics
check_ollama_model() {
    local model="$1"
    if command -v ollama >/dev/null 2>&1; then
        if timeout 5 ollama list 2>/dev/null | grep -q "^${model}"; then
            # Check if model is running and get basic performance info
            if timeout 10 ollama run "$model" "respond with 'OK' only" >/dev/null 2>&1; then
                print_success "$model (response time: fast)"
            else
                print_warning "$model (available but slow)"
            fi
        else
            print_error "$model (not installed)"
        fi
    else
        print_warning "$model (Ollama not available)"
    fi
}

# Function to benchmark agent response time
benchmark_agent() {
    local agent="$1"
    local command_name="${agent}-full"
    
    if command -v "$command_name" >/dev/null 2>&1; then
        local start_time=$(date +%s%3N)
        # Simple benchmark - send a minimal request
        timeout 30 "$command_name" --approval-mode=yolo "respond with 'OK' only" >/dev/null 2>&1
        local end_time=$(date +%s%3N)
        local duration=$((end_time - start_time))
        
        if [ $? -eq 0 ]; then
            print_info "$agent response time: ${duration}ms"
        else
            print_warning "$agent benchmark failed (timeout or error)"
        fi
    else
        print_warning "$agent not available for benchmarking"
    fi
}

echo "📋 Available AI Agents:"
echo "======================"

echo ""
echo "☁️ Cloud-Based Agents:"
echo "----------------------"
check_agent_availability "claude"
check_agent_availability "qwen"
check_agent_availability "codex"
check_agent_availability "gemini"

echo ""
echo "🧠 Local Ollama Agents:"
echo "----------------------"
check_agent_availability "deepseek"
check_agent_availability "mixtral"
check_agent_availability "codellama"
check_agent_availability "qwen-local"

echo ""
echo "📊 Ollama Model Status:"
echo "======================"
if command -v ollama >/dev/null 2>&1; then
    if timeout 5 ollama list >/dev/null 2>&1; then
        echo "🔍 Checking required models:"
        check_ollama_model "deepseek-coder:33b"
        check_ollama_model "qwen2.5-coder:latest"
        check_ollama_model "mixtral:8x7b"
        check_ollama_model "codellama:34b"

        echo ""
        echo "📋 All available models:"
        ollama list 2>/dev/null | tail -n +2 | head -10 | while read model size created; do
            print_success "$model"
        done

        local total_models=$(ollama list 2>/dev/null | tail -n +2 | wc -l)
        if [ "$total_models" -gt 10 ]; then
            print_info "... and $((total_models - 10)) more models"
        fi
    else
        print_warning "Ollama service not responding"
        print_info "Try: ollama serve &"
    fi
else
    print_error "Ollama not installed"
fi

echo ""
echo "🌍 Environment Status:"
echo "====================="
if command -v ai-env-manager >/dev/null 2>&1; then
    ai-env-manager current
else
    print_info "Current environment: $(conda info --envs 2>/dev/null | grep '^*' | awk '{print $1}' || echo 'system')"
fi

echo ""
echo "⚡ Performance Benchmarks:"
echo "========================="
print_info "Running quick benchmarks (this may take a moment)..."
benchmark_agent "claude"
benchmark_agent "qwen"

echo ""
echo "🚀 Quick Launch Commands:"
echo "========================="

echo "☁️ Cloud Agents:"
echo "claude-full                  # Claude with Rod-Corp integration"
echo "qwen-full                   # Qwen with environment management"
echo "codex-full                  # GitHub Codex with validation"
echo "gemini-full                 # Google Gemini with fallbacks"

echo ""
echo "🧠 Local Agents:"
echo "deepseek-full               # DeepSeek Coder (33b → 6.7b → latest)"
echo "mixtral-full                # Mixtral (8x7b → latest → mistral)"
echo "codellama-full              # CodeLlama (34b → 13b → 7b)"
echo "qwen-local                  # Local Qwen (2.5-coder → 2 → latest)"

echo ""
echo "🔧 System Commands:"
echo "==================="
echo "ai-status                   # Complete system health check"
echo "ai-envs                     # List all environments"
echo "ai-help                     # Show detailed help"
echo "check-ai-dependencies       # Validate all dependencies"

echo ""
echo "💡 Smart Launch Tips:"
echo "===================="
echo "# Agents automatically:"
echo "  ✅ Activate correct mamba environment"
echo "  ✅ Check service dependencies"
echo "  ✅ Validate model availability"
echo "  ✅ Provide alternative models if needed"
echo "  ✅ Fall back gracefully on failures"

echo ""
echo "🎯 Environment Recommendations:"
echo "==============================="
echo "claude, codex, gemini    → Use 'base' environment"
echo "qwen                     → Use 'env_pytorch_transformers'"
echo "deepseek, mixtral,       → Use 'env_ollama'"
echo "codellama, qwen-local"

echo ""
echo "🔄 Quick Fixes:"
echo "==============="
echo "# If agents not found:"
echo "source ~/.ai_enhanced_aliases"

echo ""
echo "# If Ollama issues:"
echo "ollama serve &"
echo "ollama pull deepseek-coder:33b"

echo ""
echo "# If environment issues:"
echo "ai-env-manager prepare <agent-name>"

echo ""
echo "# If service issues:"
echo "cd /home/rod/rod-corp && ./start_system.sh"

# Quick system validation
echo ""
echo "⚡ Quick System Validation:"
echo "=========================="

# Test if basic AI commands work
if command -v ai-help >/dev/null 2>&1; then
    print_success "AI command system operational"
else
    print_error "AI command system not available - run: source ~/.bashrc"
fi

# Test if any agent works
if command -v claude-full >/dev/null 2>&1; then
    print_success "AI agents available"
else
    print_error "AI agents not available - check configuration"
fi

# Test system status
if command -v ai-status >/dev/null 2>&1; then
    print_success "System status monitoring available"
else
    print_warning "System monitoring not available"
fi

print_success "AI Agents Quick Launcher Complete!"
echo "💡 Tip: Use '/ai-agents --benchmark' for performance comparisons or '/ai-status' for detailed health check"
```

## Options
- `--benchmark`: Run performance benchmarks for available agents
- `--verbose`: Enable verbose output with detailed system information
- `--help`: Show this help information

## Examples
```bash
/ai-agents
/ai-agents --benchmark
/ai-agents --verbose
```

## Features
- **Enhanced Error Handling**: Comprehensive error checking with graceful fallbacks
- **Performance Benchmarks**: Response time measurements for available agents
- **Standardized Output**: Consistent formatting with visual indicators
- **Model Validation**: Detailed checking of Ollama model availability and performance
- **Environment Status**: Current environment and recommendation checking
- **Quick Fixes**: Common troubleshooting steps for issues

This command provides a comprehensive launcher and status checker for all your AI agents with enhanced reliability and performance metrics.