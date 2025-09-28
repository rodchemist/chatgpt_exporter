# 🔧 AI Agent Troubleshooting Guide

**Version:** 2.1 Enhanced
**Last Updated:** $(date)

## 🎯 Quick Diagnostics

### Immediate Health Check
```bash
# Run this first for any issues
ai-status

# If ai-status command not found:
source ~/.ai_enhanced_aliases && ai-status

# For comprehensive analysis:
check-ai-dependencies
```

### Common Quick Fixes
```bash
# Reload AI agent configuration
source ~/.bashrc

# Restart Ollama service
ollama serve &

# Check Rod-Corp services
cd /home/rod/rod-corp && ./start_system.sh

# Backup current configuration
backup-bashrc manual
```

## 🚨 Common Issues and Solutions

### 1. "Command not found" Errors

#### Symptoms:
```bash
bash: qwen-full: command not found
bash: ai-help: command not found
bash: ai-status: command not found
```

#### Solutions:

**Step 1: Reload Enhanced Aliases**
```bash
source ~/.ai_enhanced_aliases
```

**Step 2: Check if Aliases File Exists**
```bash
ls -la ~/.ai_enhanced_aliases
# If missing, recreate from backup or documentation
```

**Step 3: Reload Full Shell Configuration**
```bash
source ~/.bashrc
# Or restart your shell:
exec bash
```

**Step 4: Check for Syntax Errors**
```bash
bash -n ~/.bashrc
bash -n ~/.ai_enhanced_aliases
```

#### Prevention:
- Regular configuration backups with `backup-bashrc manual`
- Verify changes before implementing them

---

### 2. Ollama Model Issues

#### Symptoms:
```bash
❌ Model deepseek-coder:33b: MISSING
❌ Ollama Service: NOT RUNNING
⚠️  Model deepseek-coder:33b not found
```

#### Solutions:

**Step 1: Check Ollama Service**
```bash
# Check if ollama is installed
which ollama

# Check if service is running
ollama list

# If not running, start it:
ollama serve &
```

**Step 2: Install Missing Models**
```bash
# Install specific models
ollama pull deepseek-coder:33b
ollama pull qwen2.5-coder:latest
ollama pull mixtral:8x7b
ollama pull codellama:34b

# Check available space first
df -h
```

**Step 3: Use Alternative Models**
```bash
# List available models
ollama list

# The system will automatically suggest alternatives
deepseek-full  # Will show available alternatives if main model missing
```

**Step 4: Verify Model Installation**
```bash
# Check model details
ollama show deepseek-coder:33b

# Test model directly
echo "Hello, how are you?" | ollama run deepseek-coder:33b
```

#### Environment-Specific Issues:
```bash
# Check if you're in the right environment
ai-envs
ai-env-manager current

# Switch to ollama environment
ai-env-manager activate env_ollama
```

---

### 3. Rod-Corp Service Connection Issues

#### Symptoms:
```bash
❌ Port 18000: OFFLINE
❌ MSSQL Authentication: FAILED
⚠️  Rod-Corp integration failed, running in standalone mode
```

#### Solutions:

**Step 1: Check Service Status**
```bash
# Comprehensive service check
check-ai-dependencies network

# Check specific ports
nc -zv localhost 18000
nc -zv localhost 17000
```

**Step 2: Start Rod-Corp Services**
```bash
cd /home/rod/rod-corp

# Check if startup script exists
ls -la start_system.sh

# Start services
./start_system.sh

# Wait a few seconds and check again
sleep 10 && check-ai-dependencies network
```

**Step 3: Check Service Logs**
```bash
# Rod-Corp system logs
cd /home/rod/rod-corp
tail -f logs/*.log

# AI system logs
tail -f ~/.rod_corp_init.log
```

**Step 4: Manual Service Recovery**
```bash
# Kill any stuck processes
pkill -f "rod-corp"

# Clean restart
cd /home/rod/rod-corp
./stop_system.sh
sleep 5
./start_system.sh
```

#### Database Connection Issues:
```bash
# Test MSSQL connectivity
rod-corp-test-db

# Check local fallback database
ls -la ~/.rod_corp_local.db

# Verify fallback database content
sqlite3 ~/.rod_corp_local.db ".tables"
```

---

### 4. Environment Management Issues

#### Symptoms:
```bash
❌ Environment activation failed
⚠️  Mamba not available, using system environment
⚠️  Environment 'env_ollama' not found
```

#### Solutions:

**Step 1: Check Mamba Installation**
```bash
# Check if mamba is available
which mamba
mamba --version

# Check conda if mamba not found
which conda
conda --version
```

