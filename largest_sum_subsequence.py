# You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.
# Return any such subsequence as an integer array of length k.
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

def maxSubsequebce(nums, k):
    # sort the array in descending order
    sorted_array = sorted(nums, reverse=True)

    # get the kth numbers in the new sorted array
    index = 0
    sorted_k_size_array = []
    while index < k:
        sorted_k_size_array.append(sorted_array[index])
        index += 1

    # store the quantity of appearences for each number in the sorted array
    hash_map = {}
    for num in sorted_k_size_array:
        if num in hash_map:
            hash_map[num] += 1
        else:
            hash_map[num] = 1

    # traverse the original array to get the right position for the result array

    result = []
    for num in nums:
        if num in hash_map and hash_map[nums] > 0:
            result.append(num)
            hash_map[num] -= 1
    
    return result
