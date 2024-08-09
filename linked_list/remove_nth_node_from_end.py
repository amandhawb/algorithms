# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Constraints
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def remove_nth_from_end(head, n):
    temp_head = Node(0)
    temp_head.next = head

    faster_pnt = temp_head
    slower_pnt = temp_head

    counter = 0

    while counter < n:
        faster_pnt = faster_pnt.next
        counter += 1

    while faster_pnt.next != None:
        slower_pnt = slower_pnt.next
        faster_pnt = faster_pnt.next
    
    slower_pnt.next = slower_pnt.next.next

    return temp_head.next


# Tests:
def create_linked_list(values):
    head = None
    tail = None

    for val in values:
        if head is None:
            head = Node(val)
            tail = head
        else:
            tail.next = Node(val)
            tail = tail.next
    return head

def Print(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

print('TEST 1')
linked_list = create_linked_list([1,2,3,4,5])
Print(linked_list)
new_head = remove_nth_from_end(linked_list, 2)
Print(new_head)
print('--------------------')

print('TEST 2')
linked_list = create_linked_list([1,2])
Print(linked_list)
new_head = remove_nth_from_end(linked_list, 1)
Print(new_head)
print('--------------------')

print('TEST 3')
linked_list = create_linked_list([1])
Print(linked_list)
new_head = remove_nth_from_end(linked_list, 1)
Print(new_head)
print('--------------------')

print('TEST 3')
linked_list = create_linked_list([1])
Print(linked_list)
new_head = remove_nth_from_end(linked_list, 1)
Print(new_head)
print('--------------------')

print('TEST 4')
linked_list = create_linked_list([1,2,3,4,5])
Print(linked_list)
new_head = remove_nth_from_end(linked_list, 5)
Print(new_head)
print('--------------------')
