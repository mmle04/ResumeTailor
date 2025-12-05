# gemini.py
# reference: https://aistudio.google.com

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
        "You are an AI career assistant and resume coach.\n\n"
        "Compare the resume skills to the job description skills.\n"
        "Return the output as plain text (not JSON). Use the following format exactly:\n\n"
        "Missing Skills:\n"
        "- list each missing skill here\n"
        "- one per line\n\n"
        "Present Skills:\n"
        "- list each matching skill here\n\n"
        "Suggestions to Improve the Resume:\n"
        "Write a short paragraph of suggestions to improve phrasing, formatting, " \
        "clarity, or suggesting skills they should develop.\n\n"
        "Match Score:\n"
        "__%\n\n"
        "Do not use asterisks. Use dashes for bullet points.\n"
        "Use the difference between resume_skills and job_skills to find missing skills.\n"
        "Calculate Match Score by taking the percent of skills present of the total skills.\n"
        "Always include a blank line between each section.\n"
        "Keep everything concise and professional." \
        "Think hard whether or not a skill in the resume matches with a skill they already have. " \
        "Consider every skill listed in the resume_skills to see if it can possibly match with anything in job_skills."
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
    return getattr(response, "text", "").strip()