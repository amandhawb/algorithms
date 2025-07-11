# Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# idea: slicing window - two pointer solution
# start both pointers in the beginning of the array
# have a curr_sum variable to hold the sum so far
# have a min_lenght variable starting at the infinite
# every time the end pointer move (expand the window), increase the curr_sum
# when curr_sum is >= target, it means that i found a valid contiguous subarray, so i need to store this length in the min_length variable, but i just want to save it if it is smaller than the previous one
# after that i need to shrink the window to see if i find a smaller length of subarray, so i decrease the curr_sum by the start pointer and then move the start pointer
# if the curr_sum is still >= target, i am safe to keep shrinking the window, if not, i need to expand the window again


from typing import List

def min_subarray_len(target: int, nums: List[int]) -> int:
    min_length = float('inf')
    current_sum = 0
    start = 0

    for end in range(len(nums)):
        current_sum += nums[end]

        while current_sum >= target:
            min_length = min(min_length, end - start + 1)
            current_sum -= nums[start]
            start += 1
    
    return 0 if min_length == float('inf') else min_length


# TEST:
print(min_subarray_len(7, [2,3,1,2,4,3])) # 2
print(min_subarray_len(4, [1,4,4])) # 1
print(min_subarray_len(11, [1,1,1,1,1,1,1]  )) # 0
