# Rod-Corp Database Architecture Documentation

## Overview

The Rod-Corp system uses a robust dual-database architecture with **MSSQL Server as the primary production database** and **SQLite as an intelligent fallback** for development and offline scenarios. This architecture ensures high availability and seamless operation regardless of network conditions.

## Database Architecture

### Primary Database: MSSQL Server

- **Host**: 10.0.0.2:1433
- **Database**: AgentDirectory
- **Authentication**: SQL Server Authentication (rdai/DareFoods116)
- **Purpose**: Production agent coordination and communication
- **Driver**: ODBC Driver 18 for SQL Server

### Fallback Database: SQLite

- **Location**: `./agent_system.db`
- **Purpose**: Development, testing, and offline operation
- **Schema**: Mirrors MSSQL structure with SQLite-specific adaptations
- **Automatic Migration**: Sample data populated on initialization

## Database Connection Management

### Enhanced Connection Handling

The `DatabaseManager` class provides:

1. **Automatic Failover**: Detects MSSQL unavailability and switches to SQLite
2. **Connection Pooling**: Optimized connection management
3. **Retry Logic**: 3-attempt retry with exponential backoff
4. **Schema Validation**: Ensures required tables exist
5. **Thread Safety**: Context managers for safe concurrent access

### Connection Flow

```python
1. Initialize DatabaseManager
2. Test MSSQL connectivity (3 attempts)
3. If successful: Use MSSQL + verify schema
4. If failed: Initialize SQLite fallback + populate sample data
5. Runtime failover: Switch to SQLite if MSSQL becomes unavailable
```

## Core Database Tables

### GlobalAgentRegistry
**Purpose**: Central registry for all agents across projects

**MSSQL Schema**:
```sql
CREATE TABLE GlobalAgentRegistry (
    AgentUUID UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
    AgentName NVARCHAR(100) NOT NULL,
    ProjectID NVARCHAR(100) NOT NULL,
    MachineHostname NVARCHAR(100) NOT NULL,
    MachineIP NVARCHAR(45) NOT NULL,
    Team NVARCHAR(100),
    Role NVARCHAR(200),
    AIModel NVARCHAR(50) CHECK (AIModel IN ('claude', 'codex', 'qwen', 'gemini')),
    Personality17Disc NVARCHAR(50),
    Specialization NVARCHAR(300),
    SeniorityLevel NVARCHAR(50),
    Status NVARCHAR(50) DEFAULT 'active',
    FirstRegistered DATETIME2 DEFAULT GETDATE(),
    LastSeen DATETIME2 DEFAULT GETDATE(),
    CommunicationPort INT DEFAULT 8888,
    PerformanceRating DECIMAL(3,2) DEFAULT 0.00,
    TotalRodCoinsEarned BIGINT DEFAULT 0,
    CurrentPayCycle INT DEFAULT 1
);
```

**Key Operations**:
- Agent registration with UUID generation
- Heartbeat updates (LastSeen timestamp)
- Performance rating tracking
- Team and specialization management

### AgentDiscussions
**Purpose**: Inter-agent communication and coordination

**Schema Features**:
- Participant identification
- Topic categorization
- Sentiment analysis
- Priority levels
- Thread management
- Real-time timestamps

**Key Operations**:
- Message posting with metadata
- Topic-based filtering
- Recent discussions retrieval
- Cross-project communication

### PayrollMaster & RodCoins System
**Purpose**: Agent compensation and performance tracking

**Components**:
- **PayrollMaster**: Base salaries, multipliers, bonuses
- **RodCoinsTransactions**: Individual transaction history
- **AgentPerformanceHistory**: Evaluation records

**Key Operations**:
- RodCoins award/deduction
- Performance evaluation recording
- Leaderboard generation
- Payroll cycle management

### AgentTodoTracking
**Purpose**: Task delegation and completion tracking

**Features**:
- Priority-based task assignment
- Completion percentage tracking
- Quality scoring
- Due date management
- Supervisor notes

**Key Operations**:
- Task creation and assignment
- Status updates (pending → in_progress → completed)
- Automatic RodCoins awards for completion
- Performance analytics

## API Operations

### Agent Management

```python
# Register new agent
agent_uuid = db.register_agent(
    agent_name="ALEX",
    team="Document Processing",
    specialization="OneDrive Integration",
    ai_model="claude",
    personality="INTJ-T",
    seniority="Senior"
)

# Update agent activity
db.update_agent_heartbeat("ALEX")

# Get agent details
agent = db.get_agent_by_name("ALEX")
active_agents = db.get_active_agents()
```

### Communication System

```python
# Post discussion message
db.post_discussion_message(
    participant="ALEX",
    topic="SYSTEM_STATUS",
    message="OneDrive integration complete",
    sentiment="positive",
    priority="normal"
)

# Retrieve discussions
recent = db.get_recent_discussions(limit=50)
topic_discussions = db.get_discussions_by_topic("SYSTEM_STATUS")
```

### RodCoins Management

```python
# Award RodCoins
db.award_rodcoins(
    agent_name="ALEX",
    amount=100,
    description="Excellent OneDrive integration",
    transaction_type="earned"
)

# Check balance and leaderboard
balance = db.get_agent_rodcoins_balance("ALEX")
leaderboard = db.get_rodcoins_leaderboard(limit=10)
```

### Task Coordination

