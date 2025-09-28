# RAG Documentation Specialist Agent

An advanced Claude agent that combines HARMONY's hierarchical documentation organization with cutting-edge RAG (Retrieval-Augmented Generation) technologies for intelligent documentation management and knowledge synthesis.

## Overview

The RAG Documentation Specialist Agent represents the evolution of Rod-Corp's documentation ecosystem from static files to a living, intelligent knowledge system. It seamlessly integrates the organizational excellence of the HARMONY agent with state-of-the-art RAG capabilities to deliver context-aware, automatically maintained, and continuously improving documentation.

## Key Features

### 🧠 Advanced RAG Architecture
- **Multi-Modal Knowledge Ingestion**: Processes code, documentation, APIs, and user feedback
- **Semantic Search**: Vector similarity for conceptual matches
- **Hybrid Retrieval**: Combines semantic + keyword approaches with Reciprocal Rank Fusion
- **Context-Aware Generation**: Multi-source synthesis with accuracy validation
- **Knowledge Graph Construction**: Real-time relationship mapping

### 📚 Intelligent Documentation Management
- **Automated Generation**: Context-aware documentation from code analysis
- **Change-Driven Updates**: Smart diff-based content modification
- **Quality Assessment**: Multi-dimensional scoring (completeness, accuracy, clarity, consistency)
- **Version Control**: Semantic versioning with automated increment logic
- **Cross-Reference Management**: Intelligent linking and broken link detection

### 🏗️ Hierarchical Organization (HARMONY Heritage)
- **Intelligent Taxonomy**: Multi-level categorization systems
- **Auto-Categorization**: Confidence-scored content classification
- **Information Architecture**: Logical content organization recommendations
- **Nested Structure Optimization**: Dynamic hierarchy adjustments

### 🔄 Continuous Quality Monitoring
- **Real-Time Assessment**: Ongoing quality monitoring and improvement suggestions
- **Coverage Analysis**: Documentation completeness tracking
- **Consistency Enforcement**: Style guide adherence and terminology standardization
- **Performance Optimization**: Vector index tuning and caching strategies

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                   RAG Documentation Specialist                  │
├─────────────────────┬─────────────────────┬─────────────────────┤
│    HARMONY Base     │     RAG Engine      │   Quality Engine    │
│                     │                     │                     │
│ • Hierarchical Org  │ • Vector Database   │ • Quality Metrics   │
│ • Taxonomy Management│ • Semantic Search   │ • Content Analysis  │
│ • Cross-References  │ • Hybrid Retrieval  │ • Improvement Recs  │
│ • Structure Optimization│ • Context Synthesis│ • Coverage Tracking │
└─────────────────────┴─────────────────────┴─────────────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Knowledge Base    │
                    │                     │
                    │ • ChromaDB Vector   │
                    │ • Multiple Collections│
                    │ • Embeddings Store  │
                    │ • Metadata Index    │
                    └─────────────────────┘
```

## Installation & Setup

### Prerequisites
- Python 3.8+
- Git repository access
- Rod-Corp AI system integration

### Required Python Packages
```bash
pip install chromadb sentence-transformers langchain gitpython jinja2 markdown pyyaml fastapi uvicorn beautifulsoup4 pypdf python-docx
```

### Quick Setup
```bash
# Navigate to agent directory
cd /home/rod/rod-corp/agents/profiles/rag-documentation-specialist

# Run initialization script
./init.sh

# Register agent
python3 register_agent.py

# Start agent
python3 start_agent.py
```

## Configuration

### Core Configuration (`config/config.json`)

```json
{
  "rag_configuration": {
    "vector_database": {
      "provider": "chromadb",
      "embedding_model": "all-MiniLM-L6-v2",
      "chunk_size": 1000,
      "chunk_overlap": 200,
      "similarity_threshold": 0.7
    },
    "retrieval_methods": {
      "semantic_search": {"enabled": true, "weight": 0.6},
      "keyword_search": {"enabled": true, "weight": 0.3},
      "hybrid_search": {"enabled": true, "weight": 0.1}
    }
  },
  "documentation_management": {
    "auto_generation": {"enabled": true},
    "quality_assessment": {"minimum_quality_threshold": 0.7},
    "version_control": {"strategy": "semantic_versioning"}
  }
}
```

### Environment Variables (`.env`)
```bash
AGENT_NAME=rag-documentation-specialist
EMBEDDINGS_MODEL=all-MiniLM-L6-v2
KNOWLEDGE_BASE_PATH=./workspace/knowledge_base
CHUNK_SIZE=1000
SIMILARITY_THRESHOLD=0.7
```

## Usage

### Starting the Agent

#### Daemon Mode (Continuous Operation)
```bash
python3 start_agent.py
```

#### Command Mode (Single Operations)
```bash
# Analyze repository
python3 start_agent.py --analyze

