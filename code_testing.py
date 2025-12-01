import unittest
from resume_parser import parse_resume
from job_parser import parse_job

class Tests(unittest.TestCase):

    # ---- TEST 1: INVALID FILE TYPE ----
    def testInvalidType1_resume(self):
        invalid_path = "fakefile.txt"
        with self.assertRaises(FileNotFoundError):
            parse_resume(invalid_path)


    def testInvalidType1_job(self):
        invalid_path = "fakefile.mp4"
        with self.assertRaises(FileNotFoundError):
            parse_job(invalid_path)


    # ---- TEST 2: NONEXISTENT FILE ----
    def testNonexistentFile_resume(self):
        invalid_path = "this_file_does_not_exist.docx"

        with self.assertRaises(FileNotFoundError):
            parse_resume(invalid_path)

    def testNonexistentFile_job(self):
        invalid_path = "this_file_does_not_exist.txt"

        with self.assertRaises(FileNotFoundError):
            parse_job(invalid_path)

if __name__ == "__main__":
    unittest.main()
