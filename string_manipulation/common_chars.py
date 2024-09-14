# Write a function that takes in a non-empty list of non-empty strings and returns a list of characters that are common to all strings in the list, ignoring multiplicity.
# Note that the strings are not guaranteed to only contain alphanumeric characters. The list you return can be in any order.

def common_chars(strings):
    common_chars = set(strings[0])

    for chars in strings[1:]:
        common_chars = { char for char in common_chars if char in chars }
    
    return list(common_chars)


# TEST 1:
strings1 = ["abc", "bcd", "cbaccd"]
print(common_chars(strings1)) # ["b", "c"]

# TEST 2:
strings2 = ["abcde", "aa", "foobar", "foobaz", "and this is a string", "aaaaaaaa", "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeea"]
print(common_chars(strings2)) # ["a"]

# TEST 3:
strings3 = ["ab&cdef!", "f!ed&cba", "a&bce!d", "ae&fb!cd", "efa&!dbc", "eff!&fff&fffffffbcda", "eeee!efff&fffbbbbbaaaaaccccdddd", "*******!***&****abdcef************", "*******!***&****a***********f*", "*******!***&****b***********c*"]
print(common_chars(strings3)) # ["!", "&"]
