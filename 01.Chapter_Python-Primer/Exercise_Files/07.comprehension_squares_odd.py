#!/usr/bin/env python3

'''
Write a single command that computes the sum from Exercise R_1.6, relying on
Python's comprehension syntax and built-in sum function
'''


def square_of_odd(n):
    if n <= 0:
        raise ValueError("n should be a positive integer")
    square_sum = sum([num**2 for num in range(1, n, 2)])
    return square_sum


print(square_of_odd(6))
