# Rod-Corp Legacy System Migration Plan

## Migration Overview
Migrating functional Rod-Corp ecosystem from `~/rod-corp-legacy/` to `~/rod-corp/` while preserving all auto-logging and monitoring capabilities.

## Current Legacy System Analysis

### ✅ **Active Services** (Successfully Running)
- **API Gateway** (Port 18000): FastAPI-based central router
- **RAG System** (Port 17000): ChromaDB vector database + knowledge management
- **AI Orchestration** (Port 16000): Multi-agent coordination hub
- **Delegation System** (Port 15000): Task delegation engine
- **N8N Workflows** (Port 5678): Automation workflows
- **Leantime** (Port 9000): Project management

### 🔍 **Auto-Logging Infrastructure**
- **Port Registry**: MSSQL-backed port tracking system
- **Service Health Monitoring**: 5-minute interval health checks
- **Performance Metrics**: Automatic collection and logging
- **Home Assistant Integration**: 50+ agent monitoring dashboard
- **Database**: MSSQL connection to AgentDirectory (61 agents, 6380 messages)

## Migration Strategy

### Phase 1: Infrastructure Migration
1. **Port Registry Enhancement**: Extend existing port registry in new repo
2. **Database Integration**: Preserve MSSQL connections and fallback mechanisms
3. **Logging Systems**: Migrate auto-logging infrastructure

### Phase 2: Core Services Migration
1. **API Gateway**: Migrate FastAPI application with CORS and security
2. **RAG System**: Migrate ChromaDB integration and vector management
3. **AI Orchestration**: Migrate agent coordination logic
4. **Delegation System**: Migrate task delegation engine

### Phase 3: Integration & Automation
1. **Home Assistant Config**: Migrate agent monitoring dashboards
2. **Startup Scripts**: Create unified startup system
3. **Service Discovery**: Implement automatic service registration
4. **Health Monitoring**: Migrate health check automation

### Phase 4: Validation & Optimization
1. **Functionality Testing**: Validate all migrated services
2. **Performance Verification**: Ensure logging and monitoring works
3. **Integration Testing**: Test service communication
4. **Documentation**: Update system documentation

## Migration Targets

### New Directory Structure
```
~/rod-corp/
├── services/
│   ├── legacy-integration/
│   │   ├── api-gateway/          # Port 18000
│   │   ├── rag-system/           # Port 17000
│   │   ├── ai-orchestration/     # Port 16000
│   │   ├── delegation-system/    # Port 15000
│   │   └── port-registry/        # Enhanced port management
│   └── homeassistant/            # HA integration configs
├── scripts/
│   ├── unified-startup.sh        # Master startup script
│   ├── service-health-monitor.sh # Health monitoring
│   └── migration-validation.sh   # Post-migration tests
└── configs/
    ├── database-config.json      # Enhanced DB config
    └── service-registry.json     # Service definitions
```

## Preserved Capabilities
- ✅ All 4 core Rod-Corp services (ports 18000, 17000, 16000, 15000)
- ✅ MSSQL database connectivity with SQLite fallback
- ✅ Auto-logging and port registry system
- ✅ Home Assistant agent monitoring (50+ agents)
- ✅ Service health monitoring and alerting
- ✅ Performance metrics collection
- ✅ Automatic service discovery and registration

## Success Criteria
1. All legacy services running on original ports
2. Auto-logging system fully functional
3. MSSQL database connectivity preserved
4. Home Assistant integration working
5. Service health monitoring active
6. Unified startup system operational
7. All existing functionality preserved