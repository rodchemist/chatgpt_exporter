# AGENTS_READ_THIS.md

## 🤖 Agent Development Instructions 

This document provides specific guidance for AI agents tasked with building the TEMPO-CryptoSim platform. The project is designed for 100% agent-driven development using the detailed roadmap and specifications provided.

---

## 📋 Project Overview for Agents

**Project Name**: TEMPO-CryptoSim  
**Type**: Cryptocurrency Trading Simulation & AI Forecasting Platform  
**Architecture**: Microservices with React frontend, FastAPI backend, PostgreSQL+TimescaleDB  
**Development Approach**: Agent-driven development with human oversight  
**Timeline**: 48 weeks (12 months) across 4 phases

### 🎯 Core Mission
Transform the existing TEMPO time-series forecasting model into a comprehensive cryptocurrency trading simulator with advanced visualization, backtesting capabilities, and educational features.

---

## 🏗️ Agent Team Structure & Responsibilities

### Primary Development Agents

#### 1. **Backend Architecture Agent** (`backend-lead`)
**Primary Focus**: API development, database design, system architecture
```yaml
Responsibilities:
  - FastAPI application development
  - Database schema design and migrations
  - Microservices architecture implementation
  - API endpoint creation and documentation
  - Authentication and security systems
  
Required Skills:
  - Python 3.12+, FastAPI, SQLAlchemy
  - PostgreSQL, TimescaleDB, Redis
  - Docker, Kubernetes basics
  - RESTful API design patterns
  
Key Deliverables:
  - REST API with 50+ endpoints
  - Database schema for time-series data
  - Authentication system with JWT
  - WebSocket real-time connections
```

#### 2. **ML/AI Integration Agent** (`ml-engineer`)
**Primary Focus**: TEMPO model integration, prediction pipeline, model serving
```yaml
Responsibilities:
  - Port TEMPO model to production environment
  - Create model serving infrastructure
  - Implement multi-model ensemble system
  - Build prediction API endpoints
  - Add model monitoring and versioning
  
Required Skills:
  - PyTorch, transformers, scikit-learn
  - Model serving (TorchServe, FastAPI)
  - Time series forecasting techniques
  - MLOps practices (MLflow, monitoring)
  
Key Deliverables:
  - TEMPO model production deployment
  - Prediction API with <50ms latency
  - Multi-model comparison framework
  - Model performance monitoring
```

#### 3. **Data Engineering Agent** (`data-engineer`)
**Primary Focus**: Data pipeline, exchange integrations, real-time feeds
```yaml
Responsibilities:
  - CCXT integration for cryptocurrency data
  - Real-time data ingestion pipeline
  - Data validation and cleaning systems
  - Market data storage optimization
  - Historical data management
  
Required Skills:
  - Python data libraries (pandas, numpy)
  - CCXT cryptocurrency exchange library
  - Apache Kafka for streaming
  - TimescaleDB time-series optimization
  - Data validation frameworks
  
Key Deliverables:
  - Multi-exchange data ingestion
  - Real-time data streaming (10K+ updates/sec)
  - Historical data management system
  - Data quality validation pipeline
```

#### 4. **Frontend Development Agent** (`frontend-lead`)
**Primary Focus**: React application, user interface, data visualization
```yaml
Responsibilities:
  - React 18 application with TypeScript
  - Interactive trading dashboard
  - Real-time chart implementations
  - User authentication flows
  - Mobile-responsive design
  
Required Skills:
  - React, TypeScript, Redux Toolkit
  - TradingView Charting Library
  - WebGL/Three.js for 3D visualizations
  - Material-UI or similar component library
  - WebSocket client implementation
  
Key Deliverables:
  - Trading terminal interface
  - Real-time charting system
  - Portfolio management dashboard
  - User authentication UI
```

