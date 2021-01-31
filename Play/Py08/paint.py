"""
Write a Python recursive function paint(n, boards) that returns the minimum time necessary to paint the list of boards by n painters. boards is a list of the time necessary to paint each board.

For example, if there are boards=[6, 2, 5, 1, 9], and painter 1 has to paint the first three ([6, 2, 5]) then he will need time=6, and if painter 2 paints the rest ([1, 9]) then he will need time=9 to paint all boards. The time required of each painter to paint the board is the maximum element in that list.

The objective is to find the minimum time required to paint the boards by choosing which boards are painted by which painters. Return the minimum time at the end of the function. Notice that since each painter must paint at least one board, the minimum time can increase when we increase painters.
Adapted from: www.geeksforgeeks.org 

"""

def paint(n, boards):
    great = 99999999999
    if n == 1:
        return max(boards)
    
    for idx in range(1, len(boards)-n+2):
        new = max(boards[:idx]) + paint(n-1, boards[idx:])
        if new < great:
            great = new
    return great