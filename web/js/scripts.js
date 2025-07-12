// Language: JavaScript ES6
// Lines of Code: 60
// File: web/js/scripts.js
// Version: 1.0.0
// Project: ChatGPT Conversation Exporter
// Repository: chatgpt_exporter
// Author: Rod Sanchez
// Created: 2025-07-12 05:54
// Last Edited: 2025-07-12 05:54

async function startExport() {
    const fileInput = document.getElementById('zip');
    if (!fileInput.files.length) return;
    const formats = Array.from(document.querySelectorAll('.options input:checked')).map(c => c.value).join(',');
    const data = new FormData();
    const zipFile = fileInput.files[0];
    data.append('file', zipFile);
    data.append('formats', formats);
    const response = await fetch('http://localhost:8000/upload', { method: 'POST', body: data });
    const { task_id } = await response.json();
    listenProgress(task_id);
}

function listenProgress(taskId) {
    const progressEl = document.getElementById('progress');
    const download = document.getElementById('download');
    const ws = new WebSocket(`ws://localhost:8000/progress/${taskId}`);
    ws.onmessage = (e) => {
        const msg = JSON.parse(e.data);
        if (msg.error) {
            progressEl.textContent = msg.error;
            ws.close();
            return;
        }
        progressEl.textContent = `Progress: ${msg.progress}%`;
        if (msg.progress >= 100) {
            download.href = `http://localhost:8000/download/${taskId}`;
            download.style.display = 'block';
            download.textContent = 'Download Export';
            ws.close();
        }
    };
    ws.onerror = () => { progressEl.textContent = 'WebSocket error'; };
}

document.getElementById('start').addEventListener('click', async () => {
    const zip = document.getElementById('zip').files[0];
    if (!zip) return;
    const reader = new FileReader();
    reader.onload = async () => {
        try {
            const zipData = await JSZip.loadAsync(reader.result);
            if (!zipData.files['conversations.json']) {
                alert('conversations.json not found in zip');
                return;
            }
            startExport();
        } catch (e) {
            alert('Invalid zip file');
        }
    };
    reader.readAsArrayBuffer(zip);
});
