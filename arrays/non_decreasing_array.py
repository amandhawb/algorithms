# Given an array nums with n integers, write a function non_decreasing() that checks if nums could become non-decreasing by modifying at most one element.
# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

def non_decreasing(nums):
    threshold = 1
    for i in range(len(nums) -1):
        if nums[i] > nums[i+1]:
            if threshold == 0:
                return False
            threshold -= 1
    return True

# TESTS
print(non_decreasing([4, 2, 3])) # True
print(non_decreasing([4, 2, 1])) # False
print(non_decreasing([1, 2, 3, 4])) # True 
print(non_decreasing([1, 4, 2, 3])) # True
        