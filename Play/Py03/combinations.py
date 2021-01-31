"""
Write a Python function C that receives the number of objects to choose from n, the number of objects selected r and produces all combinations possible.
Round the result to the floor, for example the floor of 8.4 is 8 and the floor of 5.7 is 5. 

You cannot use the math package.

"""

n = 0
r = 0
def fact(x):
    value = 1
    for num in range(2, x + 1):
        value *= num
    return value
        
def C(n, r):
    c = (fact(n) / (fact(r) * fact(n - r)))
    return int(c)

print(C(n ,r))