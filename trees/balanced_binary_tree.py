# Given a binary tree, determine if it is height-balanced.
# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

# Understand:
# What type of tree is it? Binary Tree
# Can I assume the tree will be complete? No, a node may have less than 2 children

# Match:
# Appropriate Tree Traversal (pre-order, in-order, post-order, level-order)?
# --> Since I need to get the height of the tree, I need to traverse all nodes down the tree, I
# should recursively return depth of each node upward to parent, so the Pre-Order traversal would be appropriate

# Plan:
# 1) Create function to return the height of tree and collect balance at each node
#    a) Basecase is Null Node, return 0
#    b) Collect information regarding balance of node
#    c) Recursively return the max between height of left node and right node and add one for current node
# 2) Create a variable to hold balance information
# 3) Call the function to check balance of each node
# 4) Return the balance


class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        def helper(root):
            if not root:
                return 0
        
            leftHeight = helper(root.left)
            rightHeight = helper(root.right)

            if abs(leftHeight - rightHeight) > 1:
                nonlocal balanced
                balanced = False
                return 0
            
            return max(leftHeight, rightHeight) + 1
        
        balanced = True

        helper(root)

        return balanced

        