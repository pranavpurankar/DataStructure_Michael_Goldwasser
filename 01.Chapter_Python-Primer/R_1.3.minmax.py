#!/usr/bin/env python3
'''
Write a short Python function, minmax(data), that takes a sequence of one or
more numbers, and returns the smallest and largest numbers, in the form of a
tuple of length two. Do not use the built-in functions min and max in
implementing your soulutions
'''

tuple_minmax = (45, 6, 56, 90, 3)


def minmax(data):
    sorted_tuple = sorted(data)
    min_value = sorted_tuple[0]
    max_value = sorted_tuple[-1]
    minmax_tuple = (min_value, max_value)
    return minmax_tuple


min_max = minmax(tuple_minmax)
print(min_max)
