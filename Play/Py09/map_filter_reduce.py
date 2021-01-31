"""
Write a function map_filter_reduce(lst, f1, f2, f3) that receives a list lst and three functions: f1, f2 and f3. The function filters the elements of lst using f1, applies f2 to each element of the result, and finally applies reduce() to convert the list to a scalar by using f3.

"""

import functools
def map_filter_reduce(lst, f1, f2, f3):
    return functools.reduce(f3, map(f2, filter(f1, lst)))