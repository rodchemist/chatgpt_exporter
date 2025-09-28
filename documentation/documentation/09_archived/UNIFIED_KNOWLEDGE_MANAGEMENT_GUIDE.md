# Unified Knowledge Management System

## Overview

The Unified Knowledge Management System transforms the existing static RAG system into a dynamic, agent-integrated knowledge ecosystem. This comprehensive solution provides real-time knowledge synchronization, advanced agent memory systems, cross-agent collaboration protocols, and performance optimization.

## Architecture

### Core Components

1. **Unified Knowledge Manager** (`unified_knowledge_manager.py`)
   - Central knowledge repository with vector search
   - Agent registration and permission management
   - Knowledge versioning and change tracking
   - Security-tiered access control

2. **Agent Knowledge Bridge** (`agent_knowledge_bridge.py`)
   - Seamless integration with existing RAG system
   - Legacy knowledge migration tools
   - Hybrid query interface
   - Automatic knowledge extraction

3. **Real-Time Synchronization Framework** (`realtime_sync_framework.py`)
   - Event-driven knowledge updates
   - Conflict detection and resolution
   - Multi-transport communication (WebSocket, Redis, ZMQ)
   - Distributed coordination

4. **Advanced Agent Memory** (`advanced_agent_memory.py`)
   - Episodic, semantic, and working memory systems
   - Memory consolidation and decay mechanisms
   - Vector-based similarity search
   - Emotional valence tracking

5. **Cross-Agent Protocols** (`cross_agent_protocols.py`)
   - Knowledge sharing protocols with trust management
   - Collaborative session orchestration
   - Consensus building mechanisms
   - Expertise matching and discovery

6. **Performance Optimizer** (`performance_optimizer.py`)
   - Query optimization and caching
   - Resource monitoring and alerting
   - Database index optimization
   - Connection pooling

7. **Knowledge Orchestrator** (`knowledge_orchestrator.py`)
   - Main system coordinator
   - Component integration
   - Agent lifecycle management
   - System health monitoring

## Quick Start

### Installation

```bash
# Install core dependencies
pip install sentence-transformers faiss-cpu chromadb numpy pandas
pip install fastapi uvicorn websockets redis
pip install asyncio sqlite3 pathlib psutil

# Optional for enhanced features
pip install pyarrow transformers torch
```

### Basic Setup

1. **Initialize the system:**

```python
from knowledge_orchestrator import KnowledgeOrchestrator

# Create orchestrator with default config
orchestrator = KnowledgeOrchestrator()

# Initialize all components
await orchestrator.initialize()

# Start the system
await orchestrator.start()
```

2. **Register agents:**

```python
# Register an agent
await orchestrator.register_agent('my_agent', {
    'type': 'language_model',
    'capabilities': ['reasoning', 'text_generation'],
    'security_clearance': 'internal'
})
```

3. **Store and query knowledge:**

```python
from unified_knowledge_manager import KnowledgeItem, MemoryType

# Store knowledge
knowledge = KnowledgeItem(
    id="knowledge_1",
    content="Vector databases enable semantic search through embeddings",
    source="agent_conversation",
    collection="technical_knowledge",
    metadata={'domain': 'machine_learning', 'importance': 'high'}
)

await orchestrator.unified_km.store_knowledge(knowledge, 'my_agent')

# Query knowledge
results = orchestrator.unified_km.query_knowledge(
    "semantic search",
    'my_agent',
    top_k=5
)
```

## Configuration

### System Configuration

Create a `config.json` file:

```json
{
    "node_id": "knowledge_node_1",
    "data_directory": "data",
    "api_enabled": true,
    "api_port": 8001,
    "embedding_model": "all-MiniLM-L6-v2",
    "rag_integration": {
        "enabled": true,
        "legacy_path": "output/knowledge"
    },
    "security": {
        "default_tier": "public",
        "encryption_enabled": false
    },
    "performance": {
        "connection_pool_size": 10,
        "cache_size_mb": 100,
        "monitoring_interval": 30
    }
}
```

### Security Tiers

- **public**: Accessible to all agents
- **internal**: Team members only
- **confidential**: Trusted agents only
- **restricted**: Special permission required

## Agent Integration

### Memory Systems

Each agent gets sophisticated memory capabilities:

```python
# Store episodic memory
await agent_memory.store_memory(
    "I successfully completed the document analysis task",
    MemoryType.EPISODIC,
    context_tags=['task_completion', 'document_analysis'],
    emotional_valence=0.8  # Positive experience
)

# Store semantic knowledge
await agent_memory.store_memory(
    "Document analysis involves extracting key information and patterns",
    MemoryType.SEMANTIC,
    context_tags=['knowledge', 'document_processing']
)

# Query memories
relevant_memories = await agent_memory.retrieve_memories(
    "document analysis techniques",
    memory_types=[MemoryType.EPISODIC, MemoryType.SEMANTIC]
)
```

### Cross-Agent Collaboration

#### Knowledge Sharing

```python
# Request knowledge sharing
request_id = await protocol_manager.share_protocol.request_knowledge_share(
    target_agents=['other_agent'],
    knowledge_ids=['knowledge_1', 'knowledge_2'],
    purpose="collaborative research",
    permission_level=SharePermission.TEAM
)

# Approve sharing request
await protocol_manager.share_protocol.approve_share_request(request_id, True)
```

#### Collaborative Sessions

```python
# Create collaboration session
session_id = await orchestrator.collaboration_orchestrator.create_collaboration_session(
    agent_ids=['agent1', 'agent2', 'agent3'],
    session_type="research_project",
    mode=CollaborationMode.DEMOCRATIC
)

# Share context in session
await orchestrator.collaboration_orchestrator.share_context_in_session(
    session_id,
    'agent1',
    {'research_findings': 'Key insights about vector databases...'}
)
```

