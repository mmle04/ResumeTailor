# reference: https://aistudio.google.com/

from dotenv import load_dotenv
load_dotenv()

from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# def prompt_AI(resume, job_description):
# client.files.upload(file=resume)
# client.files.upload(file=job_description)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="What color is the sky?",
)

print(response.text)