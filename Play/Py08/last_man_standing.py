# -*- coding: utf-8 -*-
"""
In a circle of people, represented by a list of integers alist, a game will take place. Counting will start at the beginning of the list, and after counting a certain number of people, specified by step, the person where the counting stopped is out of the game.

Write a Python function last_man_standing(alist, step) that returns the last person left on the circle.

Using global variables or cycles is forbidden.
Adapted from: Inspired by the Josephus problem
 
"""

def last_man_standing(alist, step):
    if len(alist) == 1:
        return alist[0]
    current = (step-1)%len(alist)
    alist = alist[current:] + alist[:current]
    alist.remove(alist[0])
    return last_man_standing(alist, step)