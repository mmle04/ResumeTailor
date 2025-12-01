import os

def load_file(path: str, allowed_exts=(".docx", ".txt")) -> str:
    # Validates that the file exists and has an allowed extension.
    if not path:
        raise ValueError("Path cannot be empty.")

    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    _, ext = os.path.splitext(path)
    ext = ext.lower()

    if ext not in allowed_exts:
        # Example: ".docx" or ".txt"
        allowed_str = ", ".join(allowed_exts)
        raise ValueError(f"Unsupported file type. Allowed types: {allowed_str}")

    return path

