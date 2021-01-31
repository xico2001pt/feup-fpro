# -*- coding: utf-8 -*-
"""
Write a Python function sort_by_value(dict) that, given a dictionary dict of colors (key is the color name and value is its hexadecimal value), returns a list of pairs ordered by the hexadecimal value. Note that it is not possible to sort a dictionary, only to get a representation of a dictionary that is sorted.

For example:

    sort_by_value({"Magenta":"#FF00FF", "Red": "#FF0000", "White":"#FFFFFF"}) returns the list: [("Magenta", "#FF00FF"), ("Red", "#FF0000"), ("White", "#FFFFFF")]

"""

def sort_by_value(dict):
    def order(tup):
        return tup[1]
    return sorted(list(dict.items()), key=order)