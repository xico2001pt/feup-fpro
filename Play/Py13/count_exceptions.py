"""
Write a function count_exceptions(f, n1, n2) that receives a function f and two integers n1 and n2. Function f accepts an integer and may throw an exception when applied to an invalid integer. The given function is applied to all integers in the range [n1, n2] and returns the amount of exceptions caught.

"""

def count_exceptions(f, n1, n2):
    counter = 0
    for i in range(n1, n2+1):
        try:
            f(i)
        except:
            counter += 1
    return counter