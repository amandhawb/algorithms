# You are given an array of integers stones where stones[i] is the weight of the ith stone.

# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.

# Return the weight of the last remaining stone. If there are no stones left, return 0.

# UMPIRE

# Understand:
# Question 1) Can the array have just one element? Yes
# Question 2) Can the element be negative? Yes
# Question 3) Is the array sorted? No
# Question 4) Will the array have letters? No, only integers

# Match:
# I believe I will need to first sort the array in ascending order. After that I will compare the two first elements. Then I do the necessary math
# to destroy both or one stone. And after each math calculated, I need to sort the array again.

# Plan:
# Done in excalidraw

# Implement:

def last_stone_weight(arr):
    while len(arr) > 1:
        arr.sort(reverse=True)
        if arr[0] == arr[1]:
            arr.remove(arr[1])
            arr.remove(arr[0])
        elif arr[0] > arr[1]:
            arr[0] = arr[0] - arr[1]
            arr.remove(arr[1])
        else:
            arr[1] = arr[1] - arr[0]
            arr.remove(arr[0])
    
    if len(arr) == 1:
        return arr[0]
    else:
        return 0
    
# Review:
# Done, in the review realized that the else statement will never occur because the array is sorted, so can remove this part of the code

# Evaluate:
# Space complexity = O(1) | Time complexity = O(n log n)


print('input', [2,2])
print('output', last_stone_weight([2,2]))