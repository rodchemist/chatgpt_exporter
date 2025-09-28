# 🔔 Slack Integration Setup Guide - Rod-Corp

## ✅ Current Status

**Connection**: ✅ **WORKING**
- **Workspace**: RodCorp
- **User**: rodrigohsanchezs
- **Bot ID**: U09GA5DCTS6
- **Token**: Valid (expires in 12 hours)

## 🚀 Quick Setup Steps

### 1. Create Channel for Rod-Corp Automation
```
1. In Slack, create a channel: #rod-corp-automation
2. Invite the bot to the channel: @rod-corp-bot
3. Grant bot permissions to post messages
```

### 2. Test Notifications
```bash
# Test the integration
python3 slack_notification_manager.py
```

### 3. Add to n8n Workflow
The bot can now send notifications when:
- Documentation analysis completes
- Workflows succeed/fail
- System alerts occur
- AI agents finish tasks

## 🔧 Integration with n8n Workflows

### Enhanced Workflow with Slack Notifications
```json
{
  "name": "Slack Notification Node",
  "type": "n8n-nodes-base.httpRequest",
  "parameters": {
    "url": "http://localhost:49152/slack/notify",
    "sendBody": true,
    "bodyContentType": "json",
    "jsonBody": {
      "type": "documentation_complete",
      "status": "success",
      "message": "Documentation analysis completed successfully"
    }
  }
}
```

### Webhook Integration
```bash
# Add to workflow commands
python3 -c "
from slack_notification_manager import SlackNotificationManager;
manager = SlackNotificationManager();
manager.notify_documentation_update({
  'status': 'completed',
  'changes_analyzed': 5,
  'documentation_updated': True
})
"
```

## ⏰ Token Management (12-hour expiry)

### Automatic Token Refresh
The tokens expire every 12 hours. Here's how to handle it:

1. **Manual Refresh** (when needed):
   - Go to Slack App settings
   - Generate new Access Token
   - Update `.env` file

2. **Automated Refresh** (recommended):
   - Set up cron job to refresh tokens
   - Use refresh token for automatic renewal

### Token Refresh Cron Job
```bash
# Add to crontab (every 11 hours)
0 */11 * * * cd /home/rod/rod-corp/services/rag-agent-training && python3 slack_token_refresh.py
```

## 📋 Bot Permissions Required

Ensure your Slack bot has these permissions:
- `chat:write` - Send messages
- `chat:write.public` - Send to public channels
- `channels:read` - Read channel information
- `users:read` - Read user information

## 🔔 Notification Types

### 1. Documentation Updates
- Triggers: When documentation agent completes
- Content: Changes analyzed, version updates
- Channel: #rod-corp-automation

### 2. Workflow Status
- Triggers: n8n workflow start/complete/error
- Content: Workflow name, status, duration
- Channel: #rod-corp-automation

### 3. System Alerts
- Triggers: System errors, warnings
- Content: Alert type, severity, details
- Channel: #rod-corp-automation

### 4. AI Agent Completion
- Triggers: When AI agents finish tasks
- Content: Agent ID, status, results
- Channel: #rod-corp-automation

## 🛠️ Troubleshooting

### Common Issues

1. **Bot not in channel**
   ```
   Error: "channel_not_found"
   Fix: Invite bot to #rod-corp-automation channel
   ```

2. **Permission denied**
   ```
   Error: "missing_scope"
   Fix: Add required permissions in Slack App settings
   ```

3. **Token expired**
   ```
   Error: "invalid_auth"
   Fix: Refresh token in Slack App settings
   ```

### Debug Commands
```bash
# Test connection
python3 -c "from slack_notification_manager import SlackNotificationManager; SlackNotificationManager().test_slack_connection()"

# Send test message
python3 -c "
from slack_notification_manager import SlackNotificationManager;
manager = SlackNotificationManager();
result = manager.send_notification('Test from Rod-Corp AI System!', '#general');
print(result)
"
```

## 🎯 Next Steps

1. **Create #rod-corp-automation channel**
2. **Invite bot to channel**
3. **Test notifications**
4. **Add to n8n workflows**
5. **Set up token refresh automation**

## 📊 Integration Benefits

### Real-time Notifications
- Instant updates on automation progress
- Error alerts for immediate attention
- Success confirmations for peace of mind

### Team Coordination
- Share automation status with team
- Centralized notification hub
- Historical record of system activity

### Monitoring & Debugging
- Quick identification of issues
- Context-rich error messages
- Automated escalation for critical alerts

---

**Your Slack integration is ready!** 🎉

**Current Setup:**
- ✅ Connected to RodCorp workspace
- ✅ Bot authenticated and active
- 🔄 Ready for channel setup and notifications
- ⏰ Token refresh needed every 12 hours