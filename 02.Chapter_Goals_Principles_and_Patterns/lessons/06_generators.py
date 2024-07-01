#!/usr/bin/env python3

'''
Generators in Python are like special functions that can generate a sequence
of values one at a timem instead of giving you all the values at once. Imagine
you have a machine that produces one item of sequence whenever you ask for it.

Whe you create a generator using a special kind of function (you use 'yield')
it dosen't compute all the values and store them in a memory right away.
Instead, it waits until you ask for the next value. This makes generators
really efficient when working with large amounts of data or when you only need
to look at one at a time.

Yield and Return difference interview question
  - The return statement is used to immediately exit a function and return a
    value to the caller.

  - The yield statement is used in a generator function to produce a value to
    the caller, but it dosen't immediately terminate the function's execution
    Instead, it temporarily suspends the functions and saves it's state

  - A function with yield is a generator function, while a function with
    return is a regular function.

  - When a generator function is called, it dosen't execute immediately.
    Instead, it returns a generator object which can be iterated over.

  - Generators are used to create iterators, which allow you to iterate over
    values one by one without loading the entire sequence into memory

  - Generator function maintain their state between calls, allowing them to
    resume execution and produce more values over multiple calls

'''
# import time


def countdown(num):
    print("Countdown starting....")
    while num > 0:
        yield num
        num = num - 1


g = countdown(5)
for i in g:
    print(i)