```python
# Create and manage tasks
task_id = db.create_task(
    agent_name="ALEX",
    description="Process Q3 documents",
    priority="high",
    due_date="2025-09-30"
)

# Update task progress
db.update_task_status(task_id, "in_progress", completion_percentage=75)
db.update_task_status(task_id, "completed", completion_percentage=100)

# Get agent tasks
tasks = db.get_agent_tasks("ALEX", status="pending")
all_tasks = db.get_agent_tasks("ALEX")
```

### Performance Tracking

```python
# Record performance evaluation
db.record_performance_evaluation(
    agent_uuid=agent_uuid,
    performance_score=4.5,
    evaluator_uuid=supervisor_uuid,
    notes="Outstanding performance in document processing"
)
```

## System Statistics and Monitoring

```python
# Get comprehensive system statistics
stats = db.get_system_statistics()
# Returns:
# {
#     'database_type': 'MSSQL' | 'SQLite',
#     'total_agents': int,
#     'active_agents': int,
#     'total_discussions': int,
#     'total_tasks': int,
#     'completed_tasks': int,
#     'total_rodcoins_awarded': int
# }
```

## Error Handling and Resilience

### Connection Recovery
- **Automatic Retry**: 3 attempts with exponential backoff
- **Graceful Degradation**: Seamless SQLite fallback
- **Connection Healing**: Automatic MSSQL reconnection when available
- **Transaction Safety**: Context managers ensure proper cleanup

### Data Consistency
- **Schema Validation**: Ensures table structure compatibility
- **Foreign Key Constraints**: Maintains referential integrity
- **Transaction Rollback**: Prevents partial updates on failure
- **Sample Data Population**: Consistent test data across environments

## Deployment Considerations

### Production Deployment
1. Ensure MSSQL Server is accessible at 10.0.0.2:1433
2. Verify ODBC Driver 18 for SQL Server is installed
3. Configure firewall rules for database access
4. Set up proper database user permissions
5. Deploy with environment variables for database credentials

### Development Environment
1. SQLite fallback automatically provides sample data
2. No external dependencies required
3. Database file stored locally: `./agent_system.db`
4. Full feature parity with MSSQL operations
5. Easy testing and validation

### Migration Strategy
1. **Data Export**: Extract from MSSQL to structured format
2. **Schema Mapping**: Convert MSSQL types to SQLite equivalents
3. **Data Import**: Populate SQLite with production data
4. **Validation**: Ensure data integrity and completeness
5. **Switchover**: Seamless transition between databases

## Security Features

### Database Security
- **SQL Injection Prevention**: Parameterized queries throughout
- **Connection Encryption**: TrustServerCertificate configuration
- **User Authentication**: SQL Server authentication required
- **Connection Timeouts**: Prevents hanging connections
- **Error Logging**: Comprehensive logging without exposing credentials

### Data Protection
- **Sensitive Data Handling**: Passwords masked in logs
- **Access Control**: Role-based database permissions
- **Audit Trail**: Complete transaction logging
- **Data Validation**: Input sanitization and type checking

## Performance Optimizations

### Database Optimizations
- **Connection Pooling**: Reuse database connections
- **Query Optimization**: Indexed columns for common queries
- **Batch Operations**: Efficient bulk data operations
- **Schema Indexing**: Strategic indexes on frequently queried columns

### Application Optimizations
- **Lazy Loading**: On-demand data retrieval
- **Caching Strategy**: Intelligent result caching
- **Thread Safety**: Concurrent operation support
- **Memory Management**: Proper resource cleanup

## Monitoring and Maintenance

### Health Checks
```python
# Database connectivity test
db_type = db.get_database_type()
is_healthy = db.mssql_available if db_type == "MSSQL" else True

# System statistics monitoring
stats = db.get_system_statistics()
```

### Maintenance Tasks
1. **Regular Backups**: Automated MSSQL backup schedule
2. **Performance Monitoring**: Query performance analytics
3. **Connection Pool Management**: Monitor connection usage
4. **Log Rotation**: Manage database operation logs
5. **Schema Evolution**: Version-controlled schema updates

## Integration Points

### API Gateway Integration
- **Service Registry**: Database operations exposed via FastAPI
- **Health Endpoints**: Database status monitoring
- **Authentication**: Integrated with system security
- **Rate Limiting**: Protection against abuse

### Agent System Integration
- **Real-time Communication**: Live agent status updates
- **Task Coordination**: Automated task distribution
- **Performance Tracking**: Continuous evaluation system
- **Compensation Management**: Automated RodCoins distribution

## Future Enhancements

### Planned Features
1. **Distributed Database**: Multi-node MSSQL clustering
2. **Advanced Analytics**: Machine learning integration
3. **Real-time Sync**: MSSQL ↔ SQLite bidirectional sync
4. **Message Queuing**: Asynchronous communication patterns
5. **Data Archiving**: Historical data management

### Scalability Considerations
1. **Horizontal Scaling**: Database sharding strategies
2. **Caching Layers**: Redis integration for performance
3. **Read Replicas**: Load distribution for read operations
4. **Connection Pooling**: Advanced connection management
5. **Microservice Architecture**: Service-specific databases

---

**Last Updated**: September 20, 2025
**Database Version**: Enhanced v2.0
**Compatibility**: MSSQL Server 2022, SQLite 3.x
**Status**: Production Ready ✅