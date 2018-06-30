"""

Jamie Thayer -- Optional Project 9 Part B

"""

from Jamie_Thayer_Proj9_OptionalA import check_file

""" Problem 2 """

def fbkup(fname):
    """
    ('filepath')->None

    Opens given file path (or file name if file is in same folder as proj9)
    reads contents if able, saves contents to a new file

    new file has same name as input but with 'fbkup' in it
    new file also retains its file type.
    Tested to work with .txt and .doc, does not work with .docx
    
    returns (new backup filename)
    """
    path = (fname)
    path1 = open(path, 'r')
    fname_splice = fname.split('.', 1)[0]
    fname_splice2 = fname.split('.', 1)[1]
    
    path_bkup = ('%s-fbkup.%s' % (fname_splice, fname_splice2))
    path_bkup1 = open(path_bkup, 'w')
    contents =''
    for line in path1:   
        contents += line
    path_bkup1.write(contents)
    return path_bkup

""" Problem 3 """

check_file("example.txt")
mybackupf = fbkup('example.txt')
check_file(mybackupf)
