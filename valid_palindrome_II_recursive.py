# Given a string s, return true if the s can be palindrome after deleting at most one character from it.
# Solve in a recursive way

class Solution:
    def validPalindrome(s):
    
        def isPalindrome(left, right, skipped):
            if skipped > 1:
                return False
            
            while left < right:
                if s[left] != s[right]:
                    return isPalindrome(left+1, right, skipped+1) or isPalindrome(left, right-1, skipped+1)
                else:
                    left += 1
                    right -= 1
            return True
        return isPalindrome(0, len(s)-1, 0)
    
    print(validPalindrome('abca'))
    print(validPalindrome('amandha'))
    print(validPalindrome('a'))
    print(validPalindrome(''))
    print(validPalindrome('cbbcc'))