# Generate API documentation
python3 start_agent.py --generate api

# Update knowledge base
python3 start_agent.py --update-kb

# Quality assessment
python3 start_agent.py --quality-check

# Health check
python3 start_agent.py --health
```

### Core Operations

#### 1. Repository Analysis
```python
# Analyze codebase for documentation needs
result = await agent.analyze_repository()
print(f"Documentation coverage: {result['documentation_coverage']['percentage']}%")
```

#### 2. RAG-Powered Documentation Generation
```python
# Generate context-aware API documentation
doc_update = await agent.generate_documentation("api", {
    "module_name": "UserService",
    "description": "User management API",
    "base_url": "https://api.example.com/v1"
})
```

#### 3. Knowledge Base Queries
```python
# Query knowledge base with semantic search
results = await agent.query_knowledge_base(
    "How to implement authentication?",
    collection_names=["documentation", "code_comments"],
    top_k=5
)
```

#### 4. Quality Assessment
```python
# Assess documentation quality
quality_report = await agent.assess_documentation_quality()
print(f"Overall quality score: {quality_report['overall_score']}")
```

## Document Collections

The agent organizes knowledge into specialized collections:

| Collection | Purpose | Content Types |
|------------|---------|---------------|
| `documentation` | General documentation | Markdown, RST, HTML files |
| `code_comments` | Code documentation | Docstrings, inline comments |
| `api_specs` | API documentation | OpenAPI specs, API guides |
| `change_logs` | Version history | Changelogs, release notes |
| `user_guides` | User documentation | Tutorials, how-to guides |
| `technical_specs` | Technical documentation | Architecture, design docs |
| `quality_metrics` | Quality assessments | Quality reports, metrics |

## Template System

### Available Templates

#### API Documentation (`api_documentation.md`)
```markdown
# {{ module_name }} API Documentation

## Overview
{{ description }}

## Endpoints
{% for endpoint in endpoints %}
### {{ endpoint.method }} {{ endpoint.path }}
{{ endpoint.description }}
{% endfor %}
```

#### Changelog (`changelog.md`)
```markdown
# Changelog

## Version {{ version }} - {{ date }}

### Added
{% for item in added %}
- {{ item }}
{% endfor %}
```

#### User Guide (`user_guide.md`)
```markdown
# {{ title }} User Guide

## Getting Started
{{ quick_start }}

