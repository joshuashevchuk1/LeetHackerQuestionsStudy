# 547. Number of Provinces

# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
#
# A province is a group of directly or indirectly connected cities and no other cities outside of the group.
#
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
#
# Return the total number of provinces.

# Constraints:
#   1 <= n <= 200
#   n == isConnected.length
#   n == isConnected[i].length
#   isConnected[i][j] is 1 or 0.
#   isConnected[i][i] == 1
#   isConnected[i][j] == isConnected[j][i]

class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        arr = isConnected
        n = len(arr)

        visited = set()
        provinces = 0

        def dfs(city):
            for neighbor in range(n):
                if arr[city][neighbor] == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        for city in range(len(arr)):
            if city not in visited:
                provinces += 1
                visited.add(city)
                dfs(city)

        return provinces
