def add_edge(mat, i, j):
    mat[i][j] = 1
    mat[j][i] = 1  # Undirected graph

def display_matrix(mat):
    for row in mat:
        print(" ".join(map(str, row)))

V = 4
mat = [[0] * V for _ in range(V)]
add_edge(mat, 0, 1)
add_edge(mat, 0, 2)
add_edge(mat, 1, 2)
add_edge(mat, 2, 3)

print("Adjacency Matrix:")
display_matrix(mat)

class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v):
        self.adj.setdefault(u, []).append(v)
        self.adj.setdefault(v, []).append(u)  # Undirected

    def display(self):
        for node in self.adj:
            print(node, "->", self.adj[node])

g = Graph()
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.display()

