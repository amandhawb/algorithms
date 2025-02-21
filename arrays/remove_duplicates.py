# Write a function remove_dupes() that accepts a sorted array items, and removes the duplicates in-place such that each element appears only once. Return the length of the modified array. You may not create another array; your implementation must modify the original input array items.

def remove_dupes(items):
    i = 0
    while i < len(items):
        if i + 1 < len(items) and items[i] == items[i+1]:
            items.remove(items[i])
        else:
            i += 1
    return len(items)
    

print(remove_dupes(["extract of malt", "haycorns", "honey", "thistle", "thistle", "thistle"])) # 4

