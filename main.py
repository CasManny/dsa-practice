from collections import deque
def topologicalSort(vertices, edges):
    adj = {v: [] for v in vertices}
    in_degress = {v: 0 for v in vertices}

    for u, v in edges:
        adj[u].append(v)
        in_degress[v] += 1 

    queue = deque([v for v in vertices if in_degress[v] == 0])
    res = []

    while queue:
        node = queue.popleft()
        res.append(node)

        for neighbor in adj[node]:
            in_degress[neighbor] -= 1
            if in_degress[neighbor] == 0:
                queue.append(neighbor)

    if len(res) != len(vertices):
        return "cycle found"

    return res


vertices = [0, 1, 2, 3, 4, 5]
edges = [(5,2), (5, 0), (2,3), (3,1), (4,1), (4, 0)]

print(*topologicalSort(vertices, edges))