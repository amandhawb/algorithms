# Given an integer array nums and an integer k, return the k most frequent elements. 
# You must solve it in O(n log n) time or better.

# idea 1 (using hashmap):
# 1) traverse the array and build a hashmap where the key is the number in the array, and the value is the occurance of the number
# 2) sort the hashmap by value (most frequent)
# 3) build an array size k
# 4) populate this array with the k most frequent elements

from typing import List

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    hash_map = {}

    for num in nums:
        if num not in hash_map:
            hash_map[num] = 1
        else:
            hash_map[num] += 1
    
    sorted_dict = dict(sorted(hash_map.items(), key=lambda item: item[1], reverse=True))

    res = []

    for item in sorted_dict.items():
        if k != 0:
            res.append(item[0])
            k -= 1
    
    return res

# TEST:
# print(top_k_frequent([1,1,1,2,2,3], 2)) # [1,2]
# print(top_k_frequent([1], 1)) # [1]


# idea 2 (using heap):
import heapq

def top_k_freq_heap(nums: List[int], k: int) -> List[int]:
    freq_map = {}

    for num in nums:
        if num not in freq_map:
            freq_map[num] = 1
        else:
            freq_map[num] += 1
    
    min_heap = []

    for num, freq in freq_map.items():
        if len(min_heap) < k:
            heapq.heappush(min_heap, (freq, num))
        if len(min_heap) == k:
            if freq > min_heap[0][0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, (freq, num))

    return [item[1] for item in min_heap]

# TEST:
print(top_k_freq_heap([1,1,1,2,2,3], 2)) # [1,2]
print(top_k_freq_heap([1], 1)) # [1]