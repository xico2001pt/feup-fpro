"""
Write a Python function to_fahrenheit(t) that, given a list t of temperatures in Celsius degrees, uses map() with a lambda function to compute the corresponding Fahrenheit degrees, rounded to 2 decimals.

"""

def to_fahrenheit(t):
    return list(map(lambda c: round(c*1.8+32, 2), t))