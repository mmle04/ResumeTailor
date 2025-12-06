# ResumeTailor

Resume Tailor – AI Resume Skill Matcher

Resume Tailor is a command-line assistant that compares a user's resume to a job description and returns:
- Skills currently present
- Skills missing or recommended
- Suggestions for resume improvement

The system uses:
- Gemini AI for content evaluation
- SkillNER + spaCy for skill extraction
- Local file validation for safe input handling

Features:

Resume Processing
- Accepts .docx resumes
- Extracts skills using SkillNER
- Captures full text for AI analysis

Job Parsing
- Accepts .txt or .docx job descriptions
- Extracts relevant skills

File Validation
- Verifies file existence and acceptable extensions
- Raises meaningful exceptions

AI Skill Comparison
Produces:
- Present skills
- Missing skills
- Suggestions for improvement

Internal Workflow

User Input -> File Validation -> Resume Parsing + Job Parsing -> AI Prompt -> Final Output

Installation:

Clone repository:
git clone <repo-url>
cd ResumeTailor

Install dependencies:
pip install -r requirements.txt
python -m spacy download en_core_web_lg

Create .env:
GEMINI_API_KEY=your_api_key_here

Running the Program

python main.py

Testing
python -m unittest code_testing.py

Future Enhancements
- Resume scoring and ranking
- Web-based user interface
- Cover letter analysis
- PDF export of AI feedback
