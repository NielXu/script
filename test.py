from fscript import _regex_match
import unittest
import re


class TestRegexMatch(unittest.TestCase):
    "Testing _regex_match() function"
    def test_match_str(self):
        regex = [".*.xyz"]
        self.assertTrue(_regex_match("abc.xyz", regex))
    
    def test_unmatch_str(self):
        regex = [".*.xyy"]
        self.assertFalse(_regex_match("abc.xyz", regex))
    
    def test_match_multi_str(self):
        regex = [".*.xyy", ".*.xyz"]
        self.assertTrue(_regex_match("abc.xyz", regex))
    
    def test_unmatch_multi_str(self):
        regex = [".*.xyy", ".*.xyz"]
        self.assertFalse(_regex_match("abc.c", regex))
    
    def test_match_rawstr(self):
        regex = [r".*.xyz"]
        self.assertTrue(_regex_match("abc.xyz", regex))
    
    def test_unmatch_rawstr(self):
        regex = [r".*.xyy"]
        self.assertFalse(_regex_match("abc.xyz", regex))
    
    def test_match_multi_rawstr(self):
        regex = [r".*.xyy", r".*.xyz"]
        self.assertTrue(_regex_match("abc.xyz", regex))
    
    def test_unmatch_multi_rawstr(self):
        regex = [r".*.xyy", r".*.xyz"]
        self.assertFalse(_regex_match("abc.c", regex))
    
    def test_match_robj(self):
        regex = [re.compile(".*.xyz")]
        self.assertTrue(_regex_match("abc.xyz", regex))
    
    def test_unmatch_robj(self):
        regex = [re.compile(".*.xyy")]
        self.assertFalse(_regex_match("abc.xyz", regex))
    
    def test_match_multi_robj(self):
        regex = [re.compile(".*.xyy"), re.compile(".*.xyz")]
        self.assertTrue(_regex_match("abc.xyz", regex))
    
    def test_unmatch_multi_robj(self):
        regex = [re.compile(".*.xyy"), re.compile(".*.xyz")]
        self.assertFalse(_regex_match("abc.c", regex))
    
    def test_match_mix(self):
        regex = [re.compile(".*.xyz"), ".*.xyz"]
        self.assertTrue(_regex_match("abc.xyz", regex))
    
    def test_unmatch_mix(self):
        regex = [re.compile(".*.xyy"), ".*.xyy"]
        self.assertFalse(_regex_match("abc.xyz", regex))
    
    def test_match_multi_mix(self):
        regex = [re.compile(".*.xyy"), ".*.xyy", re.compile(".*.xyz"), ".*.xyz"]
        self.assertTrue(_regex_match("abc.xyz", regex))
    
    def test_unmatch_multi_mix(self):
        regex = [re.compile(".*.xyy"), ".*.xyy", re.compile(".*.xyz"), ".*.xyz"]
        self.assertFalse(_regex_match("abc.c", regex))
    
    def test_dotfile(self):
        regex = [r"\..*"]
        self.assertTrue(_regex_match(".git", regex))
        self.assertTrue(_regex_match(".file", regex))
        self.assertTrue(_regex_match(".gitignore", regex))
        self.assertFalse(_regex_match("example.js", regex))
    
    def test_multi_dotsfile(self):
        regex = [r"\..*"]
        self.assertTrue(_regex_match(".example.js", regex))
        self.assertTrue(_regex_match(".file.c", regex))
        self.assertTrue(_regex_match(".gitignore.doc", regex))
        self.assertFalse(_regex_match("example.js", regex))


if __name__ == "__main__":
    unittest.main()
