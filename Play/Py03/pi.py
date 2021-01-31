"""
Write a Python program that computes and prints the number pi by using the Ramanujan formula.

You can use the math package for the factorial and square root (only!). The number K controls the precision of the formula. Use K=50. Round the result to 8 decimal places.
Adapted from: Universidade Aberta

"""

import math

K = 50

def sumatorio(k):
    result = 0
    for i in range(0, k + 1):
        result += math.factorial(4 * i) * (1103 + 26390 * i) / (math.factorial(i) ** 4 * 396 ** (4 * i))
    return result

pi = (2 * math.sqrt(2) * sumatorio(K) / 9801) ** (-1)
print(round(pi, 8))