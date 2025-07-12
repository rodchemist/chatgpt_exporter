# ChatGPT Conversation Exporter

ChatGPT Conversation Exporter is a Python-based tool to extract and export your ChatGPT conversations from a ZIP file. It now includes a modern web interface powered by FastAPI and WebSockets.

## Features

- **Multiple Export Formats:** TXT, HTML, Markdown, and SQLite.
- **Searchable HTML Index:** A dynamically generated HTML index to search conversations by text, title, role, or date.
- **User-Friendly Web UI:** Upload ZIP files directly in the browser.
- **Real-Time Progress:** WebSocket updates while processing.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Run the FastAPI server:

```bash
python src/utils/server.py
```

Then open `web/html/index.html` in your browser to use the interface.

## Project Structure

```
chatgpt_exporter/
├── src/
│   └── utils/
│       ├── exporter_utils.py
│       └── server.py
├── web/
│   ├── html/
│   │   └── index.html
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── scripts.js
├── config/
├── docs/
├── logs/
│   └── version_log.txt
├── data/
│   └── cache/
├── requirements.txt
└── README.md
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
