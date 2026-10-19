from collections import defaultdict, deque

def topologicalSort(edges, vertices):
    graph = defaultdict(list)
    indegree = {v: 0 for v in vertices}

    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    top_order = []

    queue = deque([v for v in vertices if indegree[v] == 0])

    while queue:
        node = queue.popleft()
        top_order.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(top_order) != len(vertices):
        raise ValueError("Graph found cycle and cycle not possible in topological sort")

    return top_order

vertices = [0, 1, 2, 3, 4, 5]
edges = [(5,2), (5, 0), (2,3), (3,1), (4,1), (4, 0)]

print(topologicalSort(edges, vertices))