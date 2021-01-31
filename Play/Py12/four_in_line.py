"""
Four in a Line is a popular game where two players (red and yellow) compete against each other trying to form lines with 4 circles of the same color. These lines can be (i) horizontal, (ii) vertical or (iii) diagonal in both directions.

Write a Python function four_in_line(board) that given a matrix called board of varying size, returns a set with the two extrema points: the coordinates where the winner line starts and ends. The board matrix contains either 0 (empty), 1 (red) or 2 (yellow). Return an empty set if there is no winner. At most, one winner exists.

The first test is illustrated in the picture above.

"""

def four_in_line(board):
    rows = len(board)
    cols = len(board[0])
    for player in [1, 2]:
        win = 4*[player]
        for row in range(rows): # verificar linhas
            for col in range(cols-3):
                if board[row][col:col+4] == win:
                    return {(row, col), (row, col+3)}
        for row in range(rows-3): # verificar colunas
            for col in range(cols):
                if [board[row][col], board[row+1][col], board[row+2][col], board[row+3][col]] == win:
                    return {(row, col), (row+3, col)}
        for row in range(rows-3): # verificar diagonal 1
            for col in range(cols-3):
                if [board[row][col], board[row+1][col+1], board[row+2][col+2], board[row+3][col+3]] == win:
                    return {(row, col), (row+3, col+3)}
        for row in range(rows-3): # verificar diagonal 2
            for col in range(cols-2, cols):
                if [board[row][col], board[row+1][col-1], board[row+2][col-2], board[row+3][col-3]] == win:
                    return {(row, col), (row+3, col-3)}
    return {}