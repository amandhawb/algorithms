# https://leetcode.com/problems/sort-the-people/description/

def sort_people(heights, names):
    pairs = zip(heights, names)
    sorted_pairs = sorted(pairs, reverse=True)
    return [ name for _, name in sorted_pairs ]


# TESTS
print(sort_people([180, 190, 165], ['Curry', 'Lebron', 'Amandha'])) # Lebron, Curry, Amandha