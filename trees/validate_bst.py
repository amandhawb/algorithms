# Write a function that takes in a potentially invalid Binary Search Tree (BST) and returns a boolean representing whether the BST is valid.
# Each BST node has an integer value, a left child node, and a right child node. A node is said to be a valid BST node if and only if it satisfes the BST property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; and its children nodes are either valid
# BST nodes themselves or None / null.
# A BST is valid if and only if all of its nodes are valid BST nodes.

class BST:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

# iterative approach
def validate_BST(tree):
    if not tree:
        return True

    recursive_stack = [ (tree, float('-inf'), float('inf')) ]

    while len(recursive_stack):
        node, min_value, max_value = recursive_stack.pop()

        if node is None:
            continue

        if node.value < min_value or node.value >= max_value:
            return False
        
        recursive_stack.append((node.right, node.value, max_value))
        recursive_stack.append((node.left, min_value, node.value))
    return True


# TEST 1
root1 = BST(10)
root1.left = BST(5)
root1.right = BST(15)
root1.right.right = BST(20)
root1.left.right = BST(7)
root1.left.left = BST(3)
print(validate_BST(root1)) # True

# TEST 2
root2 = BST(10)
root2.left = BST(5)
root2.right = BST(15)
root2.left.right = BST(10)
print(validate_BST(root2)) # False

# TEST 3
root3 = BST(10)
root3.right = BST(15)
root3.left = BST(5)
root3.right.right = BST(22)
root3.right.left = BST(13)
root3.right.left.right = BST(14)
root3.left.right = BST(5)
root3.left.left = BST(2)
root3.left.left.left = BST(1)
print(validate_BST(root3)) # True


