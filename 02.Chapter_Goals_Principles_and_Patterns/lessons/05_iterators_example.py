#!/usr/bin/env python3

'''
Lets make our own for loop. Without using the built in for loop.
'''


L = [10, 20, 30, 40]


def mera_for_loop(iterable):
    # first step create a iterator, for loop also create it first
    iterator = iter(iterable)
    try:
        while True:
            print(next(iterator))
    except StopIteration:
        pass


mera_for_loop(L)
