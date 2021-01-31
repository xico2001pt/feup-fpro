"""
Given the solution to go through a labyrinth, we want to minimize the number of steps by removing redundant steps. Going to the left and immediately after going to the right is a waste of energy and time.
Write a Python function min_path(path) which receives a list, path, and returns the path minimized.
The possible directions are: UP, DOWN, RIGHT, LEFT.

"""

def min_path(path):
    opposite = {'UP': 'DOWN', 'LEFT': 'RIGHT', 'DOWN': 'UP', 'RIGHT': 'LEFT'}
    change = True
    while change:
        change = False
        for idx in range(len(path)-1):
            if path[idx] == opposite[path[idx+1]]:
                change = True
                path = path[:idx] + path[idx+2:]
                break
    return path