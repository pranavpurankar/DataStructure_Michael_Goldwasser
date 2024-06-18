#!/usr/bin/env python3

'''
Creativity C-1.15
Write a Python function that takes a sequence of numbers and determines if all
the numbers are different from each other (that is, they are distinct).
'''


def unique_sequence(sequence):
    distinct_number = set(sequence)
    return distinct_number


unique = [12, 56, 1, 2, 2, 2, 2, 45, 45, 63, 56]
sequence_fun = unique_sequence(unique)
print(sequence_fun)


# Alternate approach

def are_all_distinct(numbers):
    return len(numbers) == len(set(numbers))


print(are_all_distinct([1, 2, 3, 4, 5]))
print(are_all_distinct([1, 2, 3, 3, 4, 5]))
print(are_all_distinct([]))
print(are_all_distinct([1, 1]))

