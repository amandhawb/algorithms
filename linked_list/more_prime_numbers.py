# you are given two heads of two singly linked lists, head_a and head_b. Your task is to determine which list has more prime numbers. The function should return the head of the list that has the greater count of prime numbers. if both lists have the same number of prime numbers, return head_a

class Node:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def more_prime_numbers(head_a, head_b):
    counter_a = 0
    counter_b = 0

    curr_a = head_a
    while curr_a:
        if is_prime(curr_a.data):
            counter_a += 1
        curr_a = curr_a.next
    
    curr_b = head_b
    while curr_b:
        if is_prime(curr_b.data):
            counter_b += 1
        curr_b = curr_b.next
    
    if counter_b > counter_a:
        return head_b
    else:
        return head_a
    
    # Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    curr = head
    for value in values[1:]:
        curr.next = Node(value)
        curr = curr.next
    return head

# Test Case 1: List A has more prime numbers than List B
head_a = create_linked_list([2, 3, 4, 5, 6])  # Primes: [2, 3, 5] (count: 3)
head_b = create_linked_list([1, 4, 6, 8])     # Primes: [] (count: 0)
assert more_prime_numbers(head_a, head_b) == head_a, "Test Case 1 Failed"

# Test Case 2: List B has more prime numbers than List A
head_a = create_linked_list([4, 6, 8])       # Primes: [] (count: 0)
head_b = create_linked_list([2, 3, 5])       # Primes: [2, 3, 5] (count: 3)
assert more_prime_numbers(head_a, head_b) == head_b, "Test Case 2 Failed"

# Test Case 3: Both lists have the same number of prime numbers
head_a = create_linked_list([2, 3, 6])       # Primes: [2, 3] (count: 2)
head_b = create_linked_list([5, 7, 9])       # Primes: [5, 7] (count: 2)
assert more_prime_numbers(head_a, head_b) == head_a, "Test Case 3 Failed"

# Test Case 4: One list is empty
head_a = create_linked_list([2, 3, 5])       # Primes: [2, 3, 5] (count: 3)
head_b = None                                # Empty list (count: 0)
assert more_prime_numbers(head_a, head_b) == head_a, "Test Case 4 Failed"

# Test Case 5: Both lists are empty
head_a = None
head_b = None
assert more_prime_numbers(head_a, head_b) == None, "Test Case 5 Failed"

# Test Case 6: No prime numbers in either list
head_a = create_linked_list([4, 6, 8])       # Primes: [] (count: 0)
head_b = create_linked_list([9, 10, 12])     # Primes: [] (count: 0)
assert more_prime_numbers(head_a, head_b) == head_a, "Test Case 6 Failed"

print("All test cases passed!")
