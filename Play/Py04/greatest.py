"""
Write a Python function greatest(num) that, given a non-negative integer num, computes the greatest number that can be made using all digits of num.

"""

def greatest(num):
    numbers = list(str(num))
    numbers.sort(reverse=True)
    numbers = int("".join(numbers))
    return numbers