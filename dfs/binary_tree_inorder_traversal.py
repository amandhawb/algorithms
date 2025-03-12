# Given the root of a binary tree, return the inorder traversal of its nodes' values.
# example:
# input = [1,null,2,3]
#           1 
#            \     
#             2
#            /
#           3
# output = [1,3,2]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# RECURSIVE:
def inorderTraversalRecursive(root):
    res = []
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        res.append(node.val)
        inorder(node.right)
    inorder(root)
    return res

# ITERATIVE:
def inorderTraversalIterative(root):
    res = []
    stack = []
    cur = root

    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right
    
    return res

# TESTS:
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(inorderTraversalRecursive(root)) # [1,3,2]
print(inorderTraversalIterative(root)) # [1,3,2]


root = None
print(inorderTraversalRecursive(root)) # []
print(inorderTraversalIterative(root)) # []


root = TreeNode(5)
print(inorderTraversalRecursive(root)) # [5]
print(inorderTraversalIterative(root)) # [5]


root = TreeNode(4)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.left.left = TreeNode(1)
print(inorderTraversalRecursive(root)) # [1,2,3,4]
print(inorderTraversalIterative(root)) # [1,2,3,4]


root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)
print(inorderTraversalRecursive(root)) # [1,2,3,4]
print(inorderTraversalIterative(root)) # [1,2,3,4]


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print(inorderTraversalRecursive(root)) #[4,2,5,1,6,3,7]
print(inorderTraversalIterative(root)) #[4,2,5,1,6,3,7]


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.right = TreeNode(20)
print(inorderTraversalRecursive(root)) # [2,5,7,10,15,20]
print(inorderTraversalIterative(root)) # [2,5,7,10,15,20]
