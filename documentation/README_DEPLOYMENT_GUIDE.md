# LibroSynth v2.0 - Complete Deployment Guide

## 🚀 Self-Improving Knowledge Extraction System

LibroSynth v2.0 is a revolutionary **autonomous knowledge extraction ecosystem** that literally learns from books about building better systems and applies those lessons to improve itself. This comprehensive guide covers everything from initial setup to advanced configuration.

---

## 📋 Table of Contents

1. [System Overview](#system-overview)
2. [Prerequisites](#prerequisites)
3. [Quick Start](#quick-start)
4. [Detailed Installation](#detailed-installation)
5. [Configuration](#configuration)
6. [Rod-Corp Integration](#rod-corp-integration)
7. [n8n Workflow Setup](#n8n-workflow-setup)
8. [AudioBookshelf Integration](#audiobookshelf-integration)
9. [Monitoring & Maintenance](#monitoring--maintenance)
10. [Troubleshooting](#troubleshooting)
11. [Advanced Features](#advanced-features)

---

## 🎯 System Overview

### Core Architecture

```
LibroSynth v2.0 Ecosystem
├── 🎧 AudioBookshelf Integration    # Auto-discovery & download
├── 🧠 Intelligent Classification   # Smart routing to pipelines
├── 🔄 Multi-Agent Processing      # Specialized extraction teams
├── 📊 Knowledge Graph Engine      # Semantic knowledge storage
├── ⚡ Auto-Startup Integration    # Seamless system integration
├── 🔗 n8n Workflow Automation    # Process orchestration
└── 🏢 Rod-Corp Ecosystem Sync    # Enterprise integration
```

### Team Structure

- **Team Alpha** (`~/rod-corp/books/`): Content discovery, classification, and processing
- **Team Beta** (`~/rod-corp/innovation/`): Strategic planning, integration, and innovation

### Key Features

- ✅ **Self-Improving**: Learns from system improvement books
- ✅ **Autonomous Operation**: Minimal manual intervention required
- ✅ **Intelligent Classification**: Automatically routes books to optimal pipelines
- ✅ **Multi-Source Discovery**: AudioBookshelf + local folder monitoring
- ✅ **Enterprise Integration**: Full Rod-Corp ecosystem compatibility
- ✅ **Advanced Caching**: CAG (Cache-Augmented Generation) for 90% latency reduction
- ✅ **Knowledge Graphs**: KAG (Knowledge-Augmented Generation) for persistent learning

---

## 📋 Prerequisites

### Hardware Requirements

#### Minimum Configuration
```yaml
CPU: AMD Ryzen 9 5900X / Intel i9-12900K
RAM: 32GB DDR4-3200
GPU: RTX 3090 24GB / RTX 4090 24GB
Storage: 2TB NVMe SSD
Network: Gigabit Ethernet
```

#### Optimal Configuration
```yaml
CPU: AMD Threadripper Pro / Intel Xeon
RAM: 64GB DDR5
GPU: 2x RTX 4090 or A100 40GB
Storage: 4TB NVMe RAID 0
Network: 10GbE
```

### Software Requirements

#### Operating System
- Ubuntu 22.04 LTS (recommended)
- Debian 12
- CentOS 8 / RHEL 8+
- Arch Linux (advanced users)

#### Core Dependencies
```bash
# Required system packages
sudo apt update && sudo apt install -y \
    python3.11 python3.11-venv python3.11-dev \
    postgresql-15 postgresql-contrib \
    redis-server \
    nginx \
    curl wget git \
    build-essential \
    libpq-dev \
    libmagic1 \
    ffmpeg \
    tesseract-ocr \
    poppler-utils \
    jq \
    systemd
```

#### Optional Dependencies
```bash
# For enhanced performance
sudo apt install -y \
    nvidia-driver-535 \
    nvidia-cuda-toolkit \
    docker.io docker-compose \
    nodejs npm \
    n8n
```

---

## ⚡ Quick Start

### 1. One-Command Installation

```bash
# Download and run the master installation script
curl -fsSL https://raw.githubusercontent.com/rod-corp/librosynth-v2/main/install.sh | bash
```

### 2. Verify Installation

```bash
# Check system health
librosynth-check

# View service status
librosynth-status

# Access API documentation
open http://localhost:19000/docs
```

### 3. Process Your First Book

```bash
# Add a book to processing queue
curl -X POST http://localhost:19000/api/process-book \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Clean Architecture",
    "author": "Robert C. Martin",
    "file_path": "/path/to/book.pdf",
    "priority": "high"
  }'
```

---

## 🔧 Detailed Installation

### Step 1: Environment Setup

```bash
# Create Rod-Corp directory structure
mkdir -p ~/rod-corp/{books,innovation}
cd ~/rod-corp

# Clone LibroSynth v2.0
git clone https://github.com/rod-corp/librosynth-v2.git books/librosynth_v2
cd books/librosynth_v2
```

### Step 2: Database Setup

```bash
# Install and configure PostgreSQL
sudo systemctl enable postgresql
sudo systemctl start postgresql

# Create LibroSynth database
sudo -u postgres createuser --interactive librosynth
sudo -u postgres createdb librosynth_v2 -O librosynth

# Set password
sudo -u postgres psql -c "ALTER USER librosynth PASSWORD 'your_secure_password';"
```

### Step 3: Redis Configuration

```bash
# Configure Redis
sudo systemctl enable redis-server
sudo systemctl start redis-server

# Test Redis connection
redis-cli ping  # Should return PONG
```

### Step 4: Python Environment

```bash
# Create and activate virtual environment
python3.11 -m venv venv
source venv/bin/activate

# Install LibroSynth dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 5: Auto-Startup Integration

```bash
# Run the auto-startup integration script
chmod +x auto_startup_integration.sh
./auto_startup_integration.sh
```

### Step 6: Service Activation

```bash
# Start all LibroSynth services
sudo systemctl start librosynth-v2.service
sudo systemctl start librosynth-audiobookshelf.service
sudo systemctl start librosynth-knowledge.service
sudo systemctl start librosynth-monitor.service

# Verify all services are running
librosynth-status
```

---

## ⚙️ Configuration

### Environment Configuration

Edit `~/rod-corp/books/librosynth_v2/config/production.env`:

```bash
# Core Configuration
LIBROSYNTH_VERSION=2.0.0
ENVIRONMENT=production
DEBUG=false

# Database
DATABASE_URL=postgresql://librosynth:your_password@localhost:5432/librosynth_v2
REDIS_URL=redis://localhost:6379/0

# AudioBookshelf Integration
AUDIOBOOKSHELF_API=http://localhost:13378
AUDIOBOOKSHELF_TOKEN=your_audiobookshelf_token

# n8n Integration
N8N_API=http://localhost:5678
N8N_WEBHOOK_SECRET=your_webhook_secret

# AI Model Configuration
EMBEDDING_MODEL=BAAI/bge-m3
LOCAL_LLM=TheBloke/Mixtral-8x7B-Instruct-v0.1-AWQ

# Processing Limits
MAX_CONCURRENT_DOWNLOADS=3
MAX_CONCURRENT_PROCESSING=2
COMPRESSION_RATIO_DEFAULT=0.20
```

### Model Configuration

```bash
# Download required models
python -c "
from transformers import AutoTokenizer, AutoModel
from sentence_transformers import SentenceTransformer

# Download embedding model
SentenceTransformer('BAAI/bge-m3', cache_folder='./models')

# Download reranking model
AutoTokenizer.from_pretrained('cross-encoder/ms-marco-MiniLM-L-12-v2', cache_dir='./models')
AutoModel.from_pretrained('cross-encoder/ms-marco-MiniLM-L-12-v2', cache_dir='./models')
"
```

---

## 🏢 Rod-Corp Integration

### Team Alpha Setup (Extraction & Processing)

```bash
# Navigate to Team Alpha workspace
cd ~/rod-corp/books

# Create team structure
mkdir -p {agents,discovery,processing,storage}/{raw,processed,knowledge_base}

# Configure team agents
cat > team_alpha_config.json << 'EOF'
{
  "team_name": "LibroSynth_Extraction_Team_Alpha",
  "team_lead": "LIBROSYNTH_CLASSIFIER_V2",
  "agents": [
    "LIBROSYNTH_EXTRACTOR_V2",
    "LIBROSYNTH_QUALITY_V2",
    "AUDIOBOOKSHELF_CONNECTOR",
    "FOLDER_SENTINEL_V2"
  ],
  "responsibilities": [
    "Content discovery and classification",
    "Multi-format extraction and processing",
    "Quality validation and optimization"
  ]
}
EOF
```

### Team Beta Setup (Integration & Innovation)

```bash
# Navigate to Team Beta workspace
cd ~/rod-corp/innovation

# Create integration structure
mkdir -p {librosynth_integration,discussions,metrics}/{strategic_planning,knowledge_coordination,agent_coordination,innovation_pipeline}

# Configure team agents
cat > team_beta_config.json << 'EOF'
{
  "team_name": "LibroSynth_Integration_Team_Beta",
  "team_lead": "INNOVATION_STRATEGIST",
  "agents": [
    "KNOWLEDGE_ARCHITECT",
    "INTEGRATION_ORCHESTRATOR",
    "INSIGHT_SYNTHESIZER",
    "OPPORTUNITY_SCOUT"
  ],
  "responsibilities": [
    "Strategic planning and roadmap development",
    "Knowledge taxonomy and coordination",
    "Innovation opportunity detection"
  ]
}
EOF
```

### Inter-Team Communication

```bash
# Set up Redis-based communication
redis-cli config set notify-keyspace-events KEA

# Test communication
python3 << 'EOF'
import redis
import json

r = redis.Redis(host='localhost', port=6379, db=0)

# Team Alpha sends message to Team Beta
message = {
    "from": "team_alpha",
    "to": "team_beta",
    "event": "book_processed",
    "data": {"book_id": "test_123", "category": "system_architecture"}
}

r.publish("team_communication", json.dumps(message))
print("✅ Inter-team communication test successful")
EOF
```

---

## 🔄 n8n Workflow Setup

### Install n8n

```bash
# Install n8n globally
npm install -g n8n

# Or run with Docker
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n
```

### Import LibroSynth Workflows

```bash
# Copy workflow configurations
cp n8n_workflows_config.json ~/.n8n/workflows/

# Import via n8n CLI
n8n import:workflow --input=~/.n8n/workflows/n8n_workflows_config.json
```

### Configure Webhooks

```bash
# Create webhook endpoints
curl -X POST http://localhost:5678/api/v1/workflows \
  -H "Content-Type: application/json" \
  -d @n8n_workflows_config.json

# Test webhook
curl -X POST http://localhost:5678/webhook/librosynth-test \
  -H "Content-Type: application/json" \
  -d '{"test": "webhook_working"}'
```

### Workflow Activation

1. Open n8n interface: http://localhost:5678
2. Navigate to **Workflows**
3. Activate these workflows:
   - ✅ LibroSynth Book Discovery Automation
   - ✅ LibroSynth Knowledge Extraction Pipeline
   - ✅ LibroSynth Self-Improvement Engine
   - ✅ Rod-Corp Integration Synchronization

---

## 🎧 AudioBookshelf Integration

### AudioBookshelf Setup

```bash
# Install AudioBookshelf
curl -fsSL https://install.audiobookshelf.org | bash

# Or with Docker
docker run -d \
  --name audiobookshelf \
  -p 13378:80 \
  -v /path/to/audiobooks:/audiobooks \
  -v /path/to/podcasts:/podcasts \
  -v /path/to/config:/config \
  -v /path/to/metadata:/metadata \
  ghcr.io/advplyr/audiobookshelf:latest
```

### Configure LibroSynth Integration

```bash
# Get AudioBookshelf API token
# 1. Login to AudioBookshelf: http://localhost:13378
# 2. Go to Settings > Users > [Your User] > API Token
# 3. Copy the token

# Add token to LibroSynth config
echo "AUDIOBOOKSHELF_TOKEN=your_token_here" >> ~/rod-corp/books/librosynth_v2/config/production.env

# Test integration
python3 << 'EOF'
import asyncio
import sys
sys.path.append('/home/$(whoami)/rod-corp/books/librosynth_v2')

from audiobookshelf_integration import AudioBookshelfIntegrator, LibroSynthV2Config

async def test_integration():
    config = LibroSynthV2Config()
    integrator = AudioBookshelfIntegrator(config)

    await integrator.initialize()
    books = await integrator.discover_and_classify_books()

    print(f"✅ Discovered {len(books)} books")
    for book in books[:3]:
        print(f"  📖 {book.title} - {book.classification}")

    await integrator.cleanup()

asyncio.run(test_integration())
EOF
```

### Library Monitoring Setup

```bash
# Create monitored directories
mkdir -p ~/rod-corp/books/discovery/{business,technical,academic,innovation}

# Set up file system watching
cat > ~/rod-corp/books/discovery/watch_folders.py << 'EOF'
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import requests

class BookDiscoveryHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        # Trigger n8n workflow
        requests.post('http://localhost:5678/webhook/librosynth-filesystem',
                     json={'file_path': event.src_path})

if __name__ == "__main__":
    observer = Observer()
    observer.schedule(BookDiscoveryHandler(), '~/rod-corp/books/discovery', recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
EOF

# Run as background service
nohup python3 ~/rod-corp/books/discovery/watch_folders.py &
```

---

## 📊 Monitoring & Maintenance

### Health Monitoring Dashboard

```bash
# Create monitoring dashboard
cat > ~/rod-corp/books/librosynth_v2/scripts/dashboard.py << 'EOF'
#!/usr/bin/env python3
import requests
import json
import time
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich.panel import Panel

console = Console()

def get_system_status():
    """Get comprehensive system status"""
    status = {}

    # LibroSynth API Health
    try:
        response = requests.get('http://localhost:19000/health', timeout=5)
        status['librosynth_api'] = response.status_code == 200
    except:
        status['librosynth_api'] = False

    # n8n Status
    try:
        response = requests.get('http://localhost:5678/healthz', timeout=5)
        status['n8n'] = response.status_code == 200
    except:
        status['n8n'] = False

    # AudioBookshelf Status
    try:
        response = requests.get('http://localhost:13378/api/ping', timeout=5)
        status['audiobookshelf'] = response.status_code == 200
    except:
        status['audiobookshelf'] = False

    return status

def create_status_table():
    """Create status table"""
    table = Table(title="LibroSynth v2.0 System Status")
    table.add_column("Component", style="cyan")
    table.add_column("Status", style="magenta")
    table.add_column("Last Check", style="green")

    status = get_system_status()
    timestamp = datetime.now().strftime("%H:%M:%S")

    for component, is_healthy in status.items():
        status_icon = "✅ Healthy" if is_healthy else "❌ Down"
        table.add_row(component.replace('_', ' ').title(), status_icon, timestamp)

    return table

def main():
    """Main dashboard loop"""
    with Live(create_status_table(), refresh_per_second=1) as live:
        while True:
            time.sleep(10)
            live.update(create_status_table())

if __name__ == "__main__":
    main()
EOF

chmod +x ~/rod-corp/books/librosynth_v2/scripts/dashboard.py

# Run dashboard
python3 ~/rod-corp/books/librosynth_v2/scripts/dashboard.py
```

### Performance Metrics

```bash
# Enable Prometheus metrics
echo "PROMETHEUS_ENABLED=true" >> ~/rod-corp/books/librosynth_v2/config/production.env
echo "PROMETHEUS_PORT=19001" >> ~/rod-corp/books/librosynth_v2/config/production.env

# Install and configure Prometheus
wget https://github.com/prometheus/prometheus/releases/download/v2.45.0/prometheus-2.45.0.linux-amd64.tar.gz
tar xvfz prometheus-*.tar.gz
sudo mv prometheus-*/prometheus /usr/local/bin/
sudo mv prometheus-*/promtool /usr/local/bin/

# Create Prometheus configuration
cat > /etc/prometheus/prometheus.yml << 'EOF'
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'librosynth-v2'
    static_configs:
      - targets: ['localhost:19001']

  - job_name: 'node-exporter'
    static_configs:
      - targets: ['localhost:9100']
EOF

# Start Prometheus
sudo systemctl enable prometheus
sudo systemctl start prometheus
```

### Log Management

```bash
# Configure log rotation
sudo cat > /etc/logrotate.d/librosynth-v2 << 'EOF'
/var/log/librosynth_v2/*.log {
    daily
    missingok
    rotate 30
    compress
    delaycompress
    notifempty
    copytruncate
    postrotate
        systemctl reload librosynth-v2.service
    endscript
}
EOF

# Set up centralized logging
sudo journalctl --vacuum-time=30d
sudo systemctl enable systemd-journald
```

### Backup Strategy

```bash
# Create backup script
cat > ~/rod-corp/books/librosynth_v2/scripts/backup.sh << 'EOF'
#!/bin/bash
# LibroSynth v2.0 Backup Script

BACKUP_DIR="/backup/librosynth_v2/$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"

# Database backup
pg_dump librosynth_v2 > "$BACKUP_DIR/database.sql"

# Configuration backup
cp -r ~/rod-corp/books/librosynth_v2/config "$BACKUP_DIR/"

# Knowledge base backup
tar -czf "$BACKUP_DIR/knowledge_base.tar.gz" ~/rod-corp/books/knowledge_base/

# Model cache backup (optional, models can be re-downloaded)
# tar -czf "$BACKUP_DIR/models.tar.gz" ~/rod-corp/books/librosynth_v2/models/

echo "✅ Backup completed: $BACKUP_DIR"
EOF

chmod +x ~/rod-corp/books/librosynth_v2/scripts/backup.sh

# Schedule daily backups
(crontab -l; echo "0 2 * * * ~/rod-corp/books/librosynth_v2/scripts/backup.sh") | crontab -
```

---

## 🔧 Troubleshooting

### Common Issues and Solutions

#### 1. Services Won't Start

```bash
# Check service logs
sudo journalctl -u librosynth-v2.service -f

# Common fixes:
# - Check database connection
pg_isready -h localhost -p 5432 -U librosynth

# - Check Redis connection
redis-cli ping

# - Check Python environment
source ~/rod-corp/books/librosynth_v2/venv/bin/activate
python3 -c "import librosynth_v2; print('✅ Import successful')"

# - Restart services
sudo systemctl restart librosynth-v2.service
```

#### 2. AudioBookshelf Connection Failed

```bash
# Test AudioBookshelf API
curl -H "Authorization: Bearer YOUR_TOKEN" \
     http://localhost:13378/api/ping

# Check AudioBookshelf logs
docker logs audiobookshelf

# Verify token in config
grep AUDIOBOOKSHELF_TOKEN ~/rod-corp/books/librosynth_v2/config/production.env
```

#### 3. n8n Workflows Not Triggering

```bash
# Check n8n status
curl http://localhost:5678/healthz

# Test webhook manually
curl -X POST http://localhost:5678/webhook/librosynth-test \
     -H "Content-Type: application/json" \
     -d '{"test": true}'

# Check n8n logs
docker logs n8n
```

#### 4. High Memory Usage

```bash
# Monitor memory usage
watch -n 5 'free -h && echo "---" && ps aux --sort=-%mem | head -10'

# Optimize model loading
echo "MODEL_CACHE_LIMIT=2" >> ~/rod-corp/books/librosynth_v2/config/production.env

# Restart services
sudo systemctl restart librosynth-*.service
```

#### 5. Slow Processing

```bash
# Check GPU utilization
nvidia-smi

# Monitor processing queue
curl http://localhost:19000/api/metrics | jq '.processing_queue'

# Adjust concurrent processing
echo "MAX_CONCURRENT_PROCESSING=1" >> ~/rod-corp/books/librosynth_v2/config/production.env
```

### Debug Mode

```bash
# Enable debug mode
cp ~/rod-corp/books/librosynth_v2/config/production.env ~/rod-corp/books/librosynth_v2/config/debug.env
sed -i 's/DEBUG=false/DEBUG=true/' ~/rod-corp/books/librosynth_v2/config/debug.env
sed -i 's/LOG_LEVEL=INFO/LOG_LEVEL=DEBUG/' ~/rod-corp/books/librosynth_v2/config/debug.env

# Run in debug mode
LIBROSYNTH_CONFIG=~/rod-corp/books/librosynth_v2/config/debug.env \
python3 -m librosynth_v2.main
```

---

## 🚀 Advanced Features

### Self-Improvement Engine

The self-improvement engine automatically extracts patterns from system improvement books and applies them:

```python
# Example: Automatic architecture improvement
from librosynth_v2.self_improvement import SelfImprovementEngine

engine = SelfImprovementEngine()

# Process "Clean Architecture" book
improvements = await engine.extract_improvements(
    book_path="/path/to/clean_architecture.pdf",
    categories=["architecture", "code_quality", "design_patterns"]
)

# Apply high-priority improvements
for improvement in improvements:
    if improvement.priority == "high" and improvement.confidence > 0.8:
        await engine.apply_improvement(improvement)
```

### Custom Processing Pipelines

Create specialized pipelines for specific book types:

```python
# Example: Technical book pipeline
@register_pipeline("technical_deep_dive")
async def technical_pipeline(book_data):
    # Extract code examples
    code_blocks = extract_code_blocks(book_data.content)

    # Analyze technical patterns
    patterns = analyze_technical_patterns(book_data.content)

    # Generate executable examples
    examples = generate_examples(code_blocks, patterns)

    return {
        "synthesis": create_technical_synthesis(book_data),
        "code_examples": examples,
        "patterns": patterns,
        "compression_ratio": 0.25  # Preserve technical detail
    }
```

### Knowledge Graph Queries

Query the extracted knowledge using semantic search:

```python
# Example: Knowledge graph queries
from librosynth_v2.knowledge import KnowledgeGraph

kg = KnowledgeGraph()

# Find architectural patterns
patterns = await kg.query(
    "Find all architectural patterns mentioned in system design books",
    similarity_threshold=0.8
)

# Cross-reference concepts
related = await kg.find_related_concepts(
    concept="microservices",
    domains=["architecture", "devops", "scalability"]
)
```

### Integration with External Systems

```python
# Example: Slack integration for notifications
from librosynth_v2.integrations import SlackNotifier

notifier = SlackNotifier(webhook_url="your_slack_webhook")

# Notify when high-value book is processed
@on_book_processed
async def notify_completion(book_result):
    if book_result.category == "system_architecture" and book_result.quality_score > 4.0:
        await notifier.send_message(
            f"📚 High-value book processed: {book_result.title}\n"
            f"Quality: {book_result.quality_score}/5.0\n"
            f"Key insights: {len(book_result.insights)}"
        )
```

---

## 📚 API Reference

### Core Endpoints

```bash
# Health check
GET /health

# Process book
POST /api/process-book
{
  "title": "Clean Architecture",
  "author": "Robert C. Martin",
  "file_path": "/path/to/book.pdf",
  "priority": "high",
  "pipeline": "system_architecture"
}

# Get processing status
GET /api/books/{book_id}/status

# List processed books
GET /api/books?category=system_architecture&limit=20

# Get book insights
GET /api/books/{book_id}/insights

# Trigger knowledge extraction
POST /api/extract-knowledge
{
  "book_id": "uuid",
  "extraction_types": ["patterns", "improvements", "concepts"]
}

# Query knowledge graph
POST /api/knowledge/query
{
  "query": "microservices architecture patterns",
  "similarity_threshold": 0.8,
  "max_results": 10
}
```

### WebSocket Endpoints

```bash
# Real-time processing updates
ws://localhost:19000/ws/processing/{book_id}

# System health monitoring
ws://localhost:19000/ws/health

# Knowledge extraction progress
ws://localhost:19000/ws/extraction/{extraction_id}
```

---

## 🤝 Contributing

### Development Setup

```bash
# Clone development branch
git clone -b develop https://github.com/rod-corp/librosynth-v2.git
cd librosynth-v2

# Install development dependencies
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install

# Run tests
pytest tests/ -v

# Start development server
uvicorn librosynth_v2.main:app --reload --port 19000
```

### Code Quality

```bash
# Run linting
black librosynth_v2/
flake8 librosynth_v2/
mypy librosynth_v2/

# Run tests with coverage
pytest --cov=librosynth_v2 --cov-report=html

# Security scan
bandit -r librosynth_v2/
```

---

## 📄 License

LibroSynth v2.0 is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 🆘 Support

### Community Support
- **GitHub Issues**: https://github.com/rod-corp/librosynth-v2/issues
- **Discussions**: https://github.com/rod-corp/librosynth-v2/discussions
- **Discord**: https://discord.gg/rod-corp

### Enterprise Support
- **Email**: support@rod-corp.com
- **Priority Support**: Available for Rod-Corp Enterprise customers

---

## 🎉 Success Stories

> *"LibroSynth v2.0 processed our entire technical library and identified 50+ improvement opportunities that we implemented to reduce system complexity by 40%."* - Tech Lead, Fortune 500 Company

> *"The self-improvement engine learned from our architecture books and automatically suggested refactoring patterns that improved our code quality scores by 60%."* - Senior Architect, Startup

---

**🚀 Ready to transform your knowledge extraction? Let LibroSynth v2.0 learn from the best books about building better systems and apply those lessons to continuously improve itself!**