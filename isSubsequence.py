# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Understand:
# input: s = 'adc' | t = 'ajkdoc'
# output: True
# input: s = 'poe' | t = 'ekpo'
# output: False

# Match:
# I can think in a hash map to store the letter and its position
# Also can traverse both strings 

# Plan:
# Done in excalidraw

def isSubsequence(s, t):
    indexS, indexT = 0, 0

    while indexS < len(s) and indexT < len(t):
        if s[indexS] == t[indexT]:
            indexS += 1
        indexT += 1
    
    return indexS == len(s)

print(isSubsequence('adc', 'ajkdoc')) # True
print(isSubsequence('poe', 'ekpo')) # False
print(isSubsequence('a', 'defghi')) # False


# New way to solve on July/1/2024:

def isSubsequenceNew(s, t):
    pointer_s = 0

    for letter in t:
        if letter == s[pointer_s]:
            pointer_s += 1
    
    return pointer_s == len(s)

print(isSubsequenceNew('adc', 'ajkdoc')) # True
print(isSubsequenceNew('poe', 'ekpo')) # False
print(isSubsequenceNew('a', 'defghi')) # False