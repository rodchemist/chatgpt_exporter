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

Run the FastAPI server for the web interface using the provided scripts:

```bash
./start_app.sh   # Unix/macOS
:: or
start_app.bat    # Windows
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
├── start_app.sh
├── start_app.bat
└── README.md
```

## Contributing

Issues and pull requests are welcome!

## License

MIT
