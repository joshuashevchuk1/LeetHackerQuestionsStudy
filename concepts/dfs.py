# Depth-First Search (DFS) is an algorithm used to traverse or search through data structures like graphs or trees. It starts at a specific node (or root) and explores as far as possible along each branch before backtracking to explore other branches.
#
# Characteristics of DFS
# Exploration to Depth:
#
# DFS dives deep into one branch of a graph/tree before moving to another branch.
# Traversal Order:
#
# In a tree, DFS follows the path to a leaf node before backtracking. In a graph, it explores neighbors of a node as deeply as possible before backtracking.
# Recursive or Iterative:
#
# DFS can be implemented using recursion (implicit stack) or an explicit stack for iterative traversal.
# Applications:
#
# Detecting connected components.
# Solving mazes or puzzles.
# Topological sorting.
# Pathfinding.
# Cycle detection in graphs.


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
        print(node, end=" ") # action
        visited.add(node) # once the node is added you can continue
        for neighbor in graph[node]: # the graph (set of array)
            dfs_recursive(graph, neighbor, visited) # didn't find what you are looking for, do it again.
            # Do it for every node


visited = set()
dfs_recursive(graph,'A',visited)
print("\n")
visited.clear()
dfs_recursive(graph,'B',visited)


def dfs(node):
    # Mark the node as visited
    visited.add(node)

    # Process the current node
    print(node)

    # Recursively visit neighbors
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor)

# DFS is particularly useful in solving problems that require exploring
# all possible solutions (e.g., maze problems, permutations, and combinations).

def dfs(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid) or grid[i][j] == "0":
        return
    dfs[i][j] = "0" # visited marker

    # iteration steps
    dfs([i+1][j],i,j)# right
    dfs([i-1][j],i,j) # left
    dfs([i][j-1],i,j) # up
    dfs([i][j+1],i,j) # down