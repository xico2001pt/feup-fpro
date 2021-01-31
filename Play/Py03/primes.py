"""
Write a Python program that outputs all the prime numbers within a closed interval of numbers between lower and upper, given by user input.

For example:

    for lower=2 and upper=23 the output is: Prime numbers between 2 and 23 are: 2 3 5 7 11 13 17 19 23
    for lower=5 and upper=27 the output is: Prime numbers between 5 and 27 are: 5 7 11 13 17 19 23
    for lower=-2 and upper=5 the output is: Prime numbers between -2 and 5 are: 2 3 5

"""

lower = int(input())
upper = int(input())
output = "Prime numbers between " + str(lower) + " and " + str(upper) + " are: "
def is_prime(n):
    value = True
    if n == 2:
        pass
    else:
        for i in range(2, n):
            if n % i == 0:
                value = False
    return value
if upper < 2:
    pass
elif lower < 2:
    for n in range(2, upper + 1):
        if is_prime(n) is True:
            output += str(n) + " "  
else:
    for n in range(lower, upper + 1):
        if is_prime(n) is True:
            output += str(n) + " " 
print(output)