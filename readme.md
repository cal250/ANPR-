# ANPR Project - Car Number Plate Extraction System

This project implements a simple Automatic Number Plate Recognition (ANPR) pipeline based on the required assignment flow:

**Detection → Alignment → OCR → Validation → Temporal → Save**

## Features
- Captures frames from a webcam
- Detects a likely number plate region
- Aligns the plate using perspective correction
- Reads plate text using Tesseract OCR
- Validates OCR output using plate patterns
- Confirms plate text after multiple observations
- Saves confirmed plates into `data/plates.csv`

## Project Structure
```text
anpr-project/
├── README.md
├── requirements.txt
├── src/
│   ├── camera.py
│   ├── detect.py
│   ├── align.py
│   ├── ocr.py
│   ├── validate.py
│   ├── temporal.py
│   ├── storage.py
│   └── main.py
└── screenshots/
    ├── detection.png
    ├── alignment.png
    └── ocr.png

## Quick Start

### 1. Install Tesseract OCR
This project requires **Tesseract OCR** to be installed on your system.
- **Windows**: Download and install from [UB-Mannheim/tesseract](https://github.com/UB-Mannheim/tesseract/wiki). Ensure it's installed to `C:\Program Files\Tesseract-OCR`.
- **Linux**: `sudo apt install tesseract-ocr`
- **macOS**: `brew install tesseract`

### 2. Install Dependencies
Run the following command to install the necessary Python libraries:
```bash
pip install -r requirements.txt
```

### 3. Run the Project
To start the ANPR pipeline, simply run the `run.py` script from the project root:
```bash
python run.py
```
*Note: Make sure your webcam is connected.*

## Key Controls
- **'s'**: Save debug screenshots (detection, alignment, and OCR steps) to the `screenshots/` directory.
- **'q'**: Quit the application.

## Supported Plate Formats
The system validates the OCR output against standard regional patterns using Regular Expressions. Currently supported formats in `src/validate.py` include:
- `^[A-Z]{3}[0-9]{3}[A-Z]?$` (e.g., **RAB123A** or **RAB123**)
- `^[A-Z]{2}[0-9]{3}[A-Z]{2}$` (e.g., **RA123BC**)

You can easily add new regional formats by appending to the `PLATE_PATTERNS` list in `src/validate.py`.

## Sample Screenshots
Here is a visual breakdown of the ANPR pipeline in action using the current repository screenshot builds (from `screenshots/*.png`):

### 1. Plate Detection
![Plate Detection](screenshots/detection.png)

### 2. Plate Alignment
*When a plate is successfully detected and temporally confirmed, its cropped image is automatically saved to the `data/captures/` directory.*
![Aligned Plate](screenshots/alignment.png)

### 3. OCR Image Pre-processing (from screenshots/ocr.png)
*This is the actual OCR pre-processing image stored in `screenshots/ocr.png`, used to feed Tesseract OCR with better contrast, thresholding, and noise cleaning.*
![OCR Process](screenshots/ocr.png)

### 4. Captured Plates Gallery
The pipeline writes verified plate captures to `data/captures/` after passing validation and temporal consistency checks. Each file is named with the recognized plate text and timestamp (example: `RAE327H_20260320_150237.png`).

- Review saved images to verify detection quality.
- Confirm OCR results via `data/plates.csv` entries.
- Use these images for further model tuning (noise reduction, perspective correction, OCR training dataset).