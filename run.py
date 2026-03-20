import os
import sys
import subprocess

# 1. Add 'src' to the Python path so imports like 'from camera import ...' work
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, "src")
if src_dir not in sys.path:
    sys.path.append(src_dir)

def ensure_directories():
    """Ensure that the required data and screenshot directories exist."""
    dirs = [
        "data/captures",
        "screenshots"
    ]
    for d in dirs:
        path = os.path.join(current_dir, d)
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
            print(f"[INFO] Created directory: {d}")

def check_dependencies():
    """Check if basic dependencies are installed."""
    try:
        import cv2
        import numpy
        import pytesseract
        import imutils
    except ImportError as e:
        print(f"[ERROR] Missing dependency: {e.name}")
        print("Please run: pip install -r requirements.txt")
        sys.exit(1)

def main():
    print("=== ANPR Project Runner ===")
    
    ensure_directories()
    check_dependencies()
    
    # Import main from src only after path is set
    try:
        from main import main as run_anpr
    except ImportError as e:
        print(f"[ERROR] Could not import main script: {e}")
        sys.exit(1)

    print("[INFO] Starting ANPR pipeline...")
    try:
        run_anpr()
    except KeyboardInterrupt:
        print("\n[INFO] Stopped by user.")
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
