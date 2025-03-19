# Given the head of a singly linked list, return True if the node values form a palindrome and False otherwise

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def is_palindrome(head):
    # find the middle of the list
    fast, slow = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # slow is the middle of the list


    # reverse from the middle to the end
    # 1->2->3->4->5->6 ----- 4->5->6 (6->5->4)
    prev = None
    while slow:
        tmp = slow.next
        slow.next = prev
        prev = slow
        slow = tmp

    # checks
    first, second = head, prev
    while second:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next
    
    return True

# Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head

# Test Cases
test_cases = [
    ([1, 2, 2, 1], True),  # Even length palindrome
    ([1, 2, 3, 2, 1], True),  # Odd length palindrome
    ([1, 2, 3, 4, 5], False),  # Not a palindrome
    ([1, 2, 3, 3, 2, 1], True),  # Palindrome with even length
    ([1, 2], False),  # Small non-palindrome case
    ([1, 1], True),  # Two identical elements
    ([1], True),  # Single node case
    ([], True),  # Empty list is always a palindrome
]

# Run Test Cases
for i, (values, expected) in enumerate(test_cases, 1):
    head = create_linked_list(values)
    result = is_palindrome(head)
    print(f"Test Case {i}: {'Pass' if result == expected else 'Fail'} - Output: {result}, Expected: {expected}")
