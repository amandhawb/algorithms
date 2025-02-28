# 1) Given two integer arrays nums 1 and nums2, return an array of their intersection. 
# Your answer should be returned in ascending order.
# Example 1:
# Input: nums1 = [1, 2,2,1], nums2 = [2,2]
# Expected Output: [2,2]
# Example 2:
# Input: nums1 = [4,9,5], nums2 =
# [9,4,9,8,4]
# Expected Output: [4,9]

def two_arr_intersection(nums1, nums2):
    freq_map = {}
    result = []

    for num in nums1:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1
    
    for num in nums2:
        if num in freq_map and freq_map[num] > 0:
            result.append(num)
            freq_map[num] -= 1

    return sorted(result)

print(two_arr_intersection([1,2,2,1], [2,2])) # [2,2]
print(two_arr_intersection([4,9,5], [9,4,9,8,4])) # [4,9]
print(two_arr_intersection([1, 2, 2, 3], [2])) # [2]
print(two_arr_intersection([1, 2, 3], [4, 5, 6]))  # Output: []
print(two_arr_intersection([1, 1, 1, 2], [1, 1, 2, 2]))  # Output: [1, 1, 2]


# 2) Given a pattern and a string s, return True if s follows the same pattern and False otherwise.
# Here follow means that each letter in the pattern corresponds to exactly one unique word in the string s, and each word in the strings corresponds to exactly one unique letter in the pattern. This means that:
# 1. Each letter in the pattern should map to the same word every time it appears.
# 2. Each word in the strings should map to the same letter every time it appears.
# Example 1:
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: True
# Example 2:
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: False

def is_pattern(pattern, s):
    letter_to_word = {}
    word_to_letter = {}
    words = s.split()

    if len(pattern) != len(words):
        return False
    
    for i in range(len(pattern)):
        letter = pattern[i]
        word = words[i]

        if letter in letter_to_word:
            if letter_to_word[letter] != word:
                return False
        else:
            letter_to_word[letter] = word

        if word in word_to_letter:
            if word_to_letter[word] != letter:
                return False
        else:
            word_to_letter[word] = letter
    
    return True

print(is_pattern("abba", "dog cat cat dog"))  # True
print(is_pattern("abba", "dog cat cat fish"))  # False
print(is_pattern("aaaa", "dog cat cat dog"))  # False
print(is_pattern("abba", "dog dog dog dog"))  # False
print(is_pattern("abc", "one two three"))  # True
print(is_pattern("aaa", "dog dog dog"))  # True
print(is_pattern("aaa", "dog cat dog"))  # False


# 3) Given a list of strings strs, group the anagrams together. You can return the answer in any order.
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using each of the original letters exactly once.
# Example 1:
# Input: strs = ["'eat", "tea", "tan", "ate", "nat", "bat"]
# Expected Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea" ]] 
# Answers in a different order such as [["tan", "nat"], ["bat"], ["ate","tea", "eat"]] would also be acceptable

# Example 2:
# Input: strs = [""]
# Expected Output: [[""]]

# Example 3:
# Input: strs = ["'a"]
# Expected Output: [["a"]]

def group_anagrams(strs):
    anagram_map = {}

    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word not in anagram_map:
            anagram_map[sorted_word] = [word]
        else:
            anagram_map[sorted_word].append(word)
    
    return list(anagram_map.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
print(group_anagrams([""]))
# Output: [[""]]
print(group_anagrams(["a"]))
# Output: [["a"]]


# 4) Which of the following options will remove the key-value pair with key "grade" from the dictionary student?
student = {
    "name": "Emma",
    "class": 9,
    "grade": 'A'
}
# Pick ONE option
# student.pop("grade") ---> CORRECT
# student.clear("grade")
# student.remove("grade")
# student.popitem("grade")

# 5) Which of the following options will return the value "B"?
gradebook = {
    "class": {
        "student": {
            "name": "Mike",
            "grade": {
                "physics": 'C',
                "history": 'B'
            }
        }
    }
}
# Pick ONE option
# gradebook['class']['student']['grade']['history'] ---> CORRECT
# gradebook['class']['student']['grade'][1]
# gradebook['class'][0]['grade']['history']
# gradebook['class']['student'][1]['history']

# 6) What is the output of the following code snippet?
def process_data (names, scores) :
    result = {}
    for i in range (len(names)):
        name = names[i]
        score = scores[i]
        if name not in result:
            result[name] = []
        result[name].append(score)
    return result

names = ["Alice", "Bob", "Alice", "Bob", "Charlie"]
scores = [85, 90, 95, 80, 70]
result = process_data(names, scores)
print(result)
# ANSWER ---> {"Alice": [85, 95], "Bob": [90, 80], "Charlie": [70]}

# 7) Find the bug!
# You are given a function filter_below_threshold that is intended to take two inputs:
# * A dictionary dict1 where the keys are associated with integer values.
# * An integer threshold
# The goal of the function is to return a new dictionary that contains only the key-value pairs from dict1 where the values are strictly more than the given threshold.
# However, the current implementation of the function contains one or more bugs and does not pass the test cases as expected. Your task is to identify and correct the issues in the implementation so that the function works as intended.

def filter_below_threshold(dict1, threshold):
    filtered_dict = {}
    for key, value in dict1.items():
        if value > threshold: # --> changed from value < threshold to value > threshold
            filtered_dict[key] += threshold # --> added +
    return filtered_dict