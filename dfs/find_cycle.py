def find_cycle(edges):
    graph_size = len(edges)
    edges_hash_map = { i : [] for i in range(graph_size) }

    for row in range(graph_size):
        # The extend method in Python is used to add all the elements from an iterable (like a list) to the end of the list on which it is called. Unlike the append method, which adds its argument as a single element to the end of the list, extend adds each element of the iterable individually.
        edges_hash_map[row].extend(edges[row])
    
    already_seen = set()

    def dfs(node, recursive_stack):
        if node in recursive_stack:
            return True
        recursive_stack.append(node)
        already_seen.add(node)
        
        for children in edges_hash_map[node]:
            if dfs(children, recursive_stack):
                return True
        recursive_stack.pop()
        

    for edge in range(graph_size):
        if edge not in already_seen:
            if dfs(edge, []):
                return True
    return False


edge_input = [
    [1,3],
    [2,3,4],
    [0],
    [],
    [2,5],
    []
]

edge_input2 = [
    [1],
    [2],
    []
]

edge_input3 = [
    [1,2],
    [2],
    []
]

print(find_cycle(edge_input)) # true
print(find_cycle(edge_input2)) # false
print(find_cycle(edge_input3)) # false
