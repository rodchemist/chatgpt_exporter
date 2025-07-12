#!/usr/bin/env bash
# Language: Bash 5.0
# Lines of Code: 3
# File: start_app.sh
# Version: 1.0.02
# Project: ChatGPT Conversation Exporter
# Repository: chatgpt_exporter
# Author: Rod Sanchez
# Created: 2025-07-13 10:00
# Last Edited: 2025-07-13 10:00

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR"
python -m uvicorn src.utils.api:app --reload

