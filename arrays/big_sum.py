# In this challenge, you are required to calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.

# time = O(n)
# space = O(1)
def big_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total

# TEST
print(big_sum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005])) # 5000000015