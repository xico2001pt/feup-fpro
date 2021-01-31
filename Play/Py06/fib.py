"""
Write a Python function fib(n) that returns a list of the first n Fibonacci numbers. The next number in a Fibonacci sequence is defined as the sum of the previous two numbers, and the first two numbers are defined as 0 and 1, respectively.

    fib(1) should return the list: [0]
    fib(5) should return the list: [0, 1, 1, 2, 3]

"""

def fib_num(x):
    if x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        return fib_num(x-2) + fib_num(x-1)


def fib(n):
    result = []
    for i in range(1, n+1):
        result += [fib_num(i)]
    return result