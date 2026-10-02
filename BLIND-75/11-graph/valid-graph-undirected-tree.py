from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Rule 1: A tree must have exactly n-1 edges
        if len(edges) != n - 1:
            return False

        # Build adjacency list
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False  # cycle detected
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == parent:  # skip the edge back to parent
                    continue
                if not dfs(neighbor, node):
                    return False
            return True

        # Start DFS from node 0
        if not dfs(0, -1):
            return False

        # Rule 2: Must be connected (all nodes visited)
        return len(visited) == n
