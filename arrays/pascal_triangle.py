# https://leetcode.com/problems/pascals-triangle/description/
# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly 

# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Example 2:
# Input: numRows = 1
# Output: [[1]]

def pascal_triangle(numRows):
    if numRows <= 0:
        return 0
    
    result = [[1]]
    for i in range(numRows -1):
        temp = [0] + result[-1] + [0]
        row = []
        for j in range(len(result[-1]) + 1):
            row.append(temp[j] + temp[j+1])
        result.append(row)
    
    return result

# TESTS
print(pascal_triangle(5)) # [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
print(pascal_triangle(0)) # 0
print(pascal_triangle(1)) # [[1]]
print(pascal_triangle(-5)) # 0


