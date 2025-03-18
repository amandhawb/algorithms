# create a function that receives the head of a linked list and a value and returns the number of nodes in the linked list with the value val

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def count_nodes_with_value(head, val):
    curr = head
    cnt = 0

    while curr:
        if curr.data == val:
            cnt += 1
        curr = curr.next
    
    return cnt


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

# Test Case 1: Value appears multiple times in the list
head = create_linked_list([1, 2, 3, 2, 4, 2, 5])
assert count_nodes_with_value(head, 2) == 3, "Test Case 1 Failed"

# Test Case 2: Value appears only once
head = create_linked_list([1, 2, 3, 4, 5])
assert count_nodes_with_value(head, 3) == 1, "Test Case 2 Failed"

# Test Case 3: Value does not appear in the list
head = create_linked_list([1, 2, 3, 4, 5])
assert count_nodes_with_value(head, 6) == 0, "Test Case 3 Failed"

# Test Case 4: All nodes contain the target value
head = create_linked_list([7, 7, 7, 7, 7])
assert count_nodes_with_value(head, 7) == 5, "Test Case 4 Failed"

# Test Case 5: Empty list
head = None
assert count_nodes_with_value(head, 1) == 0, "Test Case 5 Failed"

# Test Case 6: Only one node and it matches the value
head = create_linked_list([9])
assert count_nodes_with_value(head, 9) == 1, "Test Case 6 Failed"

# Test Case 7: Only one node and it does not match the value
head = create_linked_list([10])
assert count_nodes_with_value(head, 5) == 0, "Test Case 7 Failed"

print("All test cases passed!")
