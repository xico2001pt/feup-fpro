"""
The path to the treasure is given as a sequence of commands that are steps of length 1: up, left, right or down. Write a function map(pos, steps) that takes a coordinate pos, which is a tuple with values x and y as (x,y), and a sequence of commands in a string steps, with the steps separated by a hyphen, and computes the final position in the map.

"""

def map(pos, steps):
    if len(steps) == 1:
        (x, y) = pos
        if steps[0] == "up":
            y += 1
        elif steps[0] == "down":
            y += -1
        elif steps[0] == "right":
            x += 1
        else:
            x += -1
        return (x, y)
    else:
        (z, t) = map(pos, steps[1:])
        if steps[0] == "up":
            t += 1
        elif steps[0] == "down":
            t += -1
        elif steps[0] == "right":
            z += 1
        else:
            z += -1
        return (z, t)