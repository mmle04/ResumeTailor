# reference: https://aistudio.google.com/

from dotenv import load_dotenv
load_dotenv()

from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def prompt_AI(resume_file, job_description_file):
    resume = client.files.upload(file=resume_file)
    job_description = client.files.upload(file=job_description_file)

    prompt = (
        "Attached is my resume and a job description. "
        "Parse both and perform this analysis: "
        "identify sentences to improve and propose replacements; "
        "identify missing and present keywords in lists; "
        "calculate a match score from 0–100%; "
        "finally, provide counts (missing/present/suggestions) and one pro tip."
    )


    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[prompt, resume , job_description]
    )

    print(response.text)