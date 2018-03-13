import turtle

turtlecolor = input('What color would you like to fill a square with?: ')

def turtlefunction (turtlecolor):

    turtle.fillcolor(turtlecolor)
    turtle.begin_fill()
    turtle.fd(50)
    turtle.lt(90)
    turtle.fd(50)
    turtle.lt(90)
    turtle.fd(50)
    turtle.lt(90)
    turtle.fd(50)
    turtle.lt(90)
    turtle.end_fill()

turtlefunction(turtlecolor)

n = input('# of sides: ')
length = input('length of sides: ')
color = input('color: ')

def my_polygon (n, length, color):
    for i in range(int(n)):
        turtle.fillcolor(str(color))
        turtle.begin_fill()
        turtle.left(1 / (int(n)))
        turtle.fd(int(length))
        turtle.end_fill()

my_polygon(n, length, color)
