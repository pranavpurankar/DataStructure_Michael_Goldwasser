#!/usr/bin/env python3

'''
========================= Cognitive Programmer ====================

# Abstract Base Classes (ABC)

The idea of ABC is not new in the any object oriented programming language. It
is present in the C++, Java and Python also.

Before understanding this State Machine is important

• State Machines:
Any software/code/function/process which doesn't terminates immediately after
doing it's work is a State Machine.

Ex:- If you're writing a blank main() function; it is waiting for the user inp

If your software is running for longer time if it dosen't terminates as soon
as it finishes it's job; it is state machine. Whether we have created this
state machine implicity or explicitly.

Ex:- We're in the happy state, due to loss of money migrated to sad state.

• So what's the deal with states and events

- In the code, we want to easily indentify States and Events (Ideally they 
  must be similiar)

- It must be easy for programmer to expand the States and Events.

- Events are something which are signal tranformation from one state to 
  another state. For ex I moved from happy to sad event is lost money.

- Focus more on what to do
=========================== Telusko ========================
# Best explanation of Abstract Classes in programming by Gemini AI

Imagine you're writing instructions for making different shapes. A regular
class might be a blueprint for a specific shape, like a square. It would tell
you exactly how to draw the four sides.

An Abstract class is more like a general guide for shapes. It might say things
like "draw a closed figure" but wouldn't tell you exactly how many sides or
what angles. It can also have specific instructions for things all shapes
share, like having a color.

# From proper technical ground definition would be like below by Gemini:
    In object Oriented programming, an abstract class is a blueprint that
    cannot be used to create objects directly. It acts as a base class for
    other clasess(subclass) to inherit from.

====> Coming back to telusko -> The method which only has a declaration not a
definition, is known as a abstract method. And the class which will have an
abstract method is known as abstract class, it is kind of template.

You've to import ABC module, by default python does not abstract class
'''
from abc import ABC, abstractmethod


class Computer(ABC):

    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):

    def process(self):
        print("Process is running")


class Whiteboard:
    def write(self):
        print("It's writing")


class Programmer:

    def work(self, com):
        print("Building Products")
        com.process()


# com = Computer()
com1 = Laptop()
com1.process()
com2 = Whiteboard()
