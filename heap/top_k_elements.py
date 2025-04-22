# Given an integer array nums and an integer k, return the k most frequent elements within the array.
# The test cases are generated such that the answer is always unique.
# You may return the output in any order.

import heapq
def topKFrequent(nums, k):
    freq_map = {}

    for num in nums:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1
    
    min_heap = []

    for num, freq in freq_map.items():
        heapq.heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    result = [num for freq, num in min_heap]
    return result

# ===========================
# TESTS
# ===========================

print("Test 1:", topKFrequent([1,1,1,2,2,3], 2))         # Expected: [1, 2]
print("Test 2:", topKFrequent([4,1,-1,2,-1,2,3], 2))      # Expected: [-1, 2]
print("Test 3:", topKFrequent([1], 1))                    # Expected: [1]
print("Test 4:", topKFrequent([1,2,3,1,2,1], 1))          # Expected: [1]
print("Test 5:", topKFrequent([5,3,1,1,1,3,73,1], 2))     # Expected: [1, 3]
print("Test 6:", topKFrequent([0,0,0,1,1,2,2,3,3,3,3], 1))# Expected: [3]
print("Test 7:", topKFrequent([7,7,7,8,8,8,9], 2))        # Expected: [7, 8]
print("Test 8:", topKFrequent([-1,-1,-1,-2,-2,-3], 2))    # Expected: [-1, -2]