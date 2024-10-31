# https://leetcode.com/problems/max-consecutive-ones-iii/description/
# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
# Example 1:
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

def max_consecutive_ones(nums, k):
    max_consecutive = 0
    left = 0
    flipped = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            flipped += 1
        
        while flipped > k:
            if nums[left] == 0:
                flipped -=1
            left += 1
        
        max_consecutive = max(max_consecutive, right - left +1)

    return max_consecutive

print(max_consecutive_ones([1,1,1,0,0,0,1,1,1,1,0], 2)) # 6
print(max_consecutive_ones([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)) # 10