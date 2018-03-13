import turtle

"""declaring Q as the ratio of the size of the earth compared
to the size of the sun"""
Q = (1392000/12756)

turtle.up()
turtle.goto(0,-320)
turtle.down()
turtle.fillcolor('green')
turtle.begin_fill()
turtle.circle(2.75)
turtle.end_fill()
turtle.up()
turtle.goto(0,-300)
turtle.down()
turtle.fillcolor('orange')
turtle.begin_fill()
turtle.circle(Q*2.75)
turtle.end_fill()
turtle.hideturtle()
