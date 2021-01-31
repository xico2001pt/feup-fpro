"""
Write a Python function treasure(clues) that receives a dictionary of clues where each key is a location and each value is a clue of what is the next location to go. Start at (0,0) and return the tuple of the final location you end up with. Note that clues may be used only once.

For example, if clues={(0,0): (1,0), (2,1): (3,5), (1,0): (2,1)} then you should first go to (0,0) then (1,0) then (2,1) then (3,5) and then finish because there's no clue in that location. In this case, the function returns (3,5).

"""

def treasure(clues):
    if clues == {}:
        return (0, 0)
    positions = list(clues.keys())
    current = clues[positions[0]]
    used = []
    while current in positions and current not in used:
        used.append(current)
        current = clues[current]
    return current