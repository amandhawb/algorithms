# Eeyore has collected two piles of sticks to rebuild his house and needs to choose pairs of sticks whose lengths are the right proportion. Write a function good_pairs() that accepts two integer arrays pile1 and pile2 where each integer represents the length of a stick. The function also accepts a positive integer k. The function should return the number of good pairs.
# A pair (i, j) is called good if pile1[i] is divisible by pile2[j] * k. Assume 0 <= i <= len(pile1) - 1 and 0 <= j <= len(pile2) - 1.

def good_pairs(pile1, pile2, k):
    good_pairs_cnt = 0
    for i in range(len(pile1)):
        for j in range(len(pile2)):
            num = pile2[j] * k
            if pile1[i] % num == 0:
                good_pairs_cnt += 1
    
    return good_pairs_cnt

print(good_pairs([1, 3, 4], [1, 3, 4], 1)) # 5
print(good_pairs([1, 2, 4, 12], [2, 4], 3)) # 2