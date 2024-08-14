# Given a linked list of integers, return a linked list containing only nodes having odd integers in their node->data field
# Example: 
# linked_head = 1 -> 4 -> 7
# output = 1 -> 7

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def delete_even(head):
    dummy = Node(0)
    tail = dummy

    current = head
    while current:
        if current.val % 2 != 0:
            new_node = Node(current.val)
            tail.next = new_node
            tail = tail.next
        current = current.next
    return dummy.next

# test
head = Node(1, Node(4, Node(7)))
result = delete_even(head)
while result:
    print(result.val, end=' -> ')
    result = result.next
print('None')

    