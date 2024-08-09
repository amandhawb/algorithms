# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters, it reads the same forward and backward. 
# Given a string s, return true if it is a palindrome, or false otherwise.

# UMPIRE

# Understand:
# Can the string be empty? Yes, and it is a valid palindrome
# Can the string be a phrase? Yes
# Should I assume it will contain only letters? Yes
# Do I need to consider uppercase letters? Yes, convert them to lowercase

# Match:
# I can use pointers to traverse the string and compare each letter.

# Plan:
# Done on excalidraw

# Implement:

def valid_palindrome_string(string):
    new_string = ''
    for char in string:
        if char.isalpha():
            new_string += char.lower()

    if len(new_string) == 0 or len(new_string) == 1:
        return True
    
    left_pnt = 0
    right_pnt = len(new_string) - 1

    while left_pnt < right_pnt:
        if new_string[left_pnt] != new_string[right_pnt]:
            return False
        else:
            left_pnt += 1
            right_pnt -= 1
    return True

print(valid_palindrome_string('Amandha')) # False
print(valid_palindrome_string('Arara')) # True
print(valid_palindrome_string('A man, a plan, a canal: Panama')) # True
print(valid_palindrome_string('')) # True
print(valid_palindrome_string('1')) # True
print(valid_palindrome_string('a1')) # True
print(valid_palindrome_string('a1b')) # False


