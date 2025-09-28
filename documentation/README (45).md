# AI Agent Orchestration System

**Coordinating Claude, Aider, Open Interpreter & 20+ Local Models**

## 🚀 Quick Start

```bash
cd ~/rod-corp/ai-orchestration
./setup.sh                    # Setup all environments and dependencies
./test.sh                     # Test all components
```

## 📁 Repository Structure

```
ai-orchestration/
├── scripts/                  # Core orchestration scripts
│   ├── ai_orchestrator.py    # Full workflow coordination
│   ├── chain_agents.sh       # Sequential agent chaining
│   ├── claude_bridge.py      # Interactive Claude ↔ Local bridge
│   ├── task_queue.py         # Task management with dependencies
│   └── model_selector.py     # Intelligent model selection
├── configs/                  # Configuration files
│   ├── models.json           # Model configurations
│   ├── environments.json     # Environment settings
│   └── aliases.sh           # Shell aliases
├── docs/                     # Documentation
│   ├── USAGE_GUIDE.md       # How to use the system
│   ├── MODEL_GUIDE.md       # Model selection guide
│   └── WORKFLOWS.md         # Example workflows
├── tests/                    # Test scripts
│   ├── test_environments.py # Test all environments
│   ├── test_models.py       # Test model availability
│   └── test_integration.py  # Integration tests
├── examples/                 # Example workflows
│   ├── flask_api.md         # Flask API development
│   ├── data_analysis.md     # Data analysis workflow
│   └── web_scraping.md      # Web scraping project
├── logs/                     # Session logs and outputs
└── setup.sh                 # One-command setup script
```

## 🤖 Available Models (20 Total)

### 🥇 Heavy Performers
- **deepseek-coder:33b** (18GB) - Primary coding model
- **mixtral:8x7b** (26GB) - System architecture & analysis
- **qwen3:32b** (20GB) - General reasoning
- **codellama:34b** (19GB) - Code completion

### ⚡ Fast Responders  
- **deepseek-coder:6.7b** (3.8GB) - Quick coding
- **mistral:latest** (4.4GB) - Rapid responses
- **qwen2.5-coder:latest** (4.7GB) - Code review

### 🎯 Specialists
- **devstral:24b** (14GB) - Development strategies
- **neural-chat:latest** (4.1GB) - Natural conversation
- **tinyllama:latest** (637MB) - Ultra-fast testing

## 🔧 Core Components

### 1. **AI Orchestrator** (`ai_orchestrator.py`)
Full workflow coordination from Claude planning to local execution.

### 2. **Agent Chaining** (`chain_agents.sh`) 
Predefined workflows with sequential agent execution.

### 3. **Claude Bridge** (`claude_bridge.py`)
Interactive communication bridge between Claude (web) and local agents.

### 4. **Task Queue** (`task_queue.py`)
Sophisticated task management with dependencies and priorities.

### 5. **Model Selector** (`model_selector.py`)
Intelligent model selection based on task complexity and requirements.

## 🎭 Environments

- **env_aider** - Aider code implementation
- **env_openint** - Open Interpreter testing & execution  
- **env_ollama** - Ollama model management (GPU-enabled)

## 🚀 Usage Examples

### Quick Team Consultation
```bash
ai-team "design a microservices architecture"
```

### Full Workflow Orchestration
```bash
ai-orchestrate
# 1. Paste Claude's implementation plan
# 2. Watch automatic model selection and execution
```

### Task Queue Management
```bash
ai-queue add "Design API" --agent ollama --priority 10
ai-queue add "Implement endpoints" --agent aider --depends-on 1
ai-queue-run    # Execute with optimal models
```

### Interactive Development
```bash
ai-bridge
# 1. Copy Claude's response
# 2. Execute with local agents
# 3. Generate summary for Claude feedback
```

## 📊 Performance Optimization

- **Smart model selection** based on task complexity
- **GPU acceleration** via env_ollama environment
- **Resource management** for optimal performance
- **Automatic fallbacks** for failed operations

## 🛠️ Installation

1. **Clone and setup**:
   ```bash
   cd ~/rod-corp/ai-orchestration
   ./setup.sh
   ```

2. **Verify installation**:
   ```bash
   ./test.sh
   ```

3. **Start using**:
   ```bash
   ai-team "test the system setup"
   ```

## 📝 License

MIT License - Feel free to modify and distribute.

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Add tests for new functionality
4. Submit pull request

---

**Built for maximum AI productivity with intelligent orchestration! 🎭🚀**