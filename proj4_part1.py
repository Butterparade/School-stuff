import turtle

def polygon (n, length, color):
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
          
def house ():
    """
    (polyhouse)-->none
    """

    polygon(4,40,'red')
    turtle.up()
    turtle.setpos(0,40)
    turtle.down()
    polygon(3,40,'yellow')
    turtle.up()
    turtle.setpos(15,0)
    turtle.down()
    polygon(4,10,'black')



house()

    

    

    
