# Given a non-empty binary treee, return the sum of all left leaves

class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = None
        self.right = None


def sum_of_left_leaves(root):
    if root is None:
        return 0
    
    left_sum = 0

    if root.left and root.left.left is None and root.left.right is None:
        left_sum += root.left.val

    left_sum += sum_of_left_leaves(root.right)
    left_sum += sum_of_left_leaves(root.left)
        