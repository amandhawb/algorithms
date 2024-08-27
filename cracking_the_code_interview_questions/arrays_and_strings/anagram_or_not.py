# write a method to decide if two strings are anagrams or not

# anagram = a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.
# in anagram letters can not be left over either added.

def anagram_or_not(s1, s2):
    hash_map = {}

    for char in s1:
        if char not in hash_map:
            hash_map[char] = 1
        else:
            hash_map[char] += 1

    for char in s2:
        if char not in hash_map:
            return False
        elif hash_map[char] <= 0:
            if char != ' ':
                return False
        else:
            hash_map[char] -= 1

    for key, value in hash_map.items():
        if value != 0 and key != ' ':
            return False
    return True

print(anagram_or_not('casa', 'saca'))
print(anagram_or_not('cinema', 'iceman'))
print(anagram_or_not('a decimal point', 'im a dot in place'))

