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
def unique_characters_in_place(str):
    right_pointer = len(str) - 1

    for i in range(len(str)):
        if str[i] != str[right_pointer]:
            right_pointer -= 1
        else:
            return False
    return True

print(unique_characters_in_place('amandha')) # false
print(unique_characters_in_place('code')) # true
print(unique_characters_in_place('')) # true