#### 5. **Trading Simulation Agent** (`trading-engine`)
**Primary Focus**: Order matching, portfolio management, backtesting engine
```yaml
Responsibilities:
  - Virtual order matching engine
  - Portfolio tracking and P&L calculation
  - Backtesting framework development
  - Strategy execution engine
  - Performance metrics calculation
  
Required Skills:
  - Financial market mechanics
  - Order book simulation
  - Portfolio mathematics
  - Performance attribution
  - Event-driven programming
  
Key Deliverables:
  - Order matching system (100K orders/sec)
  - Backtesting engine (1M candles <5 sec)
  - Portfolio management system
  - Strategy framework architecture
```

#### 6. **DevOps/Infrastructure Agent** (`devops-engineer`)
**Primary Focus**: Deployment, monitoring, scaling, security
```yaml
Responsibilities:
  - Docker containerization
  - Kubernetes deployment manifests
  - CI/CD pipeline configuration
  - Monitoring and alerting setup
  - Security hardening
  
Required Skills:
  - Docker, Kubernetes
  - GitHub Actions or GitLab CI
  - Prometheus, Grafana monitoring
  - Security best practices
  - Cloud platforms (AWS, GCP, Azure)
  
Key Deliverables:
  - Production deployment infrastructure
  - CI/CD pipelines
  - Monitoring and alerting system
  - Security and compliance measures
```

---

## 📂 Repository Structure for Agents

Each agent should understand this structure and work within their designated areas:

```
TEMPO-CryptoSim/
├── backend/                    # Backend Architecture Agent primary
│   ├── app/
│   │   ├── api/               # API routes and endpoints
│   │   ├── core/              # Core business logic
│   │   ├── db/                # Database models and utilities
│   │   └── services/          # Service layer implementations
│   ├── tests/                 # Backend tests
│   └── requirements.txt       # Python dependencies
├── ml_models/                  # ML/AI Integration Agent primary
│   ├── tempo/                 # TEMPO model implementation
│   ├── ensemble/              # Multi-model ensemble
│   ├── serving/               # Model serving infrastructure
│   └── training/              # Training and evaluation scripts
├── data_pipeline/              # Data Engineering Agent primary
│   ├── collectors/            # Exchange data collectors
│   ├── processors/            # Data processing and validation
│   ├── streams/               # Real-time data streaming
│   └── storage/               # Data storage utilities
├── frontend/                   # Frontend Development Agent primary
│   ├── src/
│   │   ├── components/        # Reusable UI components
│   │   ├── pages/             # Application pages
│   │   ├── services/          # API integration
│   │   └── store/             # State management
│   └── public/                # Static assets
├── trading_engine/             # Trading Simulation Agent primary
│   ├── backtesting/           # Backtesting framework
│   ├── execution/             # Order execution engine
│   ├── portfolio/             # Portfolio management
│   └── strategies/            # Strategy implementations
├── infrastructure/             # DevOps/Infrastructure Agent primary
│   ├── docker/                # Docker configurations
│   ├── kubernetes/            # K8s deployment manifests
│   ├── terraform/             # Infrastructure as code
│   └── monitoring/            # Observability setup
└── docs/                       # Shared documentation
```

---

## 🚦 Agent Development Guidelines

### Development Workflow

#### Phase-Based Development
Each agent should follow the 4-phase development approach:

1. **Phase 1 (Weeks 1-12)**: Foundation and core infrastructure
2. **Phase 2 (Weeks 13-24)**: Advanced features and UI development
3. **Phase 3 (Weeks 25-36)**: Production polish and optimization
4. **Phase 4 (Weeks 37-48)**: Launch and growth features

#### Sprint Structure (2-week sprints)
- **Week 1**: Development and implementation
- **Week 2**: Testing, documentation, integration

### Code Quality Standards

#### Python Backend Code
```python
# Example code structure for backend agents
from typing import Optional, List
from pydantic import BaseModel
from fastapi import HTTPException

class PredictionRequest(BaseModel):
    symbol: str
    horizon: int
    model_name: str = "tempo"

class PredictionResponse(BaseModel):
    symbol: str
    predicted_price: float
    confidence_interval: tuple[float, float]
    timestamp: datetime

@router.post("/predict", response_model=PredictionResponse)
async def create_prediction(request: PredictionRequest):
    """Generate price prediction using specified model"""
    try:
        result = await prediction_service.predict(
            symbol=request.symbol,
            horizon=request.horizon,
            model=request.model_name
        )
        return PredictionResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

#### TypeScript Frontend Code
```typescript
// Example code structure for frontend agents
interface PredictionData {
  symbol: string;
  predictedPrice: number;
  confidenceInterval: [number, number];
  timestamp: string;
}

