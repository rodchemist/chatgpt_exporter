# 🚀 Rod-Corp Full Stack RAG Agent System

**Next-Generation Retrieval-Augmented Generation with GPU Acceleration**

Your complete ChatGPT conversation history searchable with sub-millisecond response times using RTX 4090 FAISS-GPU acceleration.

## 📊 System Overview

- **5,657 conversations** • **110,448 messages** • **549 INCIVA mentions**
- **301.6M characters** of conversation data ready for semantic search
- **GPU-accelerated** vector search with FAISS
- **Visual chat interface** for natural interaction
- **Legacy port management** integration

## 🚀 Quick Start

### 1. Initial Setup
```bash
# Run environment setup (one-time)
./setup_environment.sh

# This will:
# - Install system dependencies
# - Configure Python environment
# - Create directory structure
# - Generate configuration files
# - Test ChatGPT data access
```

### 2. Start Full Stack
```bash
# Start all Rod-Corp services
./start_rod_corp_full_stack.sh

# This will:
# - Check prerequisites
# - Assign ports (avoiding conflicts with legacy)
# - Start RAG chat server
# - Initialize GPU vector system
# - Start monitoring
# - Integrate with legacy services
```

### 3. Access Your RAG Agent
```bash
# Open in browser
http://localhost:5000

# Or check assigned port in output
```

## 🎯 Features

### 🤖 Visual Chat Interface
- **Modern UI** with chat bubbles and animations
- **Quick actions** for common queries (INCIVA, Python, Database)
- **Real-time search** through your conversation history
- **Contextual responses** with relevance scoring

### ⚡ GPU Acceleration
- **FAISS-GPU** for sub-millisecond vector search
- **RTX 4090 optimization** with memory management
- **Sentence transformers** for semantic embeddings
- **Batch processing** for efficient GPU utilization

### 🔗 Legacy Integration
- **Port management** system prevents conflicts
- **Service coordination** with existing Rod-Corp services
- **Legacy documentation** agent integration
- **Shared monitoring** and logging

### 🏛️ INCIVA Specialization
- **549 INCIVA mentions** across conversations
- **Environmental education** project knowledge
- **Database design** discussions
- **Contract justifications** and technical details

## 📁 File Structure

```
rod-corp-2/
├── start_rod_corp_full_stack.sh    # Main startup script
├── setup_environment.sh            # Environment setup
├── rag_chat_server.py              # Flask chat server
├── simple_rag_agent.py             # RAG agent logic
├── gpu_conversation_loader.py      # GPU vector loader
├── conversation_searcher.py        # Conversation search
├── templates/
│   └── chat.html                   # Web interface
├── logs/                           # Service logs
├── config/                         # Configuration files
├── gpu_conversation_vectors/       # Vector database
└── legacy/                         # Legacy services
```

## 🔧 Helper Commands

```bash
# Check system status
./check_status.sh

# Stop all services
./stop_all.sh

# View logs
tail -f logs/rag_chat.log
tail -f logs/gpu_processing.log

# Monitor system resources
cat /tmp/rod_corp_stats.json | jq
```

## 📊 Service Ports

| Service | Default Port | Description |
|---------|-------------|-------------|
| RAG Chat | 5000 | Main chat interface |
| Vector Search | 5001 | GPU vector operations |
| GPU Engine | 5002 | GPU processing engine |
| Agent Orchestrator | 8000 | Legacy coordination |
| Security Manager | 8001 | Authentication |
| Knowledge Manager | 8002 | Knowledge base |

*Ports are automatically assigned to avoid conflicts with existing services*

## 💬 Usage Examples

### INCIVA Queries
```
"What INCIVA projects did I discuss?"
"Show me INCIVA environmental education details"
"Find INCIVA database design conversations"
```

### Technical Searches
```
"Python programming discussions"
"Database design patterns"
"Project management strategies"
"Show my conversation statistics"
```

### General Knowledge
```
"help" - Show available commands
"stats" - Display conversation statistics
Any natural language question about your conversations
```

## 🔍 Troubleshooting

### Chat Server Won't Start
```bash
# Check logs
tail -f logs/rag_chat.log

# Verify Python dependencies
python3 -m pip install --user flask sentence-transformers

# Check port availability
ss -tulpn | grep :5000
```

### GPU Issues
```bash
# Check GPU status
nvidia-smi

# Verify CUDA installation
python3 -c "import torch; print(torch.cuda.is_available())"

# Fallback to CPU
export CUDA_VISIBLE_DEVICES=""
```

### No Conversation Data
```bash
# Check data path
ls -la /mnt/d/DownloadChrome/ChatGPT-history/

# Process conversations
python3 load_chatgpt_to_gpu.py

# Update path in .env if needed
```

### Port Conflicts
```bash
# View port usage
./check_status.sh

# Stop conflicting services
./stop_all.sh

# Legacy port registry
sqlite3 legacy/.rod_corp_port_registry.db ".tables"
```

## 🚀 Architecture

### Data Flow
1. **ChatGPT Export** → JSON files in `/mnt/d/DownloadChrome/ChatGPT-history/`
2. **Processing** → `load_chatgpt_to_gpu.py` extracts and structures data
3. **Embeddings** → Sentence transformers generate semantic vectors
4. **GPU Index** → FAISS-GPU builds searchable index
5. **Chat Interface** → Users interact via web UI
6. **RAG Agent** → Searches knowledge base and provides responses

### Performance
- **Sub-millisecond** search through 110K+ messages
- **GPU acceleration** with RTX 4090
- **Batch processing** for optimal throughput
- **Memory management** for large datasets

### Integration
- **Legacy services** coordination via port management
- **Monitoring** integration with existing systems
- **Log aggregation** in unified location
- **Configuration** management for all services

## 🔒 Security

- **No external dependencies** for core functionality
- **Local processing** keeps data private
- **Port isolation** prevents service conflicts
- **Legacy authentication** integration available

## 📈 Monitoring

System monitoring provides:
- **Real-time metrics** in `/tmp/rod_corp_stats.json`
- **Service health** checks and auto-restart
- **Resource usage** tracking (CPU, memory, GPU)
- **Log aggregation** in `logs/` directory

## 🎯 Next Steps

1. **Scale Up**: Add more conversation sources (Slack, Teams, etc.)
2. **Enhance UI**: Add conversation visualization and analytics
3. **API Integration**: Connect with external services
4. **Advanced RAG**: Implement conversation summarization and insights
5. **Multi-model**: Support for different embedding models

---

## 🏛️ INCIVA Knowledge Base

Your RAG agent has specialized knowledge of:

- **Environmental Education Systems** - Database design and implementation
- **Project Management** - Contract justifications and workflows
- **Technical Architecture** - MySQL schemas and optimization
- **Data Analysis** - 37 municipalities, 5,295+ activities
- **Geographic Coverage** - Valle del Cauca zones and municipalities

*Ready to answer detailed questions about your INCIVA environmental education project!*

---

**🚀 Rod-Corp Full Stack RAG Agent - Powered by GPU acceleration and your complete conversation history**