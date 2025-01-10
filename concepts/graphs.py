def create_graph(edges):
    # Create an empty dictionary to store the adjacency list
    graph = {}

    # Loop through each edge in the input
    for u, v in edges:
        if u not in graph:
            graph[u] = []  # Create an empty list for the node if it doesn't exist
        if v not in graph:
            graph[v] = []  # Create an empty list for the node if it doesn't exist
        graph[u].append(v)  # Add v as a neighbor of u
        graph[v].append(u)  # Add u as a neighbor of v (undirected graph)

    return graph


from collections import defaultdict


def create_graph(edges):
    # Create a defaultdict with a list as the default value type
    graph = defaultdict(list)

    # Loop through each edge in the input
    for u, v in edges:
        graph[u].append(v)  # Add v as a neighbor of u
        graph[v].append(u)  # Add u as a neighbor of v (undirected graph)

    return graph


# Example usage:
edges = [(0, 1), (0, 2), (1, 2), (2, 0)]
graph = create_graph(edges)
print(graph)

from collections import defaultdict, deque

def topological_sort_kahn(edges, num_nodes):
    # Create graph and indegree list
    graph = defaultdict(list)
    indegree = [0] * num_nodes

    # Build the graph and compute indegrees
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    # Initialize queue with nodes that have indegree 0
    queue = deque([i for i in range(num_nodes) if indegree[i] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        # Reduce indegree for all neighbors
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # If result contains all nodes, return it; otherwise, there's a cycle
    return result if len(result) == num_nodes else []

# Example usage:
edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
num_nodes = 6
print(topological_sort_kahn(edges, num_nodes))  # Output: [5, 4, 2, 3, 1, 0]

from collections import defaultdict

def topological_sort_dfs(edges, num_nodes):
    # Create graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    visited = [False] * num_nodes
    stack = []

    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        stack.append(node)  # Add to stack in postorder

    # Perform DFS for all unvisited nodes
    for i in range(num_nodes):
        if not visited[i]:
            dfs(i)

    # Reverse stack to get the topological order
    return stack[::-1]

# Example usage:
edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
num_nodes = 6
print(topological_sort_dfs(edges, num_nodes))  # Output: [5, 4, 2, 3, 1, 0]
