# Given the root of a binary tree, return the sum of all left leaves.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# recursive:
def is_leaf(node):
    if node is not None and node.left is None and node.right is None:
        return node

def sum_of_left_leaves(root):
    if root is None:
        return 0
    
    total_sum = 0
    if root.left and is_leaf(root.left):
        total_sum += root.left.val
    else:
        total_sum += sum_of_left_leaves(root.left)

    total_sum += sum_of_left_leaves(root.right)

    return total_sum
    

# iterative:
def sum_of_left_leaves_iterative(root):
    if root is None:
        return 0
    
    stack = [root]
    total_sum = 0

    while stack:
        node = stack.pop()
        if node.left:
            if is_leaf(node.left):
                total_sum += node.left.val
            else:
                stack.append(node.left)
        if node.right:
            stack.append(node.right)
    
    return total_sum