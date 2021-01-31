# -*- coding: utf-8 -*-
"""
Write a Python function bagdiff(xs, ys) that returns items from the first list (xs) that are not eliminated by a matching element in the second list (ys). An item in the second list may "knock out" just one matching item in the first list.

"""

def bagdiff(xs, ys):
    result = []
    for i in range(len(xs)):
        if xs[i] not in ys:
            result += [xs[i]]
        else:
            ys.remove(xs[i])
    return result