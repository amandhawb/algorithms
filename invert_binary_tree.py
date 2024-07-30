# Given the root of a binary tree, invert the tree, and return its root.

# Traversal mode: I will use DFS pre-order traversal, because I want to invert the position of each root's children recursively
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        if not root:
            return None

        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
