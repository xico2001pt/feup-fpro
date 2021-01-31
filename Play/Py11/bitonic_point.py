"""
Given a list, that is partially ascending and partially descending, the bitonic point is the point before which the list is ascending and after which the list is descending. For example in the list alist=[2, 6, 10, 25, 60, 30, 25, 10, 0], the point 60 is the bitonic point.

Write a Python function bitonic_point(f) that receives a function f that when called produces a list of integers which is sorted in bitonic way. Take advantage of the way the list is sorted to reduce complexity time from O(n) to O(log n).
Adapted from: Geeks for Geeks 

"""

def bitonic_point(f):
    alist = f()
    while True:
        comp = len(alist)
        if comp == 1:
            return alist[0]
        if comp == 2:
            return max(alist)
        mid = comp//2
        if alist[mid]>alist[mid+1]:
            alist = alist[:mid+1]
        else:
            alist = alist[mid:]