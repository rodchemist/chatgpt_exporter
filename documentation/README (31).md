# Rod-Corp Agent Coordination Framework

A production-ready multi-agent coordination system that replaces the legacy MSSQL-based approach with a distributed, scalable architecture capable of coordinating 48+ specialized agents.

## 🚀 Features

### Core Capabilities
- **Agent Registry & Discovery**: Centralized agent registration with automatic discovery and health tracking
- **Task Queue & Distribution**: Priority-based task queuing with intelligent distribution and load balancing
- **Real-time Messaging**: WebSocket-based event bus for instant agent communication and coordination
- **State Management**: Comprehensive agent state tracking with performance metrics and health monitoring
- **Load Balancing**: Adaptive load balancing with auto-scaling capabilities based on system load
- **Legacy Integration**: Seamless integration with existing agent profiles (claude-full, qwen-full, etc.)

### Advanced Features
- **Health Monitoring**: Automated health checks with alert notifications and recovery actions
- **RESTful API**: Complete REST API for external integration and management
- **Fault Tolerance**: Built-in recovery mechanisms and failover capabilities
- **Performance Monitoring**: Real-time metrics collection and analysis
- **Auto-scaling**: Dynamic agent spawning based on workload demands

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     Rod-Corp Coordination Framework             │
├─────────────────────────────────────────────────────────────────┤
│  REST API Layer (FastAPI)                                      │
├─────────────────────────────────────────────────────────────────┤
│  Core Components:                                               │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐│
│  │   Agent     │ │    Task     │ │   Event     │ │   State     ││
│  │  Registry   │ │   Queue     │ │    Bus      │ │  Manager    ││
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘│
├─────────────────────────────────────────────────────────────────┤
│  Supporting Services:                                           │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐               │
│  │    Load     │ │   Health    │ │   Legacy    │               │
│  │  Balancer   │ │  Monitor    │ │ Integration │               │
│  └─────────────┘ └─────────────┘ └─────────────┘               │
├─────────────────────────────────────────────────────────────────┤
│  Infrastructure Layer:                                         │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐               │
│  │    Redis    │ │  WebSocket  │ │   Message   │               │
│  │  Cluster    │ │   Server    │ │   Queues    │               │
│  └─────────────┘ └─────────────┘ └─────────────┘               │
└─────────────────────────────────────────────────────────────────┘
```

## 📦 Installation

### Prerequisites
- Python 3.8+
- Redis 6.0+
- Linux/Windows/macOS

### Quick Install
```bash
# Clone the repository
git clone https://github.com/rod-corp/agent-coordination-framework.git
cd agent-coordination-framework

# Install dependencies
pip install -r requirements.txt

# Start Redis (if not already running)
redis-server

# Initialize the framework
python -c "
import asyncio
from agent_coordination_framework import CoordinationFramework

async def init():
    framework = CoordinationFramework()
    await framework.initialize()
    print('Framework initialized successfully!')
    await framework.close()

asyncio.run(init())
"
```

## 🔧 Quick Start

### Basic Usage

```python
import asyncio
from agent_coordination_framework import CoordinationFramework, AgentProfile, Task

async def main():
    # Initialize framework
    framework = CoordinationFramework()
    await framework.initialize()

    # Register an agent
    agent = AgentProfile(
        agent_id="agent-001",
        name="claude-analyst",
        type="claude",
        capabilities=["analysis", "leadership"],
        specialization="data_analysis",
        max_concurrent_tasks=5,
        base_url="http://localhost:8080"
    )

    await framework.registry.register_agent(agent)

    # Submit a task
    task = Task(
        task_type="analysis",
        title="Analyze Q4 Performance",
        description="Comprehensive analysis of Q4 metrics",
        required_capabilities=["analysis"],
        payload={"data_source": "quarterly_reports"}
    )

    task_id = await framework.task_queue.submit_task(task)
    print(f"Task submitted: {task_id}")

    # Check system status
    status = await framework.get_status()
    print(f"System status: {status['framework']['status']}")

    await framework.close()

asyncio.run(main())
```

### Legacy Agent Integration

```python
# Auto-register all legacy agent profiles
async def setup_legacy_agents():
    framework = CoordinationFramework()
    await framework.initialize()

    # Automatically discover and register legacy agents
    count = await framework.auto_setup_legacy_agents()
    print(f"Registered {count} legacy agents")

    # Get legacy agent status
    status = await framework.legacy_manager.get_legacy_agent_status()
    print(f"Running legacy agents: {status['running_agents']}")

    await framework.close()
```

### REST API Server

```python
from agent_coordination_framework.api import run_api_server

