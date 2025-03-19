# Given the head of a linked list and an integer val, remove all the nodes of the linked list where listNode.val == val. Return the modified list

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None



# None -> 1 -> 2 -> 3
# 
def remove_value(head, val):
    dummy = Node(None)
    dummy.next = head
    prev, curr = dummy, head

    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    
    return dummy.next
    

# Helper function to convert linked list to Python list for easy testing
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    curr = head
    for val in values[1:]:
        curr.next = Node(val)
        curr = curr.next
    return head

# Test Cases
test_cases = [
    ([1, 2, 6, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5]),  # Remove multiple instances
    ([6, 1, 2, 3], 6, [1, 2, 3]),  # Remove head node
    ([7, 7, 7, 7], 7, []),  # Remove all nodes
    ([1, 2, 3, 4, 5], 6, [1, 2, 3, 4, 5]),  # Value not in list
    ([], 1, []),  # Empty list
    ([1, 2, 3], 3, [1, 2]),  # Remove last node
]

# Run tests
for i, (lst, val, expected) in enumerate(test_cases, 1):
    head = create_linked_list(lst)
    new_head = remove_value(head, val)
    result = linked_list_to_list(new_head)
    print(f"Test {i}: {'PASSED' if result == expected else 'FAILED'} - Expected {expected}, Got {result}")