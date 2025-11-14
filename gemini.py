# reference: https://aistudio.google.com/

from dotenv import load_dotenv
load_dotenv()

from google import genai
import os, json

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SCHEMA = {
    "type": "object",
    "properties": {
        "match_score": {"type": "number"},  # 0–100
        "missing_keywords": {"type": "array", "items": {"type": "string"}},
        "present_keywords": {"type": "array", "items": {"type": "string"}},
        "counts": {
            "type": "object",
            "properties": {
                "missing": {"type": "integer"},
                "present": {"type": "integer"},
                "suggestions": {"type": "integer"}
            },
            "required": ["missing", "present", "suggestions"]
        },
        "pro_tip": {"type": "string"},
        "sentence_suggestions": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "original": {"type": "string"},
                    "improved": {"type": "string"},
                    "reason": {"type": "string"}
                },
                "required": ["original", "improved"]
            }
        }
    },
    "required": ["match_score", "missing_keywords", "present_keywords", "counts", "pro_tip"]
}

def prompt_AI(resume_parsed, job_parsed):
    # resume = client.files.upload(file=resume_file)
    # job_description = client.files.upload(file=job_description_file)

    prompt = (
        "You are an AI resume coach. "
        "return ONLY JSON matching the given schema. Do not include markdown. "
        "Given structured inputs that were parsed offline,"
        "Compute: missing_keywords, present_keywords, sentence_suggestions "
        "(with original/improved/optional reason), counts {missing,present,suggestions}, "
        "match_score (0-100), and pro_tip."
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[prompt, resume_parsed, job_parsed],
        generation_config={
            "response_mime_type": "application/json",
            "response_schema": SCHEMA
        },
    )

    print(response.text)