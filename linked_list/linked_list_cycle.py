# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def create_linked_list(values):
    node = Node(None)
    if values:
        for val in reversed(values):
            node.next = Node(val, node.next)
    return node.next


def has_cycle(head: Node) -> bool:
    slower = faster = head
    first_pass = True

    while first_pass == True or slower != faster:
        if first_pass : first_pass = False

        if faster.next == None or faster.next.next == None:
            return False
        else:
            slower = slower.next
            faster = faster.next.next
    return True


