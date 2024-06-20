#!/usr/bin/env python3

'''
• Python uses __repr__ method when there is no __str__ method is defined.
• No __str__ method is defined then the default is used <__main__.Test Obj ..>

Use the f "String method" it is introduced in the python 3.6 and use this
'''


class Test:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f"Test a:{self.a} b:{self.b}"

    def __str__(self):
        return ('From str method of Test: a is {},b is {}'
                .format(self.a, self.b))

# Driver Code
t = Test(1234, 5678)

# This calls __str__()
print(t)

# This calls __repr__()
print([t])


print("\nWhen no __str__ python uses __repr__method")


class Test_1:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f"Test a:{self.a} b:{self.b}"


cer = Test_1(10, 20)
print([cer])
