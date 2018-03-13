"""
Jamie Thayer -- Project Week 8

"""

""" Problem 1a and 1b """

def diff_first_last(L, *opArg):
    """
    (list) -> boolean
    Precondition: len(L) >= 2

    Returns True if the first item of the list is different from the last; else returns False.

    >>> diff_first_last([3, 4, 2, 8, 3])
    False
    >>> diff_first_last(['apple', 'banana', 'pear'])
    True
    >>> diff_first_last([4.0, 4.5])
    True


    --- Additional Test Cases ---
    
    >>> diff_first_last(3, 4, 2, 8, 3)
    False
    >>> diff_first_last('apple', 'banana', 'pear')
    True
    >>> diff_first_last([5, 4], 4, 5, 4)
    True
    >>> diff_first_last([5, 4], 4, [5, 4])
    False
    >>> diff_first_last('eeee')
    Invalid length. Nothing to compare to.
    >>> diff_first_last([5])
    Invalid length. Nothing to compare to.

    Additional test cases show that the function can handle non-list inputs
    of various kinds. Function can also handle invalid inputs of various kinds
    """
    print ()
    print ('---Checking if first and last values are unequal---')
    print ('Input is: ', L, *opArg)
    if not opArg:
        if type(L) == str:
            print ('Invalid length. Nothing to compare input to.')
            return None
        elif len(L) >= 2:
            print (L[0] != L[-1])
            return (L[0] != L[-1])
        else:
            print ('Invalid length. Nothing to compare input to.')
            return None
    else:
        print (L != opArg[-1])
        return (L != opArg[-1])



diff_first_last([3, 4, 2, 8, 3])
diff_first_last(['apple', 'banana', 'pear'])
diff_first_last([4.0, 4.5])
diff_first_last(3, 4, 2, 8, 3)
diff_first_last('apple', 'banana', 'pear')
diff_first_last([5, 4], 4, 5, 5)
diff_first_last([5, 4], 4, [5, 4])
diff_first_last('eeee')
diff_first_last([5])
print ()
print ()

""" Problem 2a """

