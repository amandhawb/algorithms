# Given the root of a binary tree, return all root-to-leaf paths in any order.

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def list_to_binary_tree(l):
  if not l: return None

  t = Node(l.pop(0))
  queue = [t]

  while queue:
    node = queue.pop(0)

    if l:
      left_val = l.pop(0)
      if left_val != None:
        node.left = Node(left_val)
        queue.append(node.left)

    if l:
      right_val = l.pop(0)
      if right_val != None:
        node.right = Node(right_val)
        queue.append(node.right)

  return t

def explore_tree(root, all_paths, curr_path):
    if not root:
        return 
    
    curr_path += str(root.val)

    if root.left is None and root.right is None:
        all_paths.append(curr_path)
    else:
        curr_path += '->'
        explore_tree(root.left, all_paths, curr_path)
        explore_tree(root.right, all_paths, curr_path)

def find_paths(root):
    all_paths = []

    explore_tree(root, all_paths, '')

    return all_paths


def main():
  tests = [
    { 'input': [],                           'output': [] },
    { 'input': [1],                          'output': ['1'] },
    { 'input': [1, 2],                       'output': ['1->2'] },
    { 'input': [1, None, 3],                 'output': ['1->3'] },
    { 'input': [1, 2, 3],                    'output': ['1->2', '1->3'] },
    { 'input': [1, 2, 3, 4, 5],              'output': ['1->2->4', '1->2->5', '1->3'] },
    { 'input': [1, 2, 3, 4, 5, 6, 7],        'output': ['1->2->4', '1->2->5', '1->3->6', '1->3->7'] },
    { 'input': [1, None, 3, None, 7],        'output': ['1->3->7'] },
    { 'input': [1, 2, 3, None, None, 6, 7],  'output': ['1->2', '1->3->6', '1->3->7'] },
    { 'input': [1, 2, 3, None, 5],           'output': ['1->2->5', '1->3'] },
    { 'input': [1, 2, 3, None, 5, None, 2],  'output': ['1->2->5', '1->3->2'] },
  ]

  for i in range(len(tests)):
    print('Test', i+1, 'Pass:',
      find_paths(list_to_binary_tree(tests[i]['input'])) == tests[i]['output']
    )

main()
