# Two friends like to pool their money and go to the ice cream store. They always choose two distinct flavors and they spend all of their money.
# Given a list of prices for the flavors of ice cream, select the two that will cost all of the money they have.
# Example. m = 6 cost = [1,3,4,5,6]
# The two flavors that cost 1 and 5 meet the criteria. Using -based indexing, they are at indices 1 and 4. Return the 1 and 4.
# If there is no combination possible, return -1
# https://www.hackerrank.com/challenges/icecream-parlor/problem

# time = O(n) --> where n is the length of cost array (I am iterating over cost array once)
# space = O(n) --> in the worst case (no solution found) the hashmap woll have all the elemnts from cost array
def ice_cream_store(money, cost):
    hash_map = {}
    for i in range(len(cost)):
        diff = money - cost[i]
        if diff in hash_map:
            position = i + 1
            pair = (hash_map[diff], position)
            return pair
        hash_map[cost[i]] = i + 1
    return -1

print(ice_cream_store(4, [1,4,5,3,2])) # 1, 4
print(ice_cream_store(9, [1,3,4,6,7,9])) # 2, 4
print(ice_cream_store(8, [1,3,4,4,6,8])) # 3, 4