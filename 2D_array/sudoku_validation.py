# Sudoku Solver
# Write the function sudokuSolve that checks whether a given sudoku board (i.e. sudoku puzzle) is solvable. If so, the function will returns true. Otherwise (i.e. there is no valid solution to the given sudoku board), returns false.

# In sudoku, the objective is to fill a 9x9 board with digits so that each column, each row, and each of the nine 3x3 sub-boards that compose the board contains all of the digits from 1 to 9. The board setter provides a partially completed board, which for a well-posed board has a unique solution. As explained above, for this problem, it suffices to calculate whether a given sudoku board has a solution. No need to return the actual numbers that make up a solution.

# A sudoku board is represented as a two-dimensional 9x9 array of the characters '1','2',...,'9' and the '.' character, which represents a blank space. The function should fill the blank spaces with characters such that the following rules apply:

# In every row of the array, all characters '1','2',...,'9' appear exactly once.
# In every column of the array, all characters '1','2',...,'9' appear exactly once.
# In every 3x3 sub-board that is illustrated below, all characters '1','2',...,'9' appear exactly once.
# A solved sudoku is a board with no blank spaces, i.e. all blank spaces are filled with characters that abide to the constraints above. If the function succeeds in solving the sudoku board, it'll return true (false, otherwise).

import collections

def isValidSudoku(board):
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for row in range(9):
        for col in range(9):
            if board[row][col] == ".":
                continue
            if (board[row][col] in rows[row] or
                board[row][col] in cols[col] or
                board[row][col] in squares[(row // 3, col // 3)]):
                return False
            else:
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                squares[(row // 3, col // 3)].add(board[row][col])    
    return True


# TEST 1
board1 = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board1)) # True

board2 = [[".",".",".",".","5",".",".","1","."],
 [".","4",".","3",".",".",".",".","."],
 [".",".",".",".",".","3",".",".","1"],
 ["8",".",".",".",".",".",".","2","."],
 [".",".","2",".","7",".",".",".","."],
 [".","1","5",".",".",".",".",".","."],
 [".",".",".",".",".","2",".",".","."],
 [".","2",".","9",".",".",".",".","."],
 [".",".","4",".",".",".",".",".","."]]
print(isValidSudoku(board2)) # False
