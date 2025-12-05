from file_loader import load_file
from resume_parser import parse_resume
from job_parser import parse_job
from gemini import prompt_AI

def main():
    print("\n=== Resume Tailor CLI ===\n")
    
    try:
        resume_path = input("Enter path to your resume file (.txt / .docx): ").strip()
        job_path = input("Enter path to your job description file (.txt / .docx): ").strip()

        resume_file = load_file(resume_path)
        job_file = load_file(job_path)

        print("\n=== Files Successfully Loaded ===\n")
        print(f"Resume: {resume_path} ({len(resume_file)} bytes)")
        print(f"Job Description: {job_path} ({len(job_file)} bytes)")
        

        resume_parsed = parse_resume(resume_path)
        job_parsed = parse_job(job_path)

        ai_output = prompt_AI(resume_parsed, job_parsed)

        print("\n=== AI Response ===\n")
        print(ai_output)
        
    except FileNotFoundError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()