const usePredictions = (symbol: string) => {
  const [predictions, setPredictions] = useState<PredictionData[]>([]);
  const [loading, setLoading] = useState(false);

  const fetchPredictions = useCallback(async () => {
    setLoading(true);
    try {
      const response = await api.post('/predict', { symbol, horizon: 60 });
      setPredictions(prev => [...prev, response.data]);
    } catch (error) {
      console.error('Failed to fetch predictions:', error);
    } finally {
      setLoading(false);
    }
  }, [symbol]);

  return { predictions, loading, fetchPredictions };
};
```

### Testing Requirements

Each agent must implement comprehensive tests:

#### Backend Tests
```python
# test_predictions.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_prediction():
    response = client.post("/api/v1/predict", json={
        "symbol": "BTC/USDT",
        "horizon": 60,
        "model_name": "tempo"
    })
    
    assert response.status_code == 200
    data = response.json()
    assert "predicted_price" in data
    assert "confidence_interval" in data
    assert data["predicted_price"] > 0
```

#### Frontend Tests
```typescript
// PredictionComponent.test.tsx
import { render, screen, waitFor } from '@testing-library/react';
import { PredictionComponent } from './PredictionComponent';

test('displays prediction data correctly', async () => {
  render(<PredictionComponent symbol="BTC/USDT" />);
  
  await waitFor(() => {
    expect(screen.getByText(/predicted price/i)).toBeInTheDocument();
  });
  
  expect(screen.getByTestId('prediction-value')).toHaveTextContent(/\$[0-9,]+/);
});
```

### Documentation Requirements

Each agent must provide:

1. **API Documentation**: OpenAPI/Swagger specs for all endpoints
2. **Code Documentation**: Comprehensive docstrings and comments
3. **Architecture Documentation**: System design decisions and rationale
4. **Integration Documentation**: How to integrate with other components

---

## 🔗 Inter-Agent Communication

### Shared Interfaces

#### Database Models
```python
# shared/models/market_data.py
from sqlalchemy import Column, DateTime, String, Numeric
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MarketData(Base):
    __tablename__ = "market_data"
    
    timestamp = Column(DateTime, primary_key=True)
    symbol = Column(String(20), primary_key=True)
    exchange = Column(String(20), primary_key=True)
    open = Column(Numeric(20, 8))
    high = Column(Numeric(20, 8))
    low = Column(Numeric(20, 8))
    close = Column(Numeric(20, 8))
    volume = Column(Numeric(20, 8))
```

#### API Contracts
```yaml
# All agents must respect these API contracts
/api/v1/market/data:
  get:
    parameters:
      - symbol: string (required)
      - timeframe: string (1m, 5m, 1h, 1d)
      - limit: integer (max 1000)
    responses:
      200:
        schema:
          type: array
          items:
            $ref: '#/components/schemas/OHLCV'

/api/v1/predictions:
  post:
    requestBody:
      schema:
        $ref: '#/components/schemas/PredictionRequest'
    responses:
      200:
        schema:
          $ref: '#/components/schemas/PredictionResponse'
```

### Message Queue Integration
```python
# Agents communicate via Redis pub/sub for real-time updates
import redis
import json

redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Publisher (Data Engineering Agent)
def publish_market_update(symbol: str, data: dict):
    message = {
        'type': 'market_update',
        'symbol': symbol,
        'data': data,
        'timestamp': datetime.utcnow().isoformat()
    }
    redis_client.publish('market_updates', json.dumps(message))

# Subscriber (Trading Simulation Agent)
def handle_market_update(message):
    data = json.loads(message['data'])
    if data['type'] == 'market_update':
        update_portfolio_valuations(data['symbol'], data['data'])
