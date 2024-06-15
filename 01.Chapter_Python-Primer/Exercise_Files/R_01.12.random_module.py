#!/usr/bin/env python3

'''
=> Reinforcement 1.12

Python's random module includes a function choice(data) that returns a random
element from a non-empty sequence. The random module includes a more basic
function randrange, with parameterization similar to the built-in range
function, that return a random choice from the given range. Using only the
randrange function, implement your version of the choice function

'''
import random

# Test data sequence type list, tuple
demo_list = [36, 96, 63, 56, 12, 86]
demo_tuple = (3, 63, 96, 30, 15, 10)


def custom_choice(data):
    # Calculate the length of the sequence
    length = len(data)

    # Generate a random index using randrange
    random_index = random.randrange(length)

    # Return the element at the random index
    return data[random_index]


print('Non_empty list sequence: ', custom_choice(demo_list))
print('\nNon_empty tuple sequence: ', custom_choice(demo_tuple))
