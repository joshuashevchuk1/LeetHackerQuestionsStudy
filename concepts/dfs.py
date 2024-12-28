graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfs_recursive(graph, node, visited):
    if node not in visited: # a visited is important as it is an empty set for checking
        print(node, end=" ")
        visited.add(node) # once the node is added you can continue
        for neighbor in graph[node]: # the graph (set of array)
            dfs_recursive(graph, neighbor, visited) # didn't find what you are looking for, do it again.
            # Do it for every node


visited = set()
dfs_recursive(graph,'A',visited)
print("\n")
visited.clear()
dfs_recursive(graph,'B',visited)


# DFS is particularly useful in solving problems that require exploring
# all possible solutions (e.g., maze problems, permutations, and combinations).