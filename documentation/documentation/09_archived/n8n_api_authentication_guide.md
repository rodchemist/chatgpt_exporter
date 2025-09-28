# 🔑 n8n API Authentication & Setup Guide

## 🎯 Key Discovery: Correct Authentication Method

Based on the official n8n documentation, the authentication uses **`X-N8N-API-KEY`** header, NOT Bearer tokens!

## 📋 API Key Generation Steps

### 1. Access n8n Settings
1. Open n8n interface: http://localhost:5678
2. Navigate to **Settings** → **n8n API**
3. Click **"Create an API key"**

### 2. Configure API Key
- **Label**: Choose a descriptive name (e.g., "Rod-Corp Automation")
- **Expiration**: Set appropriate expiration time
- **Scopes** (Enterprise only): Choose access levels

### 3. Copy & Save API Key
- Copy the generated API key immediately
- Store securely for use in automation tools

## 🔧 Correct Authentication Format

### ❌ Incorrect (What we were using):
```bash
curl -H "Authorization: Bearer YOUR_API_KEY"
```

### ✅ Correct (Official method):
```bash
curl -H "X-N8N-API-KEY: YOUR_API_KEY"
```

## 🚀 Testing the Correct Authentication

### Example API Calls:
```bash
# List all workflows
curl -H "X-N8N-API-KEY: YOUR_KEY" http://localhost:5678/rest/workflows

# Get workflow executions
curl -H "X-N8N-API-KEY: YOUR_KEY" http://localhost:5678/rest/executions

# Get active workflows
curl -H "X-N8N-API-KEY: YOUR_KEY" http://localhost:5678/rest/active-workflows

# Health check (no auth needed)
curl http://localhost:5678/healthz
```

## 📊 Available API Endpoints (From Documentation)

### Workflow Management
- `GET /rest/workflows` - List all workflows
- `POST /rest/workflows` - Create new workflow
- `GET /rest/workflows/{id}` - Get specific workflow
- `PATCH /rest/workflows/{id}` - Update workflow
- `DELETE /rest/workflows/{id}` - Delete workflow
- `POST /rest/workflows/{id}/activate` - Activate workflow
- `POST /rest/workflows/{id}/deactivate` - Deactivate workflow
- `POST /rest/workflows/{id}/execute` - Execute workflow

### Execution Management
- `GET /rest/executions` - List executions
- `GET /rest/executions/{id}` - Get specific execution
- `DELETE /rest/executions/{id}` - Delete execution
- `POST /rest/executions/{id}/retry` - Retry execution

### Active Workflows
- `GET /rest/active-workflows` - List active workflows
- `GET /rest/active-workflows/{id}` - Get active workflow status

### Community Packages
- `GET /rest/community-packages` - List installed packages
- `POST /rest/community-packages` - Install package
- `DELETE /rest/community-packages/{name}` - Uninstall package

## 🛠️ Updated Tools Configuration

### 1. Monitoring Dashboard (Port 8503)
- Update authentication to use `X-N8N-API-KEY` header
- Test with proper API key from n8n settings

### 2. API Explorer (Port 8504)
- Enhanced endpoint discovery with correct authentication
- Full REST API exploration capabilities

### 3. Integration Tester
- Update authentication method
- Re-run comprehensive tests

## 🎯 Next Steps

1. **Generate API Key**:
   - Access http://localhost:5678 → Settings → n8n API
   - Create new API key with appropriate permissions

2. **Update Tools**:
   - Use correct `X-N8N-API-KEY` header format
   - Test all monitoring dashboards

3. **Full Integration**:
   - Import automation workflows
   - Set up webhook endpoints
   - Configure community nodes via API

## 🔍 Troubleshooting

### Common Issues:
- **"Unauthorized" errors**: Check API key generation and header format
- **API not available**: May require n8n upgrade (not available in free trial)
- **Scope errors**: Ensure API key has necessary permissions

### Testing Commands:
```bash
# Test basic connectivity
curl http://localhost:5678/healthz

# Test API authentication (replace YOUR_KEY)
curl -H "X-N8N-API-KEY: YOUR_KEY" http://localhost:5678/rest/workflows

# Check if API is available
curl -I http://localhost:5678/api/v1/docs/
```

## 🎉 Expected Results

Once properly authenticated:
- ✅ Full workflow management via API
- ✅ Real-time execution monitoring
- ✅ Community package installation
- ✅ Automated documentation workflows
- ✅ Enhanced Rod-Corp automation capabilities

---

**The key insight**: n8n uses `X-N8N-API-KEY` header authentication, not Bearer tokens! This explains why our previous attempts returned "Unauthorized" errors.