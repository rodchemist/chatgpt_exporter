# Dare FTP Manager

## Repository Structure

```
dare-ftp-manager/
├── README.md                 # Project overview & setup instructions
├── package.json             # Dependencies & scripts
├── .gitignore              # Version control exclusions
├── LICENSE                 # Dare proprietary license
├── CHANGELOG.md            # Version history
├── src/                    # Source code
│   ├── assets/            # Images, fonts, styles
│   │   ├── images/
│   │   │   └── dare-logo.png
│   │   └── styles/
│   │       └── dare-brand.css
│   ├── components/        # Reusable UI components
│   │   ├── DareHeader.jsx
│   │   ├── StatusPanel.jsx
│   │   ├── ConfigManager.jsx
│   │   ├── LogViewer.jsx
│   │   └── FileManager.jsx
│   ├── utils/            # Utility functions
│   │   ├── fileHelpers.js
│   │   ├── serverUtils.js
│   │   └── validation.js
│   ├── config/           # Configuration files
│   │   ├── appConfig.js
│   │   └── serverConfig.js
│   └── main/             # Main application logic
│       ├── electronMain.js
│       ├── ipcHandlers.js
│       └── pythonRunner.js
├── python/               # Python FTP server script
│   └── ftp_server.py
├── tests/                # Test files
├── docs/                # Additional documentation
│   ├── user-guide.md
│   └── api-docs.md
├── build/               # Build output (auto-generated)
└── dist/               # Distribution files (auto-generated)
```