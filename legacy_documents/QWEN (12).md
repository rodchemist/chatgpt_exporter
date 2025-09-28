# LOGS Repository - Qwen Context Documentation

This repository contains scripts and configurations for managing terminal session logs and system logging.

## Directory Structure

```
LOGS/
├── system_logs/
│   └── app.log              # Application logging
└── terminal_logs/
    └── _helpers/
        ├── Select-Environment.ps1      # PowerShell script for selecting conda environments
        ├── start_logged_bash.sh        # Bash script for starting logged terminal sessions
        └── Start-LoggedPowerShell.ps1  # PowerShell script for starting logged terminal sessions
```

## Components

### Terminal Logging Helpers

#### Select-Environment.ps1
A PowerShell script that displays a menu of available conda environments and allows the user to select and activate one.

#### start_logged_bash.sh
A bash script that:
- Creates a dedicated log directory for a terminal session
- Sets the terminal tab name
- Logs all commands with timestamps to a session log file
- Optionally executes an initial command
- Customizes the bash prompt with the tab name

#### Start-LoggedPowerShell.ps1
A PowerShell script that:
- Creates a dedicated log directory for a PowerShell session
- Sets the terminal tab name
- Starts PowerShell transcript logging
- Optionally executes an initial command
- Provides a `Stop-Logging` function to end transcription

### System Logs

#### app.log
Contains application-level logs with timestamps, including information about:
- Directory creation
- Repository validation
- Git operations (fetching, merging, pushing)