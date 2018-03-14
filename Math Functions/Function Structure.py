"""
Math function Structural core
"""

import math

def mathFace():
    """
    Front end of the math program, prompts user for input and problem type.
    """
    print ('Enter the type of problem you wish to solve for.')
    print ('Options include:')
    print ('Triangle')
    print ('Angle')
    print ('Vector')
    print ('Convert')
    print ()
    faceInput = input()
    faceInput = faceInput.lower()
    if faceInput == 'triangle':
        #possible callRightTriangle() or callOtherTriangle() spot
        print ('What triangle problem are you trying to solve?')
        print ('Options include:')
        print ('Hypotenuse length                           short:  hyp')
        print ('Side length                                 short:  side')
        print ('2 Side Lengths, 1 angle. Solve angle        short:  angle')
        print ('3 Side Lengths                              short:  3side')
        faceInputTwo = input()
        faceInputTwo = faceInputTwo.lower()
        if faceInputTwo == 'hypotenuse length' or 'hyp':
            solution = X                                     #NEEDS FUNCTION
            print (solution)
            return solution
        if faceInputTwo == 'side length' or 'side':
            solution = X                                     #NEEDS FUNCTION
            print (solution)
            return solution
        if faceInputTwo == '2 side lengths, 1 angle. solve angle' or 'angle':
            solution = X                                     #NEEDS FUNCTION
            print (solution)
            return solution
        if faceInputTwo == '3 side lengths' or '3side':
            solution = X                                     #NEEDS FUNCTION
            print (solution)
            return solution
        else:
            return None
    elif faceInput == 'angle':
        print ('What angle problem are you trying to solve?')
        print ('Options include:')
        print ('3 Side Lengths                              short:  3side')
        print ('2 Side Lengths, 1 angle. Solve angle        short:  angle')
        print ('Angles around the unit circle               short:  circle')
        faceInputTwo = input()
        faceInputTwo = faceInputTwo.lower()
        if faceInputTwo == '3 side lengths' or '3side':
            solution = X                                     #NEEDS FUNCTION
            print (solution)
            return solution
        if faceInputTwo == '2 side Lengths, 1 angle. solve angle' or 'angle':
            solution = X                                     #NEEDS FUNCTION
            print (solution)
            return solution
        if faceInputTwo == 'Angles around the unit circle' or 'circle':
            solution = X                                     #NEEDS FUNCTION
            print (solution)
            return solution
        else:
            return None
    elif faceInput == 'vector':
        print ('What vector problem are you trying to solve?')
        print ('Options include:')
        print ('Addition                   short:  add')
        print ('Subtraction                short:  sub')
        print ('Multiplication             short:  mul')
        print ()
        faceInputTwo = input()
        faceInputTwo = faceInputTwo.lower()
        if faceInputTwo == 'addition' or 'add':
            solution = X                                     #NEEDS FUNCTION
            print (solution)
            return solution
        if faceInputTwo == 'subtraction' or 'sub':
            solution = X                                     #NEEDS FUNCTION
            print (solution)
            return solution
        if faceInputTwo == 'multiplication' or 'mul':
            solution = X                                     #NEEDS FUNCTION
            print (solution)
            return solution
        else:
            return None
    elif faceInput == 'convert':
        print ('What conversion would you like to compute?')
        print ('Options include:')
        print ('Radians into Degrees            short:  r2d')
        print ('Degrees into Radians            short:  d2r')
        print ()
        faceInputTwo = input()
        faceInputTwo = faceInputTwo.lower()
        if faceInputTwo == 'radians into degrees' or 'r2d':
            solution = intoDegrees(butter)
            print (solution)
            return solution
        if faceInputTwo == 'degrees into radians' or 'd2r':
            solution = intoRadians(butter)
            print (solution)
            return solution
        else:
            return None
    else:
        print ('Invalid selection - Math Face')
        mathFace()
        return None

def mathSolve(butter):
    if butter == '':
        return None
    elif butter == '':
        return None
    elif butter == '':
        return None
    elif butter == '':
        return None
    elif butter == '':
        return None
    else:
        print ('Invalid selection - Math Solve')
        mathFace()
        return None

def callRightTriangle():
    print ('################################################')
    print ('##########################     #################')
    print ('##########################  B  #################')
    print ('########################## /|  #################')
    print ('##########################/ |###################')
    print ('#########################/  |###################')
    print ('########################/\  |###################')
    print ('#######################/  \ |###################')
    print ('######################/ <b \|###################')
    print ('#####################/      |###################')
    print ('####################/       |###################')
    print ('###################/        |###################')
    print ('##################/         |###################')
    print ('#################/          |###################')
    print ('################/           |###################')
    print ('###############/           /|###################')
    print ('##############/\<a     <c / |###################')
    print ('##########   /__\________/__|   ################')
    print ('##########  A  ############  C  ################')
    print ('##########     ############     ################')
    print ('################################################')
    return None

def callOtherTriangle():
    print ('################################################')
    print ('#######################       ##################')
    print ('#######################   B   ##################')
    print ('#######################  /\   ##################')
    print ('########################/  \####################')
    print ('#######################/    \###################')
    print ('######################/______\##################')
    print ('#####################/        \#################')
    print ('####################/    <b    \################')
    print ('###################/            \###############')
    print ('##################/              \##############')
    print ('#################/                \#############')
    print ('################/                  \############')
    print ('###############/                   /\###########')
    print ('##############/\  <a          <c  /  \##########')
    print ('#############/  \                /    \#########')
    print ('#########   /____\______________/______\    ####')
    print ('#########  A   #######################  C   ####')
    print ('#########      #######################      ####')
    print ('################################################')
    return None

mathFace()