**Step 2: List Available Environments**
```bash
# Show all environments
mamba env list
# or
conda env list

# Check our environment mappings
ai-envs
```

**Step 3: Fix Environment Issues**
```bash
# Reinitialize mamba
mamba init

# Reload shell configuration
source ~/.bashrc

# Try manual activation
mamba activate env_ollama
```

**Step 4: Create Missing Environments**
```bash
# Create basic ollama environment
mamba create -n env_ollama python=3.9

# Activate and install ollama
mamba activate env_ollama
# Install ollama following their documentation
```

#### Fallback to System Environment:
```bash
# Force system environment mode
export AI_CURRENT_ENV="system"
export AI_ENV_PREPARED="false"

# Verify system has required tools
which python
which node
which curl
```

---

### 5. Network and Connectivity Issues

#### Symptoms:
```bash
❌ MSSQL Server: UNREACHABLE (10.0.0.2:1433)
timeout: connection timed out
curl: (7) Failed to connect to localhost port 18000
```

#### Solutions:

**Step 1: Basic Network Diagnostics**
```bash
# Check general connectivity
ping -c 3 8.8.8.8

# Check specific server
ping -c 3 10.0.0.2

# Check DNS resolution
nslookup 10.0.0.2
```

**Step 2: Port-Specific Testing**
```bash
# Test Rod-Corp service ports
for port in 18000 17000 15000 16000 5678 9000; do
    echo "Testing port $port..."
    timeout 5 nc -zv localhost $port
done

# Test MSSQL port
timeout 10 nc -zv 10.0.0.2 1433
```

**Step 3: Firewall and Security**
```bash
# Check if UFW is blocking ports
sudo ufw status

# Check what's listening on ports
ss -tulpn | grep -E ':(18000|17000|15000|16000|5678|9000|1433)'

# Check for firewall rules
iptables -L -n
```

**Step 4: Service-Specific Fixes**
```bash
# Restart networking (WSL)
sudo service networking restart

# Check WSL networking
cat /etc/resolv.conf

# Test from Windows host (if applicable)
# Open PowerShell and run:
# Test-NetConnection -ComputerName localhost -Port 18000
```

---

### 6. Performance and Resource Issues

#### Symptoms:
```bash
# Slow startup times
# High memory usage
# Disk space warnings
# Model loading timeouts
```

#### Solutions:

**Step 1: Resource Monitoring**
```bash
# Check disk space
df -h

# Check memory usage
free -h

# Check CPU usage
top -bn1 | head -20

# Check AI-specific processes
ps aux | grep -E "(ollama|claude|qwen|codex)"
```

**Step 2: Clean Up Resources**
```bash
# Clean old context files
find /tmp -name "rod_corp_context_*" -mtime +1 -delete

# Clean old log files
find ~ -name "*.log" -size +100M -exec truncate -s 50M {} \;

# Clean mamba cache
mamba clean --all

# Clean ollama models (if needed)
ollama list | tail -n +2 | head -20  # Review before deleting
```

**Step 3: Optimize Performance**
```bash
# Reduce model sizes (use smaller variants)
ollama pull deepseek-coder:6.7b  # Instead of 33b
ollama pull codellama:7b          # Instead of 34b

# Use faster environments
ai-env-manager activate base  # Lighter than specialized envs
```

**Step 4: Resource Limits**
```bash
# Check system limits
ulimit -a

# Monitor real-time resource usage
htop  # or top

# Check Docker/container resources (if using containers)
docker stats  # if applicable
```

---

## 🔍 Advanced Debugging

### Enable Debug Mode

```bash
# Enable comprehensive debugging
export RODCORP_DEBUG=true
export AI_DEBUG=true

# Run command with debug output
deepseek-full --help 2>&1 | head -50

# Check debug logs
tail -f ~/.rod_corp_init.log
```

### System State Analysis

```bash
# Generate comprehensive system report
check-ai-dependencies > system_report.txt

# Environment analysis
ai-env-manager check deepseek >> system_report.txt

# Network connectivity report
debug_network_connectivity >> system_report.txt

# Database connectivity report
debug_database_connectivity >> system_report.txt
```

### Log Analysis

```bash
# Recent initialization attempts
tail -50 ~/.rod_corp_init.log

# Recent dependency checks
tail -50 ~/.ai_dependencies.log

# Recent environment changes
tail -50 ~/.ai_env_manager.log

# System errors
journalctl --user -f | grep -i "rod-corp\|ai-agent\|ollama"
```

---

## 🛠️ Repair and Recovery Procedures

### Complete System Reset

**If everything fails, follow this sequence:**

