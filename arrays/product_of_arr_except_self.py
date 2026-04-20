# Given an integer array nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# brutal force approach:
# have two for loops that makes the math and returns the new array

def brutal_force(nums):
    output = []

    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i != j:
                product *= nums[j]
        output.append(product)
    return output

# TEST:
print(brutal_force([1,2,3,4])) # [24,12,8,6]


# follow-up 1: solve it in O(n) time: --> using division and assumit there is no 0 in the array (division by zero is undefined)
def using_division(nums):
    output = []
    total = 1

    for num in nums:
        total *= num

    for num in nums:
        res = total // num
        output.append(res)
    
    return output

# TEST:
print(using_division([1,2,3,4])) # [24,12,8,6]


# follow-up 2: solve it without using division AND O(n) time:
def product_arr(nums):
    n = len(nums)
    left = [1] * n
    right = [1] * n
    output = [1] * n

    for i in range(1, n):
        left[i] = nums[i-1] * left[i-1]
    
    for i in range(n - 2, -1, -1):
        right[i] = nums[i+1] * right[i+1]

    for i in range(n):
        output[i] = right[i] * left[i]
    
    return output

# TEST:
print(product_arr([1,2,3,4])) # [24,12,8,6]