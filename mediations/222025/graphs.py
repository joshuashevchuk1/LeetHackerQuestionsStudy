from fiona.crs import defaultdict
from torch.cuda import graph

nums = [(1,2),(2,1),(3,1)]

def makeGraph(nums):
    graph = defaultdict(list)
    for u, v in nums:
        graph[u].append(v)
        graph[v].append(u)

def dfs():

    nums = [[1,2,0],[0,1,0],[0,1,0]]

    def dfs(grid,i,j):
        if i < 0 and i > len(grid) or j < 0 and j > len(grid[0]):
            return

        dfs[i][j] = "0"

        dfs([i + 1][j], i, j)  # right
        dfs([i - 1][j], i, j)  # left
        dfs([i][j - 1], i, j)  # up
        dfs([i][j + 1], i, j)  # down


    count = 0

    for i in range(len(nums)):
        for j in range(len(nums[i])):
            dfs(nums,i,j)
            if nums[i][j] == 1:  # Found an unvisited land cell
                dfs(nums, i, j)
                count += 1  # Increment island count

def graphsRecursiveSearch(nums):
    def makeGraph(nums):
        graph = defaultdict(list)
        for u, v in nums:
            graph[u].append(v)
            graph[v].append(u)
        return graph

    graph = makeGraph(nums)

    visited = set()

    def dfs(node):
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)

def hasCycle(nums):
    def makeGraph(nums):
        graph = defaultdict(list)
        for u, v in nums:
            graph[u].append(v)
            graph[v].append(u)  # Undirected graph
        return graph

    graph = makeGraph(nums)
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):  # Recurse with the current node as parent
                    return True
            elif neighbor != parent:
                # Found a back edge (cycle detected)
                return True
        return False

    # Check for disconnected components
    for node in graph:
        if node not in visited:
            if dfs(node, -1):  # -1 signifies no parent for the starting node
                return True

    return False
