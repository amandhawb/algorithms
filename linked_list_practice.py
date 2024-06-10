class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # O(1) time complexity
    def insert_at_beginning(self, data):
        new_node =  Node(data)

        new_node.next = self.head

        self.head = new_node

    # O(n) time complexity
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node

linked_list = LinkedList()
linked_list.insert_at_beginning(5)
linked_list.insert_at_beginning(3)
linked_list.insert_at_beginning(1)
linked_list.insert_at_end(10)
linked_list.insert_at_end(20)

current_node = linked_list.head
while current_node:
    print(current_node.data)
    current_node = current_node.next