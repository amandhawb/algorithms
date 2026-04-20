# Given the head of a 1-indexed singly linked list and two integers left and right where left <= right, reverse the nodes of the list from index left to index right inclusive and return the head of the modified list. Assume 1 <= left <= right <= n where n is the length of the list.

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_between(head, left, right):
    if not head or left == right:
        return head
    
    dummy = Node(0)
    dummy.next = head
    prev = dummy

    for _ in range(left - 1):
        prev = prev.next
    
    curr = prev.next
    next_node = None
    prev_sublist = prev

    for _ in range(right - left + 1):
        next_temp = curr.next
        curr.next = next_node
        next_node = curr
        curr = next_temp

    prev_sublist.next.next = curr
    prev_sublist.next = next_node

    return dummy.next
