# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

Rod-Corp Next-Gen is a high-performance multi-agent AI ecosystem that replaces a legacy MSSQL-bottlenecked system with a distributed, GPU-accelerated architecture. The system coordinates 48+ specialized AI agents with <2 second response times, leveraging RTX 4090 for local LLM inference.

## Core Architecture

### System Layers
1. **Security Layer**: Zero-trust architecture with HashiCorp Vault, JWT authentication, and network segmentation
2. **Agent Coordination Layer**: Redis-based agent registry, priority task queue, and Kafka/Redis event bus
3. **GPU Acceleration Layer**: Local LLM inference engine optimized for RTX 4090 with CUDA kernels
4. **Knowledge Management Layer**: Vector search (Weaviate), agent memory systems, real-time synchronization
5. **Data Layer**: PostgreSQL+Citus (distributed), Weaviate (vectors), InfluxDB (metrics)

### Key Components

#### Agent Orchestrator (`agent-coordination/agent_orchestrator.py`)
- FastAPI-based REST API on port 8000
- Manages agent lifecycle, task distribution, and load balancing
- Priority-based task queue with intelligent agent selection
- Real-time event bus for inter-agent communication

#### Security Manager (`security/security_manager.py`)
- HashiCorp Vault integration for secrets management
- JWT-based authentication with role-based access control (RBAC)
- Zero-trust network architecture with 6 security zones
- Automatic credential rotation and audit logging

#### GPU Engine (`gpu-acceleration/local_llm_engine.py`)
- Local inference for Llama, Mistral, Qwen, DeepSeek models
- 4-bit/8-bit quantization for memory efficiency
- Dynamic model loading/unloading with memory management
- CUDA-accelerated processing for parallel agent execution

#### System Startup (`deployment/startup.py`)
- Orchestrates complete system initialization
- Health monitoring with automatic recovery
- Component lifecycle management
- Graceful shutdown procedures

## Common Commands

### System Management
```bash
# Start complete system (requires Docker)
cd /mnt/c/_rod/_rodcorp_2_/new-rod-corp
python3 deployment/startup.py

# Start infrastructure services
cd infrastructure && docker-compose up -d

# Stop all services
cd infrastructure && docker-compose down

# Check system health
curl http://localhost:8000/system/health
```

### Individual Component Testing
```bash
# Run agent orchestrator standalone
python3 agent-coordination/agent_orchestrator.py

# Test GPU engine
python3 gpu-acceleration/local_llm_engine.py

# Initialize security system
python3 security/security_manager.py
```

### Docker Operations
```bash
# View running containers
docker ps

# Check logs
docker-compose logs -f [service_name]

# Restart a service
docker-compose restart [service_name]

# Clean up volumes
docker-compose down -v
```

### Database Access
```bash
# Connect to PostgreSQL
psql -h localhost -U rod_corp_user -d rod_corp_db

# Access Redis CLI
redis-cli

# Query Weaviate
curl http://localhost:8080/v1/schema
```

### Agent Management
```python
# Register new agent via API
curl -X POST http://localhost:8000/agents/register \
  -H "Content-Type: application/json" \
  -d '{"name": "test-agent", "type": "specialist", "capabilities": {"nlp": true}}'

# Submit task
curl -X POST http://localhost:8000/tasks/create \
  -H "Content-Type: application/json" \
  -d '{"title": "Test task", "description": "Test", "priority": 3}'
```

### Monitoring
```bash
# Access Grafana dashboard
open http://localhost:3000  # admin/[GRAFANA_PASSWORD]

# View Prometheus metrics
open http://localhost:9090

# Check Vault UI
open http://localhost:8200  # Use VAULT_TOKEN
```

## Environment Configuration

### Required Environment Variables
```bash
# Copy template and edit
cp infrastructure/.env.template infrastructure/.env

# Critical settings:
POSTGRES_PASSWORD       # PostgreSQL password
VAULT_TOKEN            # HashiCorp Vault root token
JWT_SECRET_KEY         # JWT signing key (256 bits minimum)
GRAFANA_PASSWORD       # Grafana admin password
CUDA_VISIBLE_DEVICES   # GPU device ID (usually 0)
```

### Configuration Files
- `config/system_config.yaml`: System startup configuration
- `infrastructure/docker-compose.yml`: Service definitions
- `infrastructure/sql/init.sql`: Database schema

## Development Workflow

### Adding New Agents
1. Implement agent logic following the Agent base class pattern
2. Register capabilities in agent configuration
3. Add to `startup_order` in system_config.yaml
4. Test with `python3 deployment/startup.py`

### Modifying Task Processing
Task flow: Submit → Queue → Load Balancer → Agent Selection → Assignment → Processing → Completion
Key files: `agent_orchestrator.py` (TaskQueue, LoadBalancer classes)

### GPU Model Integration
1. Add model config to `ModelManager._setup_default_configs()` in local_llm_engine.py
2. Specify quantization level (4-bit/8-bit) and memory requirements
3. Test with `engine.generate_text()` method

### Security Changes
All credential operations must go through Vault. Never hardcode secrets.
Authentication flow: Agent → JWT token → RBAC check → Resource access

## Performance Optimization

### Database Queries
- All tables are distributed via Citus for horizontal scaling
- Use appropriate indexes (already defined in init.sql)
- Monitor slow queries via Grafana dashboard

### GPU Memory Management
- Models auto-unload based on LRU when memory needed
- Adjust `GPU_MEMORY_FRACTION` in .env if OOM errors occur
- Monitor via `nvidia-smi` or performance metrics API

### Agent Coordination
- Tasks are priority-ordered (1=critical, 5=background)
- Load balancer scores agents based on capabilities, performance, and resource usage
- Busy agents can be interrupted for critical tasks

## API Endpoints

### Agent Orchestrator (Port 8000)
- POST `/agents/register` - Register new agent
- GET `/agents/{agent_id}` - Get agent details
- POST `/tasks/create` - Submit new task
- PUT `/tasks/{task_id}` - Update task status
- GET `/system/health` - System health check

### Security Manager (Port 8001)
- POST `/auth/login` - Authenticate agent
- POST `/auth/refresh` - Refresh JWT token
- GET `/security/audit` - Audit logs

## Troubleshooting

### Docker Issues
If services won't start, check: Docker daemon running, port conflicts, disk space, .env file values

### GPU Errors
For CUDA errors: Check driver version (≥12.0), GPU memory with nvidia-smi, CUDA_VISIBLE_DEVICES setting

### Database Connection
Connection failures: Verify PostgreSQL is running, check credentials in .env, ensure network connectivity

### Agent Registration
If agents can't register: Check orchestrator health, verify Redis connection, review agent capabilities format

## Migration from Legacy

Legacy agents in `/legacy/rod-corp/agents/profiles/` can be migrated by:
1. Extracting capabilities from config.json files
2. Converting to new Agent registration format
3. Registering via orchestrator API

Key differences from legacy:
- Database: MSSQL → PostgreSQL+Citus
- Communication: Polling → Event-driven
- Inference: Cloud APIs → Local GPU
- Security: Basic auth → Zero-trust + JWT