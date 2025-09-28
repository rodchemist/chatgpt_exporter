#!/usr/bin/env python
# Language: Python 3.12
# Lines of Code: 207
# File: src/chatgpt_exporter.py
# Version: 1.0.01
# Project: ChatGPT Conversation Exporter
# Repository: chatgpt_exporter
# Author: Rod Sanchez
# Created: 2025-07-12 05:54
# Last Edited: 2025-07-12 14:30

import json
import logging
import os
import re
import sqlite3
import tkinter as tk
import webbrowser
import zipfile
from datetime import datetime
from pathlib import Path
from tkinter import filedialog, messagebox, ttk

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

EXPORT_TXT = True
EXPORT_HTML = True
EXPORT_MD = True
EXPORT_SQLITE = True


def sanitize_filename(name: str) -> str:
    return re.sub(r"[\\/*?:\"<>|]", "_", name)


def format_timestamp(ts: float | int) -> str:
    if not ts:
        return "No timestamp"
    try:
        return datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        return str(ts)


def get_message(node: dict) -> str:
    msg = node.get("message", {})
    content = msg.get("content", {})
    parts = []
    if isinstance(content, dict):
        if content.get("content_type") == "audio_transcription":
            text = content.get("text", "").strip()
            return text if text else "[No transcription available]"
        if isinstance(content.get("parts"), list):
            parts = [str(p) for p in content.get("parts") if p]
    return " ".join(parts).strip() or "[No text content available]"


def extract_conversation(mapping: dict) -> list[tuple[str, str, float]]:
    result = []
    role_map = {"user": "User", "assistant": "Assistant", "system": "System", "tool": "SystemTool"}

    def walk(node_id: str):
        node = mapping.get(node_id, {})
        msg = node.get("message")
        if msg and msg.get("author"):
            role = role_map.get(msg["author"].get("role", "unknown"), msg["author"].get("role", "unknown"))
            text = get_message(node)
            ts = msg.get("create_time", 0)
            if text.strip():
                result.append((role, text, ts))
        for child in node.get("children", []):
            walk(child)

    for nid, n in mapping.items():
        if n.get("parent") is None:
            walk(nid)
    return result


def export_txt(conv: dict, title: str, path: Path) -> None:
    lines = [f"Title: {title}\n", "=" * 80]
    for role, text, ts in extract_conversation(conv.get("mapping", {})):
        lines.append(f"{role} ({format_timestamp(ts)})")
        lines.append("-" * 80)
        lines.extend([f"    {t}" for t in text.split("\n")])
        lines.append("=" * 80)
    path.write_text("\n".join(lines), encoding="utf-8")


def export_markdown(conv: dict, title: str, path: Path) -> None:
    lines = [f"# {title}"]
    for role, text, ts in extract_conversation(conv.get("mapping", {})):
        lines.append(f"## {role} ({format_timestamp(ts)})")
        lines.append(text)
        lines.append("\n---")
    path.write_text("\n".join(lines), encoding="utf-8")


def export_html(conv: dict, title: str, path: Path) -> None:
    rows = []
    for role, text, ts in extract_conversation(conv.get("mapping", {})):
        rows.append(
            f"<div class='message {role}'><div class='header'><span class='role'>{role}</span><span class='timestamp'>{format_timestamp(ts)}</span></div><div class='content'>{text}</div></div>"
        )
    html = (
        "<!DOCTYPE html><html><head><meta charset='UTF-8'><title>{0}</title>".format(title)
        + "<style>.message{margin-bottom:20px;border:1px solid #ccc;padding:10px;border-radius:5px;}" 
        + ".header{font-weight:bold;margin-bottom:5px;}" 
        + ".timestamp{float:right;color:#666;font-size:0.85em;}</style></head><body>"
        + f"<h2>{title}</h2>" + "".join(rows) + "</body></html>"
    )
    path.write_text(html, encoding="utf-8")


