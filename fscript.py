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
    if os.path.isfile(d):
        print(d)
        return
    _recur_read(d, 0, max_depth, include_file, pretty_print, ignore, False)


def _recur_read(parent, depth, max_depth, include_file, pretty_print, ignore, is_end):
    "Recursively reading files"
    if max_depth >= 0 and depth >= max_depth:
        return
    if _regex_match(parent, ignore):
        return
    files = os.listdir(parent)
    for i in range(len(files)):
        f = files[i]
        fullpath = os.path.join(parent, f)
        end = (i == len(files)-1)
        is_file = os.path.isfile(fullpath)
        if pretty_print:
            _pretty_format(depth, f, is_end, is_file)
        else:
            print(depth*"    " + f)
        if is_file:
            continue
        _recur_read(fullpath, depth+1, max_depth, include_file, pretty_print, ignore, end)


def _pretty_format(d, f, is_end, is_file):
    if is_end and is_file:
        top = "|    " * (d-1) + "     |"
        bot = "|    " * (d-1) + "     +--- " + f
    else:
        top = "|    " * d + "|"
        bot = "|    " * d + "+--- " + f
    print(top)
    print(bot)
    return d*"    " + "|" + "--- "


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