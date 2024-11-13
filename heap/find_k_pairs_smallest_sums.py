# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

# You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.
# Define a pair (u, v) which consists of one element from the first array and one element from the second array.
# Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

# example:
# input: nums1 = [1,7,11], nums2 = [2, 4, 6], k = 3
# output: [[1,2], [1,4], [1,6]]

import heapq

def kSmallestPairs(nums1, nums2, k):
    response = []
    if not nums1 or not nums2 or not k:
        return response
    
    heap = []
    visited = set()
    heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))
    visited.add((0,0))

    while k and heap:
        _, i, j = heapq.heappop(heap)
        response.append([nums1[i], nums2[j]])

        if i + 1 < len(nums1) and (i + 1, j) not in visited:
            heapq.heappush(heap, (nums1[i+1] + nums2[j], i + 1, j))
            visited.add((i+1, j))
        
        if j + 1 < len(nums2) and (i, j +1) not in visited:
            heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
            visited.add((i, j + 1))
        
        k -= 1
    
    return response

# TESTS
print(kSmallestPairs([1,7,11], [2,4,6], 3)) # [[1,2], [1,4], [1,6]]
print(kSmallestPairs([1,1,2], [1,2,3], 2)) # [[1,1], [1,1]]
