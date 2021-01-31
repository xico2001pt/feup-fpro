"""
The path to the treasure is given as a sequence of commands that are steps of length 1: up, left, right or down. Write a function map(pos, steps) that takes a coordinate pos, which is a tuple with values x and y as (x,y), and a sequence of commands in a string steps, with the steps separated by a hyphen, and computes the final position in the map.

"""

def map(pos, steps):
    (x, y) = pos
    steps = steps.split("-")
    for direction in steps:
        if direction == "up":
            y += 1
        elif direction == "down":
            y -= 1
        elif direction == "left":
            x -= 1
        else:
            x += 1
    return (x, y)