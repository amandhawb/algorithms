# Given an sorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# questions: 
# 1) Can I assume that will always have at least one sequence? No, in case there is no sequence, return 0
# 2) Can the array be empty? No, it always has at least one element


def longest_consecutive_seq_sorted(nums):
    counter = 0
    for i in range(len(nums) - 1):
        next_element = nums[i + 1]
        curr_plus_one = nums[i] + 1
        if next_element == curr_plus_one:
            counter += 1
    if counter > 0:
        return counter + 1
    return 0

print(longest_consecutive_seq_sorted([1,2,3,4,100,200]))
print(longest_consecutive_seq_sorted([100,200]))


# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

def longest_consecutive_seq_unsorted(nums):
    hash_table = set(nums)
    counter = 1
    for num in hash_table:
        if num - 1 not in hash_table:
            curr = num
            while curr + 1 in hash_table:
                curr += 1
                counter += 1
    return counter

print(longest_consecutive_seq_unsorted([100, 4, 200, 1, 3, 2])) 

