import os

def load_file(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    _, ext = os.path.splitext(path)
    ext = ext.lower()

    if ext != ".docx":
        raise ValueError("Unsupported file type. Only .docx files are allowed.")

    return path

