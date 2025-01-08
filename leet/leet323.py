# Problem: Connected Components in an Undirected Graph
#
# You are given an undirected graph with n nodes, numbered from 0 to n-1,
# and an array edges where edges[i] = [u, v] represents a connection between nodes u and v.
#
# Your task is to determine the number of connected components in the graph.

# plan of attack

# have a dfs, visited and make the graph

from collections import defaultdict

array = [[1,0],[0,1]]

# setup
visited = set()
graph = defaultdict(array)
la = len(array)
connected  = 0

def dfs(node):
    for i in range(la):
        # not sure for this part
        print("TODO")


for node in la:
    if node not in visited:
        dfs(node)
        visited.add(node)
        connected += 1

# missing

from collections import defaultdict

# Input: Edge list
array = [[1, 0], [0, 1]]  # Example input
n = 2  # Total number of nodes (can be passed as input)

# Setup
visited = set()
graph = defaultdict(list)
connected = 0

# Step 1: Build the graph
for u, v in array:
    graph[u].append(v)
    graph[v].append(u)

# Step 2: DFS function
def dfs(node):
    for neighbor in graph[node]:  # Explore all neighbors of 'node'
        if neighbor not in visited:  # Check if the neighbor is unvisited
            visited.add(neighbor)  # Mark as visited
            dfs(neighbor)  # Recursively visit the neighbor

# Step 3: Count connected components
for node in range(n):  # Iterate through all nodes
    if node not in visited:  # If the node hasn't been visited
        visited.add(node)  # Mark the node as visited
        dfs(node)  # Perform DFS to explore the component
        connected += 1  # Increment the count of connected components

print(connected)
