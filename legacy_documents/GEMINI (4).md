# GEMINI.md

## Project Overview

This project is a terminal launcher for Windows, designed to open multiple terminal tabs with specific configurations. It comes in two versions:

*   **`open_terminals_simple.py`**: A simple Tkinter GUI application that launches a predefined set of tabs ('Gemini', 'Codex', 'Claude', 'Scripts execution') in Windows Terminal. It supports both standard Windows command prompt and WSL (Windows Subsystem for Linux). It includes a feature to re-launch itself with administrator privileges.

*   **`terminal_launcher_advanced.py`**: A more feature-rich Tkinter application that provides a sophisticated GUI for launching terminals. It supports multiple terminal emulators (Windows Terminal, Wezterm, Alacritty, Tabby, Hyper), allows for custom tab names and presets, and has WSL integration. It also includes a file indexing feature to catalog files within a directory, and the ability to save and load configurations. This advanced version can also be run from the command line.

The project includes a batch file (`terminal_launcher_runner.bat`) to facilitate running the advanced launcher with necessary checks and setup.

## Building and Running

### Running the Advanced Launcher (Recommended)

The most convenient way to run the advanced terminal launcher is by using the provided batch file:

```batch
terminal_launcher_runner.bat
```

This script performs the following actions:
1.  Checks for administrator privileges and requests them if necessary.
2.  Verifies that Python is installed.
3.  Checks for the availability of WSL and supported terminal emulators.
4.  Launches the `terminal_launcher_advanced.py` script.

### Running the Python Scripts Directly

You can also run the Python scripts directly using a Python interpreter.

**For the simple version:**

```bash
python open_terminals_simple.py
```

**For the advanced version:**

```bash
python terminal_launcher_advanced.py
```

The advanced version also supports command-line arguments for indexing and launching without the GUI.

## Development Conventions

*   **GUI:** The graphical user interfaces are built using Python's built-in `tkinter` library.
*   **Python:** The code follows standard Python conventions. The advanced script shows usage of dataclasses, type hinting, and more modern Python features.
*   **Logging:** The application creates a `logs_terminals` directory to store logs from the launcher and the terminal sessions.
*   **Cross-platform:** While the GUI is cross-platform, the terminal launching logic is specific to Windows and WSL.

## Key Files

*   **`terminal_launcher_advanced.py`**: The main script for the advanced terminal launcher application. Contains the GUI code, terminal launching logic, and file indexing functionality.
*   **`open_terminals_simple.py`**: A simplified version of the terminal launcher with a basic GUI and hardcoded tab names.
*   **`terminal_launcher_runner.bat`**: A batch script for running the advanced terminal launcher. It handles environment checks and elevates privileges.
*   **`AGENTS.md`**: General repository guidelines that are not specific to this project.
*   **`install_agents_cli.sh`**: A shell script for setting up a CLI environment for AI agents. This is a separate utility and not part of the terminal launcher itself.
*   **`logs_terminals/`**: The directory where logs from the terminal sessions are stored.