def export_sqlite(conversations: list[dict], db_path: Path) -> None:
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS conversations")
    cur.execute("DROP TABLE IF EXISTS messages")
    cur.execute("CREATE TABLE conversations(id INTEGER PRIMARY KEY, title TEXT)")
    cur.execute(
        "CREATE TABLE messages(id INTEGER PRIMARY KEY AUTOINCREMENT, conv_id INTEGER, ts REAL, role TEXT, text TEXT)"
    )
    for idx, conv in enumerate(conversations, 1):
        cur.execute("INSERT INTO conversations(id, title) VALUES (?, ?)", (idx, conv.get("title", "Untitled")))
        for role, text, ts in extract_conversation(conv.get("mapping", {})):
            cur.execute(
                "INSERT INTO messages(conv_id, ts, role, text) VALUES (?, ?, ?, ?)",
                (idx, ts, role, text),
            )
    conn.commit()
    conn.close()


def create_search_index(convs: list[dict], out_dir: Path) -> Path:
    data = []
    for i, conv in enumerate(convs):
        title = conv.get("title", "Untitled")
        fname = sanitize_filename(title) or f"Conversation_{i+1}"
        text = " ".join(t for _, t, _ in extract_conversation(conv.get("mapping", {})))
        data.append({"title": title, "file": fname + ".html", "preview": text[:200], "full": text})
    items = [
        f"<div><a href='html/{d['file']}'>{d['title']}</a><p>{d['preview']}</p></div>"
        for d in data
    ]
    html = "<!DOCTYPE html><html><body><h1>ChatGPT Conversations</h1>" + "".join(items) + "</body></html>"
    index_path = out_dir / "index.html"
    index_path.write_text(html, encoding="utf-8")
    return index_path


class ExportApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("ChatGPT Conversation Exporter")
        self.zip_file = tk.StringVar()
        self.output = tk.StringVar()
        tk.Label(root, text="Conversations ZIP").grid(row=0, column=0, sticky="w")
        tk.Entry(root, textvariable=self.zip_file).grid(row=0, column=1, sticky="ew")
        tk.Button(root, text="Browse", command=self.browse_zip).grid(row=0, column=2)
        tk.Label(root, text="Output Folder").grid(row=1, column=0, sticky="w")
        tk.Entry(root, textvariable=self.output).grid(row=1, column=1, sticky="ew")
        tk.Button(root, text="Browse", command=self.browse_out).grid(row=1, column=2)
        tk.Button(root, text="Run", command=self.run).grid(row=2, column=2, pady=10)
        root.columnconfigure(1, weight=1)

    def browse_zip(self):
        file = filedialog.askopenfilename(filetypes=[("ZIP", "*.zip")])
        if file:
            self.zip_file.set(file)

    def browse_out(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output.set(folder)

    def run(self):
        if not self.zip_file.get() or not Path(self.zip_file.get()).is_file():
            messagebox.showerror("Error", "Select a valid ZIP file")
            return
        out_dir = Path(self.output.get())
        out_dir.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(self.zip_file.get(), "r") as z:
            json_file = [f for f in z.namelist() if f.endswith("conversations.json")]
            if not json_file:
                messagebox.showerror("Error", "conversations.json not found")
                return
            with z.open(json_file[0]) as f:
                conversations = json.load(f)
        txt_dir = out_dir / "txt"; txt_dir.mkdir(exist_ok=True)
        html_dir = out_dir / "html"; html_dir.mkdir(exist_ok=True)
        md_dir = out_dir / "md"; md_dir.mkdir(exist_ok=True)
        db_dir = out_dir / "sqlite"; db_dir.mkdir(exist_ok=True)
        for idx, conv in enumerate(conversations):
            title = conv.get("title", "Untitled")
            base = sanitize_filename(title) or f"conversation_{idx+1}"
            if EXPORT_TXT:
                export_txt(conv, title, txt_dir / f"{base}.txt")
            if EXPORT_HTML:
                export_html(conv, title, html_dir / f"{base}.html")
            if EXPORT_MD:
                export_markdown(conv, title, md_dir / f"{base}.md")
        if EXPORT_SQLITE:
            export_sqlite(conversations, db_dir / "conversations.sqlite")
        index_path = create_search_index(conversations, out_dir)
        webbrowser.open(str(index_path))
        messagebox.showinfo("Done", f"Exported {len(conversations)} conversations")


if __name__ == "__main__":
    root = tk.Tk()
    app = ExportApp(root)
    root.mainloop()
