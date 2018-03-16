"""

Jamie Thayer -- Optional Project 9

"""



""" Problem 1 """

def check_file(fname):
    path = (fname)
    path1 = open(path, 'r')
    for line in path1:
        print (line, end='')
    path1.close()
    return None

""" End Problem 1 """



""" Problem 2 """

def fbkup(fname):
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

"""
path_bkup1.write(contents)
path1.close()
path_bkup1.close()
return ('%s-fbkup' % (fname))
"""


""" End Problem 2 """


""" Problem 3 """

check_file("\\Users\\Hufflebluff\\Documents\\GitHub\\School-stuff\\example.txt")
mybackupf = fbkup('\\Users\\Hufflebluff\\Documents\\GitHub\\School-stuff\\example.txt')      #'example-bkup.txt'
check_file(mybackupf)

""" End Problem 3 """


