# Media Processing Tools

A collection of Python scripts for processing and organizing media files, particularly focused on video processing, timelapse creation, and metadata extraction.

## How to Run

1. Ensure all dependencies are installed:
   ```bash
   pip install opencv-python pillow numpy ffmpeg-python pandas openpyxl moviepy
   ```

2. Adjust the hardcoded paths in each script to match your directory structure

3. Run individual scripts as needed:
   ```bash
   python 01_TImelapse.py
   python 02_Classify_videos.py
   python 03_timelapse.py
   python "04_Organize videos.py"
   python 05_Merge_videos.py
   ```

4. Validate prototype compliance:
   ```bash
   python validate_prototype.py
   ```

## Features

- Create timelapse videos from image sequences
- Extract and classify video metadata into Excel spreadsheets
- Generate timelapse videos from existing videos
- Organize and rename video files with standardized naming
- Merge multiple video files into a single video
- Validate repository structure and compliance