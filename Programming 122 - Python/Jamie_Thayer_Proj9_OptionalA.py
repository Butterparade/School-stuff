"""

Jamie Thayer -- Optional Project 9 Part A

"""

""" Problem 1 """

def check_file(fname):
    """
    ('filepath')->file contents

    Opens given file path (or file name if file is in same folder as proj9)
    reads contents if able, and prints those contents if able.
    returns none

    >>> check_file("\\Users\\Hufflebluff\\Example.txt")
    Example file contents line 1
    Example file contents line 2
    Example file contents line 3...
    """
    path = (fname)
    path1 = open(path, 'r')
    for line in path1:
        print (line, end='')
    path1.close()
    print ()
    print ()
    return None










