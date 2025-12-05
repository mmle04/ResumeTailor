import os
from docx import Document
import en_core_web_lg
from spacy.matcher import PhraseMatcher
from skillNer.general_params import SKILL_DB
from skillNer.skill_extractor_class import SkillExtractor

# Initialize SkillNER once
nlp = en_core_web_lg.load()
skill_extractor = SkillExtractor(nlp, SKILL_DB, PhraseMatcher)


def parse_job(path: str) -> dict:
    """
    Reads a job description (.txt or .docx) and extracts skills using SkillNER.
    Returns both raw text and the extracted skill list.
    """
    print("Parsing job description...")

    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    _, ext = os.path.splitext(path)
    ext = ext.lower()

    # Support both .txt and .docx
    if ext == ".txt":
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            full_text = f.read()
    elif ext == ".docx":
        doc = Document(path)
        full_text = "\n".join(p.text for p in doc.paragraphs)
    else:
        raise ValueError("parse_job only supports .txt and .docx files")

    # Handle empty files gracefully
    if not full_text.strip():
        print("Warning: Job description is empty or has no readable text.")
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


    print("Parsed job successfully.")
    return {
        "raw_text": full_text,
        "skills": detected_skills,
    }
