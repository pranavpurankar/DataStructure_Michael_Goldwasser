#!/usr/bin/env python3

'''
• Difference :- iterator, iterable, iteration
• What is iterator in python?
• Everything about iterators
• Our own for loop
• Why & When to use iterators? (they are memory efficient)

what is Iterator, Iterable and Iteration? Let's understand it by example
==>
Suppose there is a rack containing 5 different fruits
container => ['apple', 'banana', 'mango', 'orange', 'strawberry']
Suppose a kid is eating each fruit one by one using his hand. So he will first
eat apple, then banana and goes till last fruit that is strawberry.

Iteration -> It is the process of visiting every element in the container and
performing some operation, this complete process is known as iteration.
(container means collection of items, in our case this is list of fruits)

Iterable -> The process of iteration is performed on the container; this list
or container is known as iterable. In our ex. list of fruits

Iterator -> The pointer which visits each element in the list is known as the
iterator. In our ex. kids hand is iterator, it is visiting each fruit in the
iterable.

CodeYug Definitions:
    > iteration :- process of taking each item of something one after another
    (something means collection of multiple items)
    ex:- Whenever you use a loop for visiting every item of sequence (list,
    tuple, dictionary, string)

    > iterator :- An iterator is an object that allows programmer to traverse
    through a sequence of data without storing the data in the memory.

    > iterable :- On which the iteration is performed, this is container of
    multiple items. (Jisake upar iteration hota hai) we can also call it
    collection.
'''

# Suppose there is a rack containing 5 different fruits.
data = ['apple', 'banana', 'mango', 'orange', 'strawberry']

iter_obj = iter(data)
print(iter_obj)
print(type(iter_obj))

print(next(iter_obj))
print(next(iter_obj), '\n')

for ele in iter_obj:
    print(ele)

print('''\n\nHow to check weather an object is iterable or not?

        1. You can run a for loop. Successful run shows obj is iterable
        But in the above example we have used for loop on the iter_obj
        It means iter_obj is also an iterator.

        *Note:-Every iterator is iterable. You can run lopp on every iterator
        But note that our list 'Data' is iterable, not iterator why? Lets see
        Basically you can check with magic method if an object only conatains
        __iter__ it means it is iterable only.

        If the an object contain magic method __iter__ & __next__ then it is
        Iterator and Iterable.

        Use print(dir(obj_name)) to check the magic methods associated with
        the objects\n''')

print("dir of data :", dir(data))
print("\ndir of iter: ", dir(iter_obj))
# Instead of using the iter(list), below dunder method is used, an actual one
# that is also used in the internal implemenatation. It is present in list
new_iter_obj = data.__iter__()
print('\nobj.__iter__():- ', type(new_iter_obj))


# Instead of using the next() we can use the iter_obj.__next__(). Which is
# present inside the __iter__ class
print('\n__next__():', new_iter_obj.__next__())     # apple
print('next(): ', next(new_iter_obj))   # banana

print('''\nOne doubt
        We pass the iterable to the iter, after this we get the iterator obj.
        By using iterator, we can fetch an each element.

        We know that iterator is also iterable, inside this there is __iter__
        magic method. Can I make an iterator of the iter_obj. Yes but there is
        no need to do this. It won't create new iterator object, rather it'll
        point to the same memory address.

        iter_obj = iter(L) --> Will create a iter_obj
        iter(iter_obj) --> creating iter obj from iter obj

        When you create an iterator of iterator. It returns itself.
        ''')

L = [10, 20, 30, 40]
iter_obj_0 = iter(L)
iter_obj_1 = iter(iter_obj_0)
print('Type iter_obj_0:', type(iter_obj_0))
print('Type iter_obj_1: ', type(iter_obj_1))
print('Addr iter_obj_0: ', id(iter_obj_0))
print('Addr iter_obj_1: ', id(iter_obj_1))

# fetch the next element
print(next(iter_obj_0))
print(next(iter_obj_0))
