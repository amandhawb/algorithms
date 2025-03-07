# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# You must solve it in O(n) time complexity.

import heapq

def find_kth_largest(nums, k):
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    return min_heap[0]

print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))  # 5
print(find_kth_largest([1], 1))  # 1
print(find_kth_largest([2, 2, 2, 2, 2], 3))  # 2
print(find_kth_largest([10, 9, 8, 7, 6, 5], 4))  # 7
print(find_kth_largest([10, 20, 30, 40, 50], 5))  # 10
print(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)) # 4






