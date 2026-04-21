# Implement a queue using two stacks

# idea:
# use 2 stacks. in_stack for enqueue operations, out_stack for dequeue and peek operations

# One stack stores newly added elements, and the other stack serves elements in queue order. For enqueue, I push onto the first stack. For dequeue, if the second stack is empty, I move all elements from the first stack into the second stack, which reverses the order and makes the oldest element available on top. Then I pop from the second stack. 

class QueueUsingStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, value):
        self.in_stack.append(value)

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("dequeue from empty queue")

        if not self.out_stack:
            self.transfer()
        
        return self.out_stack.pop()
    
    def peek(self):
        if self.isEmpty():
            raise IndexError("peek from empty queue")
    
        if not self.out_stack:
            self.transfer()

        return self.out_stack[-1]
    
    def isEmpty(self):
        return len(self.in_stack) == 0 and len(self.out_stack) == 0
    
    def transfer(self):
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())