# PS4 Game Manager - Failover Setup Guide
**Language:** Markdown  
**Lines of Code:** 80  
**File:** FAILOVER_SETUP.md  
**Version:** 2.0.0  
**Project:** PS4 Games Downloader for the Lazy Sanchez  
**Repository:** AI_PS4GameManager  
**Author:** Rod Sanchez
**Created:** 2025-07-12 16:15
**Last Edited:** 2025-07-12 19:40

## 🚀 Quick Start (Failover System)

The new failover system automatically detects your Python environment and configures the best setup for your system.

### Option 1: Batch Script (Windows - Recommended)
```batch
# Simply run this file:
start_ps4_manager.bat
```

### Option 2: Python Script (Cross-Platform)
```bash
python start_server.py
```

## 🔧 Failover Features

### Environment Detection
- **System Python**: Tests your default Python installation
- **Conda Environments**: Automatically finds and tests conda/mamba environments  
- **Auto-Install**: Attempts to install Flask if missing
- **Fallback**: Creates new conda environment if needed

### Port Management
- **Smart Detection**: Tests ports 8000-8005, 8080, 5000, 9000
- **Automatic Failover**: Finds next available port if preferred ones are busy
- **Range Configuration**: Configurable port ranges in settings.ini

### Configuration Management
- **INI File**: Easy-to-edit config/settings.ini file
- **Web Interface**: Configure settings through the web UI
- **Auto-Creation**: Creates default config if none exists
- **Live Updates**: Change games directory without restart

## 📁 Directory Structure

The failover system expects this structure:
```
AI_PS4GameManager/
├── config/
│   └── settings.ini                # Auto-generated configuration
├── src/utils/
│   ├── ps4_game_server.py         # Main server with failover
│   ├── config_manager.py          # Configuration management
│   └── environment_manager.py     # Environment detection
├── start_ps4_manager.bat          # Windows failover script
├── start_server.py               # Python failover script
└── data/ps4_games/               # Your .pkg/.fpkg files here
```

## ⚙️ Configuration File (config/settings.ini)

```ini
[SERVER]
host = 0.0.0.0
port_start = 8000
port_end = 8010
debug = false
environment_preference = auto

[GAMES]
directory = data/ps4_games
supported_extensions = .pkg,.fpkg
auto_scan = true

[SECURITY]
enable_auth = false
username = admin
password = changeme
```

## 🌐 Web Configuration

Access the web interface at `http://localhost:8000` and click **⚙️ Settings** to:

- **Change Games Directory**: Point to your .pkg files location
- **Adjust Port Range**: Set preferred port ranges
- **Enable Authentication**: Add basic security
- **View Environment Info**: See detected Python environments

## 🔄 Failover Sequence

1. **Environment Detection**:
   - Test system Python → Test conda environments → Install packages → Create new environment

2. **Port Detection**:
   - Try 8000 → Try 8001-8005 → Try 8080, 5000, 9000 → Find any available port

3. **Configuration**:
   - Load existing config → Create default config → Update with detected settings

4. **Server Start**:
   - Start with best environment → Use available port → Log startup info

## 🚨 Troubleshooting

### "No Python Environment Found"
```bash
# Option 1: Install Python
# Download from python.org, then:
pip install flask

# Option 2: Use Conda
conda create -n ps4-game-manager python=3.12 flask
conda activate ps4-game-manager
```

### "All Ports in Use"
- Check what's using ports: `netstat -an | findstr :8000`
- Edit `config/settings.ini` to change port range
- Or let the system find any available port

### "Games Directory Not Found"
- Use the web interface Settings → Games tab
- Or edit `config/settings.ini` manually
- Ensure the directory exists and contains .pkg/.fpkg files

### "Server Won't Start"
- Check `logs/ps4_server.log` for detailed errors
- Verify Python environment: `python --version` and `python -c "import flask"`
- Try running manually: `python src/utils/ps4_game_server.py`

## 📊 Startup Examples

### Successful Startup
```
PS4 Game Manager - Failover Startup
==================================================
Working directory: G:\...\AI_PS4GameManager
Python Environment Detection
==================================================
Testing system Python...
  ✓ System Python: C:\Python312\python.exe
✓ Selected environment: system
Port Detection
==================================================
✓ Found available port: 8000
Configuration Setup
==================================================
✓ Configuration created: config/settings.ini
Starting PS4 Game Manager Server
==================================================
Environment: C:\Python312\python.exe
Port: 8000
Server will be accessible at:
  Local:   http://localhost:8000
  Network: http://192.168.1.100:8000
```

### Failover Example
```
Testing system Python...
  ❌ System Python failed: Flask not available
Searching conda environments...
  ✓ Conda ps4-game-manager: C:\...\envs\ps4-game-manager\python.exe
✓ Selected environment: conda-ps4-game-manager
Testing port 8000...
  Port 8000 is in use
Testing port 8001...
  ✓ Port 8001 is available
```

## 🎯 Next Steps

1. **Run the failover script**: `start_ps4_manager.bat` or `python start_server.py`
2. **Add your games**: Copy .pkg/.fpkg files to the games directory
3. **Configure via web**: Open the web interface and adjust settings
4. **Access from network**: Use your PC's IP address to access from other devices

The failover system handles all the complexity automatically - just run the script and start using your PS4 game server!