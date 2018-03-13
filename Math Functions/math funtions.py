"""
Math functions and notes
"""

import math

def intoRadians(degrees):
    radians = (degrees * (pi/180))
    print (radians)
    return radians

def intoDegrees(radians):
    degrees = (radians * (180/pi))
    print (degrees)
    return degrees

def LOS():
    a = (input("Enter a value for A: ")).lower()
    b = (input("Enter a value for B: ")).lower()
    c = (input("Enter a value for C: ")).lower()
    theta = input("Enter a value for theta, the angle opposite C: ")
