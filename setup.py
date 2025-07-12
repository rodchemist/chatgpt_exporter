#!/usr/bin/env python
# Language: Python 3.12
# Lines of Code: 24
# File: setup.py
# Version: 1.0.0
# Project: ChatGPT Conversation Exporter
# Repository: chatgpt_exporter
# Author: Rod Sanchez
# Created: 2025-07-12 05:54
# Last Edited: 2025-07-12 05:54

import setuptools

setuptools.setup(
    name="chatgpt_exporter",
    version="1.0.0",
    author="Rod Sanchez",
    author_email="your.email@example.com",
    description="A tool to export ChatGPT conversations into various formats with a searchable HTML index.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/roderickks/chatgpt_exporter",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["tqdm>=4.0.0"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)
