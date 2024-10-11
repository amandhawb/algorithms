# In this challenge, you must first implement a queue using two stacks. Then process q queries, where each query is one of the following 3 types:
# 1: Enqueue element x into the end of the queue.
# 2: Dequeue the element at the front of the queue.
# 3: Print the element at the front of the queue.
# https://www.hackerrank.com/challenges/queue-using-two-stacks/problem

class MyQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.empty():
            return self.queue.pop(0)
        return None
    
    def empty(self):
        return len(self.queue) == 0
    
    def print_first_element(self):
        print(self.queue[0])
    
n = int(input())
queue = MyQueue()

for _ in range(n):
    query = input().split()
    if query[0] == '1':
        queue.enqueue(query[1])
    elif query[0] == '2':
        queue.dequeue()
    elif query[0] == '3':
        queue.print_first_element()
