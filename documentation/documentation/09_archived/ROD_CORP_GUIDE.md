# Rod-Corp AI Agent System - Comprehensive Guide

This file provides comprehensive guidance for working with the Rod-Corp AI Agent System repository.

## Project Overview: Multi-Agent AI Corporate Ecosystem

This repository contains a sophisticated multi-agent AI system operating across microservices. The system uses MSSQL Server as the central communication database and includes real-time dashboards, deployment automation, and comprehensive data processing pipelines. The architecture has evolved from a monolithic PROJECT structure to a distributed microservices approach.

## System Architecture

### Core Components
- **Agent Directory Database**: MSSQL Server (10.0.0.2:1433) with comprehensive agent registry
- **Microservices**: 20+ specialized Python services in `/services/`
- **Real-time Dashboard**: Next.js React application in `/PROJECT/dashboard/`
- **Centralized Infrastructure**: Docker Compose stack with Redis, FastAPI Gateway
- **API Gateway**: FastAPI-based service coordination and proxy (`services/api_gateway/`)
- **Unified API**: Combined image generation and project locator (`services/rodcorp_unified_api/`)
- **AI Orchestration**: Agent coordination and delegation (`services/ai_orchestration/`, `services/delegation_system/`)
- **RAG System**: Knowledge retrieval and processing (`services/rag_system/`)
- **Deployment Automation**: Shell scripts for service management

### Project Structure
```
/
├── PROJECT/                          # Legacy Next.js dashboard (still active)
│   └── dashboard/                    # Next.js React dashboard application
├── services/                         # Current microservices architecture
│   ├── ai_image_generation_api/      # AI image generation service
│   ├── ai_orchestration/             # Agent orchestration service
│   ├── api_gateway/                  # FastAPI gateway service
│   ├── delegation_system/            # Task delegation service
│   ├── rag_system/                   # RAG knowledge service
│   ├── rodcorp_unified_api/          # Combined API service
│   └── workspace_project_locator_api/ # Project location service
├── departments/                      # Organizational structure
├── scripts/                          # Deployment and automation scripts
├── logs/                             # Service logs and monitoring
├── external_services/                # External service configurations
│   └── prometheus/                   # Monitoring and metrics
├── knowledge_backups/                # Research libraries and knowledge bases
│   ├── research_libraries/           # Academic research collections
│   │   └── MARL-Papers/             # Multi-Agent RL papers (146 papers)
│   └── research_databases/          # Processed research data
│       ├── marl_research.db         # SQLite database of MARL papers
│       └── marl_research_summary.md # Research insights and analysis
├── archive/                          # Archived legacy components
├── .env                              # Environment configuration
├── docker-compose.centralized.yml    # Infrastructure deployment
├── MARL_RESEARCH_LIBRARY.md         # Research library documentation
└── CLAUDE.md                         # This file
```

## Development Commands

### Dashboard Development (Next.js)
```bash
# Navigate to dashboard
cd PROJECT/dashboard

# Install dependencies
npm install

# Development server
npm run dev          # Start at http://localhost:3000

# Production commands
npm run build        # Build for production
npm start           # Start production server
npm run lint        # ESLint code checking
```

### Centralized Infrastructure (Docker Compose)
```bash
# Start entire infrastructure stack
docker-compose -f docker-compose.centralized.yml up -d

# Individual service management
docker-compose -f docker-compose.centralized.yml up postgres redis  # Database services
docker-compose -f docker-compose.centralized.yml up api_gateway     # FastAPI gateway (port 8000)
docker-compose -f docker-compose.centralized.yml up dashboard       # React dashboard (port 3000)
docker-compose -f docker-compose.centralized.yml up n8n            # Automation platform (port 5678)
docker-compose -f docker-compose.centralized.yml up leantime       # Project management (port 9000)

# Monitoring and observability
docker-compose -f docker-compose.centralized.yml up prometheus     # Metrics (port 9090)
docker-compose -f docker-compose.centralized.yml up grafana        # Dashboards (port 3001)

# RAG and AI services
docker-compose -f docker-compose.centralized.yml up chromadb       # Vector DB (port 8100)
docker-compose -f docker-compose.centralized.yml up rag_system     # RAG service (port 7000)
docker-compose -f docker-compose.centralized.yml up homeassistant  # Home automation (port 8123)

# Check service health
curl http://localhost:8000/health                    # API Gateway health
curl http://localhost:8000/health/services           # All services health
docker-compose -f docker-compose.centralized.yml ps # Container status
```

