# Given the root of a binary tree, invert the tree, and return its root.

# Traversal mode: I will use DFS pre-order traversal, because I want to invert the position of each root's children recursively

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invert_tree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        
        root.left, root.right = root.right, root.left

        self.invert_tree(root.left)
        self.invert_tree(root.right)

        return root
    
# tests

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
#             4
#          /     \
#         2       7
#        /  \    /  \
#       1   3    6   9
result = Solution().invert_tree(root)
print(result.val) # 4
print(result.left.val, result.right.val) # 7, 2
print(result.left.left.val, result.left.right.val) # 9, 6
print(result.right.left.val, result.right.right.val) # 3, 1