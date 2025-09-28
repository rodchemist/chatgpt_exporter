# PS4GameManager Unified 🎮

A comprehensive PS4/PS5 game management solution combining local web server capabilities with remote package installation.

## 🚀 Features

- ✅ **Local PS4/PS5 game library management** with database storage
- ✅ **Web-based interface** accessible from any device
- ✅ **Direct installation to PS4/PS5 consoles** via network
- ✅ **Multiple console support** (PS4, PS5, GoldHEN, etaHEN)
- ✅ **Real-time installation progress** tracking
- ✅ **Multiple interface options** (Web, Desktop, PS4 Browser)
- ✅ **Modern responsive design** with dark theme
- ✅ **Game metadata extraction** and organization

## 📁 Project Structure

```
PS4GameManager_rodchem_v2/
├── backend/                 # Python Flask server
│   ├── src/
│   │   ├── core/           # Game management logic
│   │   ├── ps4/            # PS4/PS5 communication
│   │   ├── utils/          # Utility functions
│   │   └── api/            # API endpoints
│   ├── config/             # Configuration files
│   ├── data/               # Game storage & database
│   └── logs/               # Application logs
├── frontend/               # Modern Vue.js web interface
│   ├── src/
│   │   ├── components/     # Vue 3 components
│   │   ├── views/          # Page views
│   │   ├── composables/    # Vue 3 composables
│   │   └── reference/      # Legacy Vue 2 components
│   └── public/             # Static assets
├── desktop/                # Electron wrapper (future)
├── legacy/                 # Original projects (preserved)
│   ├── electron-app/       # Original Electron app
│   └── python-server/      # Original Python server
├── docs/                   # Documentation and guides
└── scripts/                # Utility scripts
```

## 🚀 Quick Start

### Backend (Python Server)
```bash
cd backend
pip install -r requirements.txt
python start_server.py
```

### Frontend Development (Coming Soon)
```bash
cd frontend
npm install
npm run dev
```

### Desktop App (Legacy)
```bash
cd legacy/electron-app
npm install
npm run dev
```

## 🔧 Configuration

- **Games Directory**: Place your `.pkg` and `.fpkg` files in `backend/data/games/`
- **Server Settings**: Configure in `backend/config/settings.ini`
- **Network**: Server runs on `http://localhost:8000` by default

## 📖 Documentation

- [Python Server Guide](docs/python-server-readme.md)
- [Electron App Documentation](docs/electron-app-readme.md)
- [Troubleshooting Guide](docs/troubleshooting.md)
- [Migration Guide](docs/failover-guide.md)

## 🔄 Migration Status

This project represents the unification of:
1. **AI_PS4GameManager** (Python web server)
2. **PS4GameManager_rodchem** (Electron desktop app)

### Phase 1: ✅ Complete
- [x] File migration and organization
- [x] Backend structure setup
- [x] Legacy preservation

### Phase 2: 🚧 In Progress
- [ ] PS4/PS5 API integration to Python
- [ ] Modern Vue 3 frontend
- [ ] Real-time communication
- [ ] Enhanced UI/UX

### Phase 3: 📋 Planned
- [ ] Desktop Electron wrapper
- [ ] Mobile optimization
- [ ] Advanced features

## 🛠️ Technology Stack

- **Backend**: Python 3.12, Flask, SQLite
- **Frontend**: Vue 3, TypeScript, Vite (planned)
- **Desktop**: Electron (wrapper)
- **Database**: SQLite with migrations
- **Communication**: WebSockets, REST API

## 🤝 Contributing

This is a personal project, but feel free to explore the code and suggest improvements!

## 📄 License

Personal use project by RodChem.

---
*🧪 Developed by RodChem - Chemistry Meets Gaming Technology*
