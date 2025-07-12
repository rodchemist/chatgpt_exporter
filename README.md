Language: Markdown
Lines of Code: 47
File: README.md
Version: 1.0.0
Project: ChatGPT Conversation Exporter
Repository: chatgpt_exporter
Author: Rod Sanchez
Created: 2025-07-12 05:54
Last Edited: 2025-07-12 05:54

# ChatGPT Conversation Exporter

ChatGPT Conversation Exporter is a Python-based GUI tool that extracts and exports your ChatGPT conversations from a ZIP file. It supports multiple export formats including plain text, HTML (with a built-in search), Markdown, and an SQLite database.

## Features

- **Multiple Export Formats:** TXT, HTML, Markdown, and SQLite.
- **Searchable HTML Index:** A dynamically generated HTML index to search conversations by text, title, role, or date.
- **User-Friendly GUI:** Built with Tkinter for easy file and folder selection.
- **Progress Feedback:** Visual progress bar and status updates during the export process.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/roderickks/chatgpt_exporter.git
   cd chatgpt_exporter
   ```
2. **Set Up a Virtual Environment (Optional but recommended):**

   ```bash
   python -m venv venv
   ```
3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the Exporter:

Navigate to the src folder and run the script:

```bash
cd src
python chatgpt_exporter.py
```

Export Directory:

When running the tool, choose your output directory.

ZIP File:

Select the ZIP file that contains your conversations.json. The tool will extract and export the conversations accordingly.

## Project Structure

```
chatgpt_exporter/
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── setup.py
└── src/
    └── chatgpt_exporter.py
```

## Contributing

Contributions, issues, and feature requests are welcome! Please check the issues page for open issues.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
