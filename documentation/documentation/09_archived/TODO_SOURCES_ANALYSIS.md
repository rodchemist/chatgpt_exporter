# Rod-Corp Todo Sources Analysis Report

## Executive Summary

This comprehensive analysis investigates the todo/task sources across the Rod-Corp multi-agent system, documenting storage patterns, file formats, and potential for automated RAG processing. The analysis reveals a rich ecosystem of agent task histories stored across multiple specialized directories.

## Directory Inventory and Status

### 1. /home/rod/.claude - Claude Agent Tasks and History
**Status**: ✅ Active with extensive todo tracking
- **File Count**: 1,831+ todo JSON files
- **Size**: ~49KB directory structure
- **Last Modified**: September 24, 2025 (active)
- **Subdirectories**:
  - `/todos/` - Main todo storage
  - `/projects/` - 27 project directories
  - `/commands/`, `/ide/`, `/shell-snapshots/`, `/statsig/`

### 2. /home/rod/.qwen - Qwen Agent Tasks and History
**Status**: ✅ Active with structured todo tracking
- **File Count**: 51 todo JSON files
- **Size**: ~48KB directory structure
- **Last Modified**: September 24, 2025 (active)
- **Key Files**:
  - `/todos/` - Session-based todo tracking
  - `QWEN.md` - Documentation
  - `settings.json`, `oauth_creds.json`
  - `/tmp/` - 64 temporary session directories

### 3. /home/rod/.codex - Codex Agent Tasks and History
**Status**: ✅ Active with comprehensive session logging
- **File Count**: 100+ JSONL session files
- **Size**: ~564KB total history
- **Last Modified**: September 23, 2025 (active)
- **Key Features**:
  - `history.jsonl` - 535KB comprehensive history
  - Session-organized directory structure by date
  - `/sessions/2025/` with monthly/daily subdivisions

### 4. /home/rod/.gemini - Gemini Agent Tasks and History
**Status**: ✅ Active but lightweight tracking
- **File Count**: ~7 configuration files
- **Size**: ~32KB directory
- **Last Modified**: September 24, 2025 (active)
- **Key Files**:
  - `GEMINI.md` - Documentation
  - `oauth_creds.json`, `settings.json`
  - `/tmp/` - 44 temporary session directories

### 5. /home/rod/.grok - Grok Agent Configuration
**Status**: ⚠️ Limited activity
- **File Count**: 1 settings file
- **Size**: ~12KB directory
- **Last Modified**: September 1, 2025
- **Contents**: Basic user settings only

### 6. /home/rod/.ollama - Ollama Model Tasks and History
**Status**: ✅ Active with model management
- **File Count**: ~6 files
- **Size**: ~24KB directory
- **Last Modified**: August 13, 2025
- **Key Files**:
  - `history` - Command history
  - SSH keys for model authentication
  - `/models/` - Model storage directory

### 7. /home/rod/.local - Local Agent Configurations
**Status**: ✅ Active with utility scripts
- **File Count**: ~10 executable scripts
- **Size**: ~24KB directory
- **Last Modified**: September 23, 2025
- **Key Scripts**:
  - `ai-context-status`, `ai-env-manager`
  - `check-ai-dependencies`, `backup-bashrc`
  - Symlinks to dashboard services

## File Type Analysis

### Claude Todo Format (.claude/todos/*.json)
```json
[
  {
    "content": "Create folder structure for three agents",
    "status": "completed|in_progress|pending",
    "activeForm": "Creating folder structure for three agents"
  }
]
```
**Characteristics**:
- Array-based structure
- Simple status tracking (3 states)
- Action-oriented content descriptions
- Present participle "activeForm" for execution context

### Qwen Todo Format (.qwen/todos/*.json)
```json
{
  "todos": [
    {
      "content": "Launch agent to create detailed PRODUCTION migration plan",
      "id": "1",
      "status": "completed|pending"
    }
  ],
  "sessionId": "uuid-formatted-session-id"
}
```
**Characteristics**:
- Object wrapper with session tracking
- Numeric ID system for todo items
- Session-based organization
- Simplified status model (2 states)

