# https://leetcode.com/problems/partition-list/description/

# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
# You should preserve the original relative order of the nodes in each of the two partitions.

# Example:
# input = head = [1,4,3,2,5,2], x = 3
# output = [1,2,2,4,3,5]

# Pseudocode: 
# I will start creating two empty lists (right and left) 
# The right list will hold all the elements in the head that are greater or equal to x
# The left list will hold all the elements in the head that are smaller than x
# To make it work, I need to keep track of the tail of each list, so I can append the correct value on it
# In the end, I need to append the first element on the right list to the tail of the left list
# And without changing, the right tail would have the next node set to the one that was on the original list (using the example, the number 5 would hold the pointer to 2)
# So because of that I need to point the next element on the right tail to be null, and then return the left list that contains all the elements

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int ) -> ListNode:
        left, right = ListNode(), ListNode()
        tail_left, tail_right = left, right

        while head:
            if head.val >= x:
                tail_right.next = head
                tail_right = tail_right.next
            else:
                tail_left.next = head
                tail_left = tail_left.next
            
            head = head.next
        
        tail_left.next = right.next # right.next due to helper node
        tail_right.next = None

        return left.next


# TEST

def create_linked_list(values):
    helper = ListNode()
    current = helper
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return helper.next

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# test 1
head1 = create_linked_list([1,4,3,2,5,2])
x1 = 3
result = Solution().partition(head1, x1)
print(linked_list_to_list(result)) # [1,2,2,4,3,5]

# test 2
head2 = create_linked_list([1,2, 2])
x2 = 3
result = Solution().partition(head2, x2)
print(linked_list_to_list(result)) # [1,2,2]
