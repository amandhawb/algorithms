# SORTED:

# Given a linked list where the elements are sorted in ascending order, write a function to remove duplicate elements from the list. 
# The function should modify the original linked list in-place (without creating a new list).

# EXAMPLE:
# Input List: 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 5 (sorted)
# Output List: 1 -> 2 -> 3 -> 4 -> 5 (duplicates removed)

# QUESTIONS:
# The linked list contains only numbers? Yes
# Can the list be empty? Yes
# What should I return if it is empty? Return None
# What is the type of linked list? Single, double, or circular? Single
# Will always have a duplicated value? No
# What should I return when there is no duplicated value? The list itself

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def remove_duplicated(self):
        if self.head is None or self.head.next is None:
            return None
        
        current = self.head
        prev = None

        while current:
            if prev and prev.data == current.data:
                current = current.next
                prev.next = current

            else:
                prev = current
                current = current.next


linked_list = LinkedList()
linked_list.head = Node(1)
linked_list.head.next = Node(1)
linked_list.head.next.next = Node(2)
linked_list.head.next.next.next = Node(3)
linked_list.head.next.next.next.next = Node(3)
linked_list.head.next.next.next.next.next = Node(4)
linked_list.head.next.next.next.next.next.next = Node(5)


print('Original List:')
current = linked_list.head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

linked_list.remove_duplicated()

print("\nNew List:")
current = linked_list.head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")


