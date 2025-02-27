# Taken captive, Captain Anne Bonny has been smuggled a secret message from her crew. She will know she can trust the message if it contains all of the letters in the alphabet. Given a string message containing only lowercase English letters and whitespace, write a function can_trust_message() that returns True if the message contains every letter of the English alphabet at least once, and False otherwise.

# idea:
# return false if the size of the string is smaller than 26 (alphabet size)
# create an hash map where the key will be letters and the value will start as 0
# for every letter in the string, if it is in the hash_map, I will update the value to += 1
# in the end, if the map has one value as 0, return False, otherwise True

import string
def can_trust_message(message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for letter in alphabet:
        if letter not in message:
            return False
    return True
    # if len(message) < 26:
    #     return False

    # alphabet_hash_map = {letter: 0 for letter in string.ascii_lowercase}

    # for letter in message:
    #     if letter in alphabet_hash_map:
    #         alphabet_hash_map[letter] += 1
    
    # for counter in alphabet_hash_map.values():
    #     if counter == 0:
    #         return False
    
    # return True
    
# Contains all letters (should return True)
print(can_trust_message("the quick brown fox jumps over the lazy dog"))  # True
print(can_trust_message("abcdefghijklmnopqrstuvwxyz"))  # True
print(can_trust_message("a bc d e f g h i j k l m n o p q r s t u v w x y z"))  # True

# Missing letters (should return False)
print(can_trust_message("the quick brown fox jumps over the lazy do"))  # False (missing 'g')
print(can_trust_message("hello world"))  # False (missing many letters)
print(can_trust_message("abcdefghijklmnoqrstuvwxyz"))  # False (missing 'p')

# Edge cases
print(can_trust_message(""))  # False (empty string)
print(can_trust_message("aaaaa bbbbb ccccc ddddd eeeee"))  # False (repeats but does not contain all letters)
print(can_trust_message("a b c d e f g h i j k l m n o p q r s t u v w x y"))  # False (missing 'z')

