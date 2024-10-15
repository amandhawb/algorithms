# https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def preorder(self, node):
        values = []
        if node is not None:
            values.append(node.val)
            values.extend(self.preorder(node.left))
            values.extend(self.preorder(node.right))
        return values

    def insert(self, val):
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
        self.insert_recursivaly(self.root, new_node)
    
    def insert_recursivaly(self, curr_node, new_node):
        if curr_node.val < new_node.val:
            if curr_node.right is None:
                curr_node.right = new_node
            else:
                self.insert_recursivaly(curr_node.right, new_node)
        elif curr_node.val > new_node.val:
            if curr_node.left is None:
                curr_node.left = new_node
            else:
                self.insert_recursivaly(curr_node.left, new_node)

# TEST
bst = BinarySearchTree()
bst.insert(4)
bst.insert(2)
bst.insert(6)
bst.insert(1)
bst.insert(3)
bst.insert(5)
bst.insert(7)
bst.insert(0)
print(bst.preorder(bst.root)) # 4 2 1 3 6 5 7