# Start the REST API server
run_api_server(host="0.0.0.0", port=8000)
```

## 📚 API Documentation

### REST API Endpoints

The framework provides a comprehensive REST API for external integration:

- **Agent Management**: `/agents/*` - Register, list, update, and remove agents
- **Task Management**: `/tasks/*` - Submit, track, and manage tasks
- **Health Monitoring**: `/health`, `/status` - System health and status
- **Legacy Integration**: `/legacy/*` - Manage legacy agent profiles
- **Event Publishing**: `/events/*` - Publish and manage events

Complete API documentation is available at `/docs` when running the API server.

### WebSocket API

Real-time communication via WebSocket:

```javascript
// Connect to event bus
const ws = new WebSocket('ws://localhost:8765');

// Authenticate
ws.send(JSON.stringify({
    type: 'auth',
    agent_id: 'your-agent-id'
}));

// Subscribe to events
ws.send(JSON.stringify({
    type: 'subscribe',
    event_types: ['task.assigned', 'agent.status_changed']
}));
```

## 🔧 Configuration

### Environment Variables

```bash
# Redis Configuration
REDIS_URL=redis://localhost:6379

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000

# WebSocket Configuration
WS_HOST=localhost
WS_PORT=8765

# Health Monitoring
HEALTH_CHECK_INTERVAL=60
ALERT_EMAIL_SMTP=smtp.example.com
ALERT_EMAIL_FROM=alerts@rod-corp.com
```

### Legacy Agent Profiles

The framework automatically discovers legacy agent profiles from:
```
/mnt/c/_rod/_rodcorp_2_/legacy/rod-corp/agents/profiles/
├── claude-full/
├── qwen-full/
├── codex-full/
├── gemini-full/
├── code-review-specialist/
└── rag-documentation-specialist/
```

## 📊 Monitoring & Observability

### Health Dashboard

Access the health dashboard at: `http://localhost:8000/health`

### Key Metrics
- **Agent Health**: Availability, response times, error rates
- **Task Metrics**: Queue depth, processing times, success rates
- **System Resources**: CPU, memory, disk usage
- **Network Performance**: Connection counts, throughput

### Alerts & Notifications

Configure alerts via REST API:
```python
await framework.health_monitor.configure_notifications(
    email_config={
        "smtp_server": "smtp.example.com",
        "username": "alerts@rod-corp.com",
        "password": "password",
        "to_emails": ["admin@rod-corp.com"]
    },
    webhook_urls=["https://hooks.slack.com/..."]
)
```

## 🚀 Deployment

### Production Deployment

1. **Redis Cluster Setup**:
```bash
# Configure Redis cluster for high availability
redis-sentinel redis.conf
```

2. **Load Balancer Configuration**:
```python
# Configure load balancing rules
await framework.load_balancer.register_balancing_rule(
    LoadBalancingRule(
        name="high_priority_tasks",
        strategy=LoadBalancingStrategy.PERFORMANCE_BASED,
        capability_requirements=["analysis"],
        priority_threshold=2
    )
)
```

3. **Auto-scaling Setup**:
```python
# Configure auto-scaling rules
await framework.load_balancer.register_scaling_rule(
    ScalingRule(
        name="cpu_based_scaling",
        trigger_metric=ResourceMetric.CPU_USAGE,
        scale_up_threshold=80.0,
        scale_down_threshold=30.0,
        min_agents=2,
        max_agents=20
    )
)
```

### Docker Deployment

```dockerfile
FROM python:3.11-slim

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8000 8765

CMD ["python", "-m", "agent_coordination_framework.api.rest_api"]
```

## 🧪 Testing

### Run Tests
```bash
# Unit tests
pytest tests/

# Integration tests
pytest tests/integration/

# Load tests
pytest tests/load/
```

### Example Test
```python
import pytest
from agent_coordination_framework import CoordinationFramework

@pytest.mark.asyncio
async def test_agent_registration():
    framework = CoordinationFramework()
    await framework.initialize()

    # Test agent registration
    agent = create_test_agent()
    success = await framework.registry.register_agent(agent)
    assert success

    # Verify agent is registered
    retrieved = await framework.registry.get_agent(agent.agent_id)
    assert retrieved.name == agent.name

    await framework.close()
```

## 🤝 Contributing

### Development Setup
```bash
# Clone repository
git clone https://github.com/rod-corp/agent-coordination-framework.git
cd agent-coordination-framework

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install development dependencies
pip install -r requirements.txt
pip install -e .

# Run pre-commit hooks
pre-commit install
```

### Code Standards
- **Black** for code formatting
- **Flake8** for linting
- **MyPy** for type checking
- **Pytest** for testing

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Documentation**: [https://docs.rod-corp.com/coordination-framework](https://docs.rod-corp.com/coordination-framework)
- **Issues**: [GitHub Issues](https://github.com/rod-corp/agent-coordination-framework/issues)
- **Discussions**: [GitHub Discussions](https://github.com/rod-corp/agent-coordination-framework/discussions)
- **Email**: dev@rod-corp.com

## 🗺️ Roadmap

### v1.1 (Q2 2024)
- [ ] Machine Learning-based load prediction
- [ ] Advanced agent orchestration patterns
- [ ] Enhanced security features
- [ ] Performance optimizations

### v1.2 (Q3 2024)
- [ ] Multi-region deployment support
- [ ] Advanced analytics dashboard
- [ ] Plugin architecture
- [ ] Integration with external ML platforms

### v2.0 (Q4 2024)
- [ ] Kubernetes operator
- [ ] Service mesh integration
- [ ] Advanced governance features
- [ ] Enterprise security enhancements

---

**Rod-Corp Agent Coordination Framework** - Empowering intelligent multi-agent systems at scale.