"""
Write a Python function to_celsius(t) that, given a list t of temperatures in Fahrenheit degrees, uses comprehensions to compute the corresponding Celsius degrees, rounded to 1 decimal.

"""

def to_celsius(t):
    return [round((c-32)/1.8,1) for c in t]