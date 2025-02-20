# 1) Write a function get_sum_of_odds () that accepts a 2D list of integers matrix. Return a list in the format [num_odds, sum] where num_odds represents the number of odd numbers in the matrix, and sum represents the sum of all odd numbers in the matrix.

def get_sum_of_odds(matrix):
    num_of_odds = 0
    sum_of_odds = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] % 2 != 0:
                num_of_odds += 1
                sum_of_odds += matrix[row][col]
    return [num_of_odds, sum_of_odds]

# TEST:
print(get_sum_of_odds([[1,2,3,4], [5,6,7,8], [9,10,11,12]])) # [6,36]
print(get_sum_of_odds([[10,-2], [-3,5], [4,8]])) # [2,2]
print(get_sum_of_odds([])) # [0,0]

# 2) You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing O s and 1's, where 0 means empty and 1 means not empty, and an integer n, return True if new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and False otherwise.

def can_place_flowers(flowerbed, n):
    size = len(flowerbed)

    for i in range(size):
        if n == 0:
            return True
        if flowerbed[i] == 0:
            prev = (i == 0) or (flowerbed[i-1] == 0)
            next = (i == size -1) or (flowerbed[i+1] == 0)

            if prev and next:
                flowerbed[i] = 1
                n -= 1

    return n == 0

# TESTS
print(can_place_flowers([1, 0, 0, 0, 1], 1))  # True
print(can_place_flowers([1, 0, 0, 0, 1], 2))  # False
print(can_place_flowers([0], 1))  # True
print(can_place_flowers([0, 1], 1))  # False
print(can_place_flowers([0, 0, 0, 0, 0], 2))  # True
print(can_place_flowers([1, 0, 0, 0, 0, 1], 1))  # True


# 3) Write a function merge_sorted_lists() that accepts two sorted lists lst1 and lst2 as parameters and
# merges them into a single sorted list.

def merge_sorted_lists(list1, list2):
    merged_list = []
    l, r = 0, 0

    while l < len(list1) and r < len(list2):
        if list1[l] < list2[r]:
            merged_list.append(list1[l])
            l += 1
        elif list2[r] < list1[l]:
            merged_list.append(list2[r])
            r += 1
        else:
            merged_list.append(list1[l])
            merged_list.append(list2[r])
            l += 1
            r += 1

    merged_list.extend(list2[r:])
    merged_list.extend(list1[l:])

    return merged_list

# TESTS
print(merge_sorted_lists([1,3,5], [2,4,6])) # [1,2,3,4,5,6]

# 4) What is the output of the following code snippet?
def mystery_function(word):
    start = 0
    end = len(word) - 1
    while start < end:
        if word[start] != word[end]:
            return False
        start += 1
        end -= 1
    return True
word = "kayak"
result = mystery_function(word)
print(result)

# ANSWER --> True

# 5) What is the output of the following code snippet?
def mystery_function(nums):
    count = 0
    max_count = 0
    for i in range(len(nums)):
        if nums[i] > 0:
            count += 1
        else:
            if count > max_count:
                max_count = count
                count = 0
        if count > max_count:
            max_count = count
    return max_count
result = mystery_function([1, 2, -3, 4, 5, -6, 7, 8, 9])
print(result)

# ANSWER --> 3

# 6) Find the bug! The following function contains a bug. sum_positives should accept a list of integers lst and return the sum of all positive values in lst.
# For example, if we passed in [-1, 2, 3, 4, -5] , sum_positives should return 9.
# Which of the following options will fix the bug?
def sum_positives(lst):
    total = 0
    for num in lst:
        if num > 0:
            total = num # --> fix here. instead of total = num, it needs to be total += num so it will increase the number instead of modifing it
    return total

# 7) Find the bug! The provided code incorrectly implements the function sum_matrix. Given a 2D list of
# integers matrix, sum_matrix should return the sum of all elements in matrix.
# Identify any bug(s) within the given implementation and correct the code so that it successfully passes the provided test cases.
def sum_matrix(matrix):
    row_length = len(matrix[0])
    total = 0 # --> added this
    for row in matrix:
        for j in range(row_length):
            total += row[j]
    return total

# TESTS
matrix = [[1,2], [3,4]]
print(sum_matrix(matrix)) # 10