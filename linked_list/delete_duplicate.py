# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def delete_duplicate(head):
    if not head:
        return None
    
    current_node = head
    faster = head.next

    while current_node.next != None:
        if current_node.val == faster.val:
            current_node.next = faster.next
            faster = faster.next
        else:
            current_node = current_node.next
            faster = faster.next
    return head

# TEST 1:
linkedList1 = Node(1)
linkedList1.next = Node(1)
linkedList1.next.next = Node(1)
linkedList1.next.next.next = Node(3)
linkedList1.next.next.next.next = Node(4)
linkedList1.next.next.next.next.next = Node(4)
linkedList1.next.next.next.next.next.next = Node(4)
linkedList1.next.next.next.next.next.next.next = Node(5)
linkedList1.next.next.next.next.next.next.next.next = Node(6)
linkedList1.next.next.next.next.next.next.next.next.next = Node(6)

print('Original list')
current = linkedList1
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")

delete_duplicate(linkedList1)

print('New list')
current = linkedList1
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")