# Given a non-empty binary treee, return the sum of all right leaves

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_of_right_leaves(root):
    if not root:
        return 0
    
    sum_right_leaves = 0

    if root.right and root.right.right is None and root.right.left is None:
        sum_right_leaves += root.right.val
    
    sum_right_leaves += sum_of_right_leaves(root.right)
    sum_right_leaves += sum_of_right_leaves(root.left)

    return sum_right_leaves



# Constructing a sample tree
root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(3)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
root.right.left = TreeNode(5)

print(sum_of_right_leaves(root)) # --> output: 4 + 3 = 7