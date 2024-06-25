#!/usr/bin/env python3

'''
Major disadvantage of Eval function is 
'''


def password():
    print('Secret passwor is 1234')


def solve_eq():
    eq = input("Enter the equation in the form of x:")
    x = int(input("Enter the value of x: "))
    ans = eval(eq, {'x': x})
    print("Solution: ", ans)


solve_eq()

# Eval functions has two another parameter that is global and local
# They can be used to solve situations like above

from math import *
print(eval('sqrt(25)'), {'sqrt': sqrt})
