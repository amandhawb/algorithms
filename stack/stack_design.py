# design a stack using array

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.isEmpty():
            raise IndexError("pop from empty stack")
        self.items.pop()
    
    def peek(self):
        if self.isEmpty():
            raise IndexError("peek from empty stack")
        return self.items[-1]
    
    def isEmpty(self):
        return len(self.items) == 0
    

# design a stack using linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isEmpty():
            raise IndexError("pop from empty stack")
        value = self.top.value
        self.top = self.top.next
        return value
    
    def peek(self):
        if self.isEmpty():
            raise IndexError("peek from empty stack")
        return self.top.value
    
    def isEmpty(self):
        return self.top is None
