# https://leetcode.com/problems/product-of-array-except-self/description/
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.


# time = O(n) --> two separated loops thourgh the whole arr
# space = O(n) --> result array holds the same length of arr
def product_except_self(arr):
    result = []

    # [1,2,3,4]
    curr = 1
    for i in range(len(arr)):
        if i == 0:
            result.append(1)
        else:
            curr *= arr[i-1]
            result.append(curr)
    
    # [1, 1, 2, 6]

    curr = 1
    for i in range(len(arr)-1, -1, -1):
        result[i] *= curr
        curr *= arr[i]
    
    # [24,12,8,6]
    return result

print(product_except_self([1,2,3,4])) # [24,12,8,6]
print(product_except_self([-1,1,0,-3,3])) # [0,0,9,0,0]
