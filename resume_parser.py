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
