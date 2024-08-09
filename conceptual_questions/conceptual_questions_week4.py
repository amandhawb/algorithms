# FIRST QUESTION:

# Question description
# Let’s say we want to remove duplicates from a linked list and we come up with two solutions:
# Solution #1: Iterate through the linked list, adding each element to a hash set. When we encounter a
# duplicate element, remove the element and keep iterating

# Solution #2: Iterate through the linked list with two pointers: current (which iterates through the
# linked list) and runner (which checks the rest of the list for duplicates).

# Which of the following statements is true?

# Solution #1 is more time-efficient but less space-efficient. --> RIGHT
# Solution #1 is less time-efficient and less space-efficient.
# Solution #2 is more time-efficient but less space-efficient.
# Solution #2 is less time-efficient and less space-efficient.

# __________________________________________________________________________________________________________________________________________

# SECOND QUESTION:

# The code below partitions a linked list such that: (1) all nodes less than x come before nodes greater than
# or equal to x (2) the original order of the nodes is preserved in each of the two partitions. Example:

# Input: head = 1 -> 4 -> 3 -> 2 -> 5 -> 2, x = 3
# Output: 1 -> 2 -> 2 -> 4 -> 3 -> 5

# Definition for singly-linked list
#
class LinkedListNode:
  def _init_(self, node_data):
      self.data = node_data
      self.next = None

def partition(head, x):
    beforeHead = before = LinkedListNode(0)
    afterHead = after = LinkedListNode(0)
    while head != None:
        if head.val < x:
            before.next = head
            before = before.next
        else:
            after.next = head
            after = after.next

        head = head.next
        before.next = afterHead.next
        after.next = None

        return beforeHead.next

# How does this code accomplish the stated problem?

# a) It takes two passes through the linked list: the first pass goes through and stores values
# less than x in a separate linked list, while the second pass goes through and stores the
# remaining values (which are greater than or equal to x) in the same separate linked list. It
# then returns the separate linked list as the result.

# b) It takes two pointers and creates two linked lists (one with lesser elements and the other
# with elements greater than or equal to x), and then returns the combination of these two
# lists as the result. --> RIGHT

# c) It takes two pointers: one that points at the head of the linked list and one at the tail. As
# both pointers advance towards the middle of the list, the values encountered are either
# prepended (if less than x) or appended (if greater than or equal to x) to a separate linked
# list, and then returns that separate linked list as the result.

# d) This code does not accomplish the stated problem and has a major bug.

# __________________________________________________________________________________________________________________________________________

# THIRD QUESTION

# You’re given two sentences A and B. (A sentence is a string of space separated words. Each word consists
# only of lowercase letters.) A word is uncommon if it appears exactly once in one of the sentences and
# does not appear in the other sentence. The function below returns a list of all uncommon words. Since
# every uncommon word occurs exactly once in total, this function counts the number of occurrences of
# every word, and then returns the words that occur exactly once.

def uncommonFromSentences(a, b):
    count = {}
    ans = []

    for word in a.split(" "):
        count[word] = count.get(word, 0) + 1

    for word in b.split(" "):
        count[word] = count.get(word, 0) + 1
    
    for word, val in count.items():
        if (val == 1):
            ans.append(word)

    return ans

# What is the time and space complexity of this algorithm?
# a) O(N) time and O(N^2) space
# b) O(N^2) time and O(N^2) space
# c) O(1) time and O(N) space
# d) O(N) time and O(N) space --> RIGHT

# __________________________________________________________________________________________________________________________________________

# FOURTH QUESTION:
# The goal of the function below is to take a non-empty, singly linked list with head node head and return a
# middle node of linked list. (If there are two middle nodes, it should return the second middle node.) It
# uses the fast-slow pointer strategy to traverse the list with a slow pointer and a fast pointer that moves
# twice as fast such that when fast reaches the end of the list, slow must be in the middle.

def middleNode(head):
    slow = head
    fast = head
    while (fast != None and fast.next != None):
        slow = slow.next
        # MISSING LINE OF CODE
    return slow

# The code is almost complete, but it’s missing one line. What code needs to be filled in on the missing line
# for this function to work as intended?
# 1. fast = fast.next.next; --> RIGHT
# 2. fast = fast.next;
# 3. fast = slow;
# 4. fast = slow.next;
