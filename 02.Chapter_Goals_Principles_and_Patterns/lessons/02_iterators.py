#!/usr/bin/env python3

'''
Types of iterators:
    - Built-in Iterators (runs internally)
        Ex: Iterator of range()

    - Custome Iterators ()
'''

# How to create custom iterators? Create own range() function

# Ex: Power of two sequence
# user entered 16 -> 1 2 4 8 16 ; 64 -> 1 2 4 8 16 32 64
# We don't have sequence, so we cannot use the iter function directly for
# creating iter object. First we create a class, iterator class, us class 
# ka object hoga iterator object, us object ka use karake hum sequence
# generate karenge by calling next function.


class PowerOfTwo:
    def __init__(self, max_value):
        self.limit = max_value
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            result = self.current
            self.current = self.current*2
            return result
        else:
            raise StopIteration


n = int(input("Enter the limi"))
iter_obj = PowerOfTwo(n)

# Initially we are getting 1 only before incrementing it.
# print(next(iter_obj))  #
# You can use for loop also
for ele in iter_obj:
    print(ele)

# --------------------------------------------------------------------------
print("\n", "-"*70, "\n")

# Let's create our own range function
# The built-in range function in the python is the iterable not a iterator
# When we run a for loop on range function, python iternally generate an
# iterator by using iter function. An this iter function is a python object
# of some class. It means here is there are two classes


class my_range:
    def __init__(self, start=0, stop=None, step=1):
        if stop is None:
            raise TypeError("range expected at least 1 argument, got 0")
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return my_range_iterator(self)


class my_range_iterator:
    def __init__(self, iterable_obj):
        self.iterable_obj = iterable_obj

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterable_obj.start < self.iterable_obj.stop:
            result = self.iterable_obj.start
            self.iterable_obj.start = \
                    self.iterable_obj.start + self.iterable_obj.step
            return result
        else:
            raise StopIteration


# a = my_range()
# iter_obj = iter(a)
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))

# You can use our custom range function
for ele in my_range(2, 20, 3):
    print(ele)

print()

for ele in range(2, 20, 3):
    print(ele)
