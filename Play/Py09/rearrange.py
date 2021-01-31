"""
Write a function rearrange(l) that, given a list of numbers l, rearranges it so that all non-positive numbers appear before the positive ones, but does not alter the numbers’ relative order (i.e., all positive numbers must appear in the same order relative to each other as in the original list; same goes for non-positive numbers).

"""

def rearrange(l):
    return [i for i in l if i<=0] + [i for i in l if i>0]