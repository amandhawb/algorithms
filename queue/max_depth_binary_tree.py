class TreeNode:
    def __init__(self, val, right, left):
        self.val = val
        self.right = None
        self.left = None

# UMPIRE

# Understand:
# I will receive the root of a binary tree and I need to return the depth of this tree
# 1) Can the root be null? Yes, for that return 0

# Match:
# I need to decide how I will traverse it. 
# BFS and DFS would work, but DFS is more commonly used for this problem because it naturally explores each path to its fullest depth before backtracking.
# And the method I will chose the postorder because I explore both left and right subtrees first and then process the root itself.

# Plan:
# There are two ways of solve it.
# 1) Recursive:
# Recursivelly I will call the maxDepth method to the right and left children and return the max between them + 1, so everytime I have one more node, I will call the maxDepth to its left and right child, but I will also add a plus one so I keep track of the level
# 2) Iterative:
# For the iterative I can either use BFS or DFS. I will do both.
# 2.1) BFS
# Using a queue to keep track and traverse all the root's children, as far as I have values in the queue, I will pop it and add its children to the queue. Also I need a leval variable to keep track of the level that I am and return this level in the end.
# 2.2) DFS
# Using a stack to simulate the recursive method, I will keep track of the node's value and its depth. After that I will traverse the stack and pop the elements, if the popped element is not null, I want to add it to the stack with a depth + 1. Inside this while loop I will update the result variable with the max between the result itself and the depth
class Solution:
    def maxDepthRecursive(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepthRecursive(root.right), self.maxDepthRecursive(root.left))
    
    def maxDepthIterativeBFS(self, root):
        if not root:
            return 0
        
        level = 0
        q = [root]

        while q:
            for _ in range(len(q)):
                node = q.pop(0)
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
            level += 1
        return level
                
    def maxDepthIterativeDFS(self, root):
        if not root:
            return 0

        stack = [[root, 1]]
        result = 1

        while stack:
            val, depth = stack.pop()
            if val.right:
                stack.append([val.right, depth + 1])
            if val.left:
                stack.append([val.left, depth + 1])
            result = max(result, depth)
        
        return result


    
