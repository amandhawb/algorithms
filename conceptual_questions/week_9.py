# 1) If the age passed to the Python function below is 18, what will the function return?

def data_protection_notice(age):
    if age < 13:
        return "Go ask a parent's permission to sign up."
    elif age < 18:
        return "Your data is protected by COPPA."
    elif age < 21:
        return "Your data is protected in the UK by article 9 of GDPR and in California through CCPA"
    else:
        return "Your data is protected in the UK by GDPR and in California through CCPA"
    
# answer --> Your data is protected in the UK by article 9 of GDPR and in California through CCPA


# 2) Which of the following calls to the 2D Array will result in the output 6?

A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

# answer --> A[1][2]


# 3) A good pair is two adjacent integers whose sum is even. Which of the following arrangements of arr[N] produce(s) the maximum number of good pairs that is possible?

# arr[8] = {10, 9, 13, 15, 3, 16, 9, 13}

# pick one or more options:
# a) 10 13 9 16 15 3 9 13 --> 2 good pairs
# b) 13 9 13 15 3 9 16 10 --> 4 good pairs --> check
# c) 13 9 13 3 9 16 15 10 --> 2 good pairs
# d) 13 9 9 13 15 3 10 16 --> 4 good pairs --> check


# 4) If I had 5 strings, each representing an email address that I intended to send emails to, what data structure would be the best way to store those strings?
# answer --> as an array of strings


# 5) We want to write a function that returns 2 times the sum of all numbers in an array. For example, given [1,2,3,4], our function should return 20, as (1+2+3+4) * 2 = 20
# We write the following solution:

def double_sum(nums):
    current_sum = 0
    for i in range(0, len(nums)):
        current_sum += 2 * nums[i]
    return current_sum

# Given the array [4, 2, 10, 5, 8, 12] what happens to our current_sum variable when i = 3?
# answer --> current_sum increases from 32 to 42


# 6) For the following binary tree, select the sequence which represents the in-order traversal
#             F
#           /  \
#          B    G
#        /  \     \
#       A    D     I
#           / \    /
#          C   E  H

# answer --> A - B - C - D - E - F - G - H - I


# 7) What is the runtime of this method?

def print_numbers(nums):
    length_of_nums = len(nums)
    for i in range(0, length_of_nums):
        for j in range(0, length_of_nums):
            print(nums[j])
    for x in range(0, length_of_nums):
        print(nums)

# answer --> O(n^2)


# 8) Here is an incorrect pseudocode for the algorithm which is supposed to determine whether a sequence of parentheses is balanced:

# declare a character stack
# while (more input is available)
# {
#   read a character
#   if the character is a '('
#       push it on the stack
#   else if the character is a ')' and the stack is not empty
#       pop a character off the stack
#   else 
#       print "unbalanced" and exit
# }
# print balanced

# which of these unbalanced sequence does the above code think is balanced?
# a) ((()) --> this
# b) ())(()
# c) (()()))
# d) A and C
# e) All of the above

# 9) consider the following code:

def addFun(n:int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 2
    return addFun(n-1) + addFun(n - 2)

# what value is returned as a result of the call addFun(6)? 16


