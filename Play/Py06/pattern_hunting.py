"""
Write a function pattern_hunting(l1, l2, p) that given two equal length lists of strings l1 and l2 and a pattern (string) p, builds a new list with elements from the original lists where the pattern occurs not in that element, but the corresponding (i.e. same index) element in the other list. The resulting list should be ordered alphabetically in descending order.

    for the list l1=['a string', 'two strings', 'not here'], another list l2=['choose me', 'me too', 'but not me'] and the pattern p='string', the result is the list ['me too', 'choose me']
    for the list l1=['not found', 'pattern here', 'skip', 'next... or not?'], another list l2=['pattern here indeed', 'i want to be chosen', 'not my day', 'sneakypatternbutitisthere'] and the pattern p='pattern', the result is the list ['not found', 'next... or not?', 'i want to be chosen']

"""

def pattern_hunting(l1, l2, p):
    result = []
    for i in range(len(l1)):
        if p in l1[i]:
            result.append(l2[i])
        elif p in l2[i]:
            result.append(l1[i])
        else:
            pass
    return sorted(result, reverse=True)