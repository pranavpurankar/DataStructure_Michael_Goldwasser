#!/usr/bin/env python3

'''
Reinforcement 1.11
Demonstrate how to use Python's list comprehension syntax to produce the list
[1, 2, 4, 8, 16, 32, 64, 128, 256]
'''

list_iteration = [2**num for num in range(1, 9)]
print(list_iteration)
