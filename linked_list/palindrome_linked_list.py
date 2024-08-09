# Given the head of a singly linked list, return true if it is a palindrome (a sequence that reads the same forward and backward) or false otherwise.

# Constraints
# The number of nodes in the list is in the range [1, 10^5].
# 0 <= Node.val <= 9

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Time = O(n) | Space = O(n)
def is_palidrome_using_array(head):
    if head is None or head.next is None:
        return True

    current = head
    array = []

    while current:
        array.append(current.val)
        current = current.next
    
    left = 0
    right = len(array) -1

    while left < right:
        if array[left] != array[right]:
            return False
        else:
            left += 1
            right -= 1
    return True

# Time = O(n) | Space = O(1)
def is_palidrome_using_pointers(head):
    return


# Tests
def create_linked_list(values):
    head = None
    tail = None

    for value in values:
        if head is None:
            head = Node(value)
            tail = head
        else:
            tail.next = Node(value)
            tail = tail.next
        
    return head

# Using array
linked_list = create_linked_list([1,2,2])
linked_list2 = create_linked_list([1,2,2,1])
linked_list3 = create_linked_list([])
linked_list4 = create_linked_list([1])
linked_list5 = create_linked_list([1,2,3,4,5,5,4,3,2,1])
linked_list6 = create_linked_list([1,2])
linked_list7 = create_linked_list([1,2,1])

print(is_palidrome_using_array(linked_list))  # False
print(is_palidrome_using_array(linked_list2)) # True
print(is_palidrome_using_array(linked_list3)) # True
print(is_palidrome_using_array(linked_list4)) # True
print(is_palidrome_using_array(linked_list5)) # True
print(is_palidrome_using_array(linked_list6)) # False
print(is_palidrome_using_array(linked_list7)) # True

# Using pointers
