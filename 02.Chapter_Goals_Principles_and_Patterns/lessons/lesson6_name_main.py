#!/usr/bin/env python3

'''
The essence of this idiom __name__ =__main__ is how your code will be executed
when it is run as script versus when you import it as a module into another
python file
'''
import os
import sys

curr_dir = os.getcwd()
sys.path.append(curr_dir)
print(curr_dir)

for index, path in enumerate(sys.path):
    print(f'{index}Current: {path}')


def greet(name):
    print(f"Hello, {name}!")


if __name__ == '__main__':
    name = input("Enter your name: ")
    greet(name)
