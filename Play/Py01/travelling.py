"""
Write a Python program to help the user arrive in Lisbon at time. Ask the user in how many hours and how many minutes she can spend travelling at most. Return the average velocity (in km/h) that she will need to drive to arrive in time. Assume the distance between Porto and Lisbon is 313 km.
Please round the result.

"""

d = 313
h = int(input())
m = int(input())
t = h + m / 60
print(int(round(d / t)))

