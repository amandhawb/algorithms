# Write a function reverse_list() that takes in a list lst and returns elements of the list in reverse order. The list should be reversed in-place without using list slicing (e.g. lst[::-1]).
# example:
# lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
# output = ["eeyore", "roo", "piglet", "christopher robin", "pooh"]

def reverse_list(lst):
    l, r = 0, len(lst) -1
    while l < r:
        lst[l], lst[r] = lst[r], lst[l]
        l += 1
        r -= 1
    return lst

print(reverse_list(["pooh", "christopher robin", "piglet", "roo", "eeyore"])) # ["eeyore", "roo", "piglet", "christopher robin", "pooh"]