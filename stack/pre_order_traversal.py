# given the root of the binary tree, return the preorder traversal of its nodes' values

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# recursive:
def pre_order_traversal(root):
    if root is None:
        return []
    
    return [root.val] + pre_order_traversal(root.left) + pre_order_traversal(root.right)

# iterative:
def pre_order_traversal_iterative(root):
    if root is None:
        return []
    
    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.val)

        if node.right:
            # push right child first on the stack so that left child will be processed first
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        
    return result