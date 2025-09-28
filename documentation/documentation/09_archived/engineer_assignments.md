# Rod-Corp n8n Integration Engineering Assignments

## Project Overview
Integration of n8n workflows with Rod-Corp AI Interaction Server and agent ecosystem.

## Engineering Team Assignments

### Senior Engineer - AI Agent Workflow Integration
**Responsibility**: Lead integration between n8n and AI agents

**Tasks**:
1. **AI Agent Communication Workflows**
   - Implement webhook triggers for agent interactions
   - Create workflow templates for each agent type (claude-full, qwen-full, etc.)
   - Handle response processing and error management
   - Integrate with port registry for dynamic service discovery

2. **Agent Coordination Workflows**
   - Multi-agent collaboration workflows
   - Task delegation and result aggregation
   - Load balancing across available agents
   - Agent health monitoring and failover

3. **Advanced Integration Features**
   - Real-time agent status monitoring
   - Workflow orchestration based on agent capabilities
   - Performance analytics and optimization
   - Custom node development for Rod-Corp specific operations

**Resources**:
- AI Interaction Server API: `http://localhost:49152`
- Agent Config Manager: `/home/rod/rod-corp/services/ai-interaction-server/agent_config_manager.py`
- Port Registry: `/home/rod/rod-corp/services/ai-interaction-server/port_registry.py`

### Junior Engineer - File Processing & FTP Workflows
**Responsibility**: Automated file processing and FTP integration

**Tasks**:
1. **FTP Integration Workflows**
   - Monitor FTP directory on 10.0.0.6 for new files
   - Automated file download and processing
   - File upload workflows for results sharing
   - Directory synchronization workflows

2. **File Processing Pipelines**
   - Document processing through AI agents
   - Image analysis and processing workflows
   - Data extraction and transformation
   - File format conversion workflows

3. **Storage and Backup**
   - Automated backup workflows
   - File archival and retention policies
   - Database integration for file metadata
   - Error handling and recovery processes

**Resources**:
- FTP Server: 10.0.0.6 (credentials: rod/r254175S!)
- Shared folder structure
- File processing templates
- Database integration scripts

## Shared Responsibilities

### Database Integration
- Rod-Corp MSSQL database connectivity
- Workflow metadata storage
- Result logging and analytics
- Performance monitoring data

### Testing and Documentation
- Unit testing for custom workflows
- Integration testing with AI agents
- Documentation of workflow templates
- User guides and troubleshooting

## Timeline and Milestones

### Phase 1 (Week 1-2)
- [ ] Setup n8n development environment
- [ ] Create basic AI agent communication workflows
- [ ] Implement FTP monitoring workflows
- [ ] Test integration with AI Interaction Server

### Phase 2 (Week 3-4)
- [ ] Advanced agent coordination workflows
- [ ] File processing pipeline automation
- [ ] Database integration and logging
- [ ] Error handling and monitoring

### Phase 3 (Week 5-6)
- [ ] Performance optimization
- [ ] Custom node development
- [ ] Comprehensive testing
- [ ] Documentation and deployment

## Contact Information

**Project Lead**: Rod (rodchemist)
**AI Interaction Server**: Port 49152
**FTP Server**: 10.0.0.6
**Database**: Rod-Corp MSSQL

## Getting Started

1. **Environment Setup**
   ```bash
   cd /home/rod/rod-corp/n8n_workflows
   # Review templates and scripts
   ```

2. **AI Server Integration**
   ```bash
   curl http://localhost:49152/health
   curl http://localhost:49152/port-registry
   ```

3. **FTP Access Test**
   ```bash
   ftp 10.0.0.6
   # Use credentials: rod/r254175S!
   ```

4. **Review Existing Infrastructure**
   - AI agents configuration: `/home/rod/rod-corp/services/ai-interaction-server/agents/`
   - Port registry system
   - Database schema and connections