# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
# Return the number  of good nodes in the binary tree

def good_nodes(root):
    def dfs(node, max_val):
        if not node:
            return 0
        
        count = 1 if node.val >= max_val else 0

        max_val = max(max_val, node.val)

        count += dfs(node.left, max_val)
        count += dfs(node.right, max_val)

        return count
    
    return dfs(root, float('-inf'))