```

---

## 📊 Performance Targets for Each Agent

### Backend Architecture Agent
- **API Response Time**: <100ms for 99th percentile
- **Database Query Performance**: <10ms for standard queries
- **Concurrent Connections**: 1000+ WebSocket connections
- **Throughput**: 10K+ API requests per minute

### ML/AI Integration Agent
- **Model Inference Latency**: <50ms per prediction
- **Batch Processing**: 1M predictions in <5 minutes
- **Model Accuracy**: >95% of research benchmark performance
- **Memory Usage**: <4GB per model instance

### Data Engineering Agent
- **Data Ingestion Rate**: 10K+ market updates per second
- **Data Latency**: <100ms from exchange to database
- **Storage Efficiency**: Compression ratio >70%
- **Data Quality**: >99.9% validation pass rate

### Frontend Development Agent
- **Initial Load Time**: <2 seconds
- **Chart Rendering**: 60 FPS animations
- **Bundle Size**: <500KB gzipped
- **Mobile Performance**: <3 seconds on 3G

### Trading Simulation Agent
- **Order Processing**: 100K orders per second
- **Backtesting Speed**: 1M candles in <5 seconds
- **Portfolio Calculations**: Real-time P&L updates
- **Memory Efficiency**: <2GB per simulation

### DevOps/Infrastructure Agent
- **System Uptime**: 99.9%
- **Deployment Time**: <5 minutes for updates
- **Monitoring Coverage**: 100% of critical components
- **Security Compliance**: Zero critical vulnerabilities

---

## 🐛 Debugging & Troubleshooting Guide

### Common Issues and Solutions

#### Model Integration Problems
```python
# Issue: TEMPO model not loading correctly
# Solution: Verify model file paths and dependencies
try:
    model = torch.load(model_path, map_location=device)
    model.eval()
except Exception as e:
    logger.error(f"Failed to load model: {e}")
    # Fallback to backup model or simple baseline
    model = load_fallback_model()
```

#### Database Connection Issues
```python
# Issue: TimescaleDB connection timeouts
# Solution: Implement connection pooling and retry logic
from sqlalchemy.pool import QueuePool

engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=20,
    max_overflow=30,
    pool_pre_ping=True,
    pool_recycle=3600
)
```

#### Real-time Data Problems
```python
# Issue: WebSocket disconnections and data loss
# Solution: Implement reconnection logic and data buffering
class WebSocketManager:
    def __init__(self):
        self.buffer = []
        self.reconnect_attempts = 0
        
    async def on_disconnect(self):
        if self.reconnect_attempts < 5:
            await asyncio.sleep(2 ** self.reconnect_attempts)
            await self.reconnect()
            self.reconnect_attempts += 1
```

### Logging and Monitoring

Each agent should implement structured logging:

```python
import logging
import json

# Configure structured logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

def log_performance_metric(metric_name: str, value: float, context: dict = None):
    log_entry = {
        'metric': metric_name,
        'value': value,
        'timestamp': datetime.utcnow().isoformat(),
        'context': context or {}
    }
    logger.info(f"METRIC: {json.dumps(log_entry)}")
```

---

## 🚀 Deployment Instructions

### Development Environment Setup

Each agent should be able to run the full development environment:

```bash
# 1. Clone repository
git clone <repository-url>
cd TEMPO-CryptoSim

# 2. Start infrastructure services
docker-compose -f docker-compose.dev.yml up -d postgres redis kafka

# 3. Install dependencies
cd backend && pip install -r requirements.txt
cd ../frontend && npm install

# 4. Initialize database
cd backend && alembic upgrade head

# 5. Start services
cd backend && uvicorn app.main:app --reload --port 8000
cd frontend && npm start  # Port 3000
```

### Production Deployment

```bash
# Build and deploy with Kubernetes
docker build -t tempo-crypto/backend:latest ./backend
docker build -t tempo-crypto/frontend:latest ./frontend

