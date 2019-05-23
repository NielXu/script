"""
Scripts that related to file/directory manipulations
"""
import os
import re


def tree(d, max_depth=-1, include_file=True, pretty_print=True, ignore=[]):
    """
    Print tree like structure from the starting directory recursively

    `d` Starting directory

    `max_depth` The max depth that will be traveled, negative numbers represent unlimited

    `include_file` Also print files, default is True

    `pretty_print` Enable pretty print if True, False otherwise

    `ignore` A list of regex objects or strings, matched files/directories will be ignored.
    If the directory is ignored, the children files/directories will also be ignored
    """
    if not os.path.isdir(d):
        raise Exception(str(d)+": is not a directory")
    _recur_read(d, 0, max_depth, include_file, pretty_print, ignore, "     ")


def _recur_read(parent, depth, max_depth, include_file, pretty_print, ignore, pad):
    "Recursively reading files"
    if max_depth >= 0 and depth >= max_depth:
        return
    if _regex_match(parent, ignore):
        return
    print(pad[0:-5] + "+--- " + os.path.split(parent)[-1])
    files = []
    if include_file:
        files = os.listdir(parent)
    else:
        files = [x for x in os.listdir(parent) if os.path.isdir(os.path.join(parent, x))]
    count = 0
    for file in files:
        count += 1
        print(pad + "|    ")
        path = os.path.join(parent, file)
        if os.path.isdir(path):
            if count == len(files):
                _recur_read(path, depth+1, max_depth, include_file, pretty_print, ignore, pad + "     ")
            else:
                _recur_read(path, depth+1, max_depth, include_file, pretty_print, ignore, pad + "|    ")
        else:
            print(pad + "+--- " + file)


def _regex_match(f, regex):
    "Check if f matches the regex, return True if it is"
    for i in regex:
        if type(i) == str:
            pat = re.compile(i)
        else:
            pat = i
        if pat.match(f):
            return True
    return False


if __name__ == "__main__":
    tree(".")