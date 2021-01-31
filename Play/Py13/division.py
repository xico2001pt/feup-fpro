"""
Write a Python function division(a, b) that, given two integers a and b, computes the divisions a/b and returns the string "<a>/<b> = <a/b>". When b is zero, the function catches the exception and returns the string "can't divide by 0!" and an argument is not a number it returns the string "unsupported operand type(s) for division".

"""

def division(a, b):
    try:
        return "{0}/{1} = {2}".format(a, b, a/b)
    except ZeroDivisionError:
        return "can't divide by 0!"
    except TypeError:
        return 'unsupported operand type(s) for division'
        return "{0}/{1} = {2}".format(a, b, div)