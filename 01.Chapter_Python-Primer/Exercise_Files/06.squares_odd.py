#!/usr/bin/env python3

'''
Reinforcement 1.6
Write a short Python function that takes a positive integer n and return the
sum of the squares of all the odd positive integers smaller than n.
'''


def square_sum_odd(n):
    if n <= 0:
        raise ValueError("n should be positive integer")
    sum_of_squares = 0
    for num in range(1, n, 2):
        sum_of_squares = sum_of_squares + (num * num)
    return sum_of_squares


print(square_sum_odd(6))


# Another approach is using list comprehension, it is more efficient and avoid
# unnecessary conditionals as well as calculations

def square_odd(n):
    if n <= 0:
        raise ValueError("n should be positive integer")

    square_num = [num**2 for num in range(1, n, 2)]
    return sum(square_num)


print(square_odd(6))
