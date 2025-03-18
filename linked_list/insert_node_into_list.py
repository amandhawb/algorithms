# implement the function insert that inserts a new node with a given value at a specific position in the linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def insert(head, value, position):
    new_node = Node(value)
    
    if position == 0:
        new_node.next = head
        return new_node

    curr = head
    idx = 0

    while curr:
        if idx == position -1:
            new_node.next = curr.next
            curr.next = new_node
            break
        idx += 1
        curr = curr.next
    
    return head


# Helper function to convert linked list to Python list for easy validation
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.value)
        head = head.next
    return result

# Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    curr = head
    for value in values[1:]:
        curr.next = Node(value)
        curr = curr.next
    return head

# Test Case 1: Insert at the beginning
head = create_linked_list([2, 3, 4])
head = insert(head, 1, 0)
assert linked_list_to_list(head) == [1, 2, 3, 4], "Test Case 1 Failed"

# Test Case 2: Insert in the middle
head = create_linked_list([1, 2, 4])
head = insert(head, 3, 2)
assert linked_list_to_list(head) == [1, 2, 3, 4], "Test Case 2 Failed"

# Test Case 3: Insert at the end
head = create_linked_list([1, 2, 3])
head = insert(head, 4, 3)
assert linked_list_to_list(head) == [1, 2, 3, 4], "Test Case 3 Failed"

# Test Case 4: Insert into an empty list (should become the only node)
head = None
head = insert(head, 10, 0)
assert linked_list_to_list(head) == [10], "Test Case 4 Failed"

# Test Case 5: Insert at an out-of-bounds position (should append to the end)
head = create_linked_list([1, 2])
head = insert(head, 3, 5)  # Since position is out of bounds, it won't be inserted
assert linked_list_to_list(head) == [1, 2], "Test Case 5 Failed"

print("All test cases passed!")
