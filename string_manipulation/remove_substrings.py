# T-I-Double Guh-Er: That spells Tigger! Write a function tiggerfy() that accepts a string word and returns a new string that removes any substrings t, i, gg, and er from word. The function should be case insensitive.

def tiggerfy(word):
    word = word.lower()
    word = word.replace("t", "")
    word = word.replace("i", "")
    word = word.replace("gg", "")
    word = word.replace("er", "")
    return word

print(tiggerfy("Trigger"))
print(tiggerfy("Programming"))


# Using regular expressions (regex)

import re

def triggerfy_regex(word):
    word = word.lower()
    substrings_to_remove = ["t", "i", "gg", "er"]
    
    pattern = "|".join(substrings_to_remove) # create fegex pattern like "t|i|gg|er"
    word.re.sub(pattern, "", word)

    return word

print(tiggerfy("Potter"))
print(tiggerfy("Jessie"))