from collections import defaultdict

def findTheCycle(graph):
    visited = set()  # Track visited nodes
    recursion_stack = set()  # Track nodes in the current recursion stack

    def dfs(node, parent):
        if node in recursion_stack:  # Cycle detected
            return True
        if node in visited:  # Already fully processed node
            return False

        visited.add(node)
        recursion_stack.add(node)

        for neighbor in graph[node]:
            # Prevent going back to the parent node
            if neighbor != parent:
                if dfs(neighbor, node):  # Recursively visit neighbors
                    return True

        recursion_stack.remove(node)  # Backtrack

        return False

    # Run DFS from every node in the graph
    for node in graph:
        if node not in visited:
            if dfs(node, None):  # Start DFS, no parent for the first node
                return True  # Cycle found

    return False  # No cycle found

# Create the graph from edges
edges = [(0,1), (1,2), (2,3), (1,4)]

def create_graph(edges):
    graph = defaultdict(list)
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)
    return graph

graph = create_graph(edges)

# Check for a cycle
print(findTheCycle(graph))  # Should print False (no cycle)
