# implement a min heap

class MinHeap:
    def __init__(self, capacity):
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0

    def getParentIndex(self, index):
        return (index - 1) // 2
    
    def getLeftChildIndex(self, index):
        return 2 * index + 1
    
    def getRightChildIndex(self, index):
        return 2 * index + 2
    
    def hasParent(self, index):
        return self.getParentIndex(index) >= 0
    
    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size
    
    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size
    
    def parent(self, index):
        return self.storage[self.getParentIndex(index)]
    
    def leftChild(self, index):
        return self.storage[self.getLeftChildIndex(index)]
    
    def rightChild(self, index):
        return self.storage[self.getRightChildIndex(index)]
    
    def isFull(self):
        return self.capacity == self.size
    
    def swap(self, index1, index2):
        self.storage[index1], self.storage[index2] = self.storage[2], self.storage[1]

    def heapifyUp(self):
        index = self.size -1
        while(self.hasParent(index) and self.parent(index) > self.storage[index]):
            self.swap(self.getParentIndex(index), index)
            index = self.getParentIndex(index)

    def insert(self, data):
        if(self.isFull()):
            raise('Heap is full!')
        self.storage[self.size] = data
        self.size += 1
        self.heapifyUp()

    def heapifyDown(self):
        index = 0
        while(self.hasLeftChild(index)):
            smallestChildIndex = self.getLeftChildIndex(index)
            if(self.hasRightChild(index) and self.rightChild(index) < self.leftChild(index)):
                smallestChildIndex = self.rightChild(index)
            if(self.storage[index] < self.storage[smallestChildIndex]):
                break
            else:
                self.swap(index, smallestChildIndex)
            index = smallestChildIndex

    def removeMin(self):
        if(self.size == 0):
            raise('Empty heap!')
        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.heapifyDown()
        return data
    