"""
Given a comma-separated string astring with sorted integers without duplicates, write a Python function summary_ranges(astring) that returns a string showing the contiguous intervals in the set.

"""

def summary_ranges(astring):
    s = astring.split(",")
    i = 0
    output = []
    while i < len(s):
        start = int(s[i])
        stop = start
        empty = True
        while i < len(s) - 1 and int(s[i]) + 1 == int(s[i + 1]):
            stop += 1
            empty = False
            i += 1
        if empty == True:
            output += [s[i],]
        else:
            output += ["{0}->{1}".format(start, stop),]
        i += 1
    return ",".join(output)