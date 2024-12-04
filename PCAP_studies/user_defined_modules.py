# Simple User-Defined Module
# Create a module named calculator.py with the following functions:

# add(a, b) for addition
# subtract(a, b) for subtraction
# Import this module in another script and use its functions.
import sys
sys.path.append('/Users/amandhabarok/Workspace/Algorithms/my_modules')
from calculator import add, subtract
print(add(2, 2))
print(subtract(10, 5))

# Reusable Functions
# Write a module string_utils.py with the following:
# capitalize_words(s) that capitalizes the first letter of every word in a string.
# Import and use it to capitalize the sentence: "hello world, python is awesome."
from string_utils import capitalize_words
print(capitalize_words("hello world, python is awesome."))