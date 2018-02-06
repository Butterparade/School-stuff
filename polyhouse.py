import turtle


'''
sidenumber = int(input('Number of Sides: '))
sidelength = int(input('Length of Sides: '))
color = str(input('Color: '))



def polyhouse (n, length, color):
    """
    (int, number, string)-->none
    Draws a polygon with n sides of a given length filled in with a given color
    """
    angle = 360/n

    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(n):
        turtle.fd(length)
        turtle.left(angle)
    turtle.end_fill()
    return None

polyhouse(sidenumber, sidelength, color)
'''

def polygon(n, length, color):
    """
    (int, number, string)-->none
    Draws a polygon of requested size and color
    """

    angle = 360/n

    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(n):
        turtle.fd(length)
        turtle.left(angle)
    turtle.end_fill()
    return None

def drawSomePolygons():
    """
    ()->None
    """
    polygon(4,100,'red')
    turtle.up()
    turtle.fd(200)
    turtle.down()
    polygon(5,200,'green')
    return None

drawSomePolygons()

'''
min(1,2,3,.05)
"""returns 0.05
returns smallest value"""
max(1,2,3,4)
"""returns 4
returns largest value"""
'''
