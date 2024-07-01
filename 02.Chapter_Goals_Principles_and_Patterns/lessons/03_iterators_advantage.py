#!/usr/bin/env python3

'''
What is the biggest advantage of iterator?
> It save memory

> In our example the first approach is that is using for loop will consume
more memory. In contrast the second approach which is using range will consume
less memory. Because it uses iter and next method internally. The iter method
iternally uses the technique called lazy evaluation.

• What is lazy evaluation?
Is is a technique where the evaluation of an expression is delayed until its
value is actually needed. This means that the expression is not evaluated 
immediately when it is assigned or defined, but rather when it is accessed or
used somewhere else in the code.

• Codeyug:-

1--> First value is 1, memory will be allocated to this. 
2--> Then the square of 1 is calculated.
3--> Print the calculated result
4--> Vanish the value and bring next value (on the same location, mem location
    can be different)
5--> same process will be followed till the last element

So that is why the memory utilisation will be limited to only single operation
this is quite useful when we have large number or data.

CodeYug Lazy evaluation definition:
    Iterators allo for lazy evaluation of elements, which means elements are
    generated on-the-fly as they are requested, saving memory and improving
    performance when dealing with large datasets.

Example:
    Suppose you've lot of images and their total size is 20 gb. My sys RAM is
    only 8GB; so if I perform this operation on this system then it will raise
    an error called MemoryError.

    In that scenario lazy evaluation is quite useful. We don't need to store
    every element.
'''

import sys

# Suppose I want to find square of first 10 numbers
# 1st Approach For loop:-
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for ele in L:
    print(ele**2)
print("Size of L: ", sys.getsizeof(L))

# 2nd Approach by using range:-
a = range(16)
for ele in a:
    print(ele**2)
print('size Of a:', sys.getsizeof(a))

