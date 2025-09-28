# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an **Intelligent Folder Organizer with RAG-Ready Indexing** system that transforms unstructured folders into searchable, agent-ready knowledge bases. Unlike simple file organization tools, this system performs deep content analysis, generates embeddings for semantic search, and produces multiple output formats suitable for LLM pipelines.

## Core Components

### Main Scripts
- **intelligent_organizer_rag.py**: Core RAG organizer that processes folders, extracts content, generates embeddings, and creates searchable indexes
- **agent_query_interface.py**: Query engine and API server for searching the generated knowledge base
- **demo_quick_start.py**: Interactive demo script with example usage patterns

### Configuration
- **rag_organizer_config.yaml**: Main configuration file for customizing chunking, embeddings, categorization, and export settings

## Common Commands

### Installation
```bash
# Install all dependencies
pip install -r requirements.txt

# Core dependencies only (minimal setup)
pip install pathlib2 pandas pyarrow numpy tiktoken
```

### Basic Usage
```bash
# Process a folder with RAG indexing
python intelligent_organizer_rag.py /path/to/input /path/to/output

# Process with custom configuration
python intelligent_organizer_rag.py /input /output --config rag_organizer_config.yaml

# Copy files instead of moving
python intelligent_organizer_rag.py /input /output --copy

# Search after processing
python intelligent_organizer_rag.py /input /output --search "query terms"
```

### API Server
```bash
# Start the query API server
python agent_query_interface.py /path/to/knowledge --server --port 8000

# Run demo with example queries
python demo_quick_start.py
```

### Testing Search Functionality
```bash
# Test search after processing
python -c "from intelligent_organizer_rag import RAGOrganizer; org = RAGOrganizer('output/knowledge'); results = org.search('your query'); print(results)"

# Test API endpoint
curl -X POST http://localhost:8000/search -H "Content-Type: application/json" -d '{"query": "test query", "top_k": 5}'
```

## Architecture Notes

### Data Flow
1. **Content Extraction**: Files are processed to extract text, metadata, and structure using appropriate extractors
2. **Smart Categorization**: Content is analyzed and categorized based on patterns defined in config
3. **Chunking**: Text is split into semantic chunks with configurable overlap for context preservation
4. **Embedding Generation**: Each chunk is converted to vector embeddings using sentence transformers
5. **Multi-Format Export**: Data is exported to JSONL (streaming), Parquet (analytics), SQLite (metadata), and FAISS (vector search)

### Key Classes
- **RAGOrganizer**: Main orchestrator class that coordinates all processing steps
- **QueryEngine**: Handles search operations across the knowledge base
- **ChunkingStrategy**: Implements intelligent text splitting with respect for document boundaries

### Output Structure
```
output/
├── organized/          # Categorized files
├── knowledge/
│   ├── canonical/      # Original documents
│   ├── exchange/       # JSONL chunks for streaming
│   ├── lakehouse/      # Parquet files for analytics
│   ├── embeddings/     # Vector representations
│   └── indexes/        # FAISS search indexes
└── metadata.db         # SQLite database with full-text search
```

## Configuration Customization

Key configuration sections in `rag_organizer_config.yaml`:
- **chunking**: Control chunk size (target_tokens: 800), overlap, and boundary respect
- **embeddings**: Choose model (default: all-MiniLM-L6-v2) and processing parameters
- **categories**: Define custom categorization rules with patterns and priorities
- **indexing**: Configure vector search parameters (FAISS settings)
- **rag.collections**: Set up different knowledge collections with security tiers

## Development Tips

- When modifying chunking logic, test with various document types to ensure boundaries are respected
- For custom extractors, inherit from base extractor class and implement extract() method
- API endpoints follow RESTful patterns - see agent_query_interface.py for adding new endpoints
- Use the monitoring section in config to track processing performance
- For large datasets, adjust performance.num_workers and chunk_size parameters