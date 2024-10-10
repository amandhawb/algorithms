# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# example:
# input = [1,2,3,4,5,6,7] k = 3
# output = [5,6,7,1,2,3,4]

def helper(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left, right = left + 1, right - 1
    return arr

def rotate_array_right(arr, k):
    k = k % len(arr)

    # [1,2,3,4,5,6,7]
    helper(arr, 0, len(arr) -1)
    # [7,6,5,4,3,2,1]
    helper(arr, 0, k -1)
    # [5,6,7,4,3,2,1]
    helper(arr, k, len(arr) -1)
    # [5,6,7,1,2,3,4]

    return arr

print(rotate_array_right([1,2,3,4,5,6,7], 3)) # [5,6,7,1,2,3,4]
print(rotate_array_right([-1, -100, 3, 99], 2)) # [3, 99, -1, -100]