from file_loader import load_file
from resume_parser import parse_resume
from job_parser import parse_job


def main():
    print("\n=== Resume Tailor CLI ===\n")
    
    try:
        resume_path = input("Enter path to your resume file (.docx): ").strip()
        jd_path = input("Enter path to your job description file (.txt): ").strip()

        resume_file = load_file(resume_path)
        job_file = load_file(jd_path)

        print("\n=== Files Successfully Loaded ===\n")
        print(f"Resume: {resume_path} ({len(resume_file)} bytes)")
        print(f"Job Description: {jd_path} ({len(job_file)} bytes)")
        

        resume_parsed = parse_resume(resume_file)
        job_parsed = parse_job(job_file)

    
        
    except FileNotFoundError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()