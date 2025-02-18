# Christopher Robin set up a scavenger hunt for Pooh, but it's a blustery day and several hidden clues have blown away. Write a function find_missing_clues() to help Christopher Robin figure out which clues he needs to remake. The function accepts two integers lower and upper and a unique integer array clues. All elements in clues are within the inclusive range [lower, upper].
# A clue x is considered missing if x is in the range [lower, upper] and x is not in clues.
# Return the shortest sorted list of ranges that exactly covers all the missing numbers. That is, no element of clues is included in any of the ranges, and each missing number is covered by one of the ranges.

# Example:
# clues = [0, 1, 3, 50, 75]
# lower = 0
# upper = 99
# find_missing_clues(clues, lower, upper) --> [[2,2], [4,49], [51,74], [76,99]]

# clues = [-1]
# lower = -1
# upper = -1
# find_missing_clues(clues, lower, upper) --> []

def find_missing_clues(clues, lower, upper):
    ans = []
    # handle the case where the lower is smaller than the first element in the clues
    if lower < clues[0]:
        ans.append([lower] + [clues[0] -1])
    
    for i in range(len(clues)):
        if clues[i] > clues[i-1] +1:
            ans.append([clues[i-1] +1] + [clues[i] -1])

    if upper > clues[-1]:
        ans.append([clues[-1] +1] + [upper])

    return ans

print(find_missing_clues([3,6], 0, 6)) # [[0,2], [4,5]]
print(find_missing_clues([0, 1, 3, 50, 75], 0, 99)) # [[2,2], [4,49], [51,74], [76,99]]
print(find_missing_clues([2, 5, 8], 1, 10)) # [[1, 1], [3, 4], [6, 7], [9, 10]]
print(find_missing_clues([3, 7], 1, 10)) # [[1, 2], [4, 6], [8, 10]]
print(find_missing_clues([1, 2, 3], 1, 3)) # [] (no missing numbers)
print(find_missing_clues([5, 10], 1, 15)) # [[1, 4], [6, 9], [11, 15]]
