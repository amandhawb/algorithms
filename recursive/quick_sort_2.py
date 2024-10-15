# https://www.hackerrank.com/challenges/quicksort2/problem

# time = O(nˆ2) in the worst case and O(n log n) in average
# space = O(n) in the worst case and O(log n) in average
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort([7,4,3,0,8,1,2,9])) # [0,1,2,3,4,7,8,9]