# Design your implementation of the linked list. You can choose to use a singly linked list.
# A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
# If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

# Implement the MyLinkedList class:

# MyLinkedList() Initializes the MyLinkedList object.
# int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
# void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
# void addAtTail(int val) Append a node of value val as the last element of the linked list.
# void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
# void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def Print(self):
        curr = self.head
        while curr:
            print(curr.val, end = " -> ")
            curr = curr.next
        print("None")
        

    def get(self, index) -> int:
        if index >= 0 and index < self.size:
            counter = 0
            curr = self.head
            while counter < index:
                counter += 1
                curr = curr.next
            return curr.val
        else:
            return -1

    def addAtHead(self, val) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def addAtTail(self, val) -> None:
        if self.size == 0:
            self.addAtHead(val)
        else:
            new_node = Node(val)
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
            self.size += 1

    def addAtIndex(self, index, val) -> None:
        if index < 0 or index > self.size:
            return 
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else: 
            # index > 0 or index < self.size
            new_node = Node(val)
            curr = self.head
            counter = 0
            index = index - 1
            while counter < index:
                counter += 1
                curr = curr.next
            new_node.next = curr.next
            curr.next = new_node
            self.size += 1

    def deleteAtIndex(self, index) -> None:
        print('entrou')
        if index == 0:
            self.head = self.head.next
            self.size -= 1
        elif index > 0 and index < self.size:
            curr = self.head
            counter = 0
            index = index - 1
            while counter < index:
                counter += 1
                curr = curr.next
            curr.next = curr.next.next
            self.size -= 1
        else:
            return None

linked_list = MyLinkedList()
linked_list.addAtHead(1)
linked_list.addAtHead(2)
linked_list.addAtHead(3)
linked_list.addAtHead(4)
linked_list.Print()
linked_list.addAtTail(5)
linked_list.Print()
linked_list.addAtIndex(2, 10)
linked_list.Print()
print(linked_list.get(0))
linked_list.deleteAtIndex(3)
linked_list.Print()
linked_list.deleteAtIndex(0)
linked_list.Print()
