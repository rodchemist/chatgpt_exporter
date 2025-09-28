# AI Agent Orchestration Guide
*Coordinating Claude, Aider, Open Interpreter & Ollama*

## Overview

While Claude (web interface) cannot directly control local CLI agents, this orchestration system provides sophisticated coordination between multiple AI agents through various communication bridges and automation tools.

## 🤖 Agent Ecosystem

| Agent | Role | Access | Best For |
|-------|------|--------|----------|
| **Claude (Web)** | Architect & Planner | Web Interface | High-level design, architecture, code review |
| **Aider** | Code Implementer | Local CLI | File editing, code implementation, refactoring |
| **Open Interpreter** | Executor & Tester | Local CLI | Code execution, testing, validation |
| **Ollama** | Direct LLM Query | Local CLI | Quick queries, explanations, debugging |

---

## 🔧 Orchestration Tools Created

### 1. **AI Orchestrator** (`ai_orchestrator.py`)
**Purpose**: Full workflow coordination from Claude planning to local execution

**Features**:
- Captures implementation plans from Claude (web)
- Parses tasks automatically or manually
- Executes with Aider for implementation
- Verifies with Open Interpreter for testing
- Session logging and progress tracking

**Usage**:
```bash
ai-orchestrate              # Run full workflow
python ~/ai_orchestrator.py --help    # Show help
```

**Workflow**:
1. Get plan from Claude (copy/paste)
2. Auto-extract or manually define tasks
3. Sequential execution: Aider → Open Interpreter
4. Progress tracking and logging

---

### 2. **Agent Chaining Script** (`chain_agents.sh`)
**Purpose**: Predefined workflows with sequential agent execution

**Features**:
- Example workflows (Flask API, etc.)
- Custom workflow creation
- Interactive execution with pauses
- Comprehensive logging and error handling
- Colored output for better UX

**Usage**:
```bash
ai-chain-example            # Run Flask API example
ai-chain-custom             # Create custom workflow
ai-chain --help             # Show all options
```

**Example Workflow**:
- Step 1: Aider creates Flask API
- Step 2: Aider adds comprehensive tests
- Step 3: Open Interpreter runs and validates
- Step 4: Aider adds documentation and deployment

---

### 3. **Claude Bridge** (`claude_bridge.py`)
**Purpose**: Interactive communication bridge between Claude (web) and local agents

**Features**:
- Clipboard integration for easy copy/paste
- Multiple input methods (clipboard, file, manual)
- Context preservation across sessions
- Automatic result summarization
- Session export and logging

**Usage**:
```bash
ai-bridge                   # Start interactive mode
python ~/claude_bridge.py --help     # Show help
```

**Interactive Features**:
1. Capture Claude responses (clipboard/file/manual)
2. Execute with local agents (Aider/Open Interpreter/Ollama)
3. Create summaries for Claude feedback
4. Context management and export

---

### 4. **Task Queue System** (`task_queue.py`)
**Purpose**: Sophisticated task management with dependencies and priorities

**Features**:
- Task dependencies and priority management
- Multiple agent support
- Automatic worker execution
- Progress tracking and timing
- Comprehensive reporting

**Usage**:
```bash
# Add tasks
ai-queue add "Create Flask API" --agent aider --priority 8
ai-queue add "Write tests" --agent aider --priority 7 --depends-on 1
ai-queue add "Run tests" --agent oi --priority 6 --depends-on 2

# Show queue
ai-queue-show               # Show all tasks
ai-queue show --status pending     # Filter by status

# Execute tasks
ai-queue-next               # Show next ready task
ai-queue-run                # Run all ready tasks automatically
ai-queue exec 1             # Execute specific task

# Management
ai-queue clear-completed    # Remove finished tasks
ai-queue report             # Generate execution report
```

---

## 🎯 Usage Patterns

### **Pattern 1: Full Orchestration**
Best for: Complete feature implementation

```bash
ai-orchestrate
# 1. Paste Claude's implementation plan
# 2. Let orchestrator parse and execute tasks
# 3. Review results and iterate
```

### **Pattern 2: Predefined Workflows**
Best for: Common development patterns

```bash
ai-chain-example            # Flask API workflow
ai-chain-custom             # Custom workflow creation
```

### **Pattern 3: Interactive Communication**
Best for: Iterative development with Claude feedback

```bash
ai-bridge
# 1. Copy Claude's response
# 2. Execute with local agent
# 3. Generate summary for Claude
# 4. Repeat cycle
```

### **Pattern 4: Complex Project Management**
Best for: Large projects with multiple dependencies

```bash
# Build task queue
ai-queue add "Setup project structure" --priority 10
ai-queue add "Implement core features" --depends-on 1 --priority 8
ai-queue add "Add tests" --depends-on 2 --priority 7
ai-queue add "Documentation" --depends-on 3 --priority 5

# Execute automatically
ai-queue-run
```

---

## 📋 Quick Reference

### **Aliases Available**

```bash
# Claude Code (Basic)
claude-full                 # Maximum permissions
claude-py                   # Python development
claude-safe                 # Planning mode only
claude-project             # Project with shared dirs

# AI Orchestration
ai-orchestrate              # Full workflow coordination
ai-chain                    # Agent chaining
ai-chain-example           # Example workflows
ai-chain-custom            # Custom workflows  
ai-bridge                  # Interactive bridge
ai-queue                   # Task queue management
ai-queue-show              # Show current queue
ai-queue-run               # Execute ready tasks
ai-queue-next              # Show next task
```

### **Common Workflows**

1. **Quick Implementation**:
   ```bash
   # Get plan from Claude → Execute with Aider
   ai-bridge
   ```

2. **Complete Feature Development**:
   ```bash
   # Full orchestration: Planning → Implementation → Testing
   ai-orchestrate
   ```

