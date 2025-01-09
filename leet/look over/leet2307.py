from typing import List, Dict


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))  # parent[i] points to the parent of i, or i itself if it's a root
        self.ratio = [1.0] * n  # ratio[i] stores the ratio of i to its parent

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            original_parent = self.parent[x]
            self.parent[x] = self.find(self.parent[x])  # Path compression
            self.ratio[x] *= self.ratio[original_parent]  # Update the ratio of x to root
        return self.parent[x]

    def union(self, x: int, y: int, value: float) -> None:
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            self.parent[rootX] = rootY  # Union the sets
            self.ratio[rootX] = self.ratio[y] * value / self.ratio[x]  # Adjust the ratio

    def isConnected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class Solution:
    def checkContradictions(self, equations: List[List[str]], values: List[float]) -> bool:
        var_map: Dict[str, int] = {}  # Mapping variable names to unique indices
        index = 0

        uf = UnionFind(2 * len(equations))  # Maximum possible unique variables

        # Step 1: Process all "==" equations and union the variables
        for eq, value in zip(equations, values):
            var1, var2 = eq
            if var1 not in var_map:
                var_map[var1] = index
                index += 1
            if var2 not in var_map:
                var_map[var2] = index
                index += 1
            uf.union(var_map[var1], var_map[var2], value)

        # Step 2: Check all "!=" equations for contradictions
        for eq, value in zip(equations, values):
            var1, var2 = eq
            if var1 not in var_map:
                var_map[var1] = index
                index += 1
            if var2 not in var_map:
                var_map[var2] = index
                index += 1
            if uf.isConnected(var_map[var1], var_map[var2]):
                return True  # Contradiction found

        return False  # No contradictions found
