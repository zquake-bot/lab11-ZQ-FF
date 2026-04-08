"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def square_root(a):
    if a < 0:
        raise ValueError("A cannot be negative")
    return math.sqrt(a)
def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        return b / a
    except ZeroDivisionError:
        return "cannot divide by zero"
# raise ZeroDivisionError if a == 0

def logarithm(a, b):
    try:
        return math.log(a, b)
    except ValueError:
        return "cannot take log of 0"
    # use math library + raise ValueError

def exp(a, b):
    return a**b



