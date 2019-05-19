"""
Scripts that related to file/directory manipulations
"""
import os
import re


def tree(d, max_depth=-1, include_file=True, print_format="pretty", ignore=[]):
    """
    Print tree like structure from the starting directory recursively

    `d` Starting directory

    `max_depth` The max depth that will be traveled, negative numbers represent unlimited

    `include_file` Also print files, default is True

    `print_format` The printing format, default is pretty, options:`[pretty | plain]`

    `ignore` A list of regex, matches files/directories will be ignored. If the
    directory is ignored, the children files/directories will also be ignored
    """
    if not os.path.isdir(d):
        raise Exception(d+": is not a directory")
    for f in os.listdir(d):
        print(os.path.join(d, f))


def _recur_read(parent):
    "Recursively reading files"


def _regex_match(f, regex):
    "Check if f matches the regex, return True if it is"
    for i in regex:
        if type(i) == str:
            pat = re.compile(regex)
        else:
            pat = i
        if pat.match(f):
            return True
    return False


if __name__ == "__main__":
    tree("C:\\Users\\Isaac Chen")