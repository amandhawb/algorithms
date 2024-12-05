# Advanced Methods:
# Use .index() to find the position of a substring in a string (handle exceptions if not found).
# Use .rfind() to search from the end of the string.
try:
    print("amandha".index('h'))
    print("amandha".index('w'))
except ValueError:
    print("Letter not found!")

print("amandha".rfind('a'))
print("amandha".rfind('w'))

# Sorting Strings:
# Sort a string alphabetically using sorted().
# Sort a list of strings by length using sorted() with a custom key function.
print(sorted('amandha'))
print(sorted('amandha', reverse=True))

# String Comparison:
# Compare two strings for equality and lexicographical order using <, >, ==.
print('amandha' == "well")
print('amanda' < "amandha")