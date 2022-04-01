#!/usr/bin/env python3

import pprint

def getfile():
    with open("numfile.txt", "r") as numfile:
        numbers = numfile.readlines()
        return numbers

def parsenumders(numbers):
    for number in numbers:
        number = int(number)
        if number % 3 == 0 and number %5 == 0:
            print("FizzBuzz")
        elif number % 5 == 0:
            print("Buzz")
        elif number % 3 == 0:
            print("Fizz")
        else:
            print(number)


numbers = getfile()
parsenumders(numbers)

