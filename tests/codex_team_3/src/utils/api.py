# Language: Python 3.12
# Lines of Code: 108
# File: src/utils/api.py
# Version: 1.0.01
# Project: ChatGPT Conversation Exporter
# Repository: chatgpt_exporter
# Author: Rod Sanchez
# Created: 2025-07-12 14:30
# Last Edited: 2025-07-12 14:30

from __future__ import annotations

import asyncio
import io
import json
import logging
import os
import shutil
import tempfile
import zipfile
from pathlib import Path

from fastapi import FastAPI, UploadFile, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

from ..chatgpt_exporter import (
    export_html,
    export_markdown,
    export_sqlite,
    export_txt,
    sanitize_filename,
    create_search_index,
)

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

clients: list[WebSocket] = []


async def notify(percent: int, message: str) -> None:
    data = json.dumps({"percent": percent, "message": message})
    for ws in clients:
        try:
            await ws.send_text(data)
        except Exception:
            pass


@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket) -> None:
    await ws.accept()
    clients.append(ws)
    try:
        while True:
            await asyncio.sleep(1)
    except WebSocketDisconnect:
        pass
    finally:
        if ws in clients:
            clients.remove(ws)


@app.post("/upload")
async def upload_file(file: UploadFile, formats: str = "[\"txt\",\"html\",\"md\",\"sqlite\"]") -> StreamingResponse:
    export_formats = json.loads(formats)
    tmpdir = Path(tempfile.mkdtemp())
    try:
        raw_path = tmpdir / "input.zip"
        with raw_path.open("wb") as f:
            f.write(await file.read())
        await notify(10, "Extracting ZIP...")
        with zipfile.ZipFile(raw_path, "r") as z:
            json_file = next((n for n in z.namelist() if n.endswith("conversations.json")), None)
            if not json_file:
                raise ValueError("conversations.json not found")
            conversations = json.load(z.open(json_file))
        out_dir = tmpdir / "out"
        out_dir.mkdir()
        txt_dir = out_dir / "txt"
        html_dir = out_dir / "html"
        md_dir = out_dir / "md"
        db_dir = out_dir / "sqlite"
        for d in (txt_dir, html_dir, md_dir, db_dir):
            d.mkdir()
        for idx, conv in enumerate(conversations, 1):
            title = conv.get("title", f"Conversation_{idx}")
            base = sanitize_filename(title) or f"conversation_{idx}"
            pct = 10 + int((idx / len(conversations)) * 70)
            await notify(pct, f"Processing {idx}/{len(conversations)}")
            if "txt" in export_formats:
                export_txt(conv, title, txt_dir / f"{base}.txt")
            if "html" in export_formats:
                export_html(conv, title, html_dir / f"{base}.html")
            if "md" in export_formats:
                export_markdown(conv, title, md_dir / f"{base}.md")
        if "sqlite" in export_formats:
            await notify(90, "Writing SQLite DB")
            export_sqlite(conversations, db_dir / "conversations.sqlite")
        await notify(95, "Creating index")
        create_search_index(conversations, out_dir)
        await notify(100, "Packaging results")
        buf = io.BytesIO()
        with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zipf:
            for folder, _, files in os.walk(out_dir):
                for name in files:
                    path = Path(folder) / name
                    zipf.write(path, path.relative_to(out_dir))
        buf.seek(0)
        return StreamingResponse(
            buf,
            media_type="application/zip",
            headers={"Content-Disposition": "attachment; filename=export.zip"},
        )
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)

