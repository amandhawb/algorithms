# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Example:
# input: list1 = [1,2,4] | list2 = [1,3,4]
# output: [1,1,2,3,4,4]

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
def mergeTwoLists(list1, list2):
    dummy = Node(0)
    current = dummy

    while list1 and list2:
        if list1.data < list2.data:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    if list1:
        current.next = list1
    if list2:
        current.next = list2

    return dummy.next

def printList(node, title):
    print(title)
    while node:
        print(node.data, end=" -> ")
        node = node.next
    print("None")

linked_list1 = LinkedList()
linked_list1.head = Node(1)
linked_list1.head.next = Node(2)
linked_list1.head.next.next = Node(4)

linked_list2 = LinkedList()
linked_list2.head = Node(1)
linked_list2.head.next = Node(3)
linked_list2.head.next.next = Node(4)


printList(linked_list1.head, 'list1')
printList(linked_list2.head, 'list2')

result = mergeTwoLists(linked_list1.head, linked_list2.head)

printList(result, 'result')






