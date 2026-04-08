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
    if a == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return b / a
# raise ZeroDivisionError if a == 0

def logarithm(a, b):
    if a == 0:
        raise ZeroDivisionError("cannot take log of 0")
    return math.log(a, b)

def exp(a, b):
    return a**b



