#!/usr/bin/env python3

'''
Write a python function, is_multiple(n,m), that takes two integer values and
return True if n is a multiple of m, that is, n = mi for some integer i, and
False otherwise
'''


def is_multiple(n, m):
    return n % m == 0


print(is_multiple(6, 2))
print(is_multiple(16, 4))
print(is_multiple(15, 2))
print(is_multiple(4, 2))
