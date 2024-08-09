# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
# time = O(n) | space = O(1)
def middle_of_linked_list(head):
    # handle edge cases
    if head is None or head.next is None:
        return head

    slower = head
    faster = head

    while faster.next and faster.next.next:
        faster = faster.next.next
        slower = slower.next

    if faster.next:
        return slower.next
    else:
        return slower
    
def Print(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

linked_list = Node(1)
linked_list.next = Node(2)
linked_list.next.next = Node(3)
linked_list.next.next.next = Node(4)
linked_list.next.next.next.next = Node(5)
Print(linked_list)

Print(middle_of_linked_list(linked_list))
