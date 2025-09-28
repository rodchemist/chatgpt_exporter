# AI Interaction Server

A lightweight FastAPI server that provides direct messaging interface to Rod-Corp AI agents with file result handling and FTP sharing capabilities.

## Features

- 🤖 **Direct AI Agent Messaging** - Send messages to any configured AI agent
- 📁 **File Result Handling** - Automatically capture and serve generated files
- 🌐 **FTP Integration** - Upload results to FTP server automatically
- 🔐 **Authentication** - Optional JWT-based authentication
- 📊 **Web Interface** - User-friendly web UI for interactions
- 🔄 **Real-time Updates** - Live status updates for agent processing
- 📋 **Session Management** - Track and manage multiple interactions

## Quick Start

### 1. Manual Start

```bash
cd services/ai-interaction-server
./start.sh
```

### 2. Install as System Service (Auto-start on boot)

```bash
cd services/ai-interaction-server
./install-service.sh
```

This will:
- Install systemd service
- Enable auto-start on boot
- Start the service immediately
- Set up proper permissions

The server will start on `http://localhost:49152` (auto-selects a nearby port if busy)

### 3. Access Web Interface

Open your browser and go to:
- **Web Interface**: http://localhost:49152
- **API Documentation**: http://localhost:49152/docs

### 4. Send Messages to AI Agents

Using the web interface:
1. Select an AI agent (Claude, Qwen, etc.)
2. Enter your message
3. Optionally add context
4. Click "Send Message"
5. View results and download files

## API Usage

### Send Message to Agent

```bash
curl -X POST "http://localhost:49152/interact" \
  -H "Content-Type: application/json" \
  -d '{
    "agent": "claude-full",
    "message": "Write a Python script to analyze data",
    "context": "Project: Data Analysis Tool",
    "return_files": true
  }'
```

### Get Results

```bash
curl "http://localhost:49152/results/{request_id}"
```

### Download Files

```bash
curl "http://localhost:49152/download/{request_id}/{filename}" -o filename
```

## Configuration

### Environment Variables

Create a `.env` file or set environment variables:

```bash
# Server settings
AI_INTERACTION_HOST=0.0.0.0
AI_INTERACTION_PORT=49152
DEBUG=true

# Security
SECRET_KEY=rodchemist-ai-interaction-secret-key
ACCESS_TOKEN_EXPIRE=30

# File handling
RESULTS_DIR=/tmp/ai_interaction_results
MAX_FILE_SIZE=104857600  # 100MB
CLEANUP_AFTER_HOURS=24

# Agent settings
AGENT_TIMEOUT=300  # 5 minutes
MAX_CONCURRENT=5

# FTP settings (optional)
FTP_ENABLED=false
FTP_HOST=rodchemist-ftp-server.com
FTP_PORT=21
FTP_USER=username
FTP_PASSWORD=password
FTP_BASE_PATH=/ai_results

# Rod-Corp integration
RODCORP_ENABLED=true
```

### FTP Configuration

Configure FTP sharing via the web interface or API:

```bash
curl -X POST "http://localhost:49152/configure-sharing" \
  -H "Content-Type: application/json" \
  -d '{
    "method": "ftp",
    "ftp_host": "rodchemist-ftp-server.com",
    "ftp_user": "username",
    "ftp_pass": "password",
    "ftp_path": "/ai_results"
  }'
```

## Supported AI Agents

The server integrates with all Rod-Corp AI agents:

- **claude-full** - Anthropic Claude with full context
- **qwen-full** - Alibaba Qwen with full context
- **codex-full** - OpenAI Codex with full context
- **gemini-full** - Google Gemini with full context
- **deepseek-full** - Local DeepSeek via Ollama
- **mixtral-full** - Local Mixtral via Ollama
- **codellama-full** - Local CodeLlama via Ollama

## Background Execution Model

- Each `/interact` request is queued as a FastAPI background task that now runs in the threadpool, keeping the main event loop free for other users.
- Blocking shell work such as `subprocess.run`, file collection, and optional FTP uploads execute outside the loop, so multiple agent requests can progress in parallel.
- Agent commands follow the `ai-help` aliases and are dispatched exactly as you would from a terminal, e.g. `codex-full exec "Fix this Python script"`, `gemini-full "Summarize the latest logs"`, or `qwen-full -p "Draft infrastructure checklist"`.
- The server automatically handles environment setup before invoking each CLI agent, so you can rely on consistent behaviour between manual CLI usage and background execution.

## File Handling

### Automatic File Detection

The server automatically detects files generated during agent execution:

- Searches common directories (`~/Downloads`, `~/Desktop`, `/tmp`, current directory)
- Captures files modified within 5 minutes of execution
- Copies files to results directory for serving

