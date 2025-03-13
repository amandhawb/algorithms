# Implement a function that iterates over a m x n integer matrix and returns a frequency map of prime numbers found in the matrix. 
# A prime number is a number greater than 1 that has no divisors other than 1 and itself.
# We have provided the helper function is_prime() to you, which accepts an integer n and returns True if n is prime and False otherwise

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_freq_map(matrix):
    freq_map = {}

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            num = matrix[row][col]
            if is_prime(num):
                if num in freq_map:
                    freq_map[num] += 1
                else:
                    freq_map[num] = 1
    
    return freq_map

# Test Case 1: Basic 3x3 matrix with some prime numbers
matrix1 = [
    [2, 3, 4],
    [5, 6, 7],
    [8, 9, 10]
]
print(prime_freq_map(matrix1))  # Expected output: {2: 1, 3: 1, 5: 1, 7: 1}

# Test Case 2: Matrix with no prime numbers
matrix2 = [
    [4, 6, 8],
    [10, 12, 14],
    [16, 18, 20]
]
print(prime_freq_map(matrix2))  # Expected output: {}

# Test Case 3: Matrix where all elements are prime numbers
matrix3 = [
    [2, 3, 5],
    [7, 11, 13],
    [17, 19, 23]
]
print(prime_freq_map(matrix3))  # Expected output: {2: 1, 3: 1, 5: 1, 7: 1, 11: 1, 13: 1, 17: 1, 19: 1, 23: 1}

# Test Case 4: Matrix with repeated prime numbers
matrix4 = [
    [2, 2, 2],
    [3, 3, 3],
    [5, 5, 5]
]
print(prime_freq_map(matrix4))  # Expected output: {2: 3, 3: 3, 5: 3}

# Test Case 5: Large numbers, including a large prime
matrix5 = [
    [97, 89, 83],
    [79, 73, 71],
    [67, 61, 59]
]
print(prime_freq_map(matrix5))  # Expected output: {97: 1, 89: 1, 83: 1, 79: 1, 73: 1, 71: 1, 67: 1, 61: 1, 59: 1}

# Test Case 6: 1xN matrix
matrix6 = [[2, 3, 5, 7, 11, 13, 17, 19]]
print(prime_freq_map(matrix6))  # Expected output: {2: 1, 3: 1, 5: 1, 7: 1, 11: 1, 13: 1, 17: 1, 19: 1}

# Test Case 7: Nx1 matrix
matrix7 = [[2], [3], [5], [7], [11]]
print(prime_freq_map(matrix7))  # Expected output: {2: 1, 3: 1, 5: 1, 7: 1, 11: 1}

# Test Case 8: Empty matrix
matrix8 = []
print(prime_freq_map(matrix8))  # Expected output: {}

# Test Case 9: Matrix with only 1s (which are not prime)
matrix9 = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]
print(prime_freq_map(matrix9))  # Expected output: {}

# Test Case 10: Mixed numbers with negative numbers and zero
matrix10 = [
    [-5, 0, 2],
    [3, -7, 5],
    [6, -11, 7]
]
print(prime_freq_map(matrix10))  # Expected output: {2: 1, 3: 1, 5: 1, 7: 1}
