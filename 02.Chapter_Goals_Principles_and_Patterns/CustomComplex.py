#!/usr/bin/env python3

'''
Let’s reinvent the wheel and implement our own class to represent complex
numbers, CustomComplex. Objects of our class will support a variety of built-
in functions and operators, making them behave very similar to the built-in
complex numbers class:
'''

from math import hypot, atan, sin, cos


class CustomComplex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def conjugate(self):
        return self.__class__(self.real, -self.imag)

    def argz(self):
        return atan(self.imag / self.real)

    def __abs__(self):
        return hypot(self.real, self.imag)

    def __repr__(self):
        return f"{self.__class__.name}({self.real}, {self.imag})"

    def __str__(self):
        return f"({self.real}{self.imag:+}j)"

    def __add__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            real_part = self.real + other
            imag_part = self.imag
        if isinstance(other, CustomComplex):
            real_part = sel.real + other.real
            imag_part = self.imag + other.imag

        return self.__class__(real_part, imag_part)



    # First learn about the complex numbers then accomplish this class from 
    # scratch. I wrote the above code just with help and that is not good
