# Given two sorted linked lists (l1 and l2), return the head of the merged and sorted linked list

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def merge_lists(l1, l2):
    dummy = Node(None)
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    
    if l1:
        tail.next = l1
    if l2:
        tail.next = l2
    
    return dummy.next

# Helper function to convert a list into a linked list
def create_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head

# Helper function to print a linked list as a list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test cases
test_cases = [
    # Case 1: Merging two non-empty sorted lists
    ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
    
    # Case 2: One list is empty
    ([1, 2, 3], [], [1, 2, 3]),
    ([], [4, 5, 6], [4, 5, 6]),

    # Case 3: Both lists are empty
    ([], [], []),

    # Case 4: Lists with duplicate elements
    ([1, 2, 2, 3], [2, 3, 4], [1, 2, 2, 2, 3, 3, 4]),

    # Case 5: Lists of different lengths
    ([1, 5], [2, 3, 4, 6, 7], [1, 2, 3, 4, 5, 6, 7]),

    # Case 6: One list has all smaller elements
    ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
    ([4, 5, 6], [1, 2, 3], [1, 2, 3, 4, 5, 6]),
]

# Run test cases
for i, (l1_vals, l2_vals, expected) in enumerate(test_cases, 1):
    l1 = create_linked_list(l1_vals)
    l2 = create_linked_list(l2_vals)
    merged_head = merge_lists(l1, l2)
    result = linked_list_to_list(merged_head)
    print(f"Test Case {i}: {'Pass' if result == expected else 'Fail'} - Output: {result}, Expected: {expected}")