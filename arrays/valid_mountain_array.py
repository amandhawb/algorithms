# Given an array of integers arr, return True if and only if is a valid mountain array. An arr is a mountain array if and only if:
# len(arr) >= 3
# there is some i with 0 < i < len(arr) - 1 such that:
#   arr[0] < arr[1] < ... < arr[i-1] < arr[i]
#   arr[i] > arr[i+1] > ... > arr[len(arr) -1]


def valid_mtn_arr(arr):
    if len(arr) < 3:
        return False
    
    # discover peak
    peak_idx = -1
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            peak_idx = i
        else:
            break
            
    if peak_idx == 0 or peak_idx == len(arr) -1:
        return False
    
    # verify decreasing starting on peak
    for i in range(peak_idx +1, len(arr)):
        if arr[i] >= arr[i -1]:
            return False
    
    return True

print(valid_mtn_arr([0, 3, 2, 1])) # True
print(valid_mtn_arr([2, 1, 4, 3])) # False
print(valid_mtn_arr([0, 3, 2, 1])) # True
print(valid_mtn_arr([3, 5, 5])) # False
print(valid_mtn_arr([2, 1])) # False 
print(valid_mtn_arr([1, 2, 3, 4, 5])) # False 
print(valid_mtn_arr([5, 4, 3, 2, 1])) # False 
print(valid_mtn_arr([1, 3, 2, 4, 5])) # False 
print(valid_mtn_arr([1, 2, 3, 2, 2, 1])) # False 
print(valid_mtn_arr([1, 2, 3, 3, 2, 1])) # False 