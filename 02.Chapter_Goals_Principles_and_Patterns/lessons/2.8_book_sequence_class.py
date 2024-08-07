#!/usr/bin/env python3

class Progression:
    '''
    Iterator producing a generic progression
    Default iterator produces the whole numbers 0, 1, 2
    '''

    def __init__(self, start=0):
        # Initialize current to the first value of the progession'''
        self._current = start

    def _advance(self):
        '''
        Update self._current to a new value.

        This should be overriden by a subclass to customize progession
        By convention, if current is set to None, this designates the
        end of a finite progression
        '''
        self._current += 1

    def __next__(self):
        # Return the next element, or else raise StopIteration error
        if self._current is None:   # Our convention to end a progression
            raise StopIteration()
        else:
            answer = self._current  # record current value to return
            self._advance()     # Advance to prepare for next time
            return answer

    def __iter__(self):
        # By convention, an iterator must return itself as an iterator
        return self

    def print_progression(self, n):
        # Print next n values of the progression
        print(' '.join(str(next(self)) for j in range(n)))


class ArithmeticProgression(Progression):
    # Iterator producing an arithmetic progression

    def __init__(self, increment=1, start=0):
        # Create a new arithmetic progression
        # increment -> the fixed constant to add to each term (default 1)
        # start -> the first term of the progression (default 0)
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        # Update current value by ading the fixed increment
        self._current += self._increment


class GeometricProgession(Progression):
    # Iterator producing a geometric progression

    def __init__(self, base=2, start=1):
        # Create a new geometric progrssion
        # base the fixed constant multiplied to each term (default 2)
        # start the first term of the progression (default 1)
        super().__init__(start)
        self._base = base

    def _advance(self):
        # Update current value by multiplying it by the base value
        self._current *= self._base     # Override inherited version


class FibonacciProgression(Progression):
    # Iterator producing a generalized Fibonacci progression

    def __init__(self, first=0, second=1):
        # Create a new fibonacci progression
        # first -> the first term of the progression (default 0)
        # second -> the second term of the progression (default 1)
        super().__init__(first)     # start progression at first
        self._prev = second - first     # fictious value preceeding the 1st

    def _advance(self):
        # Update current value by taking sum of previous two
        self._prev, self._current = self._current, self._prev + self._current
