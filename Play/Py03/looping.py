"""
A number is called a Looping Number if all adjacent digits in it differ by 1. The difference between 9 and 0 is considered as 1. All single digit numbers are considered looping numbers.
Write a Python program that receives an integer n, provided by the user, and checks whether the number is a jumping number or not. If the number is a looping number, print the message Looping number, otherwise print the message Not a looping number.
You can assume that all inputs are non-negative numbers.

"""

n_int = int(input())
n_str = str(n_int)
length = int(len(n_str))
count = 0

for i in range(0, length - 1):
    if int(n_str[i]) == (int(n_str[i+1]) + 1) % 10 or int(n_str[i]) == (int(n_str[i+1]) - 1) % 10:
        count += 1

if count == length - 1:
    print("Looping number")
else:
    print("Not a looping number")