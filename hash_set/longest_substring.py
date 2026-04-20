# Given a string s, find the length of the longest substring without repeating characters.

# idea:

# have a curr_longest variable to hold the largest substring so far
# start an empty hash set that stores the already seen chars to make sure the substring is without repeating chars
# perform a for loop that:
#   check if the curr char is already in the hashset:
#       if it is not: i added the char in the hashset, and update the curr_longest to +1 (check with max() to make sure to only update if the counter is bigger than the number before)
#       if it is: clean the hashset (delete everything), add the curr char in the hashset

def length_of_longest_substring(s: str) -> int:
    curr_longest = 0
    already_seen_chars = set()
    start = 0

    for end in range(len(s)):
        while s[end] in already_seen_chars:
            already_seen_chars.remove(s[start])
            start += 1

        already_seen_chars.add(s[end])
        curr_longest = max(curr_longest, end - start + 1)
    
    return curr_longest

print(length_of_longest_substring("pwwkep")) # 4
print(length_of_longest_substring("abcabcbb")) # 3
print(length_of_longest_substring("aaaaaa")) # 1