### Codex Session Format (.codex/sessions/**/*.jsonl)
```jsonl
{"timestamp": "2025-09-23T...", "role": "user", "content": "..."}
{"timestamp": "2025-09-23T...", "role": "assistant", "content": "..."}
```
**Characteristics**:
- JSONL format for streaming append operations
- Conversational history model
- Timestamped entries
- Role-based message tracking
- Organized by date hierarchy

## Todo/Task Extraction Possibilities

### High-Value Data Sources

1. **Claude Todos** - Most comprehensive
   - 1,831+ structured task records
   - Rich status progression tracking
   - Action-oriented task descriptions
   - Real-time active form tracking

2. **Qwen Todos** - Session-organized
   - 51 session-based todo collections
   - Migration and system planning focus
   - UUID-based session correlation

3. **Codex History** - Conversational context
   - 15+ MB of conversation data
   - Natural language task discussions
   - Temporal progression tracking
   - Multi-session correlation

### Extraction Strategies

#### 1. Structured Todo Extraction
- **Source**: `.claude/todos/*.json`, `.qwen/todos/*.json`
- **Method**: Direct JSON parsing
- **Output**: Task records with status, timestamps, categories
- **Update Frequency**: Real-time (file system watching)

#### 2. Conversational Task Mining
- **Source**: `.codex/sessions/**/*.jsonl`
- **Method**: NLP extraction from conversation logs
- **Output**: Inferred tasks, project context, decision rationale
- **Update Frequency**: Batch processing (daily/hourly)

#### 3. Session Correlation
- **Source**: Cross-directory session IDs and timestamps
- **Method**: UUID matching and temporal alignment
- **Output**: Multi-agent task correlation and handoffs
- **Update Frequency**: On-demand correlation analysis

## Recommended RAG Agent Implementations

### 1. Claude Todo Monitor Agent
```python
# Pseudo-implementation structure
class ClaudeTodoRAG:
    def __init__(self):
        self.watch_path = "/home/rod/.claude/todos/"
        self.vector_store = ChromaDB("claude_todos")

    def process_new_todos(self, file_path):
        todos = json.load(file_path)
        embeddings = self.embed_todos(todos)
        self.vector_store.upsert(embeddings)

    def query_similar_tasks(self, query):
        return self.vector_store.similarity_search(query, k=10)
```

**Features**:
- Real-time file system monitoring
- Vector embedding of task descriptions
- Status progression analysis
- Semantic similarity search

### 2. Multi-Agent Session Correlator
```python
class SessionCorrelatorRAG:
    def __init__(self):
        self.agents = ["claude", "qwen", "codex", "gemini"]
        self.session_store = Neo4jDB("agent_sessions")

    def correlate_sessions(self, timestamp_window="1h"):
        # Cross-reference session activities
        # Build relationship graph
        # Extract collaborative patterns
        pass
```

**Features**:
- Cross-agent session correlation
- Temporal pattern recognition
- Collaborative task identification
- Handoff detection and analysis

### 3. Conversational Task Extractor
```python
class ConversationalRAG:
    def __init__(self):
        self.codex_sessions = "/home/rod/.codex/sessions/"
        self.nlp_pipeline = spacy.load("en_core_web_lg")

    def extract_implicit_todos(self, jsonl_file):
        # Parse conversation for task mentions
        # Extract action items and decisions
        # Correlate with explicit todos
        pass
```

**Features**:
- NLP-based task extraction
- Intent recognition from conversations
- Decision point identification
- Context-aware task categorization

## Integration Strategies with Todo Inspector

### 1. Real-Time Update Integration
```bash
# File system watcher integration
inotifywait -m -e create,modify,move $TODO_DIRS | while read event; do
    echo "$event" | todo_inspector.py --process-event
done
```

