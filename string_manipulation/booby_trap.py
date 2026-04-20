# Captain Feathersword has found another pirate's buried treasure, but they suspect it's booby-trapped. The treasure chest has a secret code written in pirate language, and Captain Feathersword believes the trap can be disarmed if the code can be balanced. A balanced code is one where the frequency of every letter present in the code is equal. To disable the trap, Captain Feathersword must remove exactly one letter from the message. Help Captain Feathersword determine if it's possible to remove one letter to balance the pirate code.
# Given a 0-indexed string code consisting of only lowercase English letters, write a function is_balanced() that returns True if it's possible to remove one letter so that the frequency of all remaining letters is equal, and False otherwise.


# 1) Create a frequency dictionary (`freq_dict`) to count how often each character appears in the code.
# 2) Create a frequency of frequencies dictionary (`frequency_count`) to count how often each frequency appears in `freq_dict`.
# 3) Determine the number of unique frequencies.
# 4) If there are three or more unique frequencies, it's impossible to balance the code by removing just one letter, so return `False`.
# 5) If there's only one unique frequency:
#     - If all characters are the same or have a frequency of 1, return `True`.
# 6) If there are exactly two unique frequencies, check if removing one letter can balance the remaining letters:
#     - If one frequency is 1 and it occurs exactly once, return `True`.
#     - If the difference between the two frequencies is 1 and the higher frequency occurs exactly once, return `True`.
# 7) If none of the conditions are met, return `False`


def is_balanced(code):
    freq = {}

    for letter in code:
        if letter not in freq:
            freq[letter] = 0
        freq[letter] += 1

    freq_counts = {}
    for count in freq.values():
        if count not in freq_counts:
            freq_counts[count] = 0
        freq_counts[count] += 1

    if len(freq_counts) == 1:
        return True

    if len(freq_counts) == 2:
        f1, f2 = sorted(freq_counts.keys())
        #f1, f2 = keys[0], keys[1]
        if f1 == 1 and freq_counts[f1] == 1:
            return True
        if f2 == f1 + 1 and freq_counts[f2] == 1:
            return True
        # if (f1 == 1 and freq_counts[f1] == 1) or (f2 == 1 and freq_counts[f2] == 1):
        #     return True
        # if (f1 == f2 + 1 and freq_counts[f1] == 1) or (f2 == f1 + 1 and freq_counts[f2] == 1):
        #     return True
    
    return False




print(is_balanced("arghh")) # True
print(is_balanced("haha")) # False
print(is_balanced("aabb")) # False
print(is_balanced("abc")) # False --
print(is_balanced("aabbc")) # True --
print(is_balanced("zzz")) # True --
print(is_balanced("aaabbc")) # False
print(is_balanced("a")) # True
print(is_balanced("aaaaabb")) # False





