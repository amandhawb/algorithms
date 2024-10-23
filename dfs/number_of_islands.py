# https://leetcode.com/problems/number-of-islands/description/
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# time = O(n*m) where n is the number of rows and m is the number of columns, each cell in the grid is visited exactly once
# space = O(n*m) the size of the matrix because of two factors: 1) in the worst case (where all cells are 1s) the visited set will have the same amount of elements in the matrix. 2) the dfs (recursion stack), in the worst case, can go as deep as n * m if all cells are '1'.
def number_of_islands(grid):
    row_qnt = len(grid)
    col_qnt = len(grid[0])
    visited = set()
    result = 0

    for row in range(row_qnt):
        for col in range(col_qnt):
            curr_position = (row, col)
            if curr_position not in visited:
                if grid[row][col] == '1':
                    result += 1
                    dfs(curr_position, visited, grid)
    return result

def dfs(position, visited, grid):
    if position in visited:
        return
    visited.add(position)

    row, col = position
    pos_up = (row -1, col)
    pos_down = (row +1, col)
    pos_right = (row, col +1)
    pos_left = (row, col -1)

    if is_valid_position(pos_up, grid) and grid[row -1][col] == '1':
        dfs(pos_up, visited, grid)
    if is_valid_position(pos_down, grid) and grid[row +1][col] == '1':
        dfs(pos_down, visited, grid)
    if is_valid_position(pos_right, grid) and grid[row][col +1] == '1':
        dfs(pos_right, visited, grid)
    if is_valid_position(pos_left, grid) and grid[row][col -1] == '1':
        dfs(pos_left, visited, grid)
    
def is_valid_position(position, grid):
    row, col = position
    if row < 0 or row > len(grid) -1:
        return False
    if col < 0 or col > len(grid[0]) -1:
        return False
    return True


# TESTS
grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(number_of_islands(grid1)) # 1

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(number_of_islands(grid2)) # 3