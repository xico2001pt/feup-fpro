"""
Suppose we have a polynomial represented as a list of coefficients, a[0], a[1], ..., a[n-1], where a[i] is the coefficient of x**i; that is:

Write a function evaluate(a, x) that evaluates the value of the polynomial for a given integer x.

You should use comprehensions.

"""

def evaluate(a, x):
    return sum([a*x**idx for idx, a in enumerate(a)])