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
