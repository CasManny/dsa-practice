def number_of_connected_component(numOfNodes, edges):
    # Step 1: Initialize parent array
    parent = [i for i in range(numOfNodes)]
    # Each node is initially its own parent (its own set).

    # Step 2: Initialize rank array (optional optimization)
    rank = [1] * numOfNodes
    # Rank helps keep the tree balanced when merging sets.

    # Step 3: Define the "find" function
    def find(x):
        # If x is not its own parent, recursively find its root
        if parent[x] != x:
            parent[x] = find(parent[x])  # Path compression
        return parent[x]
        # Path compression flattens the tree, making future finds faster.

    # Step 4: Define the "union" function
    def union(x, y):
        rootX = find(x)
        rootY = find(y)

        if rootX == rootY:
            return False  # Already in the same set, no merge needed

        # Union by rank: attach smaller tree under bigger tree
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1
        return True

    # Step 5: Process all edges
    for u, v in edges:
        union(u, v)
        # Each edge connects two nodes, so we merge their sets.

    # Step 6: Count distinct roots
    roots = set()
    for i in range(numOfNodes):
        roots.add(find(i))
    # Each unique root represents one connected component.

    return len(roots)
