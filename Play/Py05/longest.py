"""
Write a Python function longest(s) that, given a string s, returns the length of its longest word.

"""

def longest(s):
    largest = 0
    s = s.split()
    for word in s:
        if len(word) > largest:
            largest = len(word)
    return largest