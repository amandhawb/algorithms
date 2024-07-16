# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there is an integer x such that n == 3ˆx 

# Question:
# 1) What are the constraints for this problem?
# -2ˆ31 <= n <= 2ˆ31 -1

def isPowerOfThree(n):
    i = 0
    while i < 32:
        if 3 ** i == n:
            return True
        i += 1
    return False