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

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        b / a
    except ZeroDivisionError:
        "cannot divide by zero"
# raise ZeroDivisionError if a == 0

def log(a, b):
    try:
        math.log(a, b)
    except ValueError:
        "cannot take log of 0"
    # use math library + raise ValueError

def exp(a, b):
    return a**b