3. **Predefined Patterns**:
   ```bash
   # Use built-in workflows (Flask API, etc.)
   ai-chain-example
   ```

4. **Complex Project**:
   ```bash
   # Task queue with dependencies
   ai-queue add "task1" --priority 10
   ai-queue add "task2" --depends-on 1 --priority 8
   ai-queue-run
   ```

---

## 🔄 Best Practices

### **For Planning with Claude**
- Request structured, step-by-step implementation plans
- Include file structures and code snippets
- Specify testing and validation requirements
- Ask for clear task boundaries

### **For Execution**
- Start with high-priority, independent tasks
- Use dependencies for tasks that build on each other
- Test frequently with Open Interpreter
- Keep task descriptions focused and actionable

### **For Communication**
- Use ai-bridge for iterative feedback loops
- Generate summaries for Claude to maintain context
- Export session logs for review and debugging
- Keep Claude updated with progress and issues

---

## 🛠️ Configuration

### **Environment Requirements**
```bash
# Required conda environments
env_aider           # aider-chat package
env_openint         # open-interpreter package

# Ollama models
ollama pull codellama:13b   # Local LLM for agents
```

### **File Structure**
```
~/
├── ai_orchestrator.py      # Full workflow orchestration
├── chain_agents.sh         # Sequential agent chaining
├── claude_bridge.py        # Interactive bridge
├── task_queue.py          # Task queue management
├── scripts/               # Utility scripts
│   └── claude-permission-hook.sh
└── .claude/              # Claude Code settings
    ├── settings.json
    └── settings.local.json
```

### **Session Directories**
```
./ai_workspace/            # Orchestrator working directory
./claude_bridge/           # Bridge session data
./prompts/                # Chain agent prompts
./logs/                   # Execution logs
```

---

## 🚀 Example: Complete Web App Development

```bash
# 1. Plan with Claude (web interface)
# Ask: "Create a complete implementation plan for a Flask REST API with 
#       user authentication, CRUD operations, and deployment configuration"

# 2. Execute full workflow
ai-orchestrate
# Paste Claude's plan
# Let it execute: Aider implements → Open Interpreter tests

# 3. Alternative: Use task queue for complex dependencies
ai-queue add "Setup Flask project structure" --priority 10
ai-queue add "Implement user authentication" --depends-on 1 --priority 9
ai-queue add "Create CRUD operations" --depends-on 2 --priority 8
ai-queue add "Add comprehensive tests" --depends-on 3 --priority 7
ai-queue add "Create deployment config" --depends-on 4 --priority 6
ai-queue add "Run full test suite" --depends-on 5 --agent oi --priority 5

ai-queue-run  # Execute everything automatically

# 4. Review and iterate
ai-bridge     # Get feedback from Claude, make improvements
```

---

## ✨ Summary

**You now have a complete AI agent orchestration system that provides**:

✅ **Full workflow automation** (Claude planning → Local execution)  
✅ **Interactive communication bridges** (Clipboard/file integration)  
✅ **Sophisticated task management** (Dependencies, priorities, timing)  
✅ **Predefined workflows** (Common development patterns)  
✅ **Session logging and reporting** (Full audit trail)  
✅ **Multiple coordination patterns** (Choose what fits your workflow)

**The key insight**: While Claude can't directly control local agents, this orchestration system creates seamless workflows that feel like direct coordination, giving you the best of both worlds - Claude's intelligence with local execution power.

---

## 🚀 **Model Lineup Updates (August 2025)**

### **NEW Championship Models**

Your system now includes two powerful new models that significantly enhance capabilities:

| Model | Type | Size | Strength | Best For |
|-------|------|------|----------|----------|
| **qwen2.5:32b-instruct** | 📋 Instruct | 19GB | **98** 🏆 | Complex instructions, detailed analysis |
| **granite3.3:8b** | 📋 Instruct | 4.9GB | **87** ⚡ | Medium instructions, fast responses |

### **Updated Model Hierarchy (Top 10)**

1. **qwen2.5:32b-instruct** (98) - 🏆 **NEW CHAMPION** for complex instructions
2. **deepseek-coder:33b** (95) - 🥈 Coding powerhouse  
3. **mixtral:8x7b** (92) - 🥉 Analysis & reasoning
4. **codellama:34b** (90) - Large-scale coding
5. **qwen3:32b** (90) - General reasoning
6. **yi:34b** (88) - Creative solutions
7. **qwen3:30b** (88) - General analysis  
8. **granite3.3:8b** (87) - 🆕 **NEW** fast instructions
9. **devstral:24b** (88) - Development strategies
10. **deepseek-coder:6.7b** (85) - Quick coding

### **New Smart Commands**

```bash
# NEW: Most powerful instruction model (strength 98!)
aider-instruct          # qwen2.5:32b-instruct for complex tasks
llm-instruct           # Direct access to qwen2.5:32b-instruct

# NEW: Fast instruction model  
aider-granite          # granite3.3:8b for medium complexity
llm-granite           # Direct access to granite3.3:8b
```

### **Optimized Usage Patterns**

| Scenario | Command | Model | Why |
|----------|---------|-------|-----|
| **Complex crypto analysis** | `aider-instruct` | qwen2.5:32b-instruct | Highest instruction-following (98) |
| **Heavy coding** | `aider-heavy` | deepseek-coder:33b | Best coding specialist (95) |
| **Fast instructions** | `aider-granite` | granite3.3:8b | Quick instruction following (87) |
| **General coding** | `aider-fast` | deepseek-coder:6.7b | Balanced coding (85) |
| **Complex reasoning** | `llm-smart` | mixtral:8x7b | Best analysis (92) |

**Your system upgrade delivered a 3-point strength increase at the top tier! 🚀**