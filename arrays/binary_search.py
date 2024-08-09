# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        middle = left + right // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            left = middle
        elif arr[middle] > target:
            right = middle
    
    return -1

print(binary_search([-1, 0, 3, 5, 9, 12], 9))
print(binary_search([10], 3))