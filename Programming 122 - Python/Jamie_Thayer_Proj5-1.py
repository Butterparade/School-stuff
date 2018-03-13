"""Project 5 by Jamie Thayer for CIS 122.
Subject__________"""

"""Problem 1"""

def isbn_gendigit (numStr):
    """
    (string)-->(string + 1-digit)
    Generates the 10th digit in a given 9-digit isbn string. Multiplies the values of individual digits within the given 9-digit string to determine the 10th digit.
    Prints the original string with its additional 10th digit. Prints X for the 10th digit if the value of isbn_mathremainder is 10.
    ('123456788')-->1234567881
    ('123456789')-->123456789X
    """
    
    if (len(numStr)) == 9:
        isbn_math = sum([(int(numStr[i])*(i+1)) for i in range(0,9)])
        isbn_mathremainder = (isbn_math % 11)
        if isbn_mathremainder == 10:
            print ('ISBN 10-digit: ', str(numStr) + 'X')
            return (str(numStr) + 'X')
        else:
            print ('ISBN 10-digit: ', str(numStr) + str(isbn_mathremainder))
            return (str(numStr) + str(isbn_mathremainder))
    else:
        print ('unacceptable')
        return None

    

print ('ISBN digit generator problem')

print ()


def isbn_check (isbn):
    """ 
    (string)-->(True or False)
    Determines whether a 10 digit string is a valid ISBN. Isolates last number in input string, and computes/compares this value to the correct 10th digit obtained from a string with the first 9 digits of the input string.
    Returns true if true, false if not.
    ('097522980X')--> True
    ('5678901231')--> Flase
    """
    isbn_numStr = isbn[0:-1]
    isbncheck_math = sum([(int(isbn_numStr[i])*(i+1)) for i in range(0,9)])
    isbncheck_mathremainder = (isbncheck_math % 11)
    if isbncheck_mathremainder == 10:
        isbncheck_mathremainder = str('X')
        print (isbncheck_mathremainder == isbn[-1]) == True
        return (isbncheck_mathremainder == isbn[-1])
    else:
        print (int(isbncheck_mathremainder) == int(isbn[-1]))
        return (isbncheck_mathremainder == isbn[-1])

    
isbn_gendigit('123456789')
isbn_gendigit('020141452')
isbn_gendigit('058132921')
isbn_gendigit('068333923')
isbn_gendigit('567890123')
isbn_check('097522980X')
isbn_check('0681319216')
isbn_check('5678901230')
isbn_check('5678901231')


"""Problem 2"""

def is_safelead(lead,ball,time):
    """
    (num,boolean,num)-->(Safe or Unsafe)
    Computes weather or not the lead is big enough to be considered safe based on the difference in points, possesion of the ball, and time left on the clock in seconds.
    (10,True,56)-->safe!
    (10,False,56)-->so unsafe!
    """
    safeScore = (lead - 3)
    if ball == True:
        safeScore += 0.5
        newSafeScore = safeScore*safeScore
        if newSafeScore >= time:
            print ('safe!')
        else:
            print ('so unsafe!')
    else:
        safeScore += -0.5
        newSafeScore = safeScore*safeScore
        if newSafeScore >= time:
            print ('safe!')
        else:
            print ('so unsafe!')

is_safelead(10,True,57)
is_safelead(10,False,56)

"""Problem 3"""

def transcribe(S):
    """had a lot of trouble with this one, but I did my best, and I'll keep trying to figure it out!"""
    for letter in S:
        if letter == 'A':
            S = S.replace(letter,'U')
    for letter in S:
        if letter == 'C':
            S = S.replace(letter,'G')
    for letter in S:
        if letter == 'G':
            S = S.replace(letter,'C')
    for letter in S:
        if letter == 'T':
            S = S.replace(letter,'A')
        elif letter != 'A' or 'C' or 'G' or 'T':
            S = S.replace(letter,'')
            print (S)
            return None
            
transcribe('ACGT TGCA')
