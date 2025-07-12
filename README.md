# Language: text
# Lines of Code: 48
# File: README.md
# Version: 1.0.01
# Project: ChatGPT Conversation Exporter
# Repository: chatgpt_exporter
# Author: Rod Sanchez
# Created: 2025-07-12 05:54
# Last Edited: 2025-07-12 14:30

# ChatGPT Conversation Exporter

ChatGPT Conversation Exporter provides both a Tkinter GUI and a modern web interface for exporting conversations from a ChatGPT ZIP archive. Supported export formats include plain text, HTML, Markdown, and SQLite.

## Features

- **Multiple Export Formats**: TXT, HTML, Markdown, and SQLite.
- **Searchable HTML Index**: Quickly search conversations by text, title, role, or date.
- **Web Interface**: Upload ZIP files directly in your browser and download processed exports.
- **Progress Feedback**: Real-time updates via WebSocket during processing.

## Installation

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

Run the Tkinter exporter:

```bash
cd src
python chatgpt_exporter.py
```

Run the FastAPI server for the web interface:

```bash
uvicorn src.utils.api:app --reload
```

Open `web/html/index.html` in your browser and start exporting.

## Project Structure

```
chatgpt_exporter/
├── config/
├── data/cache/
├── docs/
├── logs/
├── src/
│   ├── chatgpt_exporter.py
│   └── utils/
│       └── api.py
├── web/
│   ├── css/
│   │   └── styles.css
│   ├── html/
│   │   └── index.html
│   └── js/
│       └── scripts.js
└── README.md
```

## Contributing

Issues and pull requests are welcome!

## License

MIT
