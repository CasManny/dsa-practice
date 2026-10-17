class Node:
    def __init__(self, value=0, neighbors=None):
        self.value = value 
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node):
    if not node:
        return None 

    visited = {}

    def dfs(n: Node):
        if n in visited:
            return visited[n]

        copy = Node(n.value)
        visited[n] = copy

        for nei in n.neighbors:
            copy.neighbors.append(dfs(nei))


        return copy

    return dfs(node)

def courseSchedule(numOfCourses, prerequisites):
    preMap = {i: [] for i in range(numOfCourses)}

    for course, preq in prerequisites:
        preMap[course].append(preq)
    
    visited = set()

    def dfs(course):
        if course in visited:
            return False 

        if preMap[course] == []:
            return True 
        
        visited.add(course)
        for nei in preMap[course]:
            if not dfs(nei):
                return False 


        visited.remove(course)
        preMap[course] = []

        return True
    


    for course in range(numOfCourses):
        if not dfs(course):
            return False 

    return True 

def numberOfConnectedComponent(n, edges):
    graph = {i: [] for i in range(n)}

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(n):
        if n in visited:
            return 

        visited.add(n)

        for nei in graph[n]:
            dfs(nei)

    component = 0 


    for i in range(n):
        if i not in visited:
            dfs(i)
            component += 1

    return component


def numberOfIsland(grid):
    rows = len(grid)
    cols = len(grid[0])

    island = 0 

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
            return 

        grid[r][c] = "0"

        dfs(r +1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)


    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                island += 1
                dfs(r, c)

    return island


def pacificAtlantic(heights):
    rows = len(heights)
    cols = len(heights[0])

    pacific_set = set()
    atlantic_set = set()

    def dfs(r, c, visited, prevHeight):
        if (r,c) in visited or r < 0 or r >= rows or c < 0 or c >= cols or heights[r][c] < prevHeight:
            return 

        visited.add((r, c))

        directions = [(1, 0), (-1, 0), (0, 1),(0,-1)]
        for dr, dc in directions:
            nr = dr + r
            nc = dc + c 

            dfs(nr, nc, visited, heights[r][c])

    for r in range(rows):
        dfs(r, 0, pacific_set, heights[r][0])
        dfs(r, cols - 1, atlantic_set, heights[r][cols-1])

    for c in range(cols):
        dfs(0, c, pacific_set, heights[0][c])
        dfs(rows -1, c, atlantic_set, heights[rows-1][c])

    return list(atlantic_set & pacific_set)


def validTreeGraph(n, edges):
    if len(edges) != n - 1:
        return False 

    graph = {i: [] for i in range(n)}

    for u, v in edges:
        graph[v].append(u)
        graph[u].append(v)

    visited = set()
    def dfs(node, parent):
        if node in visited: # detect cycle
            return False 

        visited.add(node)
        for nei in graph[node]:
            if nei == parent:
                continue

            if not dfs(nei, node):
                return False

        return True 

    if not dfs(0, -1):
        return False

    return len(visited) == n # makes sure they are full connected.

