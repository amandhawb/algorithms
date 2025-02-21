# 1) Write a function get_row_col() that accepts a 2D list of unique integers matrix and an integer value. Return a list in the
# format [row, column]where row represents the 0-based row index of value and column represents the 0-based column
# index of value. If value does not exist in matrix, return [-1, -1].

def get_row_col(matrix, value):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == value:
                return [row, col]
    return [-1,-1]

# TEST
print(get_row_col([[1,2,3,4], [5,6,7,8], [9,10,11,12]], 12)) # [2,3]


# 2) Given an array of integers arr , return *true if and only if it is a valid mountain array*.
# Recall that arr is a mountain array if and only if:
#   arr.length >= 3
#   There exists some i with 0 < i < arr.length - 1 such that:
#       arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#       arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

# Example 1:
# Input: arr = [2,1]
# Output: false
# Example 2:
# Input: arr = [3,5,5]
# Output: false
# Example 3:
# Input: arr = [0,3,2,1]
# Output: true

# idea:
# return false if the arr.length >= 3
# traverse the array to find the peak position
# --> create a variable peak_position starting at 0
# --> traverse from the 2nd position (index 1), so i will be able to compare with the prev element
#   --> to find the peak: if arr[i] > arr[i-1], update the peak_position to i
#   --> handle duplicate peaks: if arr[i] == arr[i-1], return False
#   --> else (arr[i-1] > arr[i]): break the for loop
# after knowing the position of the peak:
# if the peak is on the first or last position of the array, return false
# I traverse the array starting on the peak_position +1
#   --> return False if the arr[i] >= arr[i-1]
# if I got until the end of the two loops, i return true

def valid_mountain_array(arr):
    if len(arr) < 3:
        return False
    
    peak_position = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            peak_position = i
        elif arr[i] == arr[i-1]:
            return False
        else:
            break
    
    if peak_position == 0 or peak_position == len(arr) -1:
        return False

    for i in range(peak_position +1, len(arr)):
        if arr[i] >= arr[i-1]:
            return False
    
    return True

print(valid_mountain_array([3,5,5]))  # False
print(valid_mountain_array([0,3,2,1]))  # True
print(valid_mountain_array([2,1]))  # False
print(valid_mountain_array([3,4,5,2,1]))  # True
print(valid_mountain_array([3,2,1]))  # False
print(valid_mountain_array([1,2,3,4,5,3,2,1]))  # True


# 3) You are given two strings word1 and word2 . Merge the strings by adding letters in alternating order, starting with word1 . If a
# string is longer than the other, append the additional letters onto the end of the merged string.

def merge_string(word1, word2):
    merged = []
    i = 0
    j = 0

    while i < len(word1) and j < len(word2):
        merged.append(word1[i])
        merged.append(word2[j])
        i += 1
        j += 1
    
    merged.extend(word1[i:])
    merged.extend(word2[j:])

    return "".join(merged)

print(merge_string("abc", "pqr")) # "apbqcr"
print(merge_string("ab", "pqrs")) # "apbqrs"
print(merge_string("abcd", "pq")) # "apbqcd"


# 4) Given the following two strings below, which of the following options would create a variable called final_string that is assigned to the string yelling?
string1 = "yellow"
string2 = "screaming"

# ANSWER --> final_string = string1[:3] + string2[6:]


# 5) What is the output of the following code snippet?
def mistery_function(s):
    sequence = "aeiouAEIOU"
    result = ""

    for char in s:
        if char not in sequence:
            result += char
    
    return result
result = mistery_function("CodePath")
print(result) # ANSWER --> CdPth


# 6) Find the bug. The following function should return True if a given string s is a palindrome and False otherwise. However, it may contain a bug. Choose the option that updates check_palindrome so that its implementation is correct.
def check_palindrome(s):
    left, right = 0, len(s) -1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
result = check_palindrome("racecar")
print(result) # ANSWER --> No changes needed, the code is correct.


# 7) Find the bug. The provided code incorrectly implements the function rotate_matrix . Given an n x n 2D list matrix , rotate_matrix should
# return the matrix rotated 90 degrees clockwise. The matrix must be rotated in-place; DO NOT create another 2D list You may
# assume that the following constraints hold true:
# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# Identify any bug(s) with the given implementation and correct the code so that it successfully passes the provided test cases.
# Rotation of an n x n matrix works as follows:
# The rst row of the original matrix becomes the last column of the rotated matrix.
# The second row of the original matrix becomes the second-to-last column of the rotated matrix.
# This pattern continues until the last row of the original matrix becomes the rst column of the rotated matrix.

# EXAMPLE:
# original = [
    # [1,2,3]
    # [4,5,6]
    # [7,8,9]
# ]
# rotated = [
    # [7,4,1]
    # [8,5,2]
    # [9,6,3]
# ]

def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
    return matrix

print(rotate_matrix([
    [1,2,3],
    [4,5,6],
    [7,8,9],
])) # [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]

print(rotate_matrix([
    [1,2],
    [3,4]
])) # [
#   [3,1],
#   [4,2]
# ]

print(rotate_matrix([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
])) # [
#   [13,9,5,1],
#   [14,10,6,2],
#   [15,11,7,3]
#   [16,12,8,4]
# ]