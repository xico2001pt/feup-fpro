"""
Define a function greatest_member(atuple) that given a tuple atuple, returns the member of the tuple who has the highest score; for tiebreakers return the member that appears first in the tuple.
The score is calculated by summing the ASCII code of each character for every string the member contains.
A member can be either a string or another tuple. In the second case, the total score of the member is the sum of all scores of each sub-member.
If the initial tuple has no members, return an empty tuple.

"""

def score(string):
    score = 0
    for char in string:
        score += ord(char)
    return score


def greatest_member(atuple):
    highscore = 0
    if atuple == ():
        return ()
    else:
        for member in atuple:
            n_score = 0
            if type(member) == type("jlopes"):
                n_score = score(member)   
            else:
                copy = member
                while copy:
                    deposit = ()
                    for sub in copy:
                        if type(sub) == type("jlopes"):
                            n_score += score(sub)
                        else:
                            deposit += sub
                    copy = deposit
            if n_score > highscore:
                highscore = n_score
                result = member
    return result