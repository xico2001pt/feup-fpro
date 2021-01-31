"""
In a circle of people, represented by a list of integers alist, a game will take place. Counting will start at the beginning of the list, and after counting a certain number of people, specified by step, the person where the counting stopped is out of the game.

Write a Python function last_man_standing(alist, step) that returns the last person left on the circle.
Adapted from: Inspired by the Josephus problem 
"""

def last_man_standing(alist, step):
    i = (step - 1) % len(alist)
    removed = 0
    while len(alist) > 1:
        alist.remove(alist[i])
        removed = 1
        i = (i + step - removed) % len(alist)
    return type(alist[0])(alist[0])