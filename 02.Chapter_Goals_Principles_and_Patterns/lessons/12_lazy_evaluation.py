#!/usr/bin/env python3

'''
Ref: realpython.com/python-lazy-evaluation

# What's is lazy evaluation?
->  Python lazy evaluation is when Python takes the lazy option and delays
    working out the value returned by an expression until that value is
    needed.

# Types if evaluation of expressions into two types:
    1. Eager evaluation
    2. Lazy evaluation

    1.Eager Evaluation:

    refers to cases when Python evaluates an expression as soon as it encount-
    ers it. Here are some examples of expression that are evaluated eagerly:
    >> 5 + 10
    >> import random
    >> random.randint(1, 10)
    >> numbers = [2, 4, 6, 8, 10]
    >> numbers

    Here the last defined list numbers, will acquired some memory. This is a
    small list, but if the elements or list is bigger it will acquire more
    memory.  This memory won't be freed as long as this list exists in your
    program.

    2. Lazy evaluation:

    refers to cases when Python dosen't work out the values of an expression
    immediately. Instead, the values are returned at the point when they're
    required in the program. Lazy evaluation can also be referred to as call-
    by-need.

    When large datasets are created using lazily-evaluated expressions, the
    program dosen't need to use memory to store the data structure's contents.
    The values are only generated when they're needed.

    Ex: Lazy evaluation occurs within the for loop when you iterate using
    range():
        for index in range(1, 100000001):
            print(f"This is interation {index}")

    Lazy evaluation also allows you to create infinite data structures, such
    as a live stream of audio or video data that continuously updates with new
    information, since the program dosen't need to store all the values in
    memory at the same time. Infinite data stucture are not possible with the
    eager evaluation since they can't be store in memory.

# Iterators in itertools
->  Iterators are lazy data structures since their values are evaluated when
    they're needed and not immediately when you define the iterator. There are
    many more iterator in Python besides enumerate and zip. Every iterable is
    either an iterator itself or can be converted into an iterator using
    __iter__()

'''


