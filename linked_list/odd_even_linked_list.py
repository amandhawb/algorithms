# https://leetcode.com/problems/odd-even-linked-list/description/

# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
# The first node is considered odd, and the second node is even, and so on.
# Note that the relative order inside both the even and odd groups should remain as it was in the input.
# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

# EXAMPLE:
# input = 1 -> 2 -> 3 -> 4 -> 5
# output = 1 -> 3 -> 5 -> 2 -> 4
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def oddEvenList(self, head):
        if not head or not head.next or not head.next.next:
            return head
        
        even_head = head.next
        curr_odd = head
        curr_even = even_head

        while curr_odd.next and curr_even.next:
            curr_odd.next = curr_odd.next.next
            curr_even.next = curr_even.next.next
            curr_odd = curr_odd.next
            curr_even = curr_even.next
            
        curr_odd.next = even_head
        return head

# TEST
linked_list = Node(1)
linked_list.next = Node(2)
linked_list.next.next = Node(3)
linked_list.next.next.next = Node(4)
linked_list.next.next.next.next = Node(5)

# PRINT
def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

print("BEFORE:")
print_linked_list(linked_list)
solution = Solution()
new_list = solution.oddEvenList(linked_list)
print("AFTER:")
print_linked_list(new_list)