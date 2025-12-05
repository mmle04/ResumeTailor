# gemini.py
# reference: https://aistudio.google.com/

import os

from typing import Optional
from dotenv import load_dotenv
from google import genai
from google.genai import errors

# Load .env if present (no error thrown yet if missing)
load_dotenv()

# The Gemini model version used
MODEL = "gemini-2.5-flash"

# Global Gemini client variable
_client: Optional[genai.Client] = None

# Gets API key from environment. 
# Raises an error if there is no set API key -> can't prompt Gemini
def _resolve_api_key() -> str:
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        raise RuntimeError("Set GEMINI_API_KEY in your environment/.env")
    return key

# Creates and returns Gemini AI client
def get_client() -> genai.Client:
    global _client
    if _client is None:
        _client = genai.Client(api_key=_resolve_api_key())
    return _client

# Build the prompt to ask Gemini
def _build_prompt() -> str:
    return (
        "You are an AI career assistant and resume coach. "
        "Compare the resume skills to the job description skills. "
        "Return a short summary as plain text (no JSON, no resume template). Explicitly list:\n"
        "- Missing skills (skills in job description not in resume) \n"
        "- Present skills (skills in job description and in resume) \n"
        "- Suggestions to improve the resume (rewording, reformatting, etc) \n"
        "- Match score (how the resume matches the job description from 0-100%)\n"
        "Keep it concise into bullet points."
    )

# Prompts Gemini with resume and job arguments, returns concise response with analysis
def prompt_AI(resume_parsed: dict, job_parsed: dict) -> str:
    
    # calls func to build the prompt
    prompt = _build_prompt()

    # extract skills from parsed resume and job dictionaries
    resume_skills = resume_parsed.get("skills", [])
    job_skills = job_parsed.get("skills", [])

    response = get_client().models.generate_content(
        model=MODEL,
        contents=[
            f"{prompt}\nResume Skills: {resume_skills}\nJob Skills: {job_skills}"
        ],
    )

    # Return the text output from the model
    return getattr(response, "text", "").strip()