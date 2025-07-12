#!/usr/bin/env python
# Language: Python 3.12
# Lines of Code: 51
# File: setup.py
# Version: 1.1.1
# Project: ChatGPT Conversation Exporter
# Repository: chatgpt_exporter
# Author: Rod Sanchez
# Created: 2025-07-12 05:54
# Last Edited: 2025-07-12 14:40

import setuptools
import os
import sys

# === Default Command Fallback ===
if len(sys.argv) == 1:
    print("⚠️  No command supplied. Defaulting to: 'install'")
    sys.argv.append("install")

# === README.md as long_description ===
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# === Read requirements.txt if available ===
def read_requirements():
    req_file = os.path.join(this_directory, "requirements.txt")
    if os.path.exists(req_file):
        with open(req_file, encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip() and not line.startswith("#")]
    return ["tqdm>=4.0.0"]

# === Setup Configuration ===
setuptools.setup(
    name="chatgpt_exporter",
    version="1.1.1",
    author="Rod Sanchez",
    author_email="rod@example.com",
    description="A tool to export ChatGPT conversations into various formats with a searchable HTML index.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/roderickks/chatgpt_exporter",
    project_urls={
        "Bug Tracker": "https://github.com/roderickks/chatgpt_exporter/issues",
        "Documentation": "https://github.com/roderickks/chatgpt_exporter/wiki",
        "Source Code": "https://github.com/roderickks/chatgpt_exporter",
    },
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=read_requirements(),
    extras_require={
        "dev": ["pytest>=6.0", "black>=21.0", "flake8>=3.8"],
        "docs": ["sphinx>=4.0", "sphinx-rtd-theme>=1.0"],
    },
    entry_points={
        "console_scripts": [
            "chatgpt-export=chatgpt_exporter.main:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Communications :: Chat",
        "Topic :: Text Processing :: Markup :: HTML",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    keywords="chatgpt export conversation html search",
    include_package_data=True,
    zip_safe=False,
)
