"""
Write a Python function no_consecutives1(k) that, given an integer k, determines the number of binary numbers of length k that do not have consecutive 1s in them.

For example, if k=3, then the following binaries exist: 000, 001, 010, 011, 100, 101, 110, 111. Of these, only 5 do not have a contiguous 1.

Using global variables or cycles is forbidden.
Adapted from: www.geeksforgeeks.org 

"""

def no_consecutives1(k):
    if k == 1:
        return 2
    elif k == 2:
        return 3
    else:
        return no_consecutives1(k-1) + no_consecutives1(k-2)