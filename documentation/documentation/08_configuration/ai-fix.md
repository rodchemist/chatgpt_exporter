# AI System Troubleshooting and Auto-Fix

Automatically diagnose and attempt to fix common AI agent issues.

## Usage
This command runs automated troubleshooting and repair procedures for:
- Command not found errors
- Service connectivity issues
- Environment activation problems
- Ollama model and service issues
- Configuration file problems

## Implementation
```bash
echo "🔧 AI System Auto-Fix and Troubleshooting"
echo "=========================================="

# Step 1: Check if basic commands are available
echo "1. 📋 Checking basic AI commands..."
if ! command -v ai-help >/dev/null 2>&1; then
    echo "❌ AI commands not found - attempting to reload..."
    source ~/.ai_enhanced_aliases 2>/dev/null || echo "⚠️  Could not load enhanced aliases"
    source ~/.bashrc 2>/dev/null || echo "⚠️  Could not reload bashrc"

    if command -v ai-help >/dev/null 2>&1; then
        echo "✅ AI commands restored"
    else
        echo "❌ AI commands still not available - check ~/.ai_enhanced_aliases exists"
    fi
else
    echo "✅ AI commands available"
fi

# Step 2: Check and fix Ollama service
echo ""
echo "2. 🧠 Checking Ollama service..."
if command -v ollama >/dev/null 2>&1; then
    if ! timeout 5 ollama list >/dev/null 2>&1; then
        echo "🔄 Starting Ollama service..."
        ollama serve >/dev/null 2>&1 &
        sleep 3
        if timeout 5 ollama list >/dev/null 2>&1; then
            echo "✅ Ollama service started"
        else
            echo "❌ Could not start Ollama service"
        fi
    else
        echo "✅ Ollama service running"
    fi
else
    echo "⚠️  Ollama not installed"
fi

# Step 3: Check and attempt to start Rod-Corp services
echo ""
echo "3. 🌐 Checking Rod-Corp services..."
if [ -f "/home/rod/rod-corp/start_system.sh" ]; then
    offline_ports=0
    for port in 18000 17000 15000 16000; do
        if ! timeout 3 nc -z localhost $port 2>/dev/null; then
            ((offline_ports++))
        fi
    done

    if [ $offline_ports -gt 0 ]; then
        echo "🔄 Starting Rod-Corp services ($offline_ports ports offline)..."
        cd /home/rod/rod-corp && timeout 30 ./start_system.sh >/dev/null 2>&1 &
        echo "✅ Rod-Corp startup initiated"
    else
        echo "✅ Rod-Corp services online"
    fi
else
    echo "⚠️  Rod-Corp startup script not found"
fi

# Step 4: Environment validation
echo ""
echo "4. 🌍 Checking environment status..."
if command -v mamba >/dev/null 2>&1; then
    current_env=$(mamba env list | grep "^\*" | awk '{print $1}' 2>/dev/null || echo "unknown")
    echo "✅ Mamba available, current environment: $current_env"
else
    echo "⚠️  Mamba not available, using system environment"
fi

# Step 5: Check critical file permissions and existence
echo ""
echo "5. 📁 Checking critical files..."
critical_files=(
    "~/.bashrc"
    "~/.ai_enhanced_aliases"
    "/home/rod/.local/bin/check-ai-dependencies"
    "/home/rod/.local/bin/ai-env-manager"
    "/home/rod/rod-corp/ROD_CORP_AUTO_INIT_ENHANCED.sh"
)

for file in "${critical_files[@]}"; do
    expanded_file=$(eval echo "$file")
    if [ -f "$expanded_file" ]; then
        if [ -x "$expanded_file" ] || [[ "$expanded_file" == *.sh ]] || [[ "$expanded_file" == *bashrc* ]] || [[ "$expanded_file" == *aliases* ]]; then
            echo "✅ $file: OK"
        else
            echo "🔧 $file: Making executable..."
            chmod +x "$expanded_file" 2>/dev/null || echo "❌ Could not make $file executable"
        fi
    else
        echo "❌ $file: MISSING"
    fi
done

# Step 6: Test one AI agent
echo ""
echo "6. 🤖 Testing AI agent functionality..."
if command -v claude-full >/dev/null 2>&1; then
    echo "Testing claude-full..."
    timeout 10 claude-full --help >/dev/null 2>&1 && echo "✅ Claude agent working" || echo "⚠️  Claude agent issues detected"
else
    echo "❌ claude-full command not available"
fi

# Step 7: Quick diagnostic summary
echo ""
echo "7. 📊 System Status Summary:"
ai-status 2>/dev/null || check-ai-dependencies 2>/dev/null || echo "❌ Status commands not available"

echo ""
echo "🎯 Auto-fix complete! Run 'ai-status' for detailed system health."
echo "💡 For manual troubleshooting, see: /home/rod/rod-corp/docs/ai-agents/TROUBLESHOOTING.md"
```

This command automatically diagnoses and attempts to fix the most common AI system issues.