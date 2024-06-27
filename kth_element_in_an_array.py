# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# You must solve it in O(n) time complexity.

# first idea: sort the array in descending order and return the kth index, but the sorting will give me 
# the complexity in O(n log n)
# second idea: convert the array to a min heap and make the size of the heap the same as K, after that, return the root which will be the kth largest element

import heapq

def kth_largest(nums, k):
    # convert the array in a min heap of size = k
    heapq.heapify(nums)
    while len(nums) > k:
        heapq.heappop(nums)
    return nums[0]

print(kth_largest([3,2,1,5,6,4], 2))
print(kth_largest([3,2,3,1,2,4,5,5,6], 4))
print(kth_largest([3], 1))