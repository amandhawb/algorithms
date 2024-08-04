def is_palindrome(s):
    s = s.lower()

    left,right = 0, len(s) -1

    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
        
    return True

print(is_palindrome('amandha')) # False
print(is_palindrome('aa')) # True
print(is_palindrome('arara')) # True
print(is_palindrome(' ')) # True
