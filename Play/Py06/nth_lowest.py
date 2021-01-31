"""
Write a Python function nth_lowest(lnum, n) that, given a list of numbers lnum and a positive integer n, returns the n-th lowest value in the list. Assume n always holds a valid value (i.e. does not include a number less or equal to one) and that the list never has repeated values.

    for the list lnum=[42, 234, 135, 21, 232, 12312, -2343] and n=2, the result is the number 21
    for the list lnum=[73,100,23,18,84,61,56,75,92,38,54,73,3,13] and n=12, the result is the number 84

"""

def nth_lowest(lnum, n):
    return sorted(lnum)[n-1]