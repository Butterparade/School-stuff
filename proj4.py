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

"""end problem 1"""

def max_trans1 (a,b,c):

    print(min(a,b,c))
    return None

def max_trans2 (a,b,c,d,e):

    if (min(a,b,c))>(min(d,e)):
        print(min(a,b,c))
    elif (min(a,b,c))<(min(d,e)):
        print(min(d,e))
    else:
        print(min(a,b,c,d,e))
    return None

    
max_trans1(1,2,3)
max_trans1(9,6,3)
max_trans1(0,0,0)

max_trans2(1,2,3,4,5)
max_trans2(222,110,411,54,73)
max_trans2(0,0,0,0,0)    

"""end problem 2"""

def isbn_gendigit (a):

    if (len(a)) == 9:
        isbn_math = (int(a[0]) * 1) + (int(a[1]) * 2) + (int(a[2]) * 3) + (int(a[3]) * 4) + (int(a[4]) * 5) + (int(a[5]) * 6) + (int(a[6]) * 7) + (int(a[7]) * 8) + (int(a[8]) * 9)
        isbn_mathremainder = (isbn_math % 11)
        print (str(a) + str(isbn_mathremainder))
        return None
    else:
        print ('unacceptable')
        return None

isbn_gendigit('020131452')

isbn_gendigit('068131921')

"""end problem 3"""
    
