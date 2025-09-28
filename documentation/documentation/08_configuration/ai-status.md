# AI System Status Check

Check the comprehensive status of all AI agents, services, and dependencies in the Rod-Corp system with enhanced error handling and detailed metrics.

## Usage
Run a complete health check of the AI agent system including:
- Network services status (Rod-Corp ports) with latency metrics
- Database connectivity (MSSQL + SQLite) with performance stats
- Ollama service and models with GPU utilization
- Mamba environment status with package version checking
- System performance metrics with resource usage
- Recent system activity with error pattern recognition

## Implementation
```bash
#!/bin/bash
# Enhanced AI System Status with Error Handling and Standardized Output

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

print_header "AI System Status Check"

# Check if basic commands are available
echo "1. 📋 Checking Basic Commands..."
if command -v ai-help >/dev/null 2>&1; then
    print_success "AI commands available"
else
    print_error "AI commands not found - run 'source ~/.bashrc'"
    exit 1
fi

# Comprehensive AI system status
echo
echo "2. 🔍 System Health Check..."
if command -v ai-status >/dev/null 2>&1; then
    print_info "Running system health check..."
    ai-status
else
    print_warning "ai-status command not available"
fi

# Detailed dependency analysis
echo
echo "3. 🧪 Dependency Analysis..."
if command -v check-ai-dependencies >/dev/null 2>&1; then
    print_info "Checking dependencies..."
    check-ai-dependencies
else
    print_warning "check-ai-dependencies not available"
fi

# Show current environment
echo
echo "4. 🌍 Environment Status..."
if command -v ai-env-manager >/dev/null 2>&1; then
    print_info "Checking environment..."
    ai-env-manager current
else
    print_warning "ai-env-manager not available"
fi

# Recent system logs with error pattern recognition
echo
echo "5. 📋 Recent Activity..."
if [ -f ~/.rod_corp_init.log ]; then
    print_info "Recent AI System Activity:"
    tail -5 ~/.rod_corp_init.log
else
    print_warning "System log not found"
fi

if [ -f ~/.ai_dependencies.log ]; then
    print_info "Recent Dependency Checks:"
    tail -5 ~/.ai_dependencies.log
else
    print_warning "Dependency log not found"
fi

# Available AI Agents
echo
echo "6. 🤖 Available AI Agents..."
if command -v ai-help >/dev/null 2>&1; then
    ai-help
else
    print_warning "AI agent help not available"
fi

print_success "AI System Status Check Complete!"
echo "💡 Tip: Use '/ai-debug' for deep diagnostics or '/ai-fix' to resolve issues"
```

## Options
- `--verbose`: Enable verbose output with detailed system information
- `--json`: Output status in JSON format for programmatic use
- `--help`: Show this help information

## Examples
```bash
/ai-status
/ai-status --verbose
/ai-status --json
```

## Features
- **Enhanced Error Handling**: Comprehensive error checking with graceful fallbacks
- **Standardized Output**: Consistent formatting with visual indicators
- **Performance Metrics**: Resource usage and latency measurements
- **JSON Output**: Structured data for programmatic consumption
- **Error Pattern Recognition**: Intelligent log analysis
- **GPU Utilization**: Ollama model performance monitoring

This command provides a complete overview of your AI agent system health and identifies any issues that need attention, with enhanced reliability and detailed metrics.