```bash
# 1. Backup current configuration
backup-bashrc emergency

# 2. Stop all services
pkill -f "ollama"
cd /home/rod/rod-corp && ./stop_system.sh

# 3. Reset to known good state
cp ~/.bashrc_backups/bashrc_manual_20250921_091901.bak ~/.bashrc

# 4. Reload configuration
source ~/.bashrc

# 5. Restart services
ollama serve &
cd /home/rod/rod-corp && ./start_system.sh

# 6. Test basic functionality
ai-help
ai-status
```

### Environment Recovery

```bash
# Reset mamba environments
mamba clean --all
mamba update --all

# Recreate critical environments
mamba create -n env_ollama python=3.9
mamba create -n env_pytorch_transformers python=3.9 pytorch transformers

# Reinstall ollama if needed
# Follow official installation instructions
```

### Database Recovery

```bash
# Reset local fallback database
rm ~/.rod_corp_local.db
check-ai-dependencies database  # Will recreate

# Test MSSQL connectivity
rod-corp-test-db

# If MSSQL permanently unavailable, configure permanent SQLite mode
export ROD_CORP_DB_FALLBACK="sqlite"
export ROD_CORP_DB_PATH="$HOME/.rod_corp_local.db"
```

---

## 📊 Health Monitoring and Maintenance

### Regular Maintenance Tasks

**Daily:**
```bash
# Quick health check
ai-status

# Check disk space
df -h

# Review recent errors
tail -20 ~/.rod_corp_init.log
```

**Weekly:**
```bash
# Comprehensive system check
check-ai-dependencies

# Clean up old files
find /tmp -name "rod_corp_context_*" -mtime +7 -delete

# Backup configuration
backup-bashrc manual

# Update system
cd /home/rod/rod-corp && git pull
```

**Monthly:**
```bash
# Generate health report
generate_exception_report 30

# Review and optimize environments
ai-envs
mamba clean --all

# Update Ollama models
ollama list | tail -n +2 | while read model _; do
    echo "Updating $model..."
    ollama pull "$model"
done
```

### Monitoring Scripts

**Create monitoring cron job:**
```bash
# Add to crontab (crontab -e)
*/15 * * * * /home/rod/.local/bin/check-ai-dependencies >/dev/null 2>&1
0 2 * * * find /tmp -name "rod_corp_context_*" -mtime +1 -delete
0 6 * * 0 /home/rod/.local/bin/backup-bashrc auto
```

---

## 🆘 Getting Help

### Self-Service Diagnostics

1. **Start with quick health check:** `ai-status`
2. **Check specific components:** `check-ai-dependencies [component]`
3. **Review logs:** `tail -f ~/.rod_corp_init.log`
4. **Test individual components:**
   - Network: `check-ai-dependencies network`
   - Database: `check-ai-dependencies database`
   - Ollama: `check-ai-dependencies ollama`

### Information to Collect for Support

```bash
# System information
uname -a
cat /etc/os-release

# AI system status
ai-status > support_info.txt
check-ai-dependencies >> support_info.txt

# Environment information
ai-envs >> support_info.txt
echo "Current environment: $(ai-env-manager current)" >> support_info.txt

# Recent logs
echo "=== Recent Initialization Log ===" >> support_info.txt
tail -50 ~/.rod_corp_init.log >> support_info.txt

echo "=== Recent Dependencies Log ===" >> support_info.txt
tail -50 ~/.ai_dependencies.log >> support_info.txt

# Configuration files
echo "=== Bashrc snippet ===" >> support_info.txt
grep -A 20 -B 5 "Enhanced AI Agent" ~/.bashrc >> support_info.txt
```

### Emergency Contacts and Escalation

1. **Check documentation:** `/home/rod/rod-corp/docs/ai-agents/`
2. **Review troubleshooting:** This guide
3. **Collect diagnostic information:** Use commands above
4. **Try system reset:** Follow complete system reset procedure
5. **Document the issue:** Include steps to reproduce

---

## ✅ Verification Checklist

After resolving any issue, verify:

- [ ] `ai-help` shows all available commands
- [ ] `ai-status` reports healthy system state
- [ ] At least one AI agent works: `claude-full --help`
- [ ] Environment management works: `ai-envs`
- [ ] Rod-Corp integration functional (if services available)
- [ ] Backup system operational: `backup-bashrc manual`
- [ ] Logs are being written: `tail -5 ~/.rod_corp_init.log`

---

**Troubleshooting Status:** 🟢 Comprehensive Coverage Available

*Rod-Corp AI Agent Troubleshooting Guide v2.1*
