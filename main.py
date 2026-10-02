def number_of_connected_component(numOfNodes, edges):
    adj = { i: [] for i in range(numOfNodes)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited = set()

    def dfs(node):
        for neighbor in adj[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor)

    component = 0 
    for i in range(numOfNodes):
        if i not in visited:
            visited.add(i)
            dfs(i)
            component += 1

    return component
n = 5
edges = [[0,1], [1,2], [3,4]]

print(number_of_connected_component(n, edges))
