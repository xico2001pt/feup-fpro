"""

Write a Python function pascal(n) that, for a given integer n, returns a string with the first n rows of Pascal's triangle. Each row finishes by "\n" (newline) and each value is separated by a single space. The value at the -th row and -th column of the triangle is equal to . Note that i and j start in zero. You may use math.factorial.

    for the number n=3, the result is the string 1\n1 1\n1 2 1
    for the number n=5, the result is the string 1\n1 1\n1 2 1\n1 3 3 1\n1 4 6 4 1


"""

import math

def pascal(n):
    output = ""
    for i in range(n):
        for j in range(i + 1):
            output += str(int(math.factorial(i) / (math.factorial(j) * math.factorial(i - j)))) + " "
        output = output[:-1]
        output += "\n"
    return output