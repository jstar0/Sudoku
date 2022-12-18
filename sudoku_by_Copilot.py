# A simple program to solve a sudoku puzzle
# The program takes a 9x9 matrix as input and prints the solved matrix
# If the puzzle is unsolvable, the program prints "No solution found"
# The program uses backtracking to solve the puzzle
# The program is written in Python 3
# Path: sudoku_by_ChatGPT.py
# Compare this snippet from sudoku_by_Copilot.py:
def solve(board):
     # Find an empty cell
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                # Try every number from 1 to 9
                for num in range(1, 10):
                    if is_valid(board, i, j, num):
                        # If the number is valid, place it and recursively try to solve the rest of the board
                        board[i][j] = num
                        if solve(board):
                            return True
                         # If the board cannot be solved, backtrack and try a different number
                        board[i][j] = 0
                return False
    # If the board is full and all the numbers are valid, the puzzle is solved
    return True

def is_valid(board, row, col, num):
    # Check if the number is already in the row
    for i in range(9):
        if board[row][i] == num:
            return False
    # Check if the number is already in the column
    for i in range(9):
        if board[i][col] == num:
            return False
    # Check if the number is already in the 3x3 subgrid
    subgrid_row = row // 3
    subgrid_col = col // 3
    for i in range(3):
        for j in range(3):
            if board[subgrid_row*3 + i][subgrid_col*3 + j] == num:
                return False
    # If the number is not in the row, column, or subgrid, it is a valid choice
    return True
# Example usage: solve the following Sudoku puzzle
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
if solve(board):
    for row in board:
        print(row)
else:
    print("No solution found")