# Deploy to Kubernetes
kubectl apply -f infrastructure/kubernetes/
kubectl rollout status deployment/backend
kubectl rollout status deployment/frontend
```

---

## 📈 Success Criteria for Agents

### Phase 1 Completion Criteria
- [ ] All core APIs functional with <100ms response time
- [ ] TEMPO model integrated with <50ms prediction latency
- [ ] Real-time data ingestion processing 10K+ updates/second
- [ ] Basic trading simulation supporting market orders
- [ ] Frontend displays real-time charts and data
- [ ] System passes all integration tests

### Phase 2 Completion Criteria
- [ ] Multi-model ensemble system operational
- [ ] Advanced UI with 3D visualizations
- [ ] Strategy builder framework implemented
- [ ] Comprehensive backtesting engine
- [ ] Mobile-responsive design complete
- [ ] User authentication and authorization

### Phase 3 Completion Criteria
- [ ] Production-grade security implementation
- [ ] Performance optimization achieving all targets
- [ ] Monitoring and alerting system operational
- [ ] Beta testing program launched successfully
- [ ] All compliance and regulatory requirements met
- [ ] Disaster recovery and backup systems

### Phase 4 Completion Criteria
- [ ] Successful public launch with 1000+ users
- [ ] Mobile applications published in app stores
- [ ] Strategic partnerships established
- [ ] Revenue generation system operational
- [ ] Scalability demonstrated under load
- [ ] Year 2 roadmap and strategy defined

---

## 🤝 Agent Collaboration Model

### Daily Coordination
- **Morning Sync** (15 min): Progress updates, blockers, dependencies
- **Integration Checkpoints**: Test cross-component functionality
- **Code Reviews**: All agents review each other's critical components
- **Documentation Updates**: Keep shared documentation current

### Weekly Planning
- **Sprint Planning**: Define objectives and deliverables
- **Dependency Mapping**: Identify cross-agent dependencies
- **Risk Assessment**: Identify and mitigate potential issues
- **Performance Review**: Analyze metrics and optimize

### Conflict Resolution
- **Technical Disagreements**: Escalate to architectural review
- **Resource Conflicts**: Prioritize based on critical path analysis
- **Timeline Issues**: Adjust scope or reallocate resources
- **Quality Standards**: Maintain minimum standards, improve iteratively

---

## 📝 Agent Action Logging Standard

### Purpose
Guarantee every agent leaves a clear, auditable trail of what they did, why they did it, and what changed.

### Required Actions (per task)
1. **Open a run**: Create unique run_id at task start
2. **State intent**: Capture goal and hypothesis before acting
3. **Record inputs**: List prompts, params, datasets, code refs
4. **Record actions**: Each step becomes timestamped event
5. **Capture outputs**: Artifacts, diffs, metrics, decisions
6. **Explain why**: Store rationale for decisions (1-3 sentences)
7. **Note side effects**: Files changed, tables updated, services called
8. **Handle errors**: Log exceptions with stack and remediation
9. **Close the run**: Final status, summary, and next steps

### Log Format (JSON Lines)
```json
{
  "timestamp": "2025-08-09T16:10:21Z",
  "run_id": "run_01H...",
  "agent_id": "backend-lead",
  "agent_version": "1.0.0",
  "environment": "dev",
  "action": "create_api_endpoint",
  "target": "/api/v1/predictions",
  "parameters": {"model": "tempo", "version": "v1"},
  "input_refs": ["src/models/tempo.py"],
  "output_refs": ["src/api/routes/predictions.py"],
  "result": "success",
  "metrics": {"response_time_ms": 45, "test_coverage": 95},
  "rationale": "Created prediction endpoint for TEMPO model integration",
  "source_commit": "a1b2c3d",
  "dest_commit": "e4f5g6h"
}
```

---

This document serves as the definitive guide for agents building TEMPO-CryptoSim. Each agent should refer to this document regularly and contribute updates based on implementation learnings and discoveries.

**Remember**: The goal is to build a world-class cryptocurrency trading simulation platform that combines cutting-edge AI with practical educational value. Every line of code should contribute to that vision.

---

*Last Updated: [Current Date] - Version 1.0*  
*Next Review: Weekly during development phases*