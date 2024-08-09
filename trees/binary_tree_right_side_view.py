# Given the root of a binary tree, imagine yourself stading on the right siide of it, return the values
# of the nodes you can see ordered from top to bottom.

# example:

#       1 <---
#      / \
#     2   3 <---
#      \   \
#       5   4 <---

class TreeNode:
    def __init__(self, val, right= None, left= None):
        self.val = val
        self.right = right
        self.left = left

def right_side_view(root):
    result = []
    if not root:
        return
    else:
        result.append(root.val)
        right_side_view(root.right)
    
    return result
