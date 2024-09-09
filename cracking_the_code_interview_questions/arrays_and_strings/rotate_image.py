# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees.

def rotate_image(matrix):
    size = len(matrix) # 3 -> quantity of rows
    # transpose
    for row in range(size):
        for col in range(row, len(matrix[row])):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
    # reverse
    for row in range(len(matrix)):
        matrix[row].reverse()

    return matrix
    
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotated_matrix = rotate_image(matrix)
for row in rotated_matrix:
    print(row)

# Can you solve it in place?