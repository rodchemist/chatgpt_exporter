# 🔗 n8n Webhook Integration Guide - Rod-Corp Automation

## 🎯 Webhook Strategy for Rod-Corp AI System

Based on the n8n webhook documentation and our existing automation workflow, here's how to set up powerful webhook-based automation for the Rod-Corp AI system.

## 📋 Rod-Corp Webhook Use Cases

### 1. Git Repository Changes
- **Webhook URL**: `http://localhost:5678/webhook/git-changes`
- **Trigger**: Git push, pull requests, commits
- **Action**: Trigger documentation analysis and updates

### 2. Documentation Updates
- **Webhook URL**: `http://localhost:5678/webhook/documentation-webhook`
- **Trigger**: Manual documentation requests
- **Action**: Run documentation specialist agents

### 3. AI Agent Notifications
- **Webhook URL**: `http://localhost:5678/webhook/ai-agent-status`
- **Trigger**: Agent completion, errors, status changes
- **Action**: Update monitoring dashboards

### 4. Community Node Management
- **Webhook URL**: `http://localhost:5678/webhook/node-management`
- **Trigger**: Package updates, new node availability
- **Action**: Install/update community packages

## 🔧 Webhook Configuration in n8n

### Step 1: Create Webhook Node in Workflow
1. Open n8n: http://localhost:5678
2. Create new workflow or edit existing
3. Add **Webhook** node as trigger
4. Configure webhook settings:

```json
{
  "httpMethod": "POST",
  "path": "documentation-webhook",
  "authentication": "none",
  "responseMode": "onReceived",
  "responseData": "allEntryData"
}
```

### Step 2: Configure HTTP Methods
- **POST**: For receiving data (git commits, status updates)
- **GET**: For simple triggers and health checks
- **PUT/PATCH**: For updating existing resources

### Step 3: Webhook URL Patterns
```
Production URL: http://localhost:5678/webhook/{path}
Test URL: http://localhost:5678/webhook-test/{path}
```

## 🚀 Rod-Corp Webhook Implementations

### 1. Git Integration Webhook
```bash
# Configure in your Git repository settings
curl -X POST "http://localhost:5678/webhook/git-changes" \
  -H "Content-Type: application/json" \
  -d '{
    "repository": "rod-corp",
    "commits": [
      {
        "id": "abc123",
        "message": "Add new documentation features",
        "author": "developer",
        "timestamp": "2025-09-22T00:00:00Z"
      }
    ]
  }'
```

### 2. Documentation Agent Webhook
```bash
# Trigger documentation analysis
curl -X POST "http://localhost:5678/webhook/documentation-webhook" \
  -H "Content-Type: application/json" \
  -d '{
    "action": "analyze_changes",
    "days_back": 7,
    "include_dependencies": true
  }'
```

### 3. AI Agent Status Webhook
```bash
# Agent completion notification
curl -X POST "http://localhost:5678/webhook/ai-agent-status" \
  -H "Content-Type: application/json" \
  -d '{
    "agent_id": "simple_documentation_specialist",
    "status": "completed",
    "result": {
      "changes_analyzed": 5,
      "documentation_updated": true
    }
  }'
```

## 🔄 Webhook Workflow Integration

### Enhanced Documentation Workflow
```json
{
  "workflow": "Automated Documentation & Versioning",
  "triggers": [
    {
      "node": "Git Webhook",
      "type": "webhook",
      "path": "git-changes",
      "method": "POST"
    },
    {
      "node": "Schedule Trigger",
      "type": "cron",
      "schedule": "0 6 * * *"
    }
  ],
  "actions": [
    "Run Documentation Agent",
    "Update Version History",
    "Generate Reports",
    "Notify Stakeholders"
  ]
}
```

## 📊 Webhook Testing & Monitoring

### Test Webhook Endpoints
```bash
# Test all Rod-Corp webhooks
curl http://localhost:5678/webhook/documentation-webhook
curl http://localhost:5678/webhook/git-changes
curl http://localhost:5678/webhook/ai-agent-status
curl http://localhost:5678/webhook/node-management
```

### Monitor Webhook Activity
- **n8n Executions**: Track webhook triggers in execution history
- **Monitoring Dashboard**: http://localhost:8503
- **API Explorer**: http://localhost:8504

## 🔐 Webhook Security

### Authentication Options
1. **None**: For internal Rod-Corp system calls
2. **Header Auth**: Add custom headers for validation
3. **API Key**: Use n8n API key for secure endpoints

### Example Secure Webhook
```json
{
  "authentication": "headerAuth",
  "headerAuth": {
    "name": "X-ROD-CORP-KEY",
    "value": "your-secret-key"
  }
}
```

## 🎯 Integration with Rod-Corp Components

### 1. AI Interaction Server Integration
```python
# In ai-interaction-server/main.py
import requests

def trigger_documentation_update():
    webhook_url = "http://localhost:5678/webhook/documentation-webhook"
    payload = {
        "action": "analyze_changes",
        "source": "ai_interaction_server"
    }
    requests.post(webhook_url, json=payload)
```

### 2. RAG Agent Integration
```python
# In rag-agent-training/simple_doc_agent.py
def notify_completion(self, result):
    webhook_url = "http://localhost:5678/webhook/ai-agent-status"
    payload = {
        "agent_id": self.agent_id,
        "status": "completed",
        "result": result
    }
    requests.post(webhook_url, json=payload)
```

## 📋 Webhook Workflow Examples

### 1. Complete Documentation Pipeline
```
Git Push → Webhook Trigger → Documentation Agent → Version Update → Notification
```

### 2. Scheduled Analysis
```
Cron Schedule → Webhook Trigger → Multi-Agent Analysis → Report Generation → Storage
```

### 3. Real-time Monitoring
```
System Event → Webhook Trigger → Status Update → Dashboard Refresh → Alert if needed
```

## 🛠️ Troubleshooting Webhooks

### Common Issues
1. **404 Not Found**: Webhook not registered or workflow inactive
2. **Timeout**: Workflow taking too long to process
3. **500 Error**: Internal workflow error

### Debug Commands
```bash
# Check webhook registration
curl -I http://localhost:5678/webhook/documentation-webhook

# Test with simple payload
curl -X POST http://localhost:5678/webhook/documentation-webhook \
  -H "Content-Type: application/json" \
  -d '{"test": true}'

# Monitor execution logs
# Use monitoring dashboard at http://localhost:8503
```

## 🎉 Integration Benefits

### Automated Workflows
- **Git Integration**: Automatic documentation updates on code changes
- **Scheduled Analysis**: Regular system health checks
- **Event-Driven**: Real-time response to system events

### Enhanced Monitoring
- **Real-time Tracking**: Webhook execution monitoring
- **Error Handling**: Automatic retry and notification
- **Performance Metrics**: Execution time and success rates

### Scalable Architecture
- **Modular Design**: Independent webhook endpoints
- **Easy Extension**: Add new webhooks for new features
- **Integration Ready**: Connect with external systems

---

## 🚀 Next Steps

1. **Import Automation Workflow**: Import `automated_documentation_workflow.json`
2. **Configure Webhooks**: Set up webhook nodes in the workflow
3. **Test Integration**: Use curl commands to test webhooks
4. **Set Up Git Hooks**: Configure repository webhooks
5. **Monitor Activity**: Use dashboards to track webhook executions

**The webhook system provides the foundation for fully automated Rod-Corp AI workflows!** 🔄