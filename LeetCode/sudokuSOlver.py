def SudokuSolver(sudoku, row = 0, col = 0):

    if row == 9:
        for row in sudoku:
            print(row)
        return
    if col == 9:
        SudokuSolver(sudoku, row + 1, 0)
        return


    if sudoku[row][col] > 0:
        SudokuSolver(sudoku, row, col + 1)
    else:
        for value in range(1, 10):
            if isSafe(sudoku, row, col, value):
                sudoku[row][col] = value
                SudokuSolver(sudoku, row, col + 1)
                sudoku[row][col] = 0


def isSafe(sudoku, row, col, value):

    for r in range(9):
        if sudoku[r][col] == value:
            return False
    for c in  range(9):
        if sudoku[row][col] == value:
            return False


    box_r = row - (row % 3)
    box_c = col - (col % 3)

    for r in range(box_r):
        for c in range(box_c):
            if sudoku[r][c] == value:
                return False

    return True



sudoku = [[8, 1, 0, 0, 3, 0, 0, 2, 7], 
            [0, 6, 2, 0, 5, 0, 0, 9, 0], 
            [0, 7, 0, 0, 0, 0, 0, 0, 0], 
            [0, 9, 0, 6, 0, 0, 1, 0, 0], 
            [1, 0, 0, 0, 2, 0, 0, 0, 4], 
            [0, 0, 8, 0, 0, 5, 0, 7, 0], 
            [0, 0, 0, 0, 0, 0, 0, 8, 0], 
            [0, 2, 0, 0, 1, 0, 7, 5, 0], 
            [3, 8, 0, 0, 7, 0, 0, 4, 2]]

SudokuSolver(sudoku)