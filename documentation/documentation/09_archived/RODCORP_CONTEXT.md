# Rod-Corp System Context

## System Overview
Rod-Corp is a comprehensive AI orchestration and service management platform that provides intelligent service discovery, agent coordination, automated system integration, advanced analytics, and real-time documentation management.

## Core Architecture

### Directory Structure
- `/rod-corp/configs/` - System configuration files
  - `rod-corp-auto-init.sh` - Main initialization script
  - `ai-enhanced-aliases.sh` - AI agent command aliases (includes leader agents)
  - `efficient_ollama_models.sh` - Ollama model configurations
  - `agents/` - Agent-specific configurations
  - `services/` - Service configurations

- `/rod-corp/services/` - Service implementations (23 services - 83% operational)
  - `ai-orchestration/` - AI orchestration service with setup scripts
  - `ai-interaction-server/` - Main AI agent interaction server (5+ instances active)
  - `delegation_system/` - 4-level hierarchical task delegation (Port 15000)
  - `librosynth/` - Audio transcription and book processing service
  - `advanced-rag-system/` - RAG (Retrieval-Augmented Generation) system
  - `claude-data-agent/` - Claude data processing agent
  - `unified-dashboard/` - Unified system dashboard
  - `api_gateway/` - Central service gateway (Port 8000)
  - And 15+ other specialized services

- `/rod-corp/intelligence/` - Advanced Analytics System
  - `intelligence_coordinator.py` - Main intelligence system
  - `pattern_recognition/` - Pattern analysis across services
  - `predictive_maintenance/` - System optimization recommendations
  - `performance_analytics/` - Performance monitoring and analysis
  - `decision_support/` - Automated decision-making capabilities

- `/rod-corp/agents/` - Agent Management System
  - `leader_agents.py` - Leader agent coordination system
  - `todo_inspector.py` - 15-minute todo monitoring system
  - `specialized_rag_agents.py` - Real-time RAG agents
  - `TODO_SOURCES_ANALYSIS.md` - Comprehensive todo sources analysis

- `/rod-corp/rod-documentation/` - Automated Documentation System
  - `rag_documentation_agent.py` - File change monitoring and documentation
  - `start.sh` - Documentation agent startup script

- `/rod-corp/innovation/` - New Project Development Area
  - All new projects must be developed here for system stability

## Dynamic Port Discovery System

### Port Registry
The system uses a dynamic port registry managed by:
- **Primary**: MSSQL Server (10.0.0.2:1433) - AgentDirectory database
- **Fallback**: SQLite local registry (~/.rod_corp_port_registry.db)

### Port Ranges
- AI Agents: 49152-49200
- API Services: 17000-18999
- Web Services: 3000-9999
- Databases: 1433-5432

### Service Discovery
The `agent_port_manager.py` provides:
- Real-time service discovery
- Dynamic port mapping
- Best server selection
- Context generation for AI agents

## Agent Systems

### Primary Agents (All Operational - 100% Context Sync)
- **claude-full**: Comprehensive analysis and code generation ✅
- **qwen-full**: Specialized in documentation and research ✅
- **gemini-full**: Multi-modal analysis and processing ✅
- **codex-full**: Code analysis and programming tasks ✅

### Leader Agents (Fully Implemented)
- **claude-lead**: Project leadership and coordination ✅
- **qwen-lead**: Documentation and knowledge management ✅
- **codex-lead**: Technical architecture and code review ✅
- **gemini-lead**: Multi-modal project oversight ✅

**Leader Agent Features:**
- Document project states in MSSQL database
- Replace other leaders when tokens/services are down
- Maintain centralized todo lists in database
- Cross-agent coordination and handoff capabilities
- Real-time monitoring and health checks

### Specialized Systems

#### Todo Management System
- **15-Minute Inspector Agent**: Automated todo monitoring every 15 minutes
- **Multi-Source Integration**: Monitors ~/.claude, ~/.qwen, ~/.codex, ~/.gemini, ~/.grok, ~/.ollama
- **Centralized Database**: SQLite + MSSQL integration for todo tracking
- **Real-time Processing**: File system watching with immediate updates

#### RAG Documentation System
- **File Change Monitoring**: Automated documentation via git hooks
- **Real-time Updates**: File system watching for immediate documentation
- **Service Inventory Management**: Dynamic service status tracking
- **Context Generation**: Automatic system context updates

#### Specialized RAG Agents
- **Claude Todo Monitor**: Real-time JSON todo processing
- **Qwen Session Tracker**: Session-based todo correlation
- **File System Watcher**: Generic todo extraction across all agent directories
- **Real-time Vector Storage**: Immediate semantic search capabilities

## Integration Points

### Enhanced Initialization
Location: `/home/rod/rod-corp/ROD_CORP_AUTO_INIT_ENHANCED.sh`

Features:
- Dynamic port discovery
- Real-time service mapping
- Automatic context generation
- Database connectivity testing
- Best AI server selection
- Intelligence system integration
- Leader agent coordination

