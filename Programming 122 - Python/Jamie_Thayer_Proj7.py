""" Problem 1 """

print ()
print ('Rock Paper Scissors generator')
print ('      -------1-------        ')

import random

def rockPaperScissors():
    """
    Runs a game of rock paper scissors and determines the winner using values from import random

    input: y, y --> Winner! Side 1 or Side2 orTie

    input: n or (y, n) --> Exiting...
    """
    
    print ()
    optIn = str(input('Would you like to play Rock, Paper, Scissors? \nEnter \'Y\' to play or \'N\' if you don\'t want to.\n'))
    optIn = optIn.upper()
    print ()
    
    if (optIn == 'Y'):
        def rockPaperScissorsRun():
            print ('Running a round of Rock, Paper, Scissors')
            print ('          --------------------          ')
            s1 = random.choice('rps')
            s2 = random.choice('rps')
            if (s1 == 'r') and (s2 == 'p'):
                winner = 'Side 2'
            elif (s1 == 'r') and (s2 == 's'):
                winner = 'Side 1'
            elif (s1 == 'p') and (s2 == 's'):
                winner = 'Side 2'
            elif (s1 == 'p') and (s2 == 'r'):
                winner = 'Side 1'
            elif (s1 == 's') and (s2 == 'r'):
                winner = 'Side 2'
            elif (s1 == 's') and (s2 == 'p'):
                winner = 'Side 1'
            else:
                winner = 'no one! Its a Tie!'
            print ('Side 1 chose {}! \nSide 2 chose {}!'.format(s1,s2))
            print ('The winner is {}!'.format(winner))
            print ()
            playAgain = input('Would you like to play again? \nEnter \'Y\' to run another round or \'N\' to Exit.\n')
            playAgain = playAgain.upper()
            if (playAgain == 'Y'):
                rockPaperScissorsRun()
            elif (playAgain == 'N'):
                print ('You have chosen not to play another round \nExiting...')
            else:
                print ('Invalid entry')
                rockPaperScissors()
                return None
            
        rockPaperScissorsRun()
    elif (optIn == 'N'):
        print ('You have chosen not to play, Exiting...')
        return None
    else:
        print ('Invalid Entry')
        rockPaperScissors()
        return None

rockPaperScissors()
print ()

""" Problem 2a """

print ()
print ('Vowel Counter')
print ('   --2a--    ')
def count_vowels(s):
    """
    (str)-int
    return number of vowels in s.

    >>> count_vowels('The quick brown fox')
    5
    """
    lowerS = s.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    ctr = 0
    for ch in lowerS:
        if ch in vowels:
            ctr += 1
    print ('There are {} vowels in: "{}"'.format(ctr, s))
    print ()
    return ctr

count_vowels('The quick brown fox')
count_vowels('An enormous blue whale that can jump')
count_vowels('Desert vs. Dessert')
count_vowels('Tomato potato')
count_vowels('Example 5, with numbers')

""" Problem 2b """
print ()
print ('Min/Max calculator')
print ('    ----2b----    ')

def find_min_max(values):
    """
    (string) -> None
    Find the maximum and minimum values in a non-empty string of digits and print them.
    None value is returned.
    >>> find_min_max('45312')
    The minimum value is 1.
    The maximum value is 5.
    >>> find_min_max('428')
    The minimum value is 2.
    The maximum value is 8.
    """
    
    mmin = 9
    mmax = 0

    for value in values:
        value = int(value)
        if value > mmax:
            mmax = value
        elif value < mmin:
            mmin = value
        
    print ('In "{}", the minimum and maximum values are: '.format(values))
    print ('Minimum value: ', mmin)
    print ('Maximum value: ', mmax)
    print ()
find_min_max('45312')
find_min_max('428')
find_min_max('4280000231')
find_min_max('42128987')
find_min_max('99999')
find_min_max('0000000')

""" Problem 2c """

print ()
print ('Average Calculator')
print ('    ----2c----    ')

def my_average(dataset):
    """
    (string) -> float
    returns average of values in input string values, but zeros do not count at all
    >>> my_average('23')
    2.5
    >>> my_average('203')
    2.5
    """
    
    count = 0
    total = 0

    for value in dataset:
        if value != '0':
            total += int(value)
            count += 1
    if (count == 0):
        print ('Input "{}" Invalid. No valid numbers to take an average from'.format(dataset))
    else:
        avg = total / count
        print ('Among non-zeros in dataset: "{}"'.format(dataset))
        print ('The Average is: ', avg)
        print ()
        return avg

my_average('23')
my_average('203')
my_average('2267541470000000')
my_average('2231253')
my_average('2123123')
my_average('000000')


""" Problem 3 """
print()
print('Time Converter')
print('   ---3---    ')

def minutesToHours(minutes):
    """
    (number) -> float
    convert input minutes to hours;
    return hours

    >>> minutesToHours(60)
    1.0
    >>> minutesToHours(90)
    1.5
    >>>minutesToHours(0)
    0.0
    """
    hours = minutes / 60
    hours = round(hours, 2)
    return hours

def hoursToDays(hours):
    """
    (number) -> float
    convert input hours to days; return days

    >>> hoursToDays(24)
    1.0
    >>> hoursToDays(100)
    4.17
    >>> hoursToDays(0)
    0.0
    """
    days = hours / 24
    days = round(days, 2)
    return days

def daysToYears(days):
    """
    (number) -> float
    convert input days to years; return years
    >>> daysToYears(365)
    1.0
    >>> daysToYears(100)
    0.27
    >>>
    daysToYears(0)
    0.0
    """
    years = days / 365
    years = round(years, 2)
    return years

def minutesToYears(m):
    """
    (int) -> float
    input number m minutes is converted to equivalent number of years. return years.
    call auxiliary functions to do each step.

    >>> minutesToYears(525600)
    1.0
    >>> minutesToYears(5256000)
    10.0
    >>> minutesToYears(394200)
    0.75
    >>> minutesToYears(0)
    0.0
    """
    hours = minutesToHours(m)
    days = hoursToDays(hours)
    years = daysToYears(days)
    print('{} minutes would be equal to {} years.'.format(m, years))
    return years

print ('Minutes to Years: ')
print ()
minutesToYears(525600)
minutesToYears(5256000)
minutesToYears(394200)
minutesToYears(0)
minutesToYears(908)
