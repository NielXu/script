"""
Scripts that related to file/directory manipulations
"""
import os
import re


def tree(d, max_depth=-1, include_file=True, pretty_print=True):
    """
    Print tree like structure from the starting directory recursively.
    Also return the result as one String.

    `d` Starting directory

    `max_depth` The max depth that will be traveled, negative numbers represent unlimited

    `include_file` Also print files, default is True

    `pretty_print` Enable pretty print if True, False otherwise
    """
    if not os.path.isdir(d):
        raise Exception(str(d)+": is not a directory")
    if pretty_print:
        return _pretty_read(d, 0, max_depth, include_file, "     ")
    rootf = os.path.split(d)[-1]
    print(rootf)
    return rootf+"\n"+_read(d, 1, max_depth, "     ")


def _read(parent, depth, max_depth, pad):
    if max_depth >= 0 and depth >= max_depth:
        return ""
    out = ""
    for file in os.listdir(parent):
        print(pad*depth + file)
        out += pad*depth+str(file)+"\n"
        fullpath = os.path.join(parent, file)
        if os.path.isfile(fullpath):
            continue
        out += _read(fullpath, depth+1, max_depth, pad)
    return out

def _pretty_read(parent, depth, max_depth, include_file, pad):
    "Recursively reading files"
    if max_depth >= 0 and depth >= max_depth:
        return ""
    out = pad[0:-5] + "+--- " + os.path.split(parent)[-1] + "\n"
    print(pad[0:-5] + "+--- " + os.path.split(parent)[-1])
    files = []
    if include_file:
        files = os.listdir(parent)
    else:
        files = [x for x in os.listdir(parent) if os.path.isdir(os.path.join(parent, x))]
    count = 0
    for file in files:
        count += 1
        out += pad + "|    \n"
        print(pad + "|    ")
        path = os.path.join(parent, file)
        if os.path.isdir(path):
            if count == len(files):
                out += _pretty_read(path, depth+1, max_depth, include_file, pad + "     ")
            else:
                out += _pretty_read(path, depth+1, max_depth, include_file, pad + "|    ")
        else:
            out += pad + "+--- " + file
            print(pad + "+--- " + file)
    return out


def count(d, include_blank=False, recursive=True):
    """
    Count the number of lines in one file, if
    the given file is a directory and recursive
    is enabled, all the files and subfolders will
    be counted as well.

    `d` Directory or file
    
    `include_blank` Blank line counted as one line or not, default is False
    
    `recursive` Recursively count subfiles and folders if given file
    is directory, default is enabled
    """
    if os.path.isdir(d):
        if recursive:
            return _countln_recursive(d, include_blank)
        else:
            raise Exception("count: " + str(d) + " is a directory but recursive is disabled")
    return _countln(d)


def _countln_recursive(file, include_blank):
    if os.path.isfile(file):
        return _countln(file, include_blank)
    lines = 0
    for f in os.listdir(file):
        lines += _countln_recursive(os.path.join(file, f), include_blank)
    return lines


def _countln(file, include_blank):
    with open(file, errors="ignore") as f:
        lines = f.readlines()
    count = len(lines)
    if not include_blank:
        for l in lines:
            if len(l.strip()) == 0:
                count -= 1
    return count


if __name__ == "__main__":
    print(count('C:\\Users\\daniel.xu\\Work\\fc-web-ui-test\\library'))