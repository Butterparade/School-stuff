"""
Math functions and notes
"""

import math

print ('----Math functions loaded up---- \nEnter \'list_functions()\' to display available functions')

def list_functions():
    print ('intoRadians()')
    print ('intoDegrees()')
    print ('LOS()')
    print ('vectorProduct()')
    print ('vectorMag()')

def intoRadians():
    degrees = float(input('Enter degrees: '))
    radians = (degrees * (pi/180))
    print (radians)
    return radians

def intoDegrees():
    radians = float(input('Enter radians: '))
    degrees = (radians * (180/pi))
    print (degrees)
    return degrees

def LOS():
    choice = input('Enter \'c\' to solve for c. \nEnter \'theta\' to solve for theta.')
    if choice == 'c':
        LOS_c()
    else:
        LOS_theta()

def LOS_c():
    a = float(input("Enter a value for A: "))
    b = float(input("Enter a value for B: "))
    theta = float(input("Enter a value for theta: "))
    c = (math.sqrt(((a**2) + (b**2)) - ((2*a*b) * math.cos(theta))))
    return c

def LOS_theta():
    a = float(input("Enter a value for A: "))
    b = float(input("Enter a value for B: "))
    c = float(input("Enter a value for C: "))
    theta = (math.asin(((c**2)-(b**2)-(a**2))/(-2*a*b)))
    print (theta)
    return theta

def vectorProduct():
    vector_1_i = float(input('Enter vector 1\'s i value: '))
    vector_1_j = float(input('Enter vector 1\'s j value: '))
    vector_2_i = float(input('Enter vector 2\'s i value: '))
    vector_2_j = float(input('Enter vector 2\'s j value: '))
    vector_product = [(vector_1_i * vector_2_i) + (vector_1_j * vector_2_j)]
    print (vector_product)
    return vector_product

def vectorMag():
    vector_1_i = float(input('Enter vector 1\'s i value: '))
    vector_1_j = float(input('Enter vector 1\'s j value: '))
    vec_mag = math.sqrt((vector_1_i ** 2) + (vector_1_j ** 2))
    print (vec_mag)
    return vec_mag

def coSolve():
    adj = float(input('Enter length of adjacent side: '))
    hypot = float(input('Enter length of hypotenuse: '))
    coSolution = (math.acos(adj / hypot))
    print (coSolution)

def sinSolve():
    opp = float(input('Enter length of opposite side: '))
    hypot = float(input('Enter length of hypotenuse: '))
    sinSolution = (math.asin(opp / hypot))
    print (sinSolution)
