# Dare FTP Manager

A secure and efficient FTP server management application for Dare Foods internal use. This application allows you to configure, start, monitor, and manage an FTP server for file transfers within the Dare Foods network.

## 🎯 Features

- **Simple FTP Server Management**: Start, stop, and monitor your FTP server
- **Secure Configuration**: Set up secure FTP server settings
- **File Management**: Browse and manage files in the FTP root directory
- **Duplicate Detection**: Automatic identification and handling of duplicate files
- **Real-time Monitoring**: View server logs and status in real-time
- **Cross-platform**: Works on Windows, macOS, and Linux

## 📋 Requirements

- **Node.js**: v16.0.0 or higher
- **Python**: v3.8 or higher
- **Electron**: v27.0.0 or higher

## 🚀 Installation

### Development Setup

1. Clone the repository:
```bash
git clone https://internal-git.darefoods.com/it/dare-ftp-manager.git
cd dare-ftp-manager
```

2. Install dependencies:
```bash
npm install
```

3. Start the application:
```bash
npm start
```

### Docker (WSL)

Build the Docker image and run the application:
```bash
docker build -t dare-ftp .
docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix dare-ftp
```
This container bundles Node, Python and all dependencies so the app can run under WSL.

### Production Build

To create a production build:

```bash
npm run dist
```

This will create installers in the `dist` directory for your platform.

## 💻 Usage

1. **Configuration**: Go to the "Settings" tab to configure your FTP server
   - Set the IP address (default: 127.0.0.1)
   - Set the port (default: 21)
   - Choose a root directory for FTP files

2. **Starting the Server**: Navigate to the "Dashboard" tab and click "Start Server"

3. **Monitoring**: View server logs and status in real-time

4. **File Management**: Browse and manage files in the FTP root directory

## 🛠️ Development

### Project Structure

```
dare-ftp-manager/
├── src/                    # Source code
│   ├── assets/            # Images, fonts, styles
│   ├── components/        # React components
│   ├── utils/            # Utility functions
│   ├── config/           # Configuration files
│   └── main/             # Main electron process
├── python/               # Python FTP server script
└── docs/                # Documentation
```

### Key Technologies

- **Electron**: Cross-platform desktop application framework
- **React**: UI component library
- **Python**: FTP server implementation using pyftpdlib
- **Socket.IO**: Real-time communication between Electron and Python

## 📝 License

This software is proprietary and confidential. It is developed exclusively for internal use by Dare Foods Limited and its authorized personnel. See the [LICENSE](./LICENSE) file for details.

## 👥 Support

For internal support, please contact the IT department:

- **Email**: it-support@darefoods.com
- **Phone**: x6381
- **Contact**: Rodrigo Sanchez

## 🔄 Changelog

See [CHANGELOG.md](./CHANGELOG.md) for a list of changes in each version.