#!/usr/bin/env python3

'''
Short hand way to create generators

Write a python program for finding squares of first n numbers

- This problem can be solved by multiple ways
    1. Normal way (For loop with range)
    2. Recursion technique
    3. List comprehension --> same as 1 just shorthand way of list
    4. Generator tech --> for bigger inputs
'''
# import sys

# Using list comprehensions when You used the () brackets it will create a
# generator and this is the shorthand way of creating it.

n = 100
L = (i*i for i in range(1, n))

# print(L)
# print(sys.getsizeof(L))
# print(type(L))


# Write a python program for fibonacci series using generators
# The first two terms would be 0 1 so this are the first two terms.

def fib():
    first, second = 0, 1
    while True:
        yield first
        first, second = second, first + second


g = fib()

for i in g:
    if i >= 100:
        break
    print(i)
