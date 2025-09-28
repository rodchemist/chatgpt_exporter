# PS4 Games Downloader for the Lazy Sanchez Setup Guide
**Language:** Markdown
**Lines of Code:** 277
**File:** README.md
**Version:** 1.0.3
**Project:** PS4 Games Downloader for the Lazy Sanchez
**Repository:** AI_PS4GameManager
**Author:** Rod Sanchez
**Created:** 2025-07-12 15:30
**Last Edited:** 2025-07-13 00:00
 

## Overview

This PS4 Games Downloader for the Lazy Sanchez allows you to host your legally owned PS4 game backups (fpkg format) on your local network, making them accessible for installation across multiple devices without needing external storage.
For troubleshooting and task guidance, see **AGENTS.md** in the repository root. This file lists setup steps, server commands, and debugging tips.


## Prerequisites

- Python 3.12 or higher
- Your PS4 game backups in .pkg format
- Local network access
- Flask and required Python packages

## Installation Steps

### 1. Directory Structure Setup

Create the following directory structure:

```
AI_PS4GameManager/
├── src/utils/
│   └── ps4_game_server.py
├── web/
│   ├── html/
│   │   └── index.html
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   └── scripts.js
│   └── static/
│       ├── css/
│       │   └── styles.css
│       └── js/
│           └── scripts.js
├── data/
│   ├── ps4_games/          # Place your .pkg files here
│   └── cache/              # SQLite database storage
├── logs/                   # Server logs
├── config/                 # Configuration files
└── README.md
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Your Game Files

1. Create the `data/ps4_games/` directory
2. Copy your .pkg files into this directory
3. Ensure files follow a consistent naming convention (recommended):
   - `Game_Title_CUSA12345_v1.00.pkg`
   - Example: `Spider_Man_CUSA02299_v1.08.pkg`

### 4. Start the Server

Run the cross-platform startup script:

```bash
# Linux/macOS
./run_server.sh

# Windows
run_server.bat
```

This will create `config/settings.ini` on first run and automatically select an available Python environment.

### Game Management
- **Automatic Scanning:** Detects .pkg files in the games directory
- **Metadata Storage:** Stores game information in SQLite database
- **File Integrity:** SHA256 hash verification for file safety
- **Download Tracking:** Monitors installation counts and access history

### Web Interface
- **Responsive Design:** Works on desktop, tablet, and mobile devices
- **Search Functionality:** Find games by title, ID, or filename
- **Real-time Stats:** Total games, storage usage, server status
- **Download Management:** Direct download links with progress tracking

### PS4 Browser Compatibility
For the best experience on the PlayStation 4 browser, use the simplified
interface at `/ps4` or the ultra-minimal version at `/ps4/simple`.
Example: `http://YOUR_PC_IP:8000/ps4`

### Network Features
- **Multi-device Access:** Available to all devices on your network
- **Concurrent Downloads:** Multiple users can download simultaneously
- **Bandwidth Management:** Efficient file serving with Flask
- **Security:** Local network only, no external access

## Configuration Options

### Custom Game Directory

Edit `config/settings.ini` to set your games directory:

```ini
[GAMES]
directory = /path/to/your/games
```

### Server Port Configuration

Configure the port range in `config/settings.ini`:

```ini
[SERVER]
port_start = 8000
port_end = 8010
```

### Environment Packages

Configure required Python packages for environment detection:

```ini
[ENVIRONMENT]
required_packages = flask,pathlib2,blinker
```

### Web Paths

If you move the web interface, update these paths:

```ini
[WEB]
template_dir = web/html
static_dir = static
```

### Database Location

Update the database path in the `DATABASE` section:

```ini
[DATABASE]
path = custom/path/ps4_games.db
```

### API Key

Set an API key for protected endpoints in the `SECURITY` section:

```ini
[SECURITY]
api_key = mysecretkey
```

## File Naming Convention

For best results, name your .pkg files using this format:
- `{Game_Title}_{CUSA_ID}_{Version}.pkg`
- Replace spaces in game titles with underscores
- Include the official CUSA ID if known
- Add version number (e.g., v1.00, v1.08)

Examples:
- `God_of_War_CUSA07408_v1.35.pkg`
- `Horizon_Zero_Dawn_CUSA01967_v1.52.pkg`
- `The_Last_of_Us_Part_II_CUSA07820_v1.09.pkg`

## Troubleshooting

### Server Won't Start
- Check Python version: `python --version`
- Verify all dependencies are installed
- If no Python environment is detected, check logs from EnvironmentManager.
- Ensure port 5000 isn't in use by another application
- Check file permissions on directories

### Games Not Appearing
- Click "Scan Games Directory" button
- Verify .pkg files are in the correct directory
- Check file permissions
- Review server logs in `logs/ps4_server.log`

### Network Access Issues
- Verify firewall settings allow port 5000
- Confirm devices are on the same network
- Check IP address configuration
- Test with `http://[PC_IP]:5000` format

### Download Problems
- Ensure sufficient disk space on target device
- Check network stability
- Verify file integrity (server calculates SHA256 hashes)
- Try refreshing the browser and retrying
- If downloads return a 500 error with a missing file path, run "Scan Games Directory" or restart the server to refresh database paths

## Security Considerations

- **Local Network Only:** Server binds to all interfaces but should only be accessible locally
- **No Authentication:** Basic setup has no user authentication
- **File Access:** Only serves files from the designated games directory
- **Logging:** All downloads and access attempts are logged

## Advanced Configuration

### Adding Authentication

To add basic authentication, modify the Flask app:

```python
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    return username == 'admin' and password == 'your_password'

@app.route('/')
@auth.login_required
def index():
    return render_template('index.html')
```

### Custom Templates

The web interface uses the `web/html/templates/` directory for Flask templates. You can customize:
- Color schemes in `web/css/styles.css`
- Layout in `web/html/index.html`
- Functionality in `web/js/scripts.js`

### Database Backup

Regularly backup your game database:

```bash
cp data/cache/ps4_games.db data/cache/ps4_games_backup_$(date +%Y%m%d).db
```

## Performance Optimization

### Large Libraries
- For 100+ games, consider pagination in the web interface
- Enable database indexing for faster searches
- Use SSD storage for better I/O performance

### Network Optimization
- Use wired connections for large file transfers
- Configure QoS on your router to prioritize game downloads
- Consider setting up multiple server instances for load balancing

## Legal Notice

This tool is designed for managing your legally owned PS4 game backups. Ensure you:
- Only use games you legally own
- Comply with your local laws regarding game backups
- Respect software licensing agreements
- Do not distribute copyrighted content

## Support and Updates

Check the repository for updates and submit issues for bugs or feature requests. The modular design allows for easy customization and expansion of features.

## Version History

- **v1.0.0** (2025-07-12): Initial release with core functionality
  - Web-based game management interface
  - SQLite database for metadata
  - Network-accessible downloads
  - Responsive design for all devices