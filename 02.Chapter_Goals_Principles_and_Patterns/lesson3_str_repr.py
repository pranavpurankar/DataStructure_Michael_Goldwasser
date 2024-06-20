#!/usr/bin/env python3
import pdb
pdb.set_trace()

'''
__repr__: Official string representation of an object, aiming for clarity and 
unambiguousness.

__str__: Informal or nicely printable string representation of an object for 
end users.

Seeing the actual use of __repr__ while debugging the python code. An actual 
use case using python pdb
'''


class Employee:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"My name is {self.name} and age is {self.age}"

    def __repr__(self) -> str:
        return "This is from the repr method"


emp = Employee('Pranav', 28)
print(emp)