def middle(L):
    """
    (list) --> value
    output is of the same type as the values in list

    Returns the middle value in a given list.

    
    middle([7,6,5,4,3,2,1])
    >>> 4
    middle([6,5,4,3,2,1])
    >>> 999999
    middle([])
    >>> blank detected
    middle(['apple','pear','bannanana'])
    >>> pear
    middle(['apple','pear','bannanana', 'apple'])
    >>> 999999
    """
    print ()
    print ('---Finding middle value---')
    print ('Input: ', L)
    if ((len(L) % 2) != 0):
        Q = (len(L) // 2)
        I = L[Q]
        print (I)
        return I
    elif len(L) == 0:
        print ('blank detected')
        return None
    else:
        print ('999999')
        return 999999
    

middle([7,6,5,4,3,2,1])
middle([6,5,4,3,2,1])
middle([])
middle(['apple','pear','bannanana'])
middle(['apple','pear','bannanana', 'apple'])
print ()
print ()


""" Problem 2b """

def mySum(L):
    """
    (number list) --> number

    Returns the sum of the numbers in a given list

    mySum([2,3,2])
    >>> 7
    mySum([])
    >>> blank detected
    mySum([2])
    >>> 2
    mySum([1,2,3,4,5])
    >>> 15
    mySum([-1,-2,-3,-4,-5])
    >>> -15
    """

    print ()
    print ('---Finding sum of input---')
    print ('Input: ', L)
    ctr = 0
    for x in L:
        ctr += x
    if ctr == 0:
        print('blank detected')
        return None
    else:
        print (ctr)
        return ctr

mySum([2,3,2])
mySum([])
mySum([2])
mySum([1,2,3,4,5])
mySum([-1,-2,-3,-4,-5])
print ()
print ()


""" Problem 3 """

def checklen(astring):
    """
    (str) -> Boolean

    Returns true if length of astring is at least 5 characters long, else False

    >>> checklen('', 1)
    False
    >>> checklen('four', 5)
    False
    >>> checklen('check', 5)
    True
    >>> checklen('check6', 6)
    True
    """
    return len(astring) >= 5

def is_nonalnum(astring):
    """
    (str) -> Boolean

    Returns True if astring contains at
    least one non-alphanumeric character.
    else returns False.

    >>> is_nonalnum('')
    False
    >>> is_nonalnum('abc123')
    False
    >>> is_nonalnum('#123')
    True
    """
    if len(astring) == 0:
        return False
    else:
        return not(astring.isalnum())

def is_noEe(astring):
    """
    (str) -> Boolean

    Returns True if astring does NOT
    contain characters 'E' or 'e'
    else returns False.

    >>> is_noEe('')
    True
    >>> is_noEe('e')
    False
    >>> is_noEe('CHEM 101')
    False
    >>> is_noEe('abcd')
    True
    """
    lowere = 'e' in astring
    uppere = 'E' in astring
    return not(lowere or uppere)
    
def is_uc_alpha(astring):
    """
    (str) -> Boolean

    return True if any char in astring is an 
    uppercase letter.
    else return False

    >>> is_uc_alpha('CIS122')
    True
    >>> is_uc_alpha('Ducks')
    True
    >>> is_uc_alpha('testing')
    False
    """
    for c in astring:
        if c.isupper():
            return True
    return False


def is_2numbers(astring):
    """
    (str) -> Boolean
    
    returns True if astring has at least two numbers.
    else return False.

    >>> is_2numbers('CIS122')
    True
    >>> is_2numbers('Ducks')
    False
    >>> is_2numbers('ABC-1')
    False
    """
    digits_ctr = 0

    for c in astring:
        if c.isdigit():
            digits_ctr += 1

    return digits_ctr >= 2

def is_special_char(astring):
    """
    (str) -> Boolean
    
    returns True if astring contains a
    special character:!, @, #, $, %, ^, &
    else return False.

    >>> is_special_char('CIS122')
    False
    >>> is_special_char('CIS-122')
    False
    >>> is_special_char('CIS122!')
    True
    """
    special = '!@#$%^&'
    for c in astring:
        if c in special:
            return True

    return False

def is_common_pass(astring):
    """
    (str) -> Boolean
    
    returns False if astring is also a string within common[]
    common[] contains common passwords that the function checks against.

    common includes: 'password', '12345', 'qwerty', 'letmein',
    'trustno1', '000000', 'passw0rd'

    >>> 'passwordup'
    True
    >>> 'qwerky'
    True
    >>> 'qwerty'
    False
    """
    common = ['password', '12345', 'qwerty', 'letmein', 'trustno1', '000000', 'passw0rd']
    if astring in common:
        return False
    else:
        return True

""" Problem 3 """

def passwordChecker(astring):
    """
    (str) -> Boolean

    Checks the validity of a given password
    against a variety of parameters
    
    Returns false if the password is not valid
    else return true.

    >>> 'qwerty'
    False
    >>> ' '
    False
    >>> '1111Q11@#$%'
    True
    >>> 'Qwrty01!'
    True
    >>> '13!Passw0rd!'
    True
    >>> 'Gr8P@ssw0rd123!_with_e'
    False
    """
    print ()
    print ('---Checking Password Validity---')
    print ('Input: \'%s\'' % (astring))
    print ()
    spec_check = is_special_char(astring)
    two_num_check = is_2numbers(astring)
    uc_check = is_uc_alpha(astring)
    noEe_check = is_noEe(astring)
    non_all_num_check = is_nonalnum(astring)
    len_check = checklen(astring)
    common_check = is_common_pass(astring)
    check_list = [spec_check, two_num_check, uc_check, noEe_check, non_all_num_check, len_check, common_check]

    if not spec_check:
        print ('Password does not contain a Special Character')
    if not two_num_check:
        print ('Password does not contain at least 2 numbers')
    if not uc_check:
        print ('Password does not contain at least 1 uppercase letter')
    if not noEe_check:
        print ('Password contains \'E\' or \'e\'')
    if not non_all_num_check:
        print ('Password does not contain at least 1 non-alphanumeric value')
    if not len_check:
        print ('Password must be at least 5 characters in length')
    if not common_check:
        print ('Password is too common, chose another one')
    all_check = True
    for check in check_list:
        if not check:
            all_check = False
    if all_check:
        print ('Password is Valid!')
        return True
    else:
        return False
        
passwordChecker('qwerty')
passwordChecker(' ')
passwordChecker('1111Q11@#$%')
passwordChecker('Qwrty01!')
passwordChecker('13!Passw0rd!')
passwordChecker('Gr8P@ssw0rd123!_with_e')
       






    

