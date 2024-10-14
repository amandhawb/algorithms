# https://www.hackerrank.com/challenges/insertionsort1/problem

# Given a sorted list with an unsorted number e in the rightmost cell, can you write some simple code to insert e into the array so that it remains sorted?
# Since this is a learning exercise, it won't be the most efficient way of performing the insertion. It will instead demonstrate the brute-force method in detail.

def insertion_sort(arr):
    size = len(arr)
    last_element = arr[-1]
    i = size - 2

    while size >= 0 and arr[i] > last_element:
        arr[i + 1] = arr[i]
        i -= 1
    
    arr[i + 1] = last_element
    return arr

print(insertion_sort([1,2,4,5,3]))
print(insertion_sort([2,4,6,8,3]))