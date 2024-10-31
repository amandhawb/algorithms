# https://leetcode.com/problems/max-consecutive-ones/submissions/1439253819/

# Given a binary array nums, return the maximum number of consecutive 1's in the array.
# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

def max_consecutive(nums):
    left = 0
    max_length = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            left = right + 1
        else:
            max_length = max(max_length, right - left +1)
    return max_length

print(max_consecutive([1,1,0,1,1,1])) # 3
print(max_consecutive([1,0,1,1,0,1])) # 2
        