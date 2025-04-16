# You are given an unweighted graph represented as an adjacency list, and two nodes: a start node and a target node.
# Write a function that returns the minimum number of steps required to go from the start node to the target node. If there is no path between them, return -1.


# EXAMPLE:
# graph = {
#     "A" : ["B", "C"],
#     "B" : ["D"],
#     "C": ["E"],
#     "D": ["F"],
#     "E": ["F"],
#     "F": []
# }
# start = "A"
# target = "F"

# output = 3

from collections import deque

def shortest_path(graph, start, target):
    if start == target:
        return 0
    
    visited = set()
    queue = deque()

    queue.append((start, 0))
    visited.add(start)

    while queue:
        curr_node, steps = queue.popleft()
        
        if curr_node == target:
            return steps
        
        for neighbor in graph[curr_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, steps +1))

    return -1
        
# TESTS
graph1 = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": ["F"],
    "E": ["F"],
    "F": []
}

print(shortest_path(graph1, "A", "F"))  # Output: 3

graph2 = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}
print(shortest_path(graph2, "A", "D"))  # Output: 2

graph3 = {
    "A": ["B"],
    "B": [],
    "C": ["D"],
    "D": []
}
print(shortest_path(graph3, "A", "D"))  # Output: -1
