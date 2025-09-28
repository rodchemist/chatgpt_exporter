# AI Environment Management

Manage mamba environments for AI agents and troubleshoot environment-related issues.

## Usage
This command helps you:
- Switch between AI agent environments
- Troubleshoot environment activation issues
- Prepare environments for specific AI agents
- Check environment requirements and dependencies

## Implementation
```bash
# Show current environment and available options
echo "🌍 Current Environment Status"
echo "=============================="
ai-env-manager current

echo ""
echo "📋 Available Environments:"
ai-envs

echo ""
echo "🤖 AI Agent Environment Mappings:"
echo "claude, codex, gemini     → base"
echo "qwen                      → env_pytorch_transformers"
echo "deepseek, mixtral,        → env_ollama"
echo "codellama, qwen-local"

echo ""
echo "🔧 Environment Management Commands:"
echo "ai-env-manager prepare <agent>    # Prepare environment for agent"
echo "ai-env-manager activate <env>     # Activate specific environment"
echo "ai-env-manager check <agent>      # Check environment requirements"

# Check if mamba is available
echo ""
if command -v mamba >/dev/null 2>&1; then
    echo "✅ Mamba: Available"
    echo "📊 Total environments: $(mamba env list | grep -c '^  ')"
else
    echo "❌ Mamba: Not available (using system environment)"
fi

# Show environment-specific package availability
echo ""
echo "🔍 Key Package Availability:"
echo "Python: $(which python || echo 'Not found')"
echo "Node.js: $(which node || echo 'Not found')"
echo "Ollama: $(which ollama || echo 'Not found')"
echo "Curl: $(which curl || echo 'Not found')"
```

Use this to diagnose and resolve environment-related issues with your AI agents.