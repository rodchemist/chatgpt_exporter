# Qwen Context Documentation - Media Processing Tools

## Repository Overview
This repository contains a collection of Python scripts for media processing tasks, primarily focused on video processing, timelapse creation, and metadata extraction. The tools are designed to work with video files, particularly from travel footage (e.g., "Europe 2023").

## Directory Structure
```
media_processing_tools/
├── 01_TImelapse.py              # Creates timelapse videos from image sequences, filtering out black images
├── 02_Classify_videos.py        # Extracts and classifies video metadata into Excel spreadsheets
├── 03_timelapse.py              # Creates timelapse videos from existing videos using FFmpeg
├── 04_Organize videos.py        # Renames video files to a standardized timestamp format
├── 05_Merge_videos.py           # Merges multiple video files into a single video
├── AGENTS.md                    # Prototyping guidelines for AI agents
├── AUDIT.md                     # Repository audit criteria and standards
├── CLAUDE.md                    # Prototyping guidelines (Claude-specific)
├── Full_Guidelines.md           # Comprehensive project development guidelines
├── GEMINI.md                    # Prototyping guidelines (Gemini-specific)
└── validate_prototype.py        # Validation script for prototype compliance
```

## Tool Descriptions

### 01_TImelapse.py
- Creates timelapse videos from sequences of images
- Filters out black images (moved to a separate folder)
- Uses OpenCV and PIL for image processing
- Shows progress during processing with ETA calculations

### 02_Classify_videos.py
- Extracts comprehensive metadata from video files using FFmpeg
- Supports multiple video formats (.mp4, .mov, .avi, .mkv)
- Generates Excel spreadsheets with detailed video information
- Includes file properties, video/audio codecs, resolution, bitrate, etc.

### 03_timelapse.py
- Creates timelapse videos from existing videos using FFmpeg
- Validates videos based on specific criteria (resolution, frame rate, audio codec)
- Processes videos concurrently for efficiency
- Automatically names output files based on modification dates

### 04_Organize videos.py
- Renames video files to a standardized timestamp format (yyyymmddhhmmss.mp4)
- Processes files recursively through directory structures
- Extracts date/time information from existing filenames

### 05_Merge_videos.py
- Merges multiple video files into a single continuous video
- Sorts videos by filename (assumed to be chronological)
- Uses MoviePy for video concatenation

## Development Guidelines
This repository follows specific prototyping guidelines:
- All new projects must include a README.md with a specific structure
- Source files require standardized headers with project metadata
- Prototypes should be self-contained and functional
- Validation is performed using the `validate_prototype.py` script

## Dependencies
Common dependencies across scripts include:
- OpenCV (cv2)
- FFmpeg/ffmpeg-python
- PIL/Pillow
- NumPy
- Pandas
- MoviePy
- OpenPyXL

## Usage Notes
- Most scripts contain hardcoded paths that need to be adjusted for different environments
- FFmpeg is required for several video processing operations
- Scripts are designed for Windows environments (evidenced by path formatting)
- Processing can be resource-intensive for large video collections

## Repository Standards
- Follows audit criteria outlined in AUDIT.md
- Complies with prototyping guidelines in AGENTS.md, CLAUDE.md, and GEMINI.md
- Implements repository structure guidelines from Full_Guidelines.md
- Includes validation script to ensure prototype compliance

## Author
Rod Sanchez

## Last Updated
September 21, 2025