class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
def reverse_linked_list_iterative(head):
    prev = None
    current = head

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    
    return prev

def Printer(head):
    while head:
        print(head.val, end= " -> ")
        head = head.next
    print("None")

linked_list = Node(1)
linked_list.next = Node(2)
linked_list.next.next = Node(3)
linked_list.next.next.next = Node(4)
linked_list.next.next.next.next = Node(5)

Printer(linked_list)

Printer(reverse_linked_list_iterative(linked_list))
