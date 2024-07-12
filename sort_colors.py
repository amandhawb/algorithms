# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

def sort_colors(nums):
    left = 0
    right = len(nums) -1
    middle = 0

    while middle <= right:
        if nums[middle] == 2:
            nums[right], nums[middle] = nums[middle], nums[right]
            right -= 1
        elif nums[middle] == 1:
            middle += 1
        elif nums[middle] == 0:
            nums[left], nums[middle] = nums[middle], nums[left]
            left += 1
            middle += 1

    return nums

print(sort_colors([2,0,1]))
print(sort_colors([2,0,2,1,1,0]))
print(sort_colors([2,1,2,0,0,1]))
print(sort_colors([1,2,0]))
