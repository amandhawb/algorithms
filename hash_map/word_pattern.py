# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:
# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.

# EXAMPLE:
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true

def word_pattern(pattern, s):
    words = s.split(" ")
    if len(pattern) != len(words):
        return False
    
    hash_map = {}

    for i in range(len(pattern)):
        curr_char = pattern[i]
        curr_word = words[i]
        if curr_char not in hash_map:
            if curr_word in hash_map.values():
                return False
            hash_map[curr_char] = curr_word
        if curr_word != hash_map[curr_char]:
            return False
    return True

# TEST
print(word_pattern('abba', 'dog cat cat dog')) # True
print(word_pattern('abba', 'dog cat cat fish')) # False
print(word_pattern('aaaa', 'dog cat cat dog')) # False
print(word_pattern('ab', 'dog dog')) # False
