# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

# Examples:
# 1:
# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# 2:
# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# 3:
# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

def reverse_words(s):
    arr = []
    temp = ""

    for char in s:
        if char != " ":
            temp += char
        elif temp != "":
            arr.append(temp)
            temp = ""
    
    if temp != "":
        arr.append(temp)

    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    
    return " ".join(arr)

print(reverse_words("the sky is blue"))
print(reverse_words("   hello   world"))
print(reverse_words("a good   example"))

    