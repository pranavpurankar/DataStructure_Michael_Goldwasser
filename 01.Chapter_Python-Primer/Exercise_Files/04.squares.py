#!/usr/bin/env python3

'''
# Reinforcement R-1.4
Write a short python function that takes a positive integer n and return the
sum of the squares of all the positive integers smaller than n
'''
# Below code is without looking for solution


def square_sum(n):
    squares_sum = []
    for num in range(1, n):
        square_num = num * num
        squares_sum.append(square_num)
    return sum(squares_sum)


print(square_sum(4))


# Actual solution without looping
def sum_of_squares(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    return n * (n - 1) * (2 * n - 1) // 6


print(sum_of_squares(4))


'''

# Problem Explanation:

Imagine you have a bag of marbles. The bag can hold up to n marbles, but right
now, it only has n-1 marbles in it (not the full n). This function wants to 
find the total bouncyness of all the marbles in the bag. But here's the catch:
instead of just counting the number of marbles, we want to consider how bouncy
each marble is by squaring its number (number of marbles x number of marbles).
A single marble is less bouncy than four marbles, right?

For example, if the bag can hold up to 4 marbles (n = 4), the function would 
consider 3 marbles (n-1). It would square the number of marbles each 
(1^2, 2^2, 3^2) to represent their bounciness and add those values together.
The function would then return that final sum, which represents the total 
bounciness of all the marbles in the bag.

The function works by looping through each marble (from 1 to n-1), squaring 
its number to find its bounciness, and keeping a running total of all these
bounciness values.

'''
