# reference: https://aistudio.google.com/

from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def prompt_AI(resume_parsed: dict, job_parsed: dict) -> str:
    """
    Compare resume skills to job description skills.
    Returns a concise paragraph with bullet points (no JSON, no full template).
    """

    prompt = (
        "You are an AI career assistant. "
        "Compare the skills from this resume with the job description skills. "
        "Return a short summary as plain text (no JSON, no resume template). "
        "List these:\n"
        "- Missing skills\n"
        "- Present skills\n"
        "- Suggestions to improve the resume\n"
        "Format the output as a short paragraph or bullet points."
    )

    response = client.models.generate_content(
        model="gemini-2.0-flash-lite",
        contents=[
            f"{prompt}\nResume Skills: {resume_parsed['skills']}\nJob Skills: {job_parsed['skills']}"
        ],
    )

    # Return the text output from the model
    return getattr(response, "text", "").strip()
