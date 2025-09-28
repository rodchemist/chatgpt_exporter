# Dare Internal Development Standards

## 🎯 Overview
These standards ensure all internal applications, scripts, and tools maintain consistent branding, functionality, and code quality across Dare's development ecosystem.

## 📁 Repository Structure Standard

### Required Structure
```
project-name/
├── README.md                 # Project overview & setup instructions
├── package.json             # Dependencies & scripts
├── .gitignore              # Version control exclusions
├── LICENSE                 # MIT or company license
├── CHANGELOG.md            # Version history
├── src/                    # Source code
│   ├── assets/            # Images, fonts, styles
│   │   ├── images/
│   │   │   └── dare-logo.png
│   │   └── styles/
│   │       └── dare-brand.css
│   ├── components/        # Reusable UI components
│   ├── utils/            # Utility functions
│   ├── config/           # Configuration files
│   └── main/             # Main application logic
├── tests/                # Test files
├── docs/                # Additional documentation
├── build/               # Build output (auto-generated)
└── dist/               # Distribution files (auto-generated)
```

## 🎨 Branding Requirements

### Visual Identity
- **Logo**: Use official Dare logo in header/title bar
- **Colors**: Primary red (#E31E24), supporting palette as defined
- **Typography**: System fonts with proper hierarchy
- **Styling**: Use provided Dare brand stylesheet

### Application Naming
- **Format**: `Dare [Function] [Type]`
- **Examples**: 
  - "Dare FTP Manager"
  - "Dare Image Processor"
  - "Dare Network Tools"

## 🛠️ Development Standards

### Code Organization
```javascript
// File naming: camelCase for files, PascalCase for components
src/
├── components/
│   ├── DareHeader.jsx
│   ├── StatusPanel.jsx
│   └── ConfigManager.jsx
├── utils/
│   ├── fileHelpers.js
│   ├── networkUtils.js
│   └── validation.js
└── config/
    ├── appConfig.js
    └── serverConfig.js
```

### Required Documentation
1. **README.md** with setup instructions
2. **Inline code comments** for complex logic
3. **API documentation** for exposed functions
4. **User guide** for end-user applications

### Error Handling & Logging
```javascript
// Standard error handling pattern
try {
  // Operation
  console.log(`[DARE-APP] Success: ${operation}`);
} catch (error) {
  console.error(`[DARE-APP] Error: ${error.message}`);
  // User-friendly error display
}
```

## 📱 Application Types & Guidelines

### 1. Electron Desktop Apps

#### Required Components
- **Title Bar**: Dare logo + app name
- **Status Bar**: Connection/operation status
- **Menu System**: Standard Dare menu structure
- **Error Dialogs**: Branded error messaging

#### Example Implementation (FTP Server App)
```javascript
// main.js - Electron main process
const { app, BrowserWindow, Menu } = require('electron');

function createWindow() {
  const mainWindow = new BrowserWindow({
    width: 1000,
    height: 700,
    icon: path.join(__dirname, 'src/assets/images/dare-logo.png'),
    titleBarStyle: 'hidden',
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    }
  });

  // Set application menu
  const menu = Menu.buildFromTemplate([
    {
      label: 'Dare FTP Manager',
      submenu: [
        { label: 'About', role: 'about' },
        { type: 'separator' },
        { label: 'Quit', role: 'quit' }
      ]
    }
  ]);
  Menu.setApplicationMenu(menu);
}
```

### 2. Python Scripts

#### Required Structure
```python
#!/usr/bin/env python3
"""
Dare [Script Purpose]
Author: [Developer Name]
Version: 1.0.0
Description: [Brief description]
"""

import os
import sys
import logging
from datetime import datetime

# Dare standard logging setup
def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='[DARE-%(name)s] %(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(f'dare_{os.path.basename(__file__)}.log'),
            logging.StreamHandler(sys.stdout)
        ]
    )

# Standard configuration class
class DareConfig:
    def __init__(self):
        self.app_name = "Dare Script"
        self.version = "1.0.0"
        self.author = "Dare IT Team"
```

### 3. Web Applications

#### Required Elements
- Dare navigation header
- Responsive design using brand stylesheet
- Proper error pages with Dare branding
- Footer with company information

## 🔧 Converting Scripts to Electron Apps

### Step-by-Step Process (FTP Server Example)

#### 1. Project Setup
```bash
mkdir dare-ftp-manager
cd dare-ftp-manager
npm init -y
npm install electron --save-dev
npm install express socket.io --save
```

#### 2. Create Electron Wrapper
```javascript
// src/main/electronMain.js
const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const { spawn } = require('child_process');

let mainWindow;
let ftpProcess;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1000,
    height: 700,
    icon: path.join(__dirname, '../assets/images/dare-logo.png'),
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    }
  });

  mainWindow.loadFile('src/renderer/index.html');
}

// Handle FTP server start/stop
ipcMain.handle('start-ftp-server', async (event, config) => {
  try {
    ftpProcess = spawn('python', ['src/python/ftp_server.py'], {
      env: { ...process.env, ...config }
    });
    
    ftpProcess.stdout.on('data', (data) => {
      mainWindow.webContents.send('ftp-log', data.toString());
    });
    
    return { success: true, message: 'FTP Server started' };
  } catch (error) {
    return { success: false, message: error.message };
  }
});

app.whenReady().then(createWindow);
```

#### 3. Create UI Components
```jsx
// src/renderer/components/FTPManager.jsx
import React, { useState, useEffect } from 'react';
const { ipcRenderer } = window.require('electron');

const FTPManager = () => {
  const [serverStatus, setServerStatus] = useState('stopped');
  const [logs, setLogs] = useState([]);
  const [config, setConfig] = useState({
    address: '10.0.1.251',
    port: '21',
    root: 'C:\\00_start\\auto_update_images'
  });

  const startServer = async () => {
    const result = await ipcRenderer.invoke('start-ftp-server', config);
    if (result.success) {
      setServerStatus('running');
    }
  };

  useEffect(() => {
    ipcRenderer.on('ftp-log', (event, log) => {
      setLogs(prev => [...prev, log]);
    });
  }, []);

  return (
    <div className="container mt-4">
      <div className="card">
        <div className="card-header">
          <h3 className="text-primary">FTP Server Configuration</h3>
        </div>
        <div className="card-body">
          <div className="row">
            <div className="col-6">
              <div className="form-group">
                <label className="form-label">Server Address</label>
                <input 
                  type="text" 
                  className="form-control"
                  value={config.address}
                  onChange={(e) => setConfig({...config, address: e.target.value})}
                />
              </div>
            </div>
            <div className="col-6">
              <div className="form-group">
                <label className="form-label">Port</label>
                <input 
                  type="text" 
                  className="form-control"
                  value={config.port}
                  onChange={(e) => setConfig({...config, port: e.target.value})}
                />
              </div>
            </div>
          </div>
          
          <div className="form-group">
            <label className="form-label">Root Directory</label>
            <input 
              type="text" 
              className="form-control"
              value={config.root}
              onChange={(e) => setConfig({...config, root: e.target.value})}
            />
          </div>

          <div className="d-flex gap-2 mt-3">
            <button 
              className="btn btn-primary"
              onClick={startServer}
              disabled={serverStatus === 'running'}
            >
              Start Server
            </button>
            <button 
              className="btn btn-secondary"
              disabled={serverStatus === 'stopped'}
            >
              Stop Server
            </button>
          </div>

          <div className="mt-3">
            <span className={`badge ${serverStatus === 'running' ? 'bg-success' : 'bg-secondary'}`}>
              Status: {serverStatus}
            </span>
          </div>
        </div>
      </div>

      <div className="card mt-4">
        <div className="card-header">
          <h4>Server Logs</h4>
        </div>
        <div className="card-body">
          <div className="logs-container" style={{height: '200px', overflow: 'auto'}}>
            {logs.map((log, index) => (
              <div key={index} className="log-entry">
                {log}
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default FTPManager;
```

## 📋 Quality Checklist

### Before Release
- [ ] Dare logo prominently displayed
- [ ] Brand colors implemented correctly
- [ ] Error handling with user-friendly messages
- [ ] Logging implemented with standard format
- [ ] README.md completed
- [ ] Version number updated
- [ ] All dependencies documented
- [ ] Cross-platform compatibility tested

### Code Review Requirements
- [ ] Follows naming conventions
- [ ] Proper error handling
- [ ] Security considerations addressed
- [ ] Performance optimization applied
- [ ] Documentation complete

## 🚀 Deployment Standards

### Version Control
```bash
# Standard commit format
git commit -m "feat: add FTP server status monitoring"
git commit -m "fix: resolve connection timeout issue"
git commit -m "docs: update configuration guide"
```

### Release Process
1. **Update version** in package.json/setup.py
2. **Update CHANGELOG.md** with new features/fixes
3. **Create release branch** from develop
4. **Test thoroughly** on target platforms
5. **Tag release** with semantic versioning
6. **Deploy** to internal distribution system

### Distribution
- **Electron Apps**: Package for Windows/Mac/Linux
- **Python Scripts**: Provide requirements.txt and setup instructions
- **Web Apps**: Deploy to internal server with HTTPS

## 🔐 Security Standards

### Required Practices
- **No hardcoded credentials** (use config files)
- **Input validation** for all user inputs
- **Secure communication** (HTTPS/TLS where applicable)
- **Error messages** that don't expose system information
- **Regular dependency updates**

### Example Secure Configuration
```javascript
// config/appConfig.js
const config = {
  server: {
    host: process.env.FTP_HOST || '127.0.0.1',
    port: process.env.FTP_PORT || 21,
    username: process.env.FTP_USER || 'admin',
    password: process.env.FTP_PASS || 'changeme'
  },
  security: {
    allowedIPs: process.env.ALLOWED_IPS?.split(',') || ['127.0.0.1'],
    maxConnections: parseInt(process.env.MAX_CONNECTIONS) || 10
  }
};
```

## 📞 Support & Resources

### Internal Resources
- **Brand Assets**: Contact IT for official logo files
- **Code Templates**: Available in company repository
- **Style Guide**: Complete CSS framework provided
- **Testing Environment**: [Internal server details]

### Getting Help
- **Technical Issues**: IT Support ticket system
- **Design Questions**: Brand team consultation
- **Code Review**: Senior developer assignment
- **Deployment**: DevOps team assistance

---

**These standards ensure all Dare internal applications maintain professional quality, consistent branding, and reliable functionality while supporting our company's technical excellence.**