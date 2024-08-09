# Given a 2D integer array matrix, return the transpose of matrix. The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices

def transpose(matrix):
    row, col = len(matrix), len(matrix[0])
    # transposed = [[0] * row for _ in range(col)]
    transposed = []
    for i in range(col):
        transposed.append([])
        for _ in range(row):
            transposed[i].append(0)

    for i in range(row):
        for j in range(col):
            transposed[j][i] = matrix[i][j]
    
    return transposed
