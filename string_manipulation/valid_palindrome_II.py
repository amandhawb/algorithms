# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

def valid_palindrome(s):
    if len(s) == 0 or len(s) == 1:
        return True

    right = len(s) -1
    left = 0

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            skip_left = s[left+1: right+1]
            skip_right = s[left:right]
            
            if (skip_left == skip_left[::-1] or 
                skip_right == skip_right[::-1]):
                return True
            else:
                return False
    return True

# tests:

print(valid_palindrome('abca'))
print(valid_palindrome('amandha'))
print(valid_palindrome('a'))
print(valid_palindrome(''))
print(valid_palindrome('cbbcc'))