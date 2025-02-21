# Given an integer array nums, write a function sort_by_parity() that moves all the even integers at the beginning of the array followed by all the odd integers.
# Return any array that satisfies this condition.

# naive approach:
# start two variables to hold the even numbers and odd numbers
# traverse the array from the begining to the end
# --> if the arrp[i] is odd, add on the odd array, same for even
# --> return the concatenated even array with the odd array
def sort_array_by_parity(arr):
    odd = []
    even = []

    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            odd.append(arr[i])
        else:
            even.append(arr[i])
    
    even.extend(odd)
    return even
print(sort_array_by_parity([3, 1, 2, 4])) # [2,4,3,1]


# two pointer technique:
def sort_array_by_parity_in_place(arr):
    left, right = 0, len(arr) -1

    while left < right:
        if arr[left] % 2 != 0 and arr[right] % 2 == 0:
            arr[left], arr[right] = arr[right], arr[left]
        if arr[left] % 2 == 0:
            left += 1
        if arr[right] % 2 != 0:
            right -= 1
    
    return arr
print(sort_array_by_parity_in_place([3, 1, 2, 4])) # [4,2,1,3]
