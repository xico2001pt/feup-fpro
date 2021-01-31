"""
Write a Python function count_chars(astring) that returns a tuple containing the number of characters that are alphabetic, digits and special symbols, in the respective order.

"""

def count_chars(astring):
    alfa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "0123456789"
    (x, y, z) = (0, 0, 0)
    for char in astring:
        if char.upper() in alfa:
            x += 1
        elif char in num:
            y += 1
        else:
            z += 1
    return (x, y, z)