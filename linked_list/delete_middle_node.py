# You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.
# The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def get_size_of_list(self, head):
        counter = 0
        while head:
            counter += 1
            head = head.next
        return counter

    def delete_middle(self, head):
        list_size = self.get_size_of_list(head)
        middle_of_list = list_size // 2

        counter = 0
        current = head
        while counter < middle_of_list -1:
            current = current.next
            counter += 1
        current.next = current.next.next

        return head
    
head = Node(1, Node(3, Node(4, Node(7, Node(1, Node(2, Node(6)))))))

solution = Solution()
result = solution.delete_middle(head)

while result:
    print(result.val, end=' -> ')
    result = result.next
print('None')
