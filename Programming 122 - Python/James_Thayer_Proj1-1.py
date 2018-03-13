"""CIS 122 Winter 2018 Week 1 Problem set #1-3
Author: Jamie Thayer
Credit: Just me, Jamie Thayer. Referenced https://docs.python.org/3/library/ to check function names
Description: Introduction to programming Week-1 problem set. Use of Python numeric data types and
operations to solve a variety of small problems."""


"""Problem 1. Attempting to buy some t-shirts"""

print ('---Problem 1. The cost of green dye seems to have gone up')
print ()

cost_green = 15
cost_yellow = 10
ttl_shirts = 128

ttl_green = ttl_shirts // 2
#Bug: Division not rounding. '//' was needed to round result to a whole interger

ttl_yellow = ttl_shirts - ttl_green


ttl_green_cost = ttl_green * cost_green
ttl_yellow_cost = ttl_yellow * cost_yellow


ttl_cost = ttl_yellow_cost + ttl_green_cost


print ('Total Cost: ' + str(ttl_cost))
print ()
print ()

"""Used str() to print ttl_cost alongside 'Total Cost: ' to make a nicer display. Also used a
couple blank print() lines for the same purpose"""


"""Problem 2. The Skill to counting Skittles"""

print ('---Problem 2. The Skill to counting Skittles')
print ()

orange = 7
#If one were to find they had only 6 orange skittles, they would just need to change this line

green = orange * 3
purple = orange + green
red = purple / 2
yellow = 100 - orange - green - purple - red
#Declaration of variables, including initial orange skittle count

candy_total = orange + green + purple + red + yellow
"""Candy total inserted to check the consistancy of my program with various numbers of orange skittles.
This value should always be 100 as long as the program is functioning properly."""

print ('Orange Skittle Count:  ' + str(orange))
print (' Green Skittle Count:  ' + str(green))
print ('Purple Skittle Count:  ' + str(purple))
print ('   Red Skittle Count:  ' + str(int(red)))
print ('Yellow Skittle Count:  ' + str(int(yellow)))
print ('     Total Candy Count:  ' + str(int(candy_total)))
print ()
print ()
"""Spaces inserted to align numbers for a better display. Attempted .center, .rjust, and format()
in numerous ways but couldn't get it to work properly. --- str() and int() have been inserted as a way to
print the number alongside text and without the floating zero"""


"""Problem 3. Because 3.154e+7 seconds in a year wasn't catchy enough"""

print ('---Problem 3. Because 31536000 seconds wasn\'t catchy enough')
print ()

song_number = 525600
#Making sure this number is actually the number of minutes in a year

days_inYear = 365
hours_inDay = 24
minutes_inHour = 60
seconds_inMinute = 60
#various known time convertions

minutes_inYear = days_inYear * hours_inDay * minutes_inHour
seconds_inYear = days_inYear * hours_inDay * minutes_inHour * seconds_inMinute
#declaring variables with math operators combining previous known variables

print ('           Number referenced in the song: ' + str(song_number))
print ('Minutes in a year calculated with Python: ' + str(minutes_inYear))
print ()
#Simply printing the original song number and the combined variable minutes_inYear to check consistancy

print ('Seconds in a year, simply because I was curious: ' + str(seconds_inYear))
print ()
#Printed seconds_inYear because I have the power to now, and I was curious



