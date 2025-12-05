import unittest
from resume_parser import parse_resume
from job_parser import parse_job
from file_loader import load_file
import tempfile

class Tests(unittest.TestCase):

    # ---- TEST 1: INVALID FILE TYPE ----
    def testInvalidType1_resume(self):
        print("testing testInvalidType1_resume...")
        invalid_path = "fakefile.txt"
        with self.assertRaises(FileNotFoundError):
            parse_resume(invalid_path)


    def testInvalidType1_job(self):
        print("testing testInvalidType1_job...")
        invalid_path = "fakefile.mp4"
        with self.assertRaises(FileNotFoundError):
            parse_job(invalid_path)


    # ---- TEST 2: NONEXISTENT FILE ----
    def testNonexistentFile_resume(self):
        print("testing testNonexistentFile_resume...")
        invalid_path = "this_file_does_not_exist.docx"

        with self.assertRaises(FileNotFoundError):
            parse_resume(invalid_path)

    def testNonexistentFile_job(self):
        print("testing testNonexistentFile_job...")
        invalid_path = "this_file_does_not_exist.txt"

        with self.assertRaises(FileNotFoundError):
            parse_job(invalid_path)
    
    # ---- TEST 3: testInvalidType2 ----
    # User inputs an invalid job description file type
    #
    # Idea: the job description is supposed to be .txt.
    # Here we pass a .pdf file and expect a ValueError from load_file
    # when we restrict the allowed extensions to (".txt",).
    def testInvalidType2_job(self):
        print("testing testInvalidType2_job...")
        # Create a real temporary .pdf file so existence check passes
        with tempfile.NamedTemporaryFile(suffix=".pdf") as tmp:
            invalid_job_path = tmp.name

            # Now the file exists, but the extension is wrong
            # allowed_exts only allows .txt, so this should raise ValueError
            with self.assertRaises(ValueError):
                load_file(invalid_job_path, allowed_exts=(".txt",))

    # ---- TEST 4: testNonexistentJobFile2 ----
    # User inputs a job description file that does not exist
    #
    # Steps: Enter C:/fake/missing_job.txt as the job description path.
    # We expect FileNotFoundError from parse_job (or load_file, if you use it there).
    def testNonexistentJobFile2(self):
        print("testing testNonexistentJobFile2...")
        invalid_job_path = r"C:/fake/missing_job.txt"

        with self.assertRaises(FileNotFoundError):
            parse_job(invalid_job_path)

    
    # ---- TEST 5: testEmptyResumePathInput ----
    # User presses Enter without typing a resume path
    #
    # Steps: For resume path, just press Enter → the string is "".
    # load_file() is designed to catch empty paths and raise ValueError.
    def testEmptyResumePathInput(self):
        print("testing testEmptyResumePathInput...")
        empty_path = ""

        with self.assertRaises(ValueError):
            load_file(empty_path, allowed_exts=(".docx",))

if __name__ == "__main__":
    unittest.main()
