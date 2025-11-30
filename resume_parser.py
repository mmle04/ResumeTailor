# # resume_parser.py
# import re
# from docx import Document  # pip install python-docx

# STOPWORDS = {
#     "the", "and", "a", "an", "of", "for", "in", "on", "to", "with",
#     "is", "are", "as", "at", "by", "from", "this", "that", "my"
# }

# def _extract_keywords(text: str) -> list[str]:
#     words = re.findall(r"[A-Za-z]{3,}", text.lower())
#     unique = {w for w in words if w not in STOPWORDS}
#     return sorted(unique)

# def parse_resume(path: str) -> dict:
#     # Parses a .docx resume file and returns a simple dictionary with raw text and extracted keywords.

#     doc = Document(path)
#     full_text = "\n".join(p.text for p in doc.paragraphs)

#     keywords = _extract_keywords(full_text)

#     print("Parsed resume successfully.")
#     return {
#         "raw_text": full_text,
#         "keywords": keywords
#     }




# resume_parser.py
import os
from docx import Document
import en_core_web_lg
from spacy.matcher import PhraseMatcher
from skillNer.general_params import SKILL_DB
from skillNer.skill_extractor_class import SkillExtractor

# Initialize SkillNER once
nlp = en_core_web_lg.load()
skill_extractor = SkillExtractor(nlp, SKILL_DB, PhraseMatcher)


def parse_resume(path: str) -> dict:
    """
    Reads a resume (.docx) and extracts skills using SkillNER.
    Returns both raw text and the extracted skill list.
    """
    print("Parsing resume...")

    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    _, ext = os.path.splitext(path)
    ext = ext.lower()

    if ext != ".docx":
        raise ValueError("parse_resume only supports .docx files")

    doc = Document(path)
    full_text = "\n".join(p.text for p in doc.paragraphs)

    if not full_text.strip():
        print("Warning: Resume is empty or has no readable text.")
        return {
            "raw_text": full_text,
            "skills": [],
            "skillner_raw": {}
        }

    # Extract skills using SkillNER
    result = skill_extractor.annotate(full_text)

    # Collect skill names
    detected_skills = sorted({
        item['doc_node_value']
        for item in result['results']['full_matches'] + result['results']['ngram_scored']
    })

    print(detected_skills)

    print("Parsed resume successfully.")
    return {
        "raw_text": full_text,
        "skills": detected_skills,
    }
