# Given the pointer to the head node of a linked list and an integer to insert at a certain position, create a new node with the given integer as its data attribute, insert this node at the desired position and return the head node.

# A position of 0 indicates head, a position of 1 indicates one node away from the head and so on. The head pointer given may be null meaning that the initial list is empty.

# Example
# head refers to the first node in the list (1->2->3)
# data = 4
# position = 2
# Insert a node at position 2 with data=4. The new list is 1 -> 2 -> 4 -> 3

class SinglyLinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None

def insert_node_at_position(head, data, position):
    new_node = SinglyLinkedList(data)
    if position == 0:
        new_node.next = head
        return new_node
    
    curr = head
    counter = 0

    while curr:
        if counter == position -1:
            new_node.next = curr.next
            curr.next = new_node
            break
        counter += 1
        curr = curr.next
    
    return head

# print test
def print_linked_list(head):
    curr = head
    while curr:
        print(curr.val, end = "->")
        curr = curr.next
    print("None")

# TEST 1
linked_list = SinglyLinkedList(16)
linked_list.next = SinglyLinkedList(13)
linked_list.next.next = SinglyLinkedList(7)
print("ORIGINAL LIST:")
print_linked_list(linked_list)
print("NEW LIST:")
new_list = insert_node_at_position(linked_list, 1, 2)
print_linked_list(new_list)

# TEST 2
linked_list = SinglyLinkedList(10)
linked_list.next = SinglyLinkedList(24)
linked_list.next.next = SinglyLinkedList(35)
linked_list.next.next.next = SinglyLinkedList(355)
print("ORIGINAL LIST:")
print_linked_list(linked_list)
print("NEW LIST:")
new_list = insert_node_at_position(linked_list, 199, 0)
print_linked_list(new_list)