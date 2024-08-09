# You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.
# Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def list_to_binary_tree(l):
  if not l: return None

  t = TreeNode(l.pop(0))
  queue = [t]

  while queue:
    node = queue.pop(0)

    if l:
      left_val = l.pop(0)
      if left_val != None:
        node.left = TreeNode(left_val)
        queue.append(node.left)

    if l:
      right_val = l.pop(0)
      if right_val != None:
        node.right = TreeNode(right_val)
        queue.append(node.right)

  return t

def insert(root, val):
    print('ROOT', root.val)
    if not root:
        return TreeNode(val)
    
    if val > root.val:
        root.right = insert(root.right, val)
    else:
        root.left = insert(root.left, val)
    
    print(root.val)
    return root


print(insert(list_to_binary_tree([3,1,5]), 6))