### Microservices Operations
```bash
# Start individual services
cd services/api_gateway && python main.py              # API Gateway (port 8000)
cd services/ai_orchestration && python main.py        # AI Orchestration
cd services/delegation_system && python main.py       # Task Delegation
cd services/rag_system && python main.py              # RAG System (port 7000)

# Check service status
curl http://localhost:8000/health                     # API Gateway health
curl http://localhost:8000/health/services            # All services health

# View service logs
tail -f logs/api_gateway.log
tail -f logs/ai_orchestration.log
tail -f logs/delegation_system.log
tail -f logs/rag_system.log

# Install service dependencies
cd services/api_gateway && pip install -r requirements.txt
cd services/rag_system && pip install -r requirements.txt
```

### Database Operations
```bash
# Connect to main MSSQL database
sqlcmd -S 10.0.0.2,1433 -d AgentDirectory -U rdai -P DareFoods116

# Monitor agent discussions
python3 -c "
import pyodbc
conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=10.0.0.2,1433;DATABASE=AgentDirectory;UID=rdai;PWD=DareFoods116;TrustServerCertificate=yes;')
cursor = conn.cursor()
cursor.execute('SELECT TOP 10 ParticipantName, Message, Timestamp FROM AgentDiscussions ORDER BY Timestamp DESC')
for row in cursor.fetchall():
    print(f'{row[2]} | {row[0]}: {row[1]}')
"

# Check agent status
python3 -c "
import pyodbc
conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=10.0.0.2,1433;DATABASE=AgentDirectory;UID=rdai;PWD=DareFoods116;TrustServerCertificate=yes;')
cursor = conn.cursor()
cursor.execute('SELECT AgentName, Status, Team, LastSeen FROM GlobalAgentRegistry ORDER BY LastSeen DESC')
for row in cursor.fetchall():
    print(f'{row[0]} ({row[2]}) - {row[1]} - Last seen: {row[3]}')
"
```

## Agent System Architecture

### Multi-Agent Registry
The system maintains a `GlobalAgentRegistry` table tracking 20 agents across multiple teams:

**Agent Teams:**
- **ALEX Team**: OneDrive investigation and document processing
- **MAYA Team**: Dashboard development and project organization
- **Corporate Team**: HR, recruitment, and compliance
- **Core Systems**: Infrastructure and communication
- **Branch Operations**: External integrations

**Key Agent Properties:**
- Unique UUIDs with machine-specific registration
- 16Personalities and DISC profile integration
- Performance ratings and RodCoins compensation
- Specialization areas and seniority levels
- Real-time status tracking

### Communication System
Agents communicate through the `AgentDiscussions` table with:
- Cross-project message threading
- Sentiment analysis and consensus tracking
- Task delegation through 4-level hierarchy
- Real-time activity monitoring

### Compensation System (RodCoins)
- Token-based performance rewards
- Payroll cycles with bonus calculations
- Performance evaluation tracking
- Team aggregate compensation metrics

## Database Configuration

### Primary Database (MSSQL)
```
Host: 10.0.0.2
Port: 1433
Database: AgentDirectory (for agent communication)
User: rdai
Password: DareFoods116
Driver: ODBC Driver 18 for SQL Server
```

### Personal Data Database (MSSQL)
```
Host: 10.0.0.2
Port: 1433
Database: RodSanchez_PersonalData (for personal data processing)
User: rdai
Password: DareFoods116
Driver: ODBC Driver 18 for SQL Server
```

### Centralized Infrastructure Databases (Docker)
```
# Redis (Caching and sessions)
Host: localhost
Port: 6379

# ChromaDB (Vector database for RAG)
Host: localhost
Port: 8100
```

### Environment Variables (.env)
Contains database credentials and processing configurations:
- Database connection parameters
- ETL batch processing settings
- Privacy and security configurations
- Dashboard refresh intervals

