# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/

class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(root):
    curr, nxt = root, root.left if root else None

    while curr and nxt:
        curr.left.next = curr.right
        if curr.next:
            curr.right.next = curr.next.left
        curr = curr.next
        if not curr:
            curr = nxt
            nxt = curr.left
    return root