### Environment Variables
- `RODCORP_CONTEXT` - Path to generated context file
- `ROD_CORP_PROJECT_ROOT` - Project root directory (/home/rod/rod-corp)
- `ROD_CORP_AI_SERVER` - Best available AI server URL
- `ROD_CORP_DATABASE_STATUS` - Database connectivity status
- `ROD_CORP_INTEGRATION` - Integration level (enhanced)
- `ROD_CORP_VERSION` - System version (2.1-dynamic)

## AI Agent Integration

### Supported Agents
- claude-full
- qwen-full, qwen-local
- codex-full
- gemini-full
- deepseek-full
- mixtral-full
- codellama-full

All agents source the enhanced initialization script for:
- Service discovery
- Port mapping
- Context awareness
- Database access

## Database System

### MSSQL Server
- Host: 10.0.0.2:1433
- Database: AgentDirectory
- Tables:
  - GlobalAgentRegistry (61+ agents)
  - AgentDiscussions (6380+ messages)
  - PortRegistry (dynamic port mappings)

### Fallback System
- SQLite database for local operations
- Automatic failover when MSSQL unavailable
- Synchronized with primary when possible

## Key Services

### AI Interaction Server
Multiple instances running on dynamic ports:
- Primary: 8080
- Additional: 49152, 49153, 49200, 49555
- Auto-discovery and load balancing

### Librosynth
Audio transcription and book processing:
- Audiobookshelf integration
- Real-time transcription
- Evolutionary cycle management
- Production deployment ready

### Advanced RAG System
- Document processing
- Knowledge integration
- Context-aware retrieval
- N8N workflow automation

## Advanced Systems Usage

### Intelligence System
```bash
# Run system analysis
cd ~/rod-corp/intelligence
python3 intelligence_coordinator.py

# Get system insights
python3 -c "from intelligence_coordinator import IntelligenceCoordinator;
             coord = IntelligenceCoordinator();
             print(coord.analyze_system())"
```

### Leader Agents
```bash
# Use leader agents (with fallback to primary agents)
claude-lead "Analyze project status"
qwen-lead "Research documentation needs"
codex-lead "Review architecture"
gemini-lead "Assess user experience"
```

### Todo Inspector System
```bash
# Run single inspection
cd ~/rod-corp/agents
./start_todo_inspector.sh

# Start continuous monitoring (daemon mode)
./start_todo_inspector.sh --daemon
```

### Specialized RAG Agents
```bash
# Start real-time RAG monitoring
cd ~/rod-corp/agents
python3 specialized_rag_agents.py

# Monitor specific agent todos in real-time
# (Automatically monitors ~/.claude, ~/.qwen, ~/.codex, ~/.gemini, etc.)
```

### Documentation System
```bash
# Start RAG documentation agent
cd ~/rod-corp/rod-documentation
./start.sh

# Manual documentation update
python3 rag_documentation_agent.py
```

### Git Integration
```bash
# Git hooks automatically trigger documentation updates
git commit -m "Your changes"  # Triggers pre-commit hook

# Manual context update
git add . && git commit -m "Update with auto-documentation"
```

### For AI Agents
Include this context by sourcing:
```bash
source /home/rod/rod-corp/ROD_CORP_AUTO_INIT_ENHANCED.sh
```

This provides:
- `$RODCORP_CONTEXT` - Path to this context file
- Service discovery functions
- Database connectivity
- Dynamic port mapping
- Intelligence system access
- Leader agent coordination

### For Manual Operations
```bash
# Discover services
cd ~/rod-corp/services/ai-interaction-server
python3 agent_port_manager.py --discover

# Find best server
python3 agent_port_manager.py --find-server

# Generate context
python3 agent_port_manager.py --context

# Start all systems
cd ~/rod-corp && ./start.sh
```

## System Status
- **Integration**: ✅ Complete (Enhanced mode)
- **Database**: ✅ Online (MSSQL + SQLite fallback)
- **Port Discovery**: ✅ Active (5+ AI servers detected)
- **Services**: ✅ 83% operational (19/23 services)
- **Agents**: ✅ 100% functional (4 primary + 4 leader agents)
- **Intelligence**: ✅ Active (Analytics, patterns, predictions)
- **Documentation**: ✅ Automated (RAG + git integration)
- **Todo System**: ✅ Real-time monitoring (15-minute cycles)
- **RAG Agents**: ✅ Specialized monitoring (Claude, Qwen, Generic)

## Advanced Features
- **Leader Agent Handoffs**: Automatic token/service failure recovery
- **Real-time Documentation**: Git hooks + file system monitoring
- **Intelligence Analytics**: Pattern recognition, predictive maintenance
- **Multi-Source Todo Integration**: 7+ agent directories monitored
- **Semantic Search**: Vector storage for todo correlation
- **Decision Support**: Automated recommendations and insights

## Version
- **System**: Rod-Corp 2.1-dynamic
- **Features**: Complete advanced implementation
- **Context**: Real-time generated with full system awareness
- **Last Update**: Auto-updated via RAG documentation system
- **Git Integration**: ✅ Operational with hooks
- **Validation**: ✅ All systems tested and verified