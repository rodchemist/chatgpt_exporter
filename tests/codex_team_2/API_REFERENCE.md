# API Reference

## Overview
Complete API documentation for the Universal Documentation System. This API provides programmatic access to documentation scanning, generation, and quality monitoring capabilities.

## Installation
Ensure the documentation engine is installed and initialized:

```bash
pip install -r requirements.txt
python agents/scripts/documentation_engine.py --init
```

## Usage
The API can be accessed through the command-line interface or programmatically:

```python
from agents.scripts.documentation_engine import DocumentationEngine

# Initialize engine
engine = DocumentationEngine()

# Scan project
results = engine.scan_project()

# Generate documentation
docs = engine.generate_documentation(results)
```

## Services

### Documentation Engine API

#### `GET /status`
Returns comprehensive system status and health metrics.

**Response:**
```json
{
  "status": "active",
  "version": "1.0.0",
  "database_status": "connected",
  "last_scan": "2025-09-27T14:52:05.820360",
  "documentation_count": 9,
  "quality_average": 85.5
}
```

#### `POST /scan`
Triggers comprehensive project scan for documentation needs and service discovery.

**Request:**
```bash
python agents/scripts/documentation_engine.py --scan
```

**Response:**
```json
{
  "timestamp": "2025-09-27T14:52:05.820360",
  "source_files": ["src/main.py", "src/utils/api.py"],
  "documentation_files": ["README.md", "CHANGELOG.md"],
  "services": [{"name": "api", "type": "fastapi", "port": 8000}],
  "missing_docs": ["TROUBLESHOOTING.md"]
}
```

#### `POST /generate`
Generates comprehensive documentation based on scan results and templates.

**Request:**
```bash
python agents/scripts/documentation_engine.py --generate
```

**Response:**
```json
{
  "generated_count": 7,
  "files_created": [
    "README.md",
    "CHANGELOG.md",
    "ARCHITECTURE.md",
    "API_REFERENCE.md",
    "DEPLOYMENT.md",
    "TROUBLESHOOTING.md",
    "CONTRIBUTING.md"
  ]
}
```

#### `GET /metrics`
Returns detailed quality metrics and compliance scores for all documentation.

**Response:**
```json
{
  "overall_score": 85.5,
  "documents": [
    {
      "file": "README.md",
      "score": 95.0,
      "compliant": true,
      "last_modified": "2025-09-27T14:52:05.820360"
    }
  ]
}
```

## Command Line Interface

### Initialization
```bash
python agents/scripts/documentation_engine.py --init
```

### Verification
```bash
python agents/scripts/documentation_engine.py --verify
```

### Continuous Monitoring
```bash
python agents/scripts/documentation_engine.py --monitor
```

## Error Codes

| Code | Description | Solution |
|------|-------------|----------|
| 200  | Success | Operation completed successfully |
| 400  | Bad Request | Check input parameters and format |
| 404  | Not Found | Verify file paths and dependencies |
| 500  | Internal Error | Check logs and system configuration |

## License
This API documentation is part of the Universal Documentation System, released under the MIT License.

---
*API Reference v1.0.0*
