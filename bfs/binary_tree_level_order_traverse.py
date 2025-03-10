# Given the root of a binary tree, return the level order traversal of its nodes' values (i.e., from left to right, level by level)

# example:
# input = [3,9,20,null,null,15,7]
#            3 
#           / \
#          9   20
#             / \
#            15  7
# output = [[3], [9,20], [15,7]]

import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: TreeNode):
    res = []
    q = collections.deque()
    q.append(root)

    while q:
        level = []
        for i in range(len(q)):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
        if level:
            res.append(level)
    
    return res


# TESTS:
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(levelOrder(root)) # [[3], [9, 20], [15, 7]]


root = None
print(levelOrder(root)) # []


root = TreeNode(1)
print(levelOrder(root)) # [[1]]


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(4)
print(levelOrder(root)) # [[1], [2], [3], [4]]


root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)
print(levelOrder(root)) # [[1], [2], [3], [4]]


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print(levelOrder(root)) # [[1], [2,3], [4,5,6,7]


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.right = TreeNode(7)
root.right.left = TreeNode(13)
root.right.right = TreeNode(20)
root.right.right.left = TreeNode(18)
print(levelOrder(root)) # [[10], [5,15], [7,13,20], [18]]