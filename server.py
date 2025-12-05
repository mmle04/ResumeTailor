from flask import Flask, request
import tempfile, os

from resume_parser import parse_resume
from job_parser import parse_job
from gemini import prompt_AI

app = Flask(__name__, static_folder=".", static_url_path="")

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.post("/api/analyze")
def analyze():
    if "resume" not in request.files or "job" not in request.files:
        return "Both resume and job files are required.", 400

    resume_file = request.files["resume"]
    job_file = request.files["job"]

    if resume_file.filename == "" or job_file.filename == "":
        return "Please choose both files before submitting.", 400

    with tempfile.TemporaryDirectory() as tmpdir:
        resume_path = os.path.join(tmpdir, resume_file.filename)
        job_path = os.path.join(tmpdir, job_file.filename)

        resume_file.save(resume_path)
        job_file.save(job_path)

        # Use your existing logic
        resume_parsed = parse_resume(resume_path)
        job_parsed = parse_job(job_path)
        ai_output = prompt_AI(resume_parsed, job_parsed)

    return ai_output or "No response from AI.", 200

if __name__ == "__main__":
    app.run(debug=True)
