# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class SolutionDFS:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        visited = {}

        def dfs(n):
            if n in visited:
                return visited[n]
            
            # Clone the node
            copy = Node(n.val)
            visited[n] = copy

            # Clone neighbors recursively
            for nei in n.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy

        return dfs(node)

from collections import deque

class SolutionBFS:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        visited = {}
        visited[node] = Node(node.val)

        queue = deque([node])

        while queue:
            cur = queue.popleft()
            for nei in cur.neighbors:
                if nei not in visited:
                    visited[nei] = Node(nei.val)
                    queue.append(nei)
                visited[cur].neighbors.append(visited[nei])

        return visited[node]
