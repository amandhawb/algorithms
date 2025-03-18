# Write a function that creates a linked list from a list of numbers nums and returns the head of the linked list

class Node:
    def __init__(self, node_data):
        self.node_data = node_data
        self.next = None

def create_linked_list(values):
    head = Node(None)
    curr = head

    for value in values:
        curr.next = Node(value)
        curr = curr.next
    
    return head.next


# Helper function to convert linked list to Python list for easy testing
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.node_data)
        head = head.next
    return result

# Test Case 1: Regular case
nums = [1, 2, 3, 4, 5]
head = create_linked_list(nums)
print(linked_list_to_list(head))  # Expected: [1, 2, 3, 4, 5]

# Test Case 2: Single element
nums = [42]
head = create_linked_list(nums)
print(linked_list_to_list(head))  # Expected: [42]

# Test Case 3: Empty list
nums = []
head = create_linked_list(nums)
print(linked_list_to_list(head))  # Expected: []

# Test Case 4: List with negative numbers
nums = [-3, -1, -7, -10]
head = create_linked_list(nums)
print(linked_list_to_list(head))  # Expected: [-3, -1, -7, -10]

# Test Case 5: List with duplicate numbers
nums = [4, 4, 2, 2, 4, 4]
head = create_linked_list(nums)
print(linked_list_to_list(head))  # Expected: [4, 4, 2, 2, 4, 4]

# Test Case 6: List with zero
nums = [0, 1, 2, 3, 0, 4]
head = create_linked_list(nums)
print(linked_list_to_list(head))  # Expected: [0, 1, 2, 3, 0, 4]
