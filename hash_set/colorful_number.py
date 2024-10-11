# Given a number, find out whether it is colorful.
# Colorful Number: When in a given number, the product of every contiguous sub-sequence is different. That number is called a Colorful Number. 
# Example 1:
# Given Number : 3245
# Output: Colorful
# Number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245.
# this number is a colorful number, since product of every digit of a sub-sequence are different.
# That is, 3 2 4 5 (3*2)=6 (2*4)=8 (4*5)=20, (3*2*4)= 24 (2*4*5)= 40
# https://tutorialhorizon.com/algorithms/colorful-numbers/

# time = O(n^2) --> for each element in the array, the inner loop runs up to n times 
# space = O(n^2) --> in the worst case, the set could store up to O(nˆ2) elements (since there can be n subsequences of length 1, n-1 of length 2, and so on)
def colorful_number(numbers):
    hash_set = set()
    iterable_list = [int(i) for i in str(numbers)]

    for i in range(len(iterable_list)):
        product = 1
        for j in range(i, len(iterable_list)):
            product *= iterable_list[j]
            if product in hash_set:
                return "Not colorful"
            hash_set.add(product)
    return "Colorful"

print(colorful_number(3245)) # colorful
print(colorful_number(326)) # not colorful