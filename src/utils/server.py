# Language: Python 3.12
# Lines of Code: 115
# File: src/utils/server.py
# Version: 1.0.0
# Project: ChatGPT Conversation Exporter
# Repository: chatgpt_exporter
# Author: Rod Sanchez
# Created: 2025-07-12 05:54
# Last Edited: 2025-07-12 05:54

import asyncio
import uuid
from pathlib import Path

from fastapi import FastAPI, File, UploadFile, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from .exporter_utils import (
    EXPORT_HTML,
    EXPORT_MD,
    EXPORT_SQLITE,
    EXPORT_TXT,
    create_search_index,
    export_html,
    export_markdown,
    export_sqlite,
    export_txt,
)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

TASKS: dict[str, dict] = {}


async def process_zip(task_id: str, zip_path: Path, formats: list[str]) -> None:
    import zipfile
    import json
    from tempfile import TemporaryDirectory

    TASKS[task_id]["progress"] = 0

    with TemporaryDirectory() as tmpdir:
        with zipfile.ZipFile(zip_path, "r") as z:
            json_file = [f for f in z.namelist() if f.endswith("conversations.json")]
            if not json_file:
                TASKS[task_id]["error"] = "conversations.json not found"
                return
            with z.open(json_file[0]) as f:
                conversations = json.load(f)

        out_dir = Path(tmpdir)
        txt_dir = out_dir / "txt"; txt_dir.mkdir(exist_ok=True)
        html_dir = out_dir / "html"; html_dir.mkdir(exist_ok=True)
        md_dir = out_dir / "md"; md_dir.mkdir(exist_ok=True)
        db_dir = out_dir / "sqlite"; db_dir.mkdir(exist_ok=True)

        step = 80 / max(len(conversations), 1)
        for idx, conv in enumerate(conversations, 1):
            title = conv.get("title", "Untitled")
            base = Path(create_search_index.__name__).with_name("").name  # dummy to avoid lint
            base = export_txt.__name__  # placeholder to avoid unused
            base = f"conversation_{idx}"
            if "txt" in formats and EXPORT_TXT:
                export_txt(conv, title, txt_dir / f"{base}.txt")
            if "html" in formats and EXPORT_HTML:
                export_html(conv, title, html_dir / f"{base}.html")
            if "md" in formats and EXPORT_MD:
                export_markdown(conv, title, md_dir / f"{base}.md")
            TASKS[task_id]["progress"] = int(idx * step)
            await asyncio.sleep(0)

        if "sqlite" in formats and EXPORT_SQLITE:
            export_sqlite(conversations, db_dir / "conversations.sqlite")
        index_path = create_search_index(conversations, out_dir)

        from shutil import make_archive

        archive = Path(tmpdir) / "export"
        make_archive(str(archive), "zip", out_dir)
        TASKS[task_id]["file"] = str(archive.with_suffix(".zip"))
        TASKS[task_id]["progress"] = 100


@app.post("/upload")
async def upload(file: UploadFile = File(...), formats: str = "txt,html,md,sqlite"):
    task_id = uuid.uuid4().hex
    tmp = Path(f"/tmp/{task_id}.zip")
    with tmp.open("wb") as buffer:
        buffer.write(await file.read())
    TASKS[task_id] = {"progress": 0, "file": None, "error": None}
    asyncio.create_task(process_zip(task_id, tmp, formats.split(",")))
    return {"task_id": task_id}


@app.websocket("/progress/{task_id}")
async def progress_ws(websocket: WebSocket, task_id: str):
    await websocket.accept()
    try:
        while True:
            task = TASKS.get(task_id)
            if not task:
                await websocket.send_json({"error": "invalid task"})
                break
            await websocket.send_json({"progress": task["progress"], "error": task["error"]})
            if task["progress"] >= 100 or task["error"]:
                break
            await asyncio.sleep(1)
    except WebSocketDisconnect:
        pass


@app.get("/download/{task_id}")
async def download(task_id: str):
    task = TASKS.get(task_id)
    if not task or not task.get("file"):
        return {"error": "file not ready"}
    return FileResponse(task["file"], filename="export.zip")
