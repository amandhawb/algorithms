# 1) Tree algorithms typically run in time O(d). What is d?
# Answer: The depth of the tree


# 2) Given the code below, in what order should we insert the nodes to get th efollowing binary search tree.
# Tree:
#     2
#   /   \
#  1     3

# Code:
# def insert(node, data):
#     if node is None:
#         node = TreeNode(data)
#     else:
#         if data <= node.data:
#             node.left = insert(node.left, data)
#         else:
#             node.right = insert(node.right, data)
#     return node

# Answer: 2,1,3


# 3) We are asked for the level-order traversal of a binary tree and we use a queue to implement this solution
# - crete empty queue an push root node to it
# - do the following when queue is not empty:
    # - pop a node from queue and print it
    # - push left child of popped node to queue if not null
    # - push right child of popped node to queue if not null
# What is the maximum length of the queue for level-order traversal equal to?

# Answer: Maximum elements at a level


# 4) Consider this binary search tree:
#                 14
#                /  \
#               2    16
#              / \
#             1   5
#                /
#               4

# Suppose we remove the root, replacing it with something form the left subtree. What will be the new root?
# Answer: 5


# 5) What is the order of nodes visited using an in-order traversal?
#                 14
#                /  \
#               2    11
#             /  \  /  \
#            1   3  10  30
#                   /   /
#                  7   40

# Answer: 1,2,3,14,7,10,11,40,30
