# You're given a two-dimensional array (a matrix) of potentially unequal height and width containing only 0 sand 1 s. Each 0 represents land, and each 1 represents part of a river. A river consists of any number of 1s that are either horizontally or vertically adjacent (but not diagonally adjacent).
# The number of adjacent 1s forming a river determine its size.
# Note that a river can twist. In other words, it doesn't have to be a straight vertical line or a straight horizontal line; it can be L-shaped, for example.
# Write a function that returns an arraysf the sizes of all rivers represented in the input matrix. The sizes don't need to be in any particular order.

def river_size_iterative(matrix):
    result = []
    visited = set()
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            position = (row, col)
            if position in visited:
                continue
            else:
                traverseNode(position, matrix, visited, result)
    return result

def traverseNode(position, matrix, visited, result):
    current_river_size = 0
    nodesToExplore = [position]
    while len(nodesToExplore):
        current_node = nodesToExplore.pop()
        if current_node in visited:
            continue
        visited.add(current_node)
        row, col = current_node
        if matrix[row][col] == 0:
            continue
        current_river_size += 1
        unvisitedNeighbors = getUnvisitedNeighbors(current_node, matrix, visited)
        for neighbor in unvisitedNeighbors:
            nodesToExplore.append(neighbor)
    if current_river_size > 0:
        result.append(current_river_size)

def getUnvisitedNeighbors(position, matrix, visited):
    unvisitedNeighbors = []
    row, col = position
    if row > 0 and (row -1, col) not in visited:
        unvisitedNeighbors.append((row -1, col))
    if row < len(matrix) -1 and (row +1, col) not in visited:
        unvisitedNeighbors.append((row +1, col))
    if col > 0 and (row, col -1) not in visited:
        unvisitedNeighbors.append((row, col -1))
    if col < len(matrix[0]) - 1 and (row, col + 1) not in visited:
        unvisitedNeighbors.append((row, col +1))
    return unvisitedNeighbors

# TEST 1
matrix1 = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 1, 0]
]
print(river_size_iterative(matrix1)) # [2, 1, 3]

# TEST 2
matrix2 = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
]
print(river_size_iterative(matrix2)) # [2, 1, 5, 2, 2]
