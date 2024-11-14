# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Given a string s, find the length of the longest substring without repeating characters.
# Example:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

def lengthOfLongestSubstring(s):
    char_idx = {}
    longest = 0
    start = 0

    for end, char in enumerate(s):
        if char in char_idx and char_idx[char] >= start:
            start = char_idx[char] + 1
        
        char_idx[char] = end
        longest = max(longest, end - start + 1)
    
    return longest

# TEST
print(lengthOfLongestSubstring("abcabcbb")) # 3
print(lengthOfLongestSubstring("pwwkew")) # 3
print(lengthOfLongestSubstring("bbbbb")) # 1
print(lengthOfLongestSubstring("dvdf")) # 3
