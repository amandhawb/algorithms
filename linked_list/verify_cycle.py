# A linked list is said to contain a cycle if any node is visited more than once while traversing the list. 
# Given a pointer to the head of a linked list, determine if it contains a cycle. If it does, return 1. Otherwise, return 0.

class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None

# time = O(n) --> traversing the whole list once
# space = O(n) --> hash_set has the same size as the list
def verify_cycle(head):
    hash_set = set()
    curr = head

    while curr:
        if curr in hash_set:
            return 1
        hash_set.add(curr)
        curr = curr.next
    return 0

# print list
def print_linked_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

# TEST 1
linked_list_1 = LinkedList(1)
linked_list_1.next = LinkedList(2)
linked_list_1.next.next = LinkedList(3)
print_linked_list(linked_list_1)
print(verify_cycle(linked_list_1)) # 0

# TEST 1
linked_list_2 = LinkedList(1)
linked_list_2.next = LinkedList(2)
linked_list_2.next.next = LinkedList(3)
linked_list_2.next.next.next = linked_list_2
# print_linked_list(linked_list_2) --> not printing because it never ends
print(verify_cycle(linked_list_2)) # 1