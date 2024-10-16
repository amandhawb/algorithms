# https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem
# Given a binary tree, return its height

# time = O(n) where n is the total edge quantity in the tree
# space O(h) where h is the height of the tree due to additional space on the call stack
def height(root):
    if not root:
        return -1
    return 1 + max(height(root.right), height(root.left))