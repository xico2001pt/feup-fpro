"""
Write a Python function called bubble_sort(alist) that receives a list alist and returns its sorted version.

The way this algorithm works is by comparing each element against its neighbor and swapping if the second is bigger than the first.

Save a flag indicating whether any swap was made. Keep doing the cycle until any swap is done.

"""

def bubble_sort(alist):
    flag = True
    while flag:
        flag = False
        for idx in range(len(alist)-1):
            if alist[idx]>alist[idx+1]:
                alist[idx], alist[idx+1] = alist[idx+1], alist[idx]
                flag = True
    return alist