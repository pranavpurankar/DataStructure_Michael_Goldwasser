#!/usr/bin/env python3

'''
How to chain multiple generators?

Ex:
Suppose you have a list of numbers, and you want to filter out even numbers,
square the filtered even numbers and then sum up them.

Approach:
    Suppose this is a list --> [10, 20, 30, 40, ....]
    So we need to store even number --> even_number list [2,4,6,8]
    If there are many numbers in the list then it will consume too much to
    store this list elements.

Generators Approach:
    We will create three different generators:
        1. Filter out even numbers
        2. Square the filtered even number
        3. To add all the square filtered even numbers
'''


def filter_even(seq):
    for num in seq:
        if num % 2 == 0:
            yield num


def find_squares(seq):
    for num in seq:
        yield num * num


def summation(seq):
    total = 0
    for num in seq:
        total += num
    yield total


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
g = summation(find_squares(filter_even(numbers)))
print(type(g))
print(next(g))