#### Consensus Building

```python
# Propose consensus
consensus_id = await protocol_manager.consensus_protocol.propose_consensus(
    participating_agents=['agent1', 'agent2', 'agent3'],
    topic="research_methodology",
    proposal={"approach": "systematic_review", "timeline": "4_weeks"}
)

# Vote on proposal
await protocol_manager.consensus_protocol.vote_on_consensus(
    consensus_id,
    'agent1',
    True,  # Vote yes
    "The proposed methodology is sound and timeline is realistic"
)
```

## API Reference

### REST API Endpoints

The system provides a comprehensive REST API:

- `POST /agents/{agent_id}/register` - Register agent
- `POST /knowledge` - Store knowledge item
- `GET /knowledge/search` - Search knowledge base
- `POST /agents/{agent_id}/memory` - Store agent memory
- `GET /agents/{agent_id}/memory` - Retrieve agent memories
- `POST /knowledge/share` - Share knowledge between agents
- `GET /analytics` - Get system analytics

### WebSocket API

Real-time communication through WebSocket:

```javascript
const ws = new WebSocket('ws://localhost:8765/ws/my_agent');

ws.onmessage = (event) => {
    const message = JSON.parse(event.data);
    console.log('Received:', message);
};

// Send knowledge update
ws.send(JSON.stringify({
    type: 'knowledge_update',
    content: 'New knowledge item...'
}));
```

## Migration from Existing RAG System

### Automatic Migration

The system automatically migrates existing knowledge:

```python
# Migration runs automatically on startup
migration_stats = await knowledge_bridge.migrate_existing_knowledge()
print(f"Migrated {migration_stats['migrated_chunks']} knowledge chunks")
```

### Hybrid Queries

Query both legacy and unified systems:

```python
# Hybrid search across both systems
results = await hybrid_interface.hybrid_search(
    "vector databases",
    agent_id='my_agent',
    prefer_unified=True,
    total_results=10
)
```

## Performance Optimization

### Query Optimization

The system automatically optimizes queries:

- **Query caching** with LRU eviction
- **Index optimization** based on query patterns
- **Connection pooling** for database access
- **Resource monitoring** with automatic cleanup

### Memory Management

- **Memory consolidation** for long-term storage
- **Decay mechanisms** for unused memories
- **Cache management** with size limits
- **Garbage collection** optimization

### Monitoring

```python
# Get performance report
report = performance_optimizer.get_performance_report()
print(f"Cache hit rate: {report['query_optimizer']['cache_stats']['hit_rate']}")
print(f"Average query time: {report['recent_performance'][-1]['query_latency_ms']}ms")
```

## Security Features

### Access Control

- **Role-based permissions** for knowledge access
- **Security tier enforcement** at query time
- **Agent authentication** and authorization
- **Audit logging** for all operations

### Trust Management

```python
# Trust scores automatically updated based on interactions
trust_score = protocol_manager.share_protocol.get_trust_score('other_agent')
print(f"Trust level: {trust_score}")
```

## Advanced Features

### Knowledge Versioning

All knowledge items are automatically versioned:

```python
# Get version history
history = versioning_system.get_version_history('knowledge_id')
for version in history:
    print(f"Version {version['version_number']}: {version['change_type']}")
```

### Emotional Context

Agent memories include emotional valence:

```python
# Store memory with emotional context
await agent_memory.store_memory(
    "The project failed due to communication issues",
    MemoryType.EPISODIC,
    emotional_valence=-0.6  # Negative experience
)
```

### Expertise Matching

Find experts for specific domains:

```python
# Register expertise
orchestrator.collaboration_orchestrator.register_expertise(
    'expert_agent',
    domains=['machine_learning', 'nlp'],
    skills=['python', 'tensorflow', 'research'],
    confidence_scores={'machine_learning': 0.9, 'nlp': 0.8}
)

# Find experts
experts = orchestrator.collaboration_orchestrator.find_experts(
    'machine_learning',
    required_skills=['python'],
    min_confidence=0.7
)
```

## Troubleshooting

### Common Issues

1. **High Memory Usage**
   - Check cache sizes in configuration
   - Monitor memory decay settings
   - Review embedding model size

2. **Slow Queries**
   - Verify database indexes are optimized
   - Check query cache hit rates
   - Monitor connection pool usage

3. **Sync Issues**
   - Verify transport layer configuration
   - Check network connectivity
   - Review conflict resolution logs

### Logging

Set appropriate logging levels:

```python
import logging
logging.basicConfig(level=logging.DEBUG)  # For detailed debugging
```

### Health Checks

```python
# Get system status
status = orchestrator.get_system_status()
print(f"System health: {status['components']}")
print(f"Active agents: {status['registered_agents']}")
```

## Development

### Extending the System

1. **Custom Memory Types**
2. **New Protocol Handlers**
3. **Additional Transport Layers**
4. **Custom Optimization Strategies**

### Testing

```python
# Run system tests
python -m pytest tests/

# Performance benchmarks
python benchmark_performance.py

# Integration tests
python test_agent_integration.py
```

## Production Deployment

### Scaling Considerations

- **Horizontal scaling** with multiple nodes
- **Database clustering** for high availability
- **Load balancing** for API endpoints
- **Caching layers** (Redis/Memcached)

### Monitoring

- **Prometheus metrics** integration
- **Grafana dashboards** for visualization
- **Alert management** for critical issues
- **Performance profiling** tools

## Support

For issues and questions:
- Check the troubleshooting section
- Review system logs for error details
- Monitor performance metrics for bottlenecks
- Use the health check endpoints for system status

## License

This unified knowledge management system is part of the Rod-Corp AI ecosystem.