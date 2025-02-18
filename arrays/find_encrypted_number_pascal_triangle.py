# Given the initial sequence of the digits of numbers, find the encrypsted number using Pascal Triangle scheme.
# When an array of digits is fed to this system, it sums the adjacent digits. It takes the rightmost digit (least signficant digit) of each addition for the next step. Thus the number of digits in each step is reduced by 1. This procedure is repeated unitl there are only 2 digits left, and this sequence of 2 digits forms the encrypted number.
# You should report a string of digits representing the encrypted number.

# Example:
# numbers = [4,5,6,7]
# output = "04"

def encrypted_pascal_triangle(nums):
    while len(nums) > 2:
        new_nums = []
        for i in range(len(nums) -1):
            summed_value = (nums[i] + nums[i+1]) % 10
            new_nums.append(summed_value)
        nums = new_nums
    return "".join(map(str, nums))

# TESTS
print(encrypted_pascal_triangle([4,5,6,7]))
