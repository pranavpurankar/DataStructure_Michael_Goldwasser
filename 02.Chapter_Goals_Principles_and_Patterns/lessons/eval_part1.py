#!/usr/bin/env python3

'''
What is eval() in python?

• eval() is a built-in function used in python.

• eval function parses the string argument and evaluates it as a python
  expression.

• string - as a python expression (It only takes string arguments only)

• syntax of eval() :
    eval(expression, globals=None, locals=None)
    - expression :- A string to evaluate
    - globals :- available gloabal methods and variables
    - locals :- available local methods and variables

• Return value of eval()?
    result of expression present in string argument
    num = 3
    var = eval('num*num') -> ('3*3') -> output is 9
    so the type of the return function of the eval function is the actual
    output of that expression In above case the expression returned the value
    of int so the returned value by expression is int.

Where is the eval function mostly used?
• To solve mathematical expression from string
• To take inputs
• If the user want to evaluate the string into code then can use eval function

Warning when using eval()
• Unix system (macOS, Linux etc)
• imported the os module
• command:- eval('em -rf*') -> Will delete everything, OS files also
    In above case you wrote a program on the linux/mac machine and use command
    mentioned above will erase everything. So use it with caution.
'''

num = 3
var = eval('[1,2,3,4]+[5,6,7,8]')
print(type(var))
print(var)

# You can use the eval function while taking an input from the user
input_user = eval(input('List elements: '))
print(type(input_user))
print(input_user)


def password():
    print("Secret password is 1234: ")


def solve_eq():
    eq = input("Enter the equation in the form of x: ")
    x = int(input("Enter the value of x: "))
    ans = eval(eq)
    print("Solution: ", ans)


solve_eq()
