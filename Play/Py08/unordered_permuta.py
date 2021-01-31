"""
Write a recursive Python function permutations(atuple) that returns a set of permutations of the tuple atuple. Notice that since the result is a set, then order does not matter.

A suggestion is to use induction. Start by doing a function that works for len(atuple) == 1, then for len(atuple) == 2, then for len(atuple) == 3. It should then become clear how you can do a permutation by breaking it down into smaller subproblems that can be solved with recursion.

You cannot use itertools.

"""

def permutations(atuple):
    if len(atuple) == 1:
        return {atuple}
    else:
        result = set()
        for i in range(len(atuple)):
            for s in permutations(atuple[:i] + atuple[i+1:]):
                new = (atuple[i],) + s
                result |= {new}
    return result