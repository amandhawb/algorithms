# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
# Example 1:
# Input: strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

def group_anagrams(strs):
    hash_map = {}

    for word in strs:
        sorted_word = str(sorted(word))
        if sorted_word in hash_map:
            hash_map[sorted_word].append(word)
        else:
            hash_map[sorted_word] = [word]
    
    result = []

    for value in hash_map.values():
        result.append(value)
    
    return result

# TESTS
print(group_anagrams(["eat","tea","tan","ate","nat","bat"])) # [["bat"],["nat","tan"],["ate","eat","tea"]]
print(group_anagrams([""])) # [[""]]
print(group_anagrams(["a"])) # [["a"]]