# Q: What is the average run time complexity of inserting an item to a hash table?
# A: O(1)


# Q: What is the space complexity of the following algorithm? --> ASK
def containsDuplicate(nums):
    h = set()
    for num in nums:
        if num in h:
            return True
        h.add(num)
    return False

# A: O(n)

# Q: Consider the following sequence of operations on a stack:
# push(1), push(2), pop, push(1), push(2), pop, pop, pop, push(2), pop
# What is the sequence of popped out values?
# A: 2 2 1 1 2