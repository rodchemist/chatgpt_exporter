# AI System Debug and Diagnostics

Comprehensive debugging and diagnostic tools for the AI agent system.

## Usage
This command provides deep debugging capabilities for troubleshooting complex AI system issues, including log analysis, configuration validation, and performance monitoring.

## Implementation
```bash
echo "🔍 AI System Debug and Diagnostics"
echo "=================================="

# Enable debug mode
export RODCORP_DEBUG=true
export AI_DEBUG=true

echo "🐛 Debug mode enabled - verbose logging active"

echo ""
echo "1. 📊 System Information"
echo "======================="
echo "OS: $(uname -a)"
echo "Shell: $SHELL"
echo "User: $USER"
echo "Working Directory: $(pwd)"
echo "Date: $(date)"

echo ""
echo "2. 🔧 AI System Components Status"
echo "================================="

# Check critical files
echo "📁 Critical Files:"
critical_files=(
    "~/.bashrc"
    "~/.ai_enhanced_aliases"
    "/home/rod/.local/bin/check-ai-dependencies"
    "/home/rod/.local/bin/ai-env-manager"
    "/home/rod/.local/bin/backup-bashrc"
    "/home/rod/rod-corp/ROD_CORP_AUTO_INIT_ENHANCED.sh"
)

for file in "${critical_files[@]}"; do
    expanded_file=$(eval echo "$file")
    if [ -f "$expanded_file" ]; then
        local perms=$(ls -l "$expanded_file" | cut -d' ' -f1)
        local size=$(ls -lh "$expanded_file" | cut -d' ' -f5)
        echo "  ✅ $file ($perms, $size)"
    else
        echo "  ❌ $file (MISSING)"
    fi
done

echo ""
echo "3. 🌐 Network Connectivity Debug"
echo "==============================="

echo "🔍 Testing Rod-Corp service ports:"
for port in 18000 17000 15000 16000 5678 9000; do
    if timeout 3 nc -z localhost $port 2>/dev/null; then
        echo "  ✅ Port $port: ONLINE"
    else
        echo "  ❌ Port $port: OFFLINE"
        # Check what might be using the port
        local process=$(lsof -ti:$port 2>/dev/null || echo "none")
        echo "     Process: $process"
    fi
done

echo ""
echo "🔍 Testing external connectivity:"
if ping -c 1 8.8.8.8 >/dev/null 2>&1; then
    echo "  ✅ Internet connectivity: OK"
else
    echo "  ❌ Internet connectivity: FAILED"
fi

if ping -c 1 10.0.0.2 >/dev/null 2>&1; then
    echo "  ✅ MSSQL server reachable: OK"
else
    echo "  ❌ MSSQL server unreachable: FAILED"
fi

echo ""
echo "4. 🗄️ Database Connectivity Debug"
echo "================================"

echo "🔍 Testing MSSQL connection:"
if timeout 10 nc -z 10.0.0.2 1433 2>/dev/null; then
    echo "  ✅ MSSQL port accessible"

    if command -v sqlcmd >/dev/null 2>&1; then
        echo "  🔍 Testing authentication..."
        if timeout 15 sqlcmd -S "10.0.0.2,1433" -U "$ROD_CORP_MSSQL_USER" -P "$ROD_CORP_MSSQL_PASSWORD" -Q "SELECT 1" >/dev/null 2>&1; then
            echo "  ✅ MSSQL authentication: SUCCESS"
        else
            echo "  ❌ MSSQL authentication: FAILED"
        fi
    else
        echo "  ⚠️  sqlcmd not available for auth test"
    fi
else
    echo "  ❌ MSSQL port not accessible"
fi

echo ""
echo "🔍 Checking SQLite fallback:"
local fallback_db="$HOME/.rod_corp_local.db"
if [ -f "$fallback_db" ]; then
    echo "  ✅ SQLite fallback exists: $(ls -lh "$fallback_db" | cut -d' ' -f5)"
    echo "  📊 Tables: $(sqlite3 "$fallback_db" ".tables" | wc -w)"
    echo "  📊 Agents: $(sqlite3 "$fallback_db" "SELECT COUNT(*) FROM agents;" 2>/dev/null || echo "N/A")"
else
    echo "  ⚠️  SQLite fallback not created yet"
fi

echo ""
echo "5. 🧠 Ollama System Debug"
echo "========================"

if command -v ollama >/dev/null 2>&1; then
    echo "  ✅ Ollama command available: $(which ollama)"

    if timeout 10 ollama list >/dev/null 2>&1; then
        echo "  ✅ Ollama service responding"

        echo "  📊 Model inventory:"
        ollama list 2>/dev/null | tail -n +2 | head -10 | while read model size created; do
            echo "    - $model ($size)"
        done

        local total_models=$(ollama list 2>/dev/null | tail -n +2 | wc -l)
        echo "  📊 Total models: $total_models"

        # Check disk usage for Ollama
        local ollama_dir="$HOME/.ollama"
        if [ -d "$ollama_dir" ]; then
            echo "  💽 Ollama storage: $(du -sh "$ollama_dir" 2>/dev/null | cut -f1)"
        fi
    else
        echo "  ❌ Ollama service not responding"
        echo "  🔍 Checking Ollama processes:"
        ps aux | grep -E "(ollama|llama)" | grep -v grep || echo "    No Ollama processes found"
    fi
else
    echo "  ❌ Ollama not installed"
fi

echo ""
echo "6. 🌍 Environment Debug"
echo "======================"

if command -v mamba >/dev/null 2>&1; then
    echo "  ✅ Mamba available: $(which mamba)"
    echo "  📊 Current environment: $(mamba env list | grep '^\*' | awk '{print $1}' || echo 'none')"
    echo "  📊 Total environments: $(mamba env list | grep -c '^  ')"

    echo "  🔍 Environment validation:"
    echo "    Python: $(which python || echo 'not found')"
    echo "    Node.js: $(which node || echo 'not found')"
    echo "    Curl: $(which curl || echo 'not found')"
else
    echo "  ❌ Mamba not available"
    if command -v conda >/dev/null 2>&1; then
        echo "  ✅ Conda available: $(which conda)"
    else
        echo "  ❌ Conda also not available"
    fi
fi

echo ""
echo "7. 📋 System Logs Analysis"
echo "=========================="

echo "🔍 Recent AI system activity:"
local log_files=(
    "$HOME/.rod_corp_init.log"
    "$HOME/.ai_dependencies.log"
    "$HOME/.ai_env_manager.log"
)

for log_file in "${log_files[@]}"; do
    if [ -f "$log_file" ]; then
        local log_size=$(ls -lh "$log_file" | cut -d' ' -f5)
        local last_entry=$(tail -1 "$log_file" 2>/dev/null | cut -d']' -f1 | cut -d'[' -f2)
        echo "  📄 $(basename "$log_file"): $log_size (last: $last_entry)"

        echo "    Recent entries:"
        tail -3 "$log_file" 2>/dev/null | sed 's/^/      /' || echo "      No recent entries"
    else
        echo "  ❌ $(basename "$log_file"): Not found"
    fi
done

echo ""
echo "8. 🚨 Error Detection"
echo "===================="

echo "🔍 Scanning for recent errors:"
for log_file in "${log_files[@]}"; do
    if [ -f "$log_file" ]; then
        local errors=$(grep -i "error\|failed\|exception" "$log_file" 2>/dev/null | tail -3)
        if [ -n "$errors" ]; then
            echo "  ⚠️  Errors in $(basename "$log_file"):"
            echo "$errors" | sed 's/^/      /'
        fi
    fi
done

# Check system journal for AI-related errors
if command -v journalctl >/dev/null 2>&1; then
    local journal_errors=$(journalctl --user -n 10 --no-pager 2>/dev/null | grep -i "rod-corp\|ai-agent\|ollama" || echo "")
    if [ -n "$journal_errors" ]; then
        echo "  📰 System journal entries:"
        echo "$journal_errors" | sed 's/^/      /'
    fi
fi

echo ""
echo "9. 🔧 Configuration Validation"
echo "=============================="

echo "🔍 Validating AI agent aliases:"
if declare -f claude-full >/dev/null 2>&1; then
    echo "  ✅ claude-full function defined"
else
    echo "  ❌ claude-full function not defined"
fi

if alias | grep -q "ai-help\|ai-status"; then
    echo "  ✅ AI utility aliases available"
else
    echo "  ❌ AI utility aliases not loaded"
fi

echo ""
echo "🔍 Environment variables:"
env_vars=("RODCORP_INTEGRATED" "RODCORP_AGENT_ID" "RODCORP_CONTEXT" "AI_CURRENT_ENV")
for var in "${env_vars[@]}"; do
    local value="${!var}"
    if [ -n "$value" ]; then
        echo "  ✅ $var: ${value:0:50}..."
    else
        echo "  ⚠️  $var: Not set"
    fi
done

echo ""
echo "10. 📊 Performance Metrics"
echo "========================="

echo "🔍 System resources:"
echo "  💾 Memory: $(free -h | grep '^Mem:' | awk '{print $3 "/" $2 " (" $3/$2*100 "% used)"}')"
echo "  💽 Disk: $(df -h / | tail -1 | awk '{print $3 "/" $2 " (" $5 " used)"}')"
echo "  🖥️  Load: $(uptime | sed 's/.*load average: //')"

echo ""
echo "🔍 AI system overhead:"
ai_processes=$(ps aux | grep -E "(ollama|claude|qwen|codex)" | grep -v grep | wc -l)
echo "  🤖 AI processes: $ai_processes"

if [ -d "$HOME/.ollama" ]; then
    echo "  🧠 Ollama storage: $(du -sh "$HOME/.ollama" 2>/dev/null | cut -f1)"
fi

echo ""
echo "🎯 Debug Summary:"
echo "================="
echo "✅ Debug mode active - verbose logging enabled"
echo "📊 System diagnostics complete"
echo "📋 Check sections above for specific issues"
echo "💡 For targeted fixes, run: /ai-fix"
echo "📖 For detailed troubleshooting: cat /home/rod/rod-corp/docs/ai-agents/TROUBLESHOOTING.md"

# Disable debug mode
unset RODCORP_DEBUG
unset AI_DEBUG
```

This command provides comprehensive debugging and diagnostic capabilities for deep troubleshooting.