# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above 
# https://leetcode.com/problems/pascals-triangle-ii/description/

# Example 1:
# Input: rowIndex = 3
# Output: [1,3,3,1]

# Example 2:
# Input: rowIndex = 0
# Output: [1]

# Example 3:
# Input: rowIndex = 1
# Output: [1,1]

def pascal_triangle(rowIndex):
    result = [[1]]
    for i in range(rowIndex):
        temp = [0] + result[-1] + [0]
        row = []
        for j in range(len(result[-1]) +1):
            row.append(temp[j] + temp[j+1])
        result.append(row)
    return result[-1]

print(pascal_triangle(3)) # [1,3,3,1]
        
    