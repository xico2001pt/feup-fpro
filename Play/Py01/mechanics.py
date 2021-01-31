"""
A king needs your help to defend his castle! He will tell you the angle of his cannon (in degrees) and you will tell him how far (horizontally) the cannon ball will go (until it hits the ground).

The cannon ball fires at the velocity of 18 m/s. Air resistance (drag) is negligible. Assume g=-10m/s². Please round the result.

Some code is already provided for you:

import math
angle = int(input())*math.pi/180  # convert to radians
cos_angle = math.cos(angle)
sin_angle = math.sin(angle)

"""

import math
angle = int(input())*math.pi/180  # convert to radians
cos_angle = math.cos(angle)
sin_angle = math.sin(angle)
v0 = 18
g = -10

# Find how much times the ball is in the air
vy = sin_angle * v0
time = -2 * vy / g

#Find horizontal distance
vx = cos_angle * v0
distance = vx * time

print(int(round(distance)))