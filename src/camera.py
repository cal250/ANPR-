import cv2


# On Windows, try these backends in order of reliability
BACKENDS = [
    ("MSMF", cv2.CAP_MSMF),
    ("ANY",  cv2.CAP_ANY),
    ("DSHOW", cv2.CAP_DSHOW),
]


def find_available_camera(max_index: int = 5):
    """
    Scan camera indices with multiple backends and return the first
    (index, backend) pair that successfully opens.
    """
    for backend_name, backend in BACKENDS:
        for i in range(max_index):
            cap = cv2.VideoCapture(i, backend)
            if cap.isOpened():
                cap.release()
                print(f"[INFO] Found camera at index {i} using {backend_name} backend.")
                return i, backend
            cap.release()
    return -1, cv2.CAP_ANY


def open_camera(camera_index: int = None, width: int = 1280, height: int = 720):
    """
    Open a camera. Auto-detects the first available camera if camera_index is None.
    Tries multiple Windows-compatible backends (MSMF, default, DSHOW).
    """
    if camera_index is None:
        camera_index, backend = find_available_camera()
    else:
        backend = cv2.CAP_MSMF  # default to MSMF for explicit index

    if camera_index == -1:
        raise RuntimeError(
            "No webcam found. Please check that:\n"
            "  1. No other app is using the camera (Teams, Zoom, Windows Camera app, browser).\n"
            "  2. Camera access is enabled: Settings > Privacy & security > Camera.\n"
            "  3. The correct camera drivers are installed in Device Manager."
        )

    cap = cv2.VideoCapture(camera_index, backend)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    if not cap.isOpened():
        raise RuntimeError(f"Could not open camera at index {camera_index}.")

    print(f"[INFO] Camera opened successfully at index {camera_index}.")
    return cap