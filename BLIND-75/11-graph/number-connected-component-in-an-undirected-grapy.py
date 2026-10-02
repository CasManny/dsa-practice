from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)

        components = 0
        for i in range(n):
            if i not in visited:
                dfs(i)       # explore this component
                components += 1
        return components


n = 6
edges = [[1, 2], [2, 3], [4, 5]]
sol = Solution()

print(sol.countComponents(n, edges))