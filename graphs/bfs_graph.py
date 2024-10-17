# https://www.algoexpert.io/questions/breadth-first-search
# You're given a Node class that has a name and an array of optional together, nodes form an acyclic tree-like structure. children nodes. When put
# Implement the breadthFirstSearch method on the Node class, which takes in an empty array, traverses the tree using the Breadth-first Search approach (specifically navigating the tree from left to right), stores all of the nodes' names in the input array, and returns it.


# time = O(v + e) where v are the vertixes and e are the edges because I will traverse each of them
# space = O(v) where v is the vertixes because the array will cointain all the vertices (nodes) that are on the graph
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name
    
    def addChild(self, name):
        self.children.append(Node(name))
        return self
    
    def breadthFirstSearch(self, array):
        queue = [self]
        while queue:
            curr = queue.pop(0)
            array.append(curr.name)
            for child in curr.children:
                queue.append(child)
        return array

# TEST 1
root = Node('A')
root.addChild('B').addChild('C')
result = []
root.breadthFirstSearch(result)
print(result) # ['A', 'B', 'C']

# TEST 2
root2 = Node('A')
root2.addChild('B').addChild('C')
root2.children[0].addChild('D').addChild('E')
root2.children[1].addChild('F')
result2 = []
root2.breadthFirstSearch(result2)
print(result2) # ['A', 'B', 'C', 'D', 'E', 'F']

# TEST 3
root3 = Node('A')
root3.addChild('M').addChild('A')
root3.children[0].addChild('N').addChild('D')
root3.children[1].addChild('H').addChild('A')
result3 = []
root3.breadthFirstSearch(result3)
print(result3) # ['A', 'M', 'A', 'N', 'D', 'H', 'A']