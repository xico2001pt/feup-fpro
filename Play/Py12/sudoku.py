"""
Write a Python function solve_sudoku(board) that, given an incomplete Sudoku matrix in board, returns the complete version.

For example, if you are given this board:
8	4	1	7	2	6	3	5	9
7	5	3	8	1	9	4	6	2
0	9	2	5	3	4	1	8	7
1	2	8	9	5	7	6	4	3
9	6	5	1	4	3	2	7	8
4	3	7	6	8	2	9	1	5
3	1	4	2	7	8	5	9	6
2	8	9	4	6	5	7	0	1
5	7	6	3	9	1	8	2	4

Then, you must complete all values equal to zero, and return the completed board. In this case, the first should be 6 and the second should be 3.

The rules of Sudoku are:

    Each cell must have a value between 1 and 9
    For each line, all values should be different
    For each column, all values should be different
    For each of the nine 3x3 square, all values should be different.

"""

def solve_sudoku(board):
    rows, cols = 9, 9
    check = False
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == 0:
                #verificar linhas
                available_num_row = board[row]
                if available_num_row.count(0) == 1:
                    for x in range(1, cols+1):
                        if x not in available_num_row:
                            board[row][col] = x
                            check = True
                            break
                if check:
                    check = False
                    continue
                #verifica colunas
                available_num_col = [board[i][col] for i in range(9)]
                if available_num_col.count(0) == 1:
                    for y in range(1, rows+1):
                        if y not in available_num_col:
                            board[row][col] = y
                            continue
    return board