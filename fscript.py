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


def scan(d, ignore=[], skip=[], name=[], ext=[], recursive=False):
    """
    Scan through the file or directory and return a list of files
    that matches the given restriction.

    `d` Directory or file

    `ignore=[]` Ignore files that match the given `regex patterns`, they
    will not be added to the output list

    `skip=[]` Skip the directories that match the `regex patterns`, their
    children will not be scanned as well

    `name=[]` Only matches files that have the given name, NOT regex
    patterns but regular `string`

    `ext=[]` Only matches files that have the given extention, NOT regex
    patterns but regular `string`. Dot are required, for example `.py`
    or `.txt`

    `recursive=False` Recursively scan all the folders until everything
    is scanned
    """
    if not recursive:
        return _scan(d, ignore, skip, name, ext)
    result = []
    _scan_recursive(d, ignore, skip, name, ext, result)
    return result


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


def _scan(f, ignore, skip, name, ext):
    result = []
    if os.path.isfile(f):
        if _file_save(f, ignore, name, ext):
            result.append(f)
        return result
    for d in skip:
        if d in f:
            return result
    for file in os.listdir(f):
        fullpath = os.path.join(f, file)
        if os.path.isfile(fullpath):
            if _file_save(fullpath, ignore, name, ext):
                result.append(fullpath)
    return result


def _scan_recursive(f, ignore, skip, name, ext, result):
    if os.path.isfile(f):
        if _file_save(f, ignore, name, ext):
            result.append(f)
        return
    for d in skip:
        if d in f:
            return
    for file in os.listdir(f):
        fullpath = os.path.join(f, file)
        _scan_recursive(fullpath, ignore, skip, name, ext, result)


def _file_save(f, ignore, name, ext):
    "Return True if file matches none of the restrictions"
    fname, fext = os.path.splitext(f)
    for i in name:
        if fname == i:
            return False
    for i in ext:
        if i == fext:
            return False
    for i in ignore:
        if re.match(f, i):
            return False
    return True
