"""
Write a recursive Python function sum_digits_rec(n) that returns the sum of the digits of an integer number.

Using global variables or cycles is forbidden.
Adapted from: www.w3resource.com 

"""

def sum_digits_rec(n):
    n = str(n)
    if len(n) == 1:
        return int(n)
    else:
        return int(n[0]) + sum_digits_rec(n[1:])