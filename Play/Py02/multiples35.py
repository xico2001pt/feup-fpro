"""
Define a function sum_multiples(n) that returns the sum of all the natural numbers that are a multiple of 3 or 5 up until n (inclusive).

def sum_multiples(n):
    # my code here
    return # FIXME

The sum of all natural numbers up to n can be calculated using the formula:
n*(n+1)/2

For example, the sum of all numbers up to 5 is 1+2+3+4+5=15, or using the formula:
5*(5+1)/2

"""

def sum_multiples(n):
    sum_n = 0
    for num in range(1, n + 1):
        if num % 3 == 0 or num % 5 == 0:
            sum_n += num
    return sum_n