### 2. Data Pipeline Architecture
```
[File System] → [RAG Processors] → [Vector Stores] → [Todo Inspector Query Interface]
     ↓                ↓                   ↓                        ↓
[Real-time]    [Batch Process]    [Indexed Search]         [User Queries]
[Monitoring]   [NLP Analysis]     [Similarity Match]       [Task Insights]
```

### 3. Enhanced Todo Inspector Features
- **Semantic Search**: "Show me all database migration tasks"
- **Pattern Recognition**: "What tasks typically follow deployment?"
- **Cross-Agent Insights**: "Which agent handles security reviews?"
- **Progress Tracking**: "Show incomplete tasks from last week"

## Implementation Priority Matrix

| Priority | Component | Effort | Impact | Timeline |
|----------|-----------|--------|---------|----------|
| P1 | Claude Todo Monitor | Low | High | 1-2 days |
| P2 | Qwen Session Tracker | Low | Medium | 1 day |
| P3 | File System Watcher | Medium | High | 2-3 days |
| P4 | Basic RAG Integration | Medium | High | 3-5 days |
| P5 | Conversational Extractor | High | Medium | 1-2 weeks |
| P6 | Session Correlator | High | High | 2-3 weeks |

## Technical Specifications

### File System Monitoring
```bash
# Dependencies
- inotify-tools (Linux file system monitoring)
- watchdog (Python cross-platform alternative)
- systemd (service management)

# Directory Watch Targets
/home/rod/.claude/todos/
/home/rod/.qwen/todos/
/home/rod/.codex/sessions/
/home/rod/.gemini/tmp/
```

### Vector Database Requirements
```python
# Recommended: ChromaDB for embeddings
# Alternative: Weaviate, Pinecone, or PostgreSQL with pgvector
# Local storage: ~/.rod_corp_vector_store/

# Embedding Models
- sentence-transformers/all-MiniLM-L6-v2 (lightweight)
- OpenAI text-embedding-ada-002 (cloud)
- sentence-transformers/all-mpnet-base-v2 (high quality)
```

### API Integration Points
```python
# Todo Inspector Query Interface
GET /api/todos/search?q={query}&agent={agent}&status={status}
GET /api/todos/similar?task_id={id}&limit={n}
GET /api/todos/patterns?timeframe={range}
GET /api/sessions/correlate?agents={list}&window={time}
```

## Testing and Validation Strategy

### 1. Data Integrity Testing
- Verify JSON parsing accuracy across all todo formats
- Test file system monitoring reliability
- Validate embedding quality and retrieval relevance

### 2. Performance Testing
- Load testing with 1000+ concurrent todo updates
- Query response time benchmarks
- Memory usage profiling for large vector stores

### 3. Integration Testing
- End-to-end todo creation → RAG processing → query retrieval
- Cross-agent session correlation accuracy
- Real-time update propagation delays

## Security and Privacy Considerations

### Data Protection
- Todo content may contain sensitive project information
- Implement access controls aligned with existing Rod-Corp security
- Consider encryption for vector stores containing private data

### Authentication Integration
- Leverage existing `.claude`, `.qwen` authentication mechanisms
- Maintain agent-specific permission boundaries
- Implement audit logging for RAG access patterns

## Conclusion and Next Steps

The Rod-Corp system contains a wealth of structured and unstructured task data across multiple agents. The analysis reveals:

### Key Findings:
1. **1,882+ structured todo records** across Claude and Qwen agents
2. **15+ MB of conversational history** in Codex sessions
3. **Real-time update capabilities** through file system monitoring
4. **Rich cross-agent correlation potential** via session IDs and timestamps

### Immediate Actions:
1. Implement Claude Todo Monitor RAG agent (P1)
2. Set up file system watching infrastructure
3. Create basic vector storage and search capabilities
4. Integrate with existing todo_inspector.py

### Long-term Vision:
- Unified multi-agent task intelligence
- Predictive task recommendations
- Automated project context correlation
- Cross-agent workload balancing insights

The foundation exists for a sophisticated RAG-powered task intelligence system that can provide real-time insights across the entire Rod-Corp multi-agent ecosystem.