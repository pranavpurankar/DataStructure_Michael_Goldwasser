#!/usr/bin/env python3

'''
Write a program which takes an input from the user, this will check whether
the python object is iterator or iterable or none of this.
According to the indentified type of the object we can perform the operations.
If it is iterable then iterable related operations, if it is iterator then
iterator related operations.
'''

object1 = eval(input("Enter object"))
object_dir = dir(object1)

if '__iter__' in object_dir and '__next__' in object_dir:
    print(f'This {object1} is:- Iterator')

elif '__iter__' in object_dir:
    print(f'This {object1} is:- Iterable')

else:
    print('Not Supported')
