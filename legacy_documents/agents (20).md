# Language: Markdown
# Lines of Code: 30
# File: AGENTS.md
# Version: 1.0.0
# Project: PS4 Games Downloader for the Lazy Sanchez
# Repository: AI_PS4GameManager
# Author: Rod Sanchez
# Created: 2025-07-13 00:00
# Last Edited: 2025-07-13 00:00

## Troubleshooting and Setup Tasks
0. Ensure the respository works with relative position to not affect the locations
1. **Activate Environment**
   - `conda activate ps4-game-manager`
   - Install requirements: `pip install -r requirements.txt`
2. **Verify Directory Structure**
   - Ensure `web/html/index.html` exists.
   - Confirm `data/ps4_games/` contains your `.pkg` files.
3. **Check Template Path**
   - In `src/utils/ps4_game_server.py`, set:
     ```python
     app = Flask(__name__, template_folder="web/html", static_folder="web")
     ```
   - Run the server from the repository root.
4. **Start the Server**
   - Windows: `run_server.bat`
   - Linux/Mac: `./run_server.sh`
   - Or manually:
     ```bash
     conda activate ps4-game-manager
     python src/utils/ps4_game_server.py
     ```
5. **Access Interface**
   - Open `http://localhost:8000` in your browser.
6. **Review Logs**
   - Logs are stored in `logs/app.log`.
   - Check for `TemplateNotFound` errors and verify paths.
7. **Validate Repository**
   - Run `python universal_file_validator.py` to ensure headers and structure.

Test it and ensure it works. If you could not propose tasks to validate the and confirm solution 