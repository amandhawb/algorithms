# Captain Blackbeard has an integer array chests of length n where all the integers in chests are in the range [1, n] and each integer appears once or twice. Return an array of all the integers that appear twice, representing the treasure chests that have duplicates.

# idea:
# create an empty set called elements
# create an empty array called result
# for every number in the array, I will check:
#   --> if the number is not in the set, add it
#   --> if the number is in the set (it means it is duplicated), I will add on the result array
# return the result

def find_duplicate_chests(chests):
    elements = set()
    result = []

    for num in chests:
        if num not in elements:
            elements.add(num)
        else:
            result.append(num)

    return result

print(find_duplicate_chests([4, 3, 2, 7, 8, 2, 3, 1])) # [2,3]
print(find_duplicate_chests([1, 1, 2])) # [1]
print(find_duplicate_chests([1])) # []


# SOLVE IN PLACE (no extra space):

def find_duplicate_chests_in_place(chests):
    result = []

    for num in chests:
        index = abs(num) -1

        if chests[index] < 0:
            result.append(abs(num))
        else:
            chests[index] = -chests[index]
    
    return result

print(find_duplicate_chests_in_place([1, 2, 3, 4, 5])) # []
print(find_duplicate_chests_in_place([1, 1])) # [1]
print(find_duplicate_chests_in_place([2, 2, 3, 3, 4, 4, 5, 5])) # [2,3,4,5]
print(find_duplicate_chests_in_place([5, 5, 1, 2, 3, 4])) # [5]
