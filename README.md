# Vidify

A collection of Python tools for converting images and live video into ASCII art.

## Scripts

| Script | What it does |
|---|---|
| `ascii_art.py` | Converts a JPG/PNG to ASCII, prints it, and saves it as an image |
| `art2.py` / `art3.py` | Variations on image-to-ASCII conversion |
| `video2.py` | Plays a video file as live ASCII in the terminal |
| `video_output.py` | Records your webcam as an ASCII art MP4 |

## Requirements

- Python 3.x
- Pillow
- OpenCV
- NumPy

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install pillow opencv-python numpy
```

## Usage

**Image to ASCII (print + save):**
```python
# edit ascii_art.py — set image_path at the bottom
python3 ascii_art.py
```

**Video file as ASCII in terminal:**
```python
# edit video2.py — set video_path at the bottom
# main(0) uses webcam, main("file.mp4") uses a file
python3 video2.py
```

**Record webcam as ASCII MP4:**
```bash
python3 video_output.py
# saves to output.mp4, records for 10 seconds
```

## Controls

| Input | Action |
|---|---|
| `q` | Quit video playback |

```
      ___           ___           ___
     /\  \         /\  \         /\  \          ___         ___
    /::\  \       /::\  \       /::\  \        /\  \       /\  \
   /:/\:\  \     /:/\ \  \     /:/\:\  \       \:\  \      \:\  \
  /::\~\:\  \   _\:\~\ \  \   /:/  \:\  \      /::\__\     /::\__\
 /:/\:\ \:\__\ /\ \:\ \ \__\ /:/__/ \:\__\  __/:/\/__/  __/:/\/__/
 \/__\:\/:/  / \:\ \:\ \/__/ \:\  \  \/__/ /\/:/  /    /\/:/  /
      \::/  /   \:\ \:\__\    \:\  \       \::/__/     \::/__/
      /:/  /     \:\/:/  /     \:\  \       \:\__\      \:\__\
     /:/  /       \::/  /       \:\__\       \/__/       \/__/
     \/__/         \/__/         \/__/
      ___           ___           ___           ___           ___
     /\  \         /\  \         /\__\         /\  \         /\__\
    /::\  \       /::\  \       /::|  |       /::\  \       /:/  /
   /:/\:\  \     /:/\:\  \     /:|:|  |      /:/\:\  \     /:/__/
  /::\~\:\  \   /::\~\:\  \   /:/|:|  |__   /:/  \:\  \   /::\  \ ___
 /:/\:\ \:\__\ /:/\:\ \:\__\ /:/ |:| /\__\ /:/__/ \:\__\ /:/\:\  /\__\
 \/_|::\/:/  / \/__\:\/:/  / \/__|:|/:/  / \:\  \  \/__/ \/__\:\/:/  /
    |:|::/  /       \::/  /      |:/:/  /   \:\  \            \::/  /
    |:|\/__/        /:/  /       |::/  /     \:\  \           /:/  /
    |:|  |         /:/  /        /:/  /       \:\__\         /:/  /
     \|__|         \/__/         \/__/         \/__/         \/__/
```
