# Language: Python 3.12
# Lines of Code: 115
# File: src/utils/exporter_utils.py
# Version: 1.0.0
# Project: ChatGPT Conversation Exporter
# Repository: chatgpt_exporter
# Author: Rod Sanchez
# Created: 2025-07-12 05:54
# Last Edited: 2025-07-12 05:54

import json
import re
import sqlite3
from datetime import datetime
from pathlib import Path

EXPORT_TXT = True
EXPORT_HTML = True
EXPORT_MD = True
EXPORT_SQLITE = True


def sanitize_filename(name: str) -> str:
    return re.sub(r"[\/*?:"<>|]", "_", name)


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
    parts: list[str] = []
    if isinstance(content, dict):
        if content.get("content_type") == "audio_transcription":
            text = content.get("text", "").strip()
            return text if text else "[No transcription available]"
        if isinstance(content.get("parts"), list):
            parts = [str(p) for p in content.get("parts") if p]
    return " ".join(parts).strip() or "[No text content available]"


def extract_conversation(mapping: dict) -> list[tuple[str, str, float]]:
    result: list[tuple[str, str, float]] = []
    role_map = {"user": "User", "assistant": "Assistant", "system": "System", "tool": "SystemTool"}

    def walk(node_id: str) -> None:
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
    lines = [f"Title: {title}
", "=" * 80]
    for role, text, ts in extract_conversation(conv.get("mapping", {})):
        lines.append(f"{role} ({format_timestamp(ts)})")
        lines.append("-" * 80)
        lines.extend([f"    {t}" for t in text.split("
")])
        lines.append("=" * 80)
    path.write_text("
".join(lines), encoding="utf-8")


def export_markdown(conv: dict, title: str, path: Path) -> None:
    lines = [f"# {title}"]
    for role, text, ts in extract_conversation(conv.get("mapping", {})):
        lines.append(f"## {role} ({format_timestamp(ts)})")
        lines.append(text)
        lines.append("
---")
    path.write_text("
".join(lines), encoding="utf-8")


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
    index_path.write_text(html, encoding='utf-8')
    return index_path
