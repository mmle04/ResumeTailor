# resume_parser.py
import re
from docx import Document  # pip install python-docx

STOPWORDS = {
    "the", "and", "a", "an", "of", "for", "in", "on", "to", "with",
    "is", "are", "as", "at", "by", "from", "this", "that", "my"
}

def _extract_keywords(text: str) -> list[str]:
    words = re.findall(r"[A-Za-z]{3,}", text.lower())
    unique = {w for w in words if w not in STOPWORDS}
    return sorted(unique)

def parse_resume(path: str) -> dict:
    # Parses a .docx resume file and returns a simple dictionary with raw text and extracted keywords.

    doc = Document(path)
    full_text = "\n".join(p.text for p in doc.paragraphs)

    keywords = _extract_keywords(full_text)

    print("Parsed resume successfully.")
    return {
        "raw_text": full_text,
        "keywords": keywords
    }