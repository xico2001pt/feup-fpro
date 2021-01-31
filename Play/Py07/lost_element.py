"""
Write a Python function lost_element(s1, s2) that, given two sets of integers s1 and s2 which are duplicates of each other except one element (that is one element from one of the sets is missing) returns that missing element.

    lost_elements([{1, 4, 5, 7, 9}, {4, 5, 7, 9}) returns 1 (1 is missing from the second array)
    lost_elements({2, 3, 4, 5}, {2, 3, 4, 5, 6}) returns 6 (6 is missing from first array)

"""

def lost_element(s1, s2):
    return ((s1 | s2) - (s1 & s2)).pop()