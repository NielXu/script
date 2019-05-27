import unittest
import sys
from fscript import tree

# Test for fscript.tree()
class TestTreeFunc(unittest.TestCase):

    def test_mock1_pretty(self):
        r = tree('mock\\mock1')
        e = "+--- mock1\n" +\
            "     |    \n" +\
            "     +--- a\n" +\
            "     |    \n" +\
            "     +--- b\n" +\
            "     |    \n" +\
            "     +--- c\n"
        self.assertEqual(e, r)
    
    def test_mock2_pretty(self):
        r = tree('mock\\mock2')
        e = "+--- mock2\n" +\
            "     |    \n" +\
            "     +--- a\n" +\
            "          |    \n" +\
            "          +--- b\n" +\
            "               |    \n" +\
            "               +--- c\n"
        self.assertEqual(e, r)
    
    def test_mock3_pretty(self):
        r = tree('mock\\mock3')
        e = "+--- mock3\n" +\
            "     |    \n" +\
            "     +--- a\n" +\
            "     |    |    \n" +\
            "     |    +--- b\n" +\
            "     |    \n" +\
            "     +--- c\n"
        self.assertEqual(e, r)
    
    def test_mock1_normal(self):
        r = tree('mock\\mock1', pretty_print=False)
        e = "mock1\n" +\
            "     a\n" +\
            "     b\n" +\
            "     c\n"
        self.assertEqual(e, r)
    
    def test_mock2_normal(self):
        r = tree('mock\\mock2', pretty_print=False)
        e = "mock2\n" +\
            "     a\n" +\
            "          b\n" +\
            "               c\n"
        self.assertEqual(e, r)
    
    def test_mock3_normal(self):
        r = tree('mock\\mock3', pretty_print=False)
        e = "mock3\n" +\
            "     a\n" +\
            "          b\n" +\
            "     c\n"
        self.assertEqual(e, r)


if __name__ == "__main__":
    unittest.main()
