# https://leetcode.com/problems/group-anagrams/description/
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# Example:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# time = O(n * k log k) --> due to the sorted function. N is the number of words in the strs and K is the maximum length of a word in strs.
# space = O(n * k) --> in the worst case, every word in strs could be unique when sorted, resunting in N unique keys. Each key has a length up to K, where K is the max length of any word in strs.

from collections import defaultdict
def group_anagrams(strs):
    anagrams = defaultdict(list)

    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    
    return list(anagrams.values())

print(group_anagrams(["eat","tea","tan","ate","nat","bat"])) # [["bat"],["nat","tan"],["ate","eat","tea"]]
print(group_anagrams([""])) # [[""]]
print(group_anagrams(["a"])) # [["a"]]