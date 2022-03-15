#!/usr/bin/env python3
"""SSS | DGish
   if, elif, else - A simple program using conditionals to make a decision."""


message = 'Your Synopsis is: '

# wrap connection in a float() to accept decimals as numbers
Book = int(input("Enter the book number in the LotR series you would like to retrieve a synopsis of (1 = The Hobbit):"))

# if input value was higher or equal to 25
if Book  == 1 :
    message = message + 'Bilbo finds the ring.'
elif Book == 2:
    message = message + 'Bilbo gives the ring to Frodo and the adventure begins.'
elif Book == 3:
    message = message + 'Frodo and Sam go to Mordor and some armies fight.'
elif Book == 4:
    message = message + 'Some more armies fight and Frodo throws the ring in the fire'
else:
    message = message + 'There are only 4 books in the LotR series the Amazon show dosn\'t count.'
print(message)

