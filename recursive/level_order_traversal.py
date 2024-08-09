# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

# recursive:
def level_order_traversal(root):
    def helper(node, level):
        if node is None:
            return
        
        if len(results) == level:
            results.append([])
        results[level].append(node.val)
        helper(node.left, level + 1)
        helper(node.right, level +1)

    results = []
    helper(root, 0)
    return results

# iterative:
def level_order_traversal_iterative(root):
    result = []
    queue = [root]

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.pop(0)
            if node:
                current_level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        
        result.append(current_level)
    
    return result