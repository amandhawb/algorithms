# basic implementation of a queue:

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item) # add to the end
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0) # remove and return the first item (FIFO)
        return None # if it is empty
    
    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)