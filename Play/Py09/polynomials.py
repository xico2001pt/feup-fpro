"""
Suppose we have a polynomial represented as a list of coefficients, a[0], a[1], ..., a[n-1], where a[i] is the coefficient of x**i; that is:

Write a function evaluate(a, x) that evaluates the value of the polynomial for a given integer x.

Use map() and lambda functions.

"""

def evaluate(a, x):
    return sum(map(lambda cof: cof*x**a.index(cof), a))