"""
Write a Python function to_fahrenheit(t) that, given a list t of temperatures in Celsius degrees, uses comprehensions to compute the corresponding Fahrenheit degrees, rounded to 2 decimals.

"""

def to_fahrenheit(t):
    return [round(c*1.8+32, 2) for c in t]