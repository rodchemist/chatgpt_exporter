// Language: JavaScript ES6
// Lines of Code: 81
// File: web/js/scripts.js
// Version: 1.0.01
// Project: ChatGPT Conversation Exporter
// Repository: chatgpt_exporter
// Author: Rod Sanchez
// Created: 2025-07-12 14:30
// Last Edited: 2025-07-12 14:30

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('exportForm');
    const fileInput = document.getElementById('zipFile');
    const fileDisplay = document.getElementById('fileInputDisplay');
    const progressContainer = document.getElementById('progressContainer');
    const progressFill = document.getElementById('progressFill');
    const progressText = document.getElementById('progressText');
    const errorBox = document.getElementById('error');
    const errorText = document.getElementById('errorText');
    const results = document.getElementById('results');
    const links = document.getElementById('downloadLinks');
    const resultsText = document.getElementById('resultsText');

    fileInput.addEventListener('change', () => {
        if (fileInput.files.length > 0) {
            fileDisplay.textContent = fileInput.files[0].name;
            fileDisplay.classList.add('has-file');
        } else {
            fileDisplay.textContent = '📁 Click to select your conversations.zip file';
            fileDisplay.classList.remove('has-file');
        }
    });
    fileDisplay.addEventListener('click', () => fileInput.click());

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        hideError();
        results.style.display = 'none';
        progressContainer.style.display = 'block';
        progressFill.style.width = '0%';
        progressText.textContent = 'Uploading...';

        if (!fileInput.files.length) {
            showError('Please select a ZIP file');
            return;
        }

        const formats = ['txt', 'html', 'md', 'sqlite'].filter(f =>
            document.getElementById('export' + capitalize(f)).checked
        );

        const ws = new WebSocket(`ws://${location.host}/ws`);
        ws.onmessage = (event) => {
            const data = JSON.parse(event.data);
            progressFill.style.width = `${data.percent}%`;
            progressText.textContent = data.message;
        };
        ws.onerror = () => showError('WebSocket error');

        const formData = new FormData();
        formData.append('file', fileInput.files[0]);
        formData.append('formats', JSON.stringify(formats));

        try {
            const response = await fetch('/upload', { method: 'POST', body: formData });
            if (!response.ok) throw new Error('Upload failed');
            const blob = await response.blob();
            const zip = await JSZip.loadAsync(blob);
            links.innerHTML = '';
            for (const name of Object.keys(zip.files)) {
                const fileBlob = await zip.files[name].async('blob');
                const url = URL.createObjectURL(fileBlob);
                const a = document.createElement('a');
                a.href = url;
                a.download = name;
                a.className = 'download-btn';
                a.textContent = name;
                links.appendChild(a);
            }
            resultsText.textContent = `Successfully exported ${Object.keys(zip.files).length} files`;
            results.style.display = 'block';
        } catch (err) {
            showError(err.message);
        } finally {
            ws.close();
        }
    });

    function showError(msg) {
        errorText.textContent = msg;
        errorBox.style.display = 'block';
    }
    function hideError() {
        errorBox.style.display = 'none';
    }
    function capitalize(str) {
        return str.charAt(0).toUpperCase() + str.slice(1);
    }
});
