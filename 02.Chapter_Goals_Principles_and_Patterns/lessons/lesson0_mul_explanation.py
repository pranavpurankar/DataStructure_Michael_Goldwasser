#!/usr/bin/env python3

class Number:

    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value)
        else:
            return Number(self.value * other)

    def __str__(self):
        return f"Number({self.value})"


num1 = Number(5)
num2 = Number(10)

result1 = num1 * num2
print(result1)

result2 = num1 * 3
print(result2)
