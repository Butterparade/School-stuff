"""Project 4 by Jamie Thayer for CIS 122.
Determining max loads, making houses, and finding the 10th ISBN digit"""

import turtle

def polygon (n, length, color):
    """
    (int, number, string)-->none
    Draws a polygon with n sides of a given length, filled in with a given color
    """
    angle = 360/n

    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(n):
        turtle.ht()
        turtle.up()
        turtle.fd(length)
        turtle.left(angle)
        turtle.down()
    turtle.end_fill()
    return None

"""The example house on the assignment doesn't have any borders so I added .up, and .down to recreate a house without those borders.
The drawing process looked a bit weird at that point though, so I used .ht to hide the turtle's movement from view. The result looks a bit better,
but now it feels like it has a delay since nothing appears until the turtle has completed the first polygon. It does get the job done though"""
          
def house ():
    """
    (house)-->none
    Draws a house, complete with roof and door.

    1st polygon defines house base
    2nd polygon defines roof
    3rd polygon defines door
    """

    polygon(4,40,'green')
    turtle.up()
    turtle.setpos(0,40)
    turtle.down()
    polygon(3,40,'yellow')
    turtle.up()
    turtle.setpos(15,0)
    turtle.down()
    polygon(4,10,'black')
    return None


house()


"""Problem 2"""

def max_trans1 (a,b,c):
    """
    (int, int, int)-->Returns lowest value among the inputs a, b, and c
    Determines the maximum load allowed over three consequtive bridges by finding the lowest maximum load among the three
    (5,7,9)-->5
    """
    print('Max load: ', min(a,b,c))
    return None

def max_trans2 (a,b,c,d,e):
    """
    (int, int, int, int, int)-->none
    Determines the maximum load allowed between two possible routes, one traveling over bridges with max loads of a, b, and c, and the other traveling over bridges with max loads d, and e.
    (5,7,9,6,6)-->6
    """
    
    if (min(a,b,c))>(min(d,e)):
        print('Max load: ', min(a,b,c))
    elif (min(a,b,c))<(min(d,e)):
        print('Max load: ', min(d,e))
    else:
        print('Max load: ', min(a,b,c,d,e))
    return None


print ('Maximum Load Problem')
print ()

print ('Part 1: Finding the max load along consequtive 3 bridges')
max_trans1(1,2,3)
max_trans1(9,6,3)
max_trans1(0,0,0)
print ()

print ('Part 2: Finding the max load between two possible paths')
max_trans2(1,2,3,4,5)
max_trans2(222,110,411,54,73)
max_trans2(0,0,0,0,0)    
print()
print()

"""Problem 3"""

def isbn_gendigit (numStr):
    """
    (string)-->(string + 1-digit)
    Generates the 10th digit in a given 9-digit isbn string. Multiplies the values of individual digits within the given 9-digit string to determine the 10th digit.
    Prints the original string with its additional 10th digit.
    ('123456788')-->1234567881
    """
    
    if (len(numStr)) == 9:
        isbn_math = (int(numStr[0]) * 1) + (int(numStr[1]) * 2) + (int(numStr[2]) * 3) + (int(numStr[3]) * 4) + (int(numStr[4]) * 5) + (int(numStr[5]) * 6) + (int(numStr[6]) * 7) + (int(numStr[7]) * 8) + (int(numStr[8]) * 9)
        isbn_mathremainder = (isbn_math % 11)
        print ('ISBN 10-digit: ', str(numStr) + str(isbn_mathremainder))
        return None
    else:
        print ('unacceptable')
        return None

print ('ISBN digit generator problem')
print ()

isbn_gendigit('020131452')

isbn_gendigit('068131921')
