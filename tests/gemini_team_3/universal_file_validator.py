# Language: Python 3.12
# Lines of Code: 64
# File: universal_file_validator.py
# Version: 1.0.01
# Project: ChatGPT Conversation Exporter
# Repository: chatgpt_exporter
# Author: Rod Sanchez
# Created: 2025-07-12 14:30
# Last Edited: 2025-07-12 14:30

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

EXPECTED_DIRS = [
    "src/utils",
    "web/html",
    "web/css",
    "web/js",
    "config",
    "docs",
    "logs",
    "data/cache",
]

errors: list[str] = []


def check_header(path: Path) -> None:
    try:
        with path.open("r", encoding="utf-8") as f:
            lines = []
            for _ in range(15):
                line = f.readline()
                if not line:
                    break
                lines.append(line.strip())
            if lines and lines[0].startswith("#!"):
                lines = lines[1:]
            header = [
                l
                for l in lines
                if l.startswith("#")
                or l.startswith("<!--")
                or l.startswith("/*")
                or l.startswith("//")
            ][:9]
    except Exception:
        errors.append(f"Cannot read header from {path}")
        return
    fields = [
        "Language",
        "Lines of Code",
        "File",
        "Version",
        "Project",
        "Repository",
        "Author",
        "Created",
        "Last Edited",
    ]
    for field in fields:
        if not any(field in line for line in header):
            errors.append(f"{path} missing {field} header")


for d in EXPECTED_DIRS:
    if not (ROOT / d).exists():
        errors.append(f"Missing directory: {d}")

for p in ROOT.rglob("*.*"):
    if any(part in {"logs", "data"} for part in p.parts):
        continue
    if p.suffix in {".py", ".js", ".css", ".html", ".md", ".txt"}:
        check_header(p)

if errors:
    for e in errors:
        print(e)
    sys.exit(1)
print("Validation passed")
