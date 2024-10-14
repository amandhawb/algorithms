# https://www.hackerrank.com/challenges/insertionsort2/problem
# implement the insertion sort in an unsorted array

# time = O(nˆ2)
# space = O(1)
def insertion_sort(arr):
    size = len(arr)
    for i in range(1, size):
        key = arr[i]
        prev = i - 1
        
        while prev >= 0 and arr[prev] > key:
            arr[prev + 1] = arr[prev]
            prev -= 1
        
        arr[prev + 1] = key
    return arr

print(insertion_sort([1,4,3,5,6,2]))
print(insertion_sort([9,4,1,1,8,0]))
