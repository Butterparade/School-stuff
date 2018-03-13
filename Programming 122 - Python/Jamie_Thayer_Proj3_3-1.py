import turtle
import math

radiusinput = int(input('Give me the radius of your desired circle: '))

circumference = (radiusinput*2)*math.pi

def turtlecircle (radiusinput):
    for i in range(int(circumference)):
        turtle.speed(0)
        turtle.fd(1)
        turtle.left(360 / int(circumference))

turtlecircle(radiusinput)



"""after 90 movements, should be at point (0,radius)"""
