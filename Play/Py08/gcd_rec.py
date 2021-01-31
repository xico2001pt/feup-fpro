# -*- coding: utf-8 -*-
"""
Write a recursive Python function gcd_rec(n1, n2) to find the greatest common divisor (gcd) of two integers n1 and n2.

Using global variables or cycles is forbidden.
Adapted from: www.w3resource.com 

"""

def gcd_rec(n1, n2):
    if n2 == 0:
        return n1
    return gcd_rec(n2, n1 % n2)