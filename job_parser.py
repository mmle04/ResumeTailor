import os
import re

STOPWORDS = {
    "the", "and", "a", "an", "of", "for", "in", "on", "to", "with",
    "is", "are", "as", "at", "by", "from", "this", "that", "my"
}

def _extract_keywords(text: str) -> list[str]:
    words = re.findall(r"[A-Za-z]{3,}", text.lower())
    unique = {w for w in words if w not in STOPWORDS}
    return sorted(unique)

def parse_job(path: str) -> dict:
    print("Parsing job description...")

    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    _, ext = os.path.splitext(path)
    ext = ext.lower()

    if ext != ".txt":
        raise ValueError("parse_job only supports .txt files")

    # Read raw text from the .txt file
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        full_text = f.read()

    keywords = _extract_keywords(full_text)

    print("Parsed job successfully.")
    return {
        "raw_text": full_text,
        "keywords": keywords
    }
