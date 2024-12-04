# Indexing and Slicing:
# Extract characters from a string using indexing (positive and negative) and slicing.
string = "amandhab"
print(string[0]) # a
print(string[-1]) # last element --> b
print(string[-2]) # a
print(string[0:3]) # ama
print(string[-4:-1]) # dha
print(string[0::]) # amandhab
print(string[-1::]) # b

# String Methods:
# Use .isalpha(), .isdigit(), .islower(), and .isupper() to check string properties.
# Try .join() to combine a list of strings into one string.
print(string.isalpha()) # true
print(string.isdigit()) # false
nums = 123
print(nums.is_integer()) # true
print("amandha123".isdigit()) # false
print("123".isdigit()) # true
print("AMANDHA".islower()) # false
print("Amandha".islower()) # false
list_str = ["amandha", "wingert", "barok"]
print(' '.join(list_str))

# String Manipulation:
# Reverse a string using slicing: string[::-1].
print("amandha"[::-1])