## Use Cases
{% for use_case in use_cases %}
### {{ use_case.title }}
{{ use_case.description }}
{% endfor %}
```

### Custom Templates
Create custom templates in the `templates/` directory using Jinja2 syntax.

## Quality Metrics

The agent evaluates documentation across multiple dimensions:

### Quality Dimensions
- **Completeness** (0-1): Information coverage and comprehensiveness
- **Accuracy** (0-1): Factual correctness and code synchronization
- **Clarity** (0-1): Readability and user comprehension
- **Consistency** (0-1): Style guide adherence and uniformity
- **Coverage** (0-1): Presence of expected documentation sections

### Quality Scoring
```python
QualityMetrics(
    completeness=0.85,
    accuracy=0.92,
    clarity=0.78,
    consistency=0.88,
    coverage=0.75,
    overall_score=0.84
)
```

## Integration

### Rod-Corp Ecosystem Integration

#### AI Interaction Server
```python
# Register with AI server
POST http://localhost:49152/agents/register
{
    "agent_id": "rag-documentation-specialist",
    "capabilities": ["documentation", "rag", "knowledge_management"]
}
```

#### Database Integration
- **SQLite**: Local agent registry and state
- **MSSQL**: Rod-Corp central database integration
- **ChromaDB**: Vector embeddings storage

#### File Sharing
- **FTP Server**: Document distribution (10.0.0.6)
- **Shared Folders**: Cross-agent document access
- **Git Integration**: Version control and change tracking

### Agent Collaboration

The agent collaborates with other Rod-Corp agents:

- **ALEX_ENGINEERING_DIRECTOR**: Technical architecture documentation
- **ECHO**: Quality assurance and validation
- **HARMONY**: Hierarchical organization (legacy integration)
- **Code Review Specialists**: Technical accuracy validation

## Monitoring & Maintenance

### Health Monitoring
```bash
# Check agent health
python3 health_check.py
```

### Log Files
- `logs/agent.log`: Main agent operations
- `logs/registration.log`: Agent registration events
- `logs/startup_info.json`: Startup configuration
- `logs/shutdown_info.json`: Shutdown status

### Performance Metrics
- Knowledge base query response times
- Documentation generation speed
- Quality assessment accuracy
- Vector database performance

## API Reference

### Core Methods

#### `initialize()` → `bool`
Initialize the RAG Documentation agent with all components.

#### `query_knowledge_base(query: str, collections: List[str], top_k: int)` → `Dict`
Query the knowledge base using semantic search.

#### `generate_documentation(doc_type: str, context: Dict)` → `DocumentationUpdate`
Generate documentation using RAG and templates.

#### `analyze_repository()` → `Dict`
Analyze repository for documentation needs and coverage.

#### `assess_documentation_quality()` → `Dict`
Perform comprehensive quality assessment.

#### `refresh_knowledge_base()` → `Dict`
Update knowledge base with latest content.

### Data Structures

#### `DocumentChunk`
```python
@dataclass
class DocumentChunk:
    content: str
    metadata: Dict[str, Any]
    embedding: Optional[List[float]]
    quality_score: float
```

#### `QualityMetrics`
```python
@dataclass
class QualityMetrics:
    completeness: float
    accuracy: float
    clarity: float
    consistency: float
    coverage: float
    overall_score: float
```

## Advanced Features

### Multi-Modal Processing
- **PDF Extraction**: Automatic text extraction from PDF documents
- **DOCX Processing**: Microsoft Word document parsing
- **Code Analysis**: AST-based Python code documentation
- **Markdown Processing**: Semantic section parsing

### Intelligent Chunking
- **Semantic Boundaries**: Respect document structure
- **Code-Aware Chunking**: Function and class boundaries
- **Overlap Strategy**: Configurable overlap for context preservation
- **Metadata Enrichment**: Enhanced chunk metadata

### Vector Database Optimization
- **Collection Specialization**: Domain-specific vector collections
- **Embedding Caching**: Efficient embedding storage and retrieval
- **Similarity Tuning**: Configurable similarity thresholds
- **Index Optimization**: Performance-tuned vector indices

## Troubleshooting

### Common Issues

#### Import Errors
```bash
# Install missing dependencies
pip install -r requirements.txt

# Check Python path
export PYTHONPATH="/home/rod/rod-corp:$PYTHONPATH"
```

#### Vector Database Issues
```bash
# Clear and rebuild vector database
rm -rf workspace/knowledge_base/vector_db/*
python3 start_agent.py --update-kb
```

#### Performance Issues
```bash
# Check embedding model loading
python3 -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')"

# Monitor resource usage
top -p $(pgrep -f rag-documentation-specialist)
```

### Debug Mode
Enable detailed logging:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Development

### Contributing
1. Follow Rod-Corp coding standards
2. Add comprehensive docstrings
3. Include unit tests for new features
4. Update documentation templates

### Testing
```bash
# Run agent health check
python3 health_check.py

# Test knowledge base queries
python3 -c "
import asyncio
from rag_documentation_agent import RAGDocumentationAgent
from config import get_agent_context

async def test():
    agent = RAGDocumentationAgent(get_agent_context())
    await agent.initialize()
    result = await agent.query_knowledge_base('test query')
    print(result)

asyncio.run(test())
"
```

### Extension Points
- Custom document processors
- Additional vector database providers
- Enhanced quality metrics
- New template formats

## License

Part of the Rod-Corp AI System. All rights reserved.

## Support

For technical support:
- Check the [troubleshooting guide](#troubleshooting)
- Review agent logs in `logs/`
- Contact Rod-Corp AI System administrators

---

**Generated by RAG Documentation Specialist Agent**
*Combining HARMONY's organizational excellence with cutting-edge RAG technologies*