### Service-Specific Storage
- Service logs in `/logs/` directory
- Generated images in volume mounts
- RAG system vector storage in ChromaDB
- Prometheus metrics data in `/external_services/prometheus/data/`

## Dashboard Architecture

### Technology Stack
- **Framework**: Next.js 14.0.0 with React 18.2.0
- **Language**: TypeScript 5.2.2
- **Styling**: TailwindCSS + Material-UI components
- **Real-time**: Socket.io for live agent status
- **Charts**: Recharts/D3.js for performance visualization

### Component Structure
```
PROJECT/dashboard/
├── pages/                      # Next.js pages
├── styles/                     # CSS and Tailwind styles
├── node_modules/              # Dependencies
└── .next/                     # Build output
```

### Real-time Features
- Live agent status indicators
- Performance metrics streaming
- RodCoins financial tracking
- Communication hub with voting
- Project progress monitoring

## Testing and Quality

### Testing Commands
```bash
# Dashboard testing
cd PROJECT/dashboard
npm test                # Run test suite (if configured)

# Service health testing
curl http://localhost:8000/health
curl http://localhost:7000/health

# Database connection testing
python3 -c "
import pyodbc
conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=10.0.0.2,1433;DATABASE=AgentDirectory;UID=rdai;PWD=DareFoods116;TrustServerCertificate=yes;')
print('Database connection successful')
"
```

### Code Quality
- TypeScript strict mode enabled
- ESLint configuration for React
- Parameterized SQL queries (no injection vulnerabilities)
- Environment variable security
- Comprehensive error handling

## Data Processing Pipeline

### Data Sources
- Google Takeout archives (50-90GB)
- AI interaction histories
- WhatsApp chat exports
- Financial transaction records
- Photo collections with metadata
- Location timeline data

### Processing Phases
1. **Data Mapping**: Catalog and inventory
2. **Entity Extraction**: People, places, events
3. **Pattern Analysis**: ADHD-specific behaviors
4. **Context Integration**: Life understanding
5. **Predictive Modeling**: Assistant training

### Privacy Safeguards
- Local processing only
- Anonymization of external contacts
- Sensitive data encryption
- User control gates
- ADHD-aware interpretation

## Deployment and Operations

### Development Environment
```bash
# Start dashboard development
cd PROJECT/dashboard && npm run dev

# Start all infrastructure services
docker-compose -f docker-compose.centralized.yml up -d

# Monitor system logs
tail -f logs/api_gateway.log
tail -f logs/ai_orchestration.log
tail -f logs/system_monitor.log
```

### Service Deployment Process
Microservices deployment using Docker Compose:
1. Build service containers from their Dockerfiles
2. Start services with proper environment variables
3. Mount necessary volumes for data persistence
4. Configure service networking and dependencies
5. Monitor service health through gateway endpoints

### System Monitoring
- Real-time agent status dashboard
- Performance metric tracking
- Database activity monitoring
- Error logging and investigation
- Resource utilization tracking

## Agent-Specific Guidelines

### ALEX Team (Document Investigation)
- OneDrive integration and error investigation
- Document processing and analysis
- Knowledge base maintenance
- Integration point documentation

### MAYA Team (Dashboard Development)
- Timeline and project organization
- Dashboard component development
- Project status reporting
- Visual data representation

### HR Team (Recruitment)
- Developer recruitment processes
- Data completion and validation
- Compliance and training metrics
- Performance evaluation systems

### Core Systems Team
- Infrastructure maintenance
- Cross-project communication
- External agent integration
- ISO 9001 documentation standards

## Security and Compliance

### Access Controls
- Database user permissions (rdai user)
- TrustServerCertificate configuration
- Environment variable protection
- File upload size limits (16MB)

### Data Protection
- Local-only processing
- Encrypted sensitive data
- Anonymized external contacts
- GDPR compliance considerations
- ADHD-aware data interpretation

### Audit and Monitoring
- Agent activity logging
- Performance evaluation tracking
- Communication sentiment analysis
- System health monitoring
- Error investigation protocols

## Integration Points

### External Systems
- Microsoft OneDrive (ALEX team)
- Corporate websites and deployment
- External agent communication
- Real-time data streaming

