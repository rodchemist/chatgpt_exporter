@echo off
REM Language: Batch 10
REM Lines of Code: 2
REM File: start_app.bat
REM Version: 1.0.02
REM Project: ChatGPT Conversation Exporter
REM Repository: chatgpt_exporter
REM Author: Rod Sanchez
REM Created: 2025-07-13 10:00
REM Last Edited: 2025-07-13 10:00

cd %~dp0
python -m uvicorn src.utils.api:app --reload

