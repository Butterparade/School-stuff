"""Project 5 by Jamie Thayer for CIS 122.
Subject__________"""

"""Problem 1"""

def isbn_gendigit (numStr):
    """
    (string)-->(string + 1-digit)
    Generates the 10th digit in a given 9-digit isbn string. Multiplies the values of individual digits within the given 9-digit string to determine the 10th digit.
    Prints the original string with its additional 10th digit.
    ('123456788')-->1234567881
    """
    
    if (len(numStr)) == 9:
        isbn_math = sum([(int(numStr[i])*i+1) for i in range(0,9)])
        isbn_mathremainder = (isbn_math % 11)
        if (isbn_mathremainder) == 10:
            print ('ISBN 10-digit: ', str(numStr) + str('X')
        else:
            print ('ISBN 10-digit: ', str(numStr) + str(isbn_mathremainder))
            return None
    else:
        print ('unacceptable')
        return None

print ('ISBN digit generator problem')
print ()

isbn_gendigit('020131452')

isbn_gendigit('068131921')


"""Problem 2"""

        


"""Problem 3"""

