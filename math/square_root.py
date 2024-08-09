# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.

def square_root(num):
    left, right = 0, num

    while left <= right:
        middle = (left + right) // 2

        if middle ** 2 == num:
            return middle
        elif middle ** 2 < num:
            left = middle + 1
        else:
            right = middle - 1
    return right
