# Design your implementation of the doubly linked list.

# Implement the LinkedList class:

# int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
# void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
# void addAtTail(int val) Append a node of value val as the last element of the linked list.
# void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
# void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def addAtHead(self, val):
        new_node = Node(val)
        if self.head:
            second_node = self.head
            new_node.next = second_node
            second_node.prev = new_node
        self.head = new_node
        self.size += 1

    def addAtTail(self, val):
        if self.head is None:
            self.addAtHead(val)
        else:
            new_node = Node(val)
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr
            self.size += 1

    def get(self, index):
        if self.size == 0:
            return -1
        elif index < 0 or index >= self.size:
            return -1
        else:
            curr = self.head
            counter = 0
            while counter < index:
                curr = curr.next
                counter += 1
            return curr.val

    def addAtIndex(self, index, val):
        if index > self.size:
            return 
        
        if self.size == index:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            new_node = Node(val)
            curr = self.head
            counter = 0
            while counter < index -1:
                curr = curr.next
                counter += 1 
            new_node.next = curr.next
            curr.next = new_node
            self.size += 1

    def deleteAtIndex(self, index):
        if index >= self.size or index < 0:
            return
        
        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            counter = 0
            while counter < index - 1:
                curr = curr.next
                counter += 1
            curr.next = curr.next.next

        self.size -= 1


dll = LinkedList()
dll.addAtHead(2)
dll.addAtHead(1)
dll.addAtTail(3)
dll.addAtTail(4)
dll.addAtTail(5)
print(dll.get(3))
dll.addAtIndex(0, 0)
dll.deleteAtIndex(5)
print(dll.get(5))

curr = dll.head
print('\nsize = ', dll.size)
while curr:
    print(curr.val, end=" <-> ")
    curr = curr.next
print("None")
