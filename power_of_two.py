# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.

# iterative:
def power_of_two(n):
    x = 1
    while x < n:
        x *= 2
    return x == n

# recursive:
def power_of_two_recursive(n):
    if n == 1:
        return True
    
    if n % 2 != 0 or n == 0:
        return False
    
    return power_of_two_recursive(n / 2)