### File Sharing Methods

1. **Local Download** (default)
   - Files served via HTTP from results directory
   - Access via `/download/{request_id}/{filename}`

2. **FTP Upload**
   - Automatically uploads files to configured FTP server
   - Organizes files by request ID
   - Provides FTP URLs for access

## Authentication

### Development Mode

Authentication is optional in debug mode. Access without credentials.

### Production Mode

Enable authentication by setting `DEBUG=false`:

```python
# Default users (change in production)
Username: admin  Password: admin123
Username: user   Password: user123
```

### JWT Tokens

Get token via login endpoint:

```bash
curl -X POST "http://localhost:8080/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=admin&password=admin123"
```

Use token in requests:

```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
  "http://localhost:8080/interact"
```

## Integration Examples

### Python Client

```python
import requests

# Send message
response = requests.post("http://localhost:49152/interact", json={
    "agent": "claude-full",
    "message": "Create a data visualization script",
    "return_files": True
})

request_id = response.json()["request_id"]

# Poll for results
import time
while True:
    result = requests.get(f"http://localhost:49152/results/{request_id}")
    status = result.json()["status"]

    if status != "processing":
        break
    time.sleep(2)

# Download files
for filename in result.json()["files"]:
    file_response = requests.get(f"http://localhost:49152/download/{request_id}/{filename}")
    with open(filename, "wb") as f:
        f.write(file_response.content)
```

### Bash Script

```bash
#!/bin/bash
# Send message and wait for results

REQUEST_ID=$(curl -s -X POST "http://localhost:49152/interact" \
  -H "Content-Type: application/json" \
  -d '{"agent": "deepseek-full", "message": "'"$1"'"}' | \
  jq -r .request_id)

echo "Request ID: $REQUEST_ID"

# Wait for completion
while true; do
    STATUS=$(curl -s "http://localhost:49152/results/$REQUEST_ID" | jq -r .status)
    echo "Status: $STATUS"

    if [ "$STATUS" != "processing" ]; then
        break
    fi
    sleep 2
done

# Get final results
curl -s "http://localhost:49152/results/$REQUEST_ID" | jq .
```

## System Service Management

### Service Commands

```bash
# Check service status
./check-service.sh

# Start/stop/restart service
sudo systemctl start ai-interaction-server
sudo systemctl stop ai-interaction-server
sudo systemctl restart ai-interaction-server

# View logs
sudo journalctl -u ai-interaction-server -f

# Uninstall service
./uninstall-service.sh
```

## Troubleshooting

### Service Issues

1. **Service won't start**
   ```bash
   # Check logs
   sudo journalctl -u ai-interaction-server -n 50

   # Check permissions
   ls -la /home/rod/rod-corp/services/ai-interaction-server/

   # Reinstall service
   ./uninstall-service.sh
   ./install-service.sh
   ```

2. **Auto-start not working**
   ```bash
   # Check if enabled
   sudo systemctl is-enabled ai-interaction-server

   # Enable if needed
   sudo systemctl enable ai-interaction-server
   ```

### Common Issues

1. **Agent not found**
   - Verify AI agents are properly installed
   - Run `ai-status` to check agent availability

2. **Timeout errors**
   - Increase `AGENT_TIMEOUT` environment variable
   - Check agent responsiveness individually

3. **File not captured**
   - Ensure files are created in monitored directories
   - Check file timestamps (must be within 5 minutes)

4. **FTP upload fails**
   - Verify FTP credentials and connectivity
   - Check FTP server permissions

### Debug Mode

Enable verbose logging:

```bash
export DEBUG=true
python3 main.py
```

### Health Check

```bash
curl http://localhost:49152/health
```

## Security Considerations

- Change default passwords in production
- Use HTTPS in production environments
- Restrict network access to trusted IPs
- Regularly rotate JWT secret keys
- Monitor file upload sizes and cleanup old files

## Architecture

```
┌─────────────────────────────────────────────────┐
│                Web Interface                    │
├─────────────────────────────────────────────────┤
│                FastAPI Server                   │
├─────────────────────────────────────────────────┤
│  Authentication │ File Handler │ FTP Handler    │
├─────────────────────────────────────────────────┤
│              AI Agent Executor                  │
├─────────────────────────────────────────────────┤
│  Rod-Corp AI Agents │ Local Models │ Results   │
└─────────────────────────────────────────────────┘
```

## Development

### Setup Development Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run Tests

```bash
python3 -m pytest tests/
```

### API Documentation

Start server and visit: http://localhost:49152/docs

---

**Ready to interact with your AI agents remotely!** 🚀
