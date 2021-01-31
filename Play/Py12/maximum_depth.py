"""
Write a function maximum_depth(l) that receives a list l, which can contain other lists, and returns what is the maximum depth in that list.

The depth corresponds to the number of sub-lists: [] has depth=1, [[]] has depth=2, [[[]]] has depth=3.

"""

def maximum_depth(l):
    if l == []:
        return 1
    max_l = 0
    for elem in l:
        depth = maximum_depth(elem)+1
        if depth>max_l:
            max_l = depth
    return max_l