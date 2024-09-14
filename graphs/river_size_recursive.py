# You're given a two-dimensional array (a matrix) of potentially unequal height and width containing only 0 sand 1 s. Each 0 represents land, and each 1 represents part of a river. A river consists of any number of 1s that are either horizontally or vertically adjacent (but not diagonally adjacent).
# The number of adjacent 1s forming a river determine its size.
# Note that a river can twist. In other words, it doesn't have to be a straight vertical line or a straight horizontal line; it can be L-shaped, for example.
# Write a function that returns an arraysf the sizes of all rivers represented in the input matrix. The sizes don't need to be in any particular order.

def river_size_recursive(matrix):
    matrix_row_qnt = len(matrix)  # width
    matrix_col_qnt = len(matrix[0]) # height
    result = []
    visited = set()

    for row in range(matrix_row_qnt):
        for col in range(matrix_col_qnt):
            curr_position = (row,col)
            if curr_position in visited:
                continue
            size = [0]
            dfs(curr_position, size, visited, matrix)
            if size[0] > 0:
                result.append(size[0])
    return result

def dfs(position, size, visited, matrix):
        curr_row, curr_col = position
        if position in visited:
            return
        visited.add(position)
        if matrix[curr_row][curr_col] == 0:
            return
        if matrix[curr_row][curr_col] == 1:
            size[0] += 1
            new_position1 = (curr_row+1, curr_col)
            new_position2 = (curr_row, curr_col+1)
            new_position3 = (curr_row, curr_col-1)
            new_position4 = (curr_row-1, curr_col)
            if is_valid_position(new_position1, matrix, visited):
                dfs(new_position1, size, visited, matrix)
            if is_valid_position(new_position2, matrix, visited):
                dfs(new_position2, size, visited, matrix)
            if is_valid_position(new_position3, matrix, visited):
                dfs(new_position3, size, visited, matrix)
            if is_valid_position(new_position4, matrix, visited):
                dfs(new_position4, size, visited, matrix)

def is_valid_position(position, matrix, visited):
    matrix_row_qnt = len(matrix) -1  # width
    matrix_col_qnt = len(matrix[0]) -1 # height
    row, col = position
    if row < 0 or row > matrix_row_qnt:
        return False
    if col < 0 or col > matrix_col_qnt:
        return False
    else:
        return True


# TEST
matrix1 = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 1, 0]
]
print(river_size_recursive(matrix1)) # [2,1,3]

# TEST 2
matrix2 = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
]
print(river_size_recursive(matrix2)) # [2, 1, 5, 2, 2]