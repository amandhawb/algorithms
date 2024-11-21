# https://leetcode.com/problems/symmetric-tree/description/
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# example: input = [1,2,2,3,4,4,3]
#          1
#        /   \
#       2     2
#      / \   / \
#     3  4  4   3
# output = True

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root) -> bool:
        def dfs(right, left):
            if not right and not left:
                return True
            if not right or not left:
                return False
            
            return (left.val == right.val and
             dfs(left.left, right.right) and
             dfs(left.right, right.left))

        return dfs(root.right, root.left)
    
# test
root1 = TreeNode(1,
                TreeNode(2, TreeNode(3), TreeNode(4)),
                TreeNode(2, TreeNode(4), TreeNode(3)))
print(Solution().isSymmetric(root1)) # True

root2 = TreeNode(1,
                TreeNode(2, None, TreeNode(3)),
                TreeNode(2, None, TreeNode(3)))
#          1
#        /   \
#       2     2
#        \     \
#        3      3
print(Solution().isSymmetric(root2)) # False

root3 = TreeNode(1,
                TreeNode(2, None, TreeNode(3)),
                TreeNode(2, TreeNode(3), None))
#          1
#        /   \
#       2     2
#      /       \
#     3        3
print(Solution().isSymmetric(root3)) # True
