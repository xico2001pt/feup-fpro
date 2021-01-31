"""
Write a recursive Python function permuta(alist, step=0) that returns the list of permutations. The step controls the order by which the permutations are created.

At each step, each element whose index ≥ step permutates (changes the order) with the element whose index = step.

"""

def permuta(alist, step=0):
    result = []
    if step == len(alist)-1:
        return [alist]
    for n in range(step, len(alist)):
        alist_copy = alist.copy()
        alist_copy[step], alist_copy[n] = alist_copy[n], alist_copy[step]
        result += permuta(alist_copy, step+1)
    return result