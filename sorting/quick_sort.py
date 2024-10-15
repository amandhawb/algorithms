# https://www.hackerrank.com/challenges/quicksort1/problem
# Given arr and p = arr[0], partition arr into left, right,and equal using the Divide instructions. 
# Return a 1-dimensional array containing each element in left first, followed by each element in equal, followed by each element in right.

def quick_sort(arr):
    pivot = arr[0]
    left = []
    right = []
    
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
    
    return left + [pivot] + right

print(quick_sort([4,5,3,7,2])) # [3,2,4,5,7]