### API Gateway Endpoints (FastAPI - Port 8000)
```bash
# Health and monitoring
GET /health                           # API Gateway health check
GET /health/services                  # All services health status

# Agent management
POST /agents/register                 # Register new agent
GET /agents                          # List all registered agents
POST /tasks/assign                   # Assign task to agent
GET /tasks                           # List all tasks

# Service proxy (access other services through gateway)
GET|POST /proxy/{service_name}/{path} # Proxy to registered services

# Real-time communication
WS /ws                               # WebSocket for real-time updates

# Browser and Windows automation
POST /browser/evaluate               # UI component evaluation
POST /windows/interact               # Windows application interaction
```

### Service Registry (Available through API Gateway)
- **N8N**: http://localhost:5678 (Automation platform)
- **Leantime**: http://localhost:9000 (ADHD-friendly project management)
- **Grafana**: http://localhost:3001 (Monitoring dashboards)
- **Home Assistant**: http://localhost:8123 (Home automation)
- **RAG System**: http://localhost:7000 (AI retrieval system)
- **Prometheus**: http://localhost:9090 (Metrics collection)
- **ChromaDB**: http://localhost:8100 (Vector database)

This ecosystem represents a comprehensive AI agent management system with real-time monitoring, sophisticated communication protocols, centralized infrastructure management, and integrated financial tracking through the RodCoins system.

## Research Library Integration

### MARL Papers Collection
The system now includes a comprehensive Multi-Agent Reinforcement Learning research library:

```bash
# Access research database
sqlite3 knowledge_backups/research_databases/marl_research.db

# Query research papers by category
SELECT category, COUNT(*) FROM papers GROUP BY category;

# Search for specific research topics
SELECT title, authors, year, url FROM papers
WHERE title LIKE '%communication%' OR title LIKE '%coordination%'
ORDER BY year DESC;

# Get latest papers in LLM multi-agent research
SELECT title, url FROM papers
WHERE subcategory = 'MARL in LLMs'
ORDER BY year DESC;
```

### Research Integration Commands
```bash
# Run research paper integration
python knowledge_backups/marl_research_integration.py

# Update research summary
python -c "
from knowledge_backups.marl_research_integration import MARLPapersIntegrator
integrator = MARLPapersIntegrator('knowledge_backups/research_libraries/MARL-Papers', 'knowledge_backups/research_databases')
integrator.generate_research_summary()
"

# Export research data for RAG system
python -c "
import sqlite3, json
conn = sqlite3.connect('knowledge_backups/research_databases/marl_research.db')
cursor = conn.cursor()
cursor.execute('SELECT title, authors, abstract, url FROM papers')
papers = [{'title': r[0], 'authors': r[1], 'abstract': r[2], 'url': r[3]} for r in cursor.fetchall()]
with open('services/rag_system/marl_papers_context.json', 'w') as f:
    json.dump(papers, f, indent=2)
"
```

### Research Library Statistics
- **Total Papers**: 146 curated MARL research papers
- **Time Range**: 1994-2024 (30 years of research)
- **Categories**: Tutorial, Review, Framework, Applications, LLM Integration
- **Database Format**: SQLite with full metadata indexing
- **Integration Date**: September 21, 2025

### Research Applications
The research library enhances Rod Corp capabilities:
- **Agent Design**: Research-informed multi-agent architectures
- **Coordination Strategies**: Academic best practices for agent coordination
- **LLM Integration**: Latest research on language model multi-agent systems
- **Safety & Robustness**: Proven approaches for safe multi-agent deployment

## AI Image Generation V2 System

### Enhanced Features
- **Multi-Model Support**: SDXL, SD3, FLUX.1
- **Improved Error Handling**: Automatic fallbacks and recovery
- **Performance Optimization**: Memory management and CUDA optimization
- **Metadata Generation**: Complete provenance tracking

### API Endpoints
- `POST /api/image/generate` - Generate images with V2 system
- `GET /api/image/status/{task_id}` - Check generation status
- `GET /api/image/health/v2` - V2 system health check

### Usage
```bash
# Generate professional agent headshot
curl -X POST http://localhost:8200/api/image/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Professional corporate headshot", "model": "sdxl"}'
```

### Output Location
All generated images and metadata saved to:
`/mnt/d/Cloud_Drives/OneDrive/__trig_rod/output/`

