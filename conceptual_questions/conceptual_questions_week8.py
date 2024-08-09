# 1) What are the contents of mat after the following code segmnt has been executed?

mat = [[0 for c in range(3)] for r in range(4)]
# mat = [[0, 0, 0],
#        [0, 0, 0],
#        [0, 0, 0],
#        [0, 0, 0]]

for row in range(4):
    for col in range(3):
        if row < col:
            mat[row][col] = 1
        elif row == col:
            mat[row][col] = 2
        else:
            mat[row][col] = 3

# Answer:
# mat = [[2, 1, 1],
#        [3, 2, 1],
#        [3, 3, 2],
#        [3, 3, 3]]


# 2) A two-dimensional array, imagePixels, holds the brightness values for the pixels in an image. The brightness can range from 0 to 255. What does the following method compute?

def findMax(imagePixels: list[list[int]]):
    i = iMax = 0
    for r in range(len(imagePixels)):
        for c in range(len(imagePixels[0])):
            i = imagePixels[r][c]
            if i > iMax:
                iMax = i
    return iMax

# Answer: The maximum brightness value for all pixels in imagePixel


# 3) What are the contents of arr after the following code has been executed?

arr = [[3,2,1],[1,2,3]]
value = 0
for row in range(1, len(arr)):
    for col in range(1, len(arr[0])):
        if arr[row][col] % 2 == 1:
            arr[row][col] = arr[row][col] + 1
        if arr[row][col] % 2 == 0:
            arr[row][col] = arr[row][col] * 2

# Answer:
# arr = [[3, 2, 1],
#        [1, 4, 8]]

# 4) Given the follow matrix
grid = [ [1, 2, 3, 4], 
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]

# Which is the breadth first search traversal of this matrix?
# Answer: 1,2,5,3,6,9,4,7,10,13,8,11,14,12,15,16

# 5) Given the follow matrix
grid = [ [-1, 2, 3], 
         [0, 9, 8],
         [1, 0, 1]]

# Which is the depth first search traversal of this matrix?
# Answer: -1,2,3,8,1,0,1,0,9