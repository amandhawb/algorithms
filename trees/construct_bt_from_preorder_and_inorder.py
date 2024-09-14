# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# example:
# INPUT: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# OUTPUT: 3
#        / \
#       9   20
#          /  \
#         15   7

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = buildTree(preorder[1: mid +1], inorder[:mid])
    root.right = buildTree(preorder[mid +1 :], inorder[mid +1 :])

    return root


# TEST
from collections import deque
def print_level_order(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
root = buildTree(preorder, inorder)
print_level_order(root)
