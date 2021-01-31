"""
Define a function biggest_member(atuple) that given a tuple atuple, returns the member of the tuple or any sub-tuple which is the biggest (in length). You should not care about ties.

"""

def biggest_member(atuple):
    biggest = ()
    for member in atuple:
        if type(member).__name__ == 'tuple':
            member = biggest_member(member)
        else:
            member = atuple
        if len(member) > len(biggest):
            biggest = member
    return biggest