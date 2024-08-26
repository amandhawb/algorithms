# Implement an algorithm to determine if a string has all unique characters. 
def unique_characters(str):
    hash_set = set()
    for char in str:
        if char in hash_set:
            return False
        else:
            hash_set.add(char) 
    return True

print(unique_characters('amandha')) # false
print(unique_characters('code')) # true
print(unique_characters('')) # true

# What if you can not use additional data structures?
def unique_characters_no_extra_space(s):
    s_length = len(s)

    for i in range(s_length):
        for j in range(i + 1, s_length):
            if s[i] == s[j]:
                return False
    return True

print(unique_characters_no_extra_space('amandh')) # false
print(unique_characters_no_extra_space('code')) # true
print(unique_characters_no_extra_space('')) # true
