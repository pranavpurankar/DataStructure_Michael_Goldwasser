#!/usr/bin/env python3

'''
Reinforcement 1.5
Give a single command that computes the sum from Exercise R-1.4, relying on
python's comprehension syntax and the built-in sum function
'''

n = 4
sum_of_squares = sum(num**2 for num in range(1, n))
print(sum_of_squares)
