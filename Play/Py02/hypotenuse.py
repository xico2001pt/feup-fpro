"""
Write a Python script that given the length n, by user input, which corresponds to two sides of a right-angled triangle, prints the length of the hypotenuse. Please use round with two decimal places.

"""

from math import sqrt

n = int(input())
print(round(sqrt(2 * n ** 2), 2))