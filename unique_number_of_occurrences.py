# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

# Understand:
# Questions:
# - Is the array sorted? It could be, but we don't know
# - Can the array be empty? Yes
# - The array contain only integers? Yes

# Match:
# The hash set can be a good strategy on this solution. The hash set will store the values encountered during a for loop on the array.

# Plan:
# Done on excalidraw

# Implement:

def unique_number_of_occurrences(arr):
    hash_map = {}

    for item in arr:
        if item in hash_map:
            hash_map[item] += 1
        else:
            hash_map[item] = 1
    
    counter = set()
    for value in hash_map.values():
        if value in counter:
            return False
        else:
            counter.add(value)
    return True

print(unique_number_of_occurrences([1,2,2,1,1,3])) # True
print(unique_number_of_occurrences([1,2])) # False
print(unique_number_of_occurrences([-3,0,1,-3,1,1,1,-3,10,0])) # True
