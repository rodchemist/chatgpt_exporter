# 🔄 AI System Migration Guide - From Old to New Orchestration

## 🎯 **Current Situation**

You have **two AI agent systems** conflicting with each other:

1. **Old System**: `ai-help` commands (oi-codellama, aider-mistral, etc.)
2. **New System**: Smart orchestration with optimal model selection

## ✅ **Recommended Migration**

### **Step 1: Use New Smart Commands**

**Instead of old commands, use these:**

| Old Command | New Smart Command | Model Used |
|-------------|-------------------|------------|
| `oi-codellama` | `oi-smart` | llama3.1:latest (better) |
| `oi-mistral` | `oi-fast` | mistral:latest |
| `oi-deepseek` | `oi-heavy` | mixtral:8x7b (superior) |
| `aider` | `aider-auto` | Auto-selected optimal |
| `aider-deepseek` | `aider-heavy` | deepseek-coder:33b |
| `aider-mistral` | `aider-fast` | deepseek-coder:6.7b |

### **Step 2: Load New Environment**

```bash
# Always run this first in new sessions:
source ~/ai-orchestration/configs/aliases.sh
```

### **Step 3: Test New System**

```bash
# Smart model selection based on project complexity
aider-auto

# Or direct commands:
aider-heavy     # For complex tasks (deepseek-coder:33b)
aider-fast      # For quick tasks (deepseek-coder:6.7b)

# Open Interpreter (fixed commands):
mamba run -n env_openint interpreter --local --model ollama/llama3.1:latest
mamba run -n env_openint interpreter --local --model ollama/mistral:latest
```

---

## 🔧 **Fixing Open Interpreter Issues**

The `oi-codellama` error was caused by incorrect host configuration. Here's the fix:

### **Corrected Open Interpreter Commands**

```bash
# Smart aliases (add to ~/.bashrc if missing):
alias oi-smart='mamba run -n env_openint interpreter --local --model ollama/llama3.1:latest'
alias oi-fast='mamba run -n env_openint interpreter --local --model ollama/mistral:latest'
alias oi-heavy='mamba run -n env_openint interpreter --local --model ollama/mixtral:8x7b'

# Or use directly:
mamba run -n env_openint interpreter --local --model ollama/llama3.1:latest
```

---

## 🚀 **Your New Workflow**

### **For Development Work**
```bash
# 1. Load environment
source ~/ai-orchestration/configs/aliases.sh

# 2. Navigate to project
cd /mnt/c/_Repos_Rod/MERGING\ REPOS\ ROD/mycrypto

# 3. Use smart Aider
aider-auto --task "analyze cryptocurrency codebase"
# → Automatically selects deepseek-coder:33b for complex crypto project

# 4. Or use orchestration
ai-orchestrate
# → Full workflow with Claude planning + local execution
```

### **For Quick Tasks**
```bash
# Fast coding
aider-fast filename.py

# Quick testing
mamba run -n env_openint interpreter --local --model ollama/mistral:latest
```

### **For Complex Analysis**
```bash
# Team consultation first
ai-team "What's the best way to merge these crypto repositories?"

# Then heavy implementation
aider-heavy
```

---

## 🎭 **Model Quality Comparison**

### **Your New System Uses Better Models**

| Task Type | Old System | New System | Improvement |
|-----------|------------|------------|-------------|
| **Complex Coding** | deepseek-coder:6.7b | deepseek-coder:33b | 🚀 5x larger, much smarter |
| **General Tasks** | codellama:13b | llama3.1:latest | ✨ Newer, more capable |
| **Analysis** | mistral:latest | mixtral:8x7b | 🧠 8x expert ensemble |
| **Quick Tasks** | codellama:13b | deepseek-coder:6.7b | ⚡ Specialized for code |

---

## 📋 **Migration Checklist**

### **Immediate Actions**
- [ ] Run: `source ~/ai-orchestration/configs/aliases.sh`
- [ ] Test: `aider-auto --list-models`
- [ ] Try: `ai-models` to see recommendations
- [ ] Use: `aider-auto` instead of old `aider` commands

### **Optional: Clean Up Old System**
If you want to remove the conflicting old system:

```bash
# Check what's in your old AI aliases
cat ~/.ai_agents_aliases

# You can comment out the old aliases if needed
# But it's safe to keep both - just use the new ones
```

---

## ✨ **Summary**

**Problem**: Old `oi-codellama` failed due to host configuration issues  
**Solution**: Use new smart system with proper environment management

**Your optimal command for crypto work**:
```bash
source ~/ai-orchestration/configs/aliases.sh
cd /mnt/c/_Repos_Rod/MERGING\ REPOS\ ROD/mycrypto
aider-auto --task "merge and refactor cryptocurrency repositories"
```

**This will give you the best AI coding experience with your strongest models! 🎯**