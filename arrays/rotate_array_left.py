# A left rotation operation on an array shifts each of the array's elements 1 unit to the left. For example, if 2 left rotations are performed on array [1,2,3,4,5], then the array would become [3,4,5,1,2]. Note that the lowest index item moves to the highest index in a rotation. This is called a circular array.
# Given an array a of n integers and a number, d, perform d left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.

# time = O(1)
# space = O(1)
def rotate_to_the_left(arr, k):
    k = k % len(arr)
    return arr[k:] + arr[:k]

# TEST
print(rotate_to_the_left([1,2,3,4,5], 4)) # [5,1,2,3,4]
