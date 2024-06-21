#!/usr/bin/env python3

'''
> Operator overloading

# Adds the two number
1 + 2 = 3

# concatenates the two strings
'Real' + 'Python' = RealPython

# Gives the product
3 * 2 = 6

# Repeats the string
'Python' * 3 = 'PythonPythonPython'

You might have wondered how the same built-in operator or function shows
different behaviour for objects of different classes. This is called operator
overloading or function overloading respectively.

> The python data mode
We have a class representing an online order having a cart a list) and a 
customer (a str or instance of another class which represents a customer). In 
short there are special methods and way to manage your data this is know as
data model.


> Cart functionalities (Code is written for this ex):-
1) get the length of the cart
2) append something to cart

'''


class Order_1:
    def __init__(self, cart, customer):
        self.cart = list(cart)
        self.customer = customer

    def __len__(self):
        return len(self.cart)

    def __str__(self):
        return f"Cart Len{self.cart} and customer {self.customer}"

    def __bool__(self):
        return len(self.cart) > 0


order_1 = Order_1(['Apple', 'Cherry', 'Mango'], 'Pranav Purankar')
print(len(order_1))
print(order_1)
print('Checking Truthy & Falsy: ', bool(order_1))


# Vector class, abs() can be used to get the length of the vector.

class Vector:
    def __init__(self, x_comp, y_comp):
        self.x_comp = x_comp
        self.y_comp = y_comp

    def __abs__(self):
        return (self.x_comp ** 2 + self.y_comp ** 2) ** 0.5

    def __str__(self):
        return f"Vector is {self.x_comp}, {self.y_comp}"
    

vector = Vector(3, 4)
print(abs(vector))
print(vector)


# Functionality of the add Simple and very useful

class Order:
    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer

    def __add__(self, new_item):
        new_cart = self.cart.copy()
        new_cart.append(new_item)
        return Order(new_cart, self.customer)

    def __str__(self):
        return f"Items in cart {self.cart} and Customer {self.customer}"


customer = Order(['Apples', 'Mango', 'Bananas'], 'Pranav Purankar')
print(customer)
customer += "Origano"
print(customer)
