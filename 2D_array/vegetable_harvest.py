# Rabbit is collecting carrots from his garden to make a feast for Pooh and friends. Write a function harvest() that accepts a 2D n x m matrix vegetable_patch and returns the number of of carrots that are ready to harvest in the vegetable patch. A carrot is ready to harvest if vegetable_patch[i][j] has value 'c'.
# Assume n = len(vegetable_patch) and m = len(vegetable_patch[0]). 0 <= i < n and 0 <= j < m.

def vegetable_harvest(vegetable_patch):
    counter = 0
    for row in range(len(vegetable_patch)):
        for col in range(len(vegetable_patch[0])):
            if vegetable_patch[row][col] == 'c':
                counter += 1
    
    return counter

# cleaner version:
def veg_harvest(veg_patch):
    return sum(cell == 'c' for row in veg_patch for cell in row) 

vegetable_patch = [
	['x', 'c', 'x'],
	['x', 'x', 'x'],
	['x', 'c', 'c'],
	['c', 'c', 'c']
]
print(vegetable_harvest(vegetable_patch)) # 6
print(veg_harvest(vegetable_patch)) # 6

patch = [
    ['c', '.', '.'],
    ['.', 'c', 'c'],
    ['.', '.', '.']
]
print(vegetable_harvest(patch))  # Output: 3
print(veg_harvest(patch)) # Output: 3

patch2 = [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.']
]
print(vegetable_harvest(patch2))  # Output: 0
print(veg_harvest(patch2)) # Output: 0