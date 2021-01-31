"""
Write a Python script that given two integers a and b, prints the value of their sum. However, if the difference of a and b is an even number, the value of the sum is doubled, on the other hand, if the difference is an odd number, the value of the product of a and b gets added to the value of the sum.

"""

a = int(input())
b = int(input())
is_even = (a - b)%2 == 0
print((a + b) +  is_even * (a + b) + (not is_even) * (a * b))