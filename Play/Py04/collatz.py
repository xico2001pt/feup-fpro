"""
Write a Python function collatz(n) that returns a comma-separated string with the Collatz sequence. Starting by the positive integer n, the next term of the Collatz sequence is obtained from the previous by: (i) diving the previous term by 2, if the previous term is even; or (ii) multiplying the previous term by 3 and then summing 1, if the previous term is odd. The sequence ends when it reaches 1.

    for the number n=3, the result is the string 3,10,5,16,8,4,2,1
    for the number n=12, the result is the string 12,6,3,10,5,16,8,4,2,1

"""

def collatz(n):
    output = ""
    while n > 1:
        output += str(n) + ","
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
    output += str(n)
    return output