from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])

        # Sets to keep track of cells reachable by each ocean
        pacific_reachable = set()
        atlantic_reachable = set()

        # Directions for moving up, down, left, right
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # DFS function
        def dfs(r, c, visited, prev_height):
            # Stop if out of bounds or already visited
            if ((r, c) in visited or 
                r < 0 or c < 0 or r >= rows or c >= cols or 
                heights[r][c] < prev_height):
                return

            # Mark current cell as visited
            visited.add((r, c))

            # Explore neighbors
            for dr, dc in directions:
                dfs(r+dr, c+dc, visited, heights[r][c])

        # Run DFS from Pacific border (top row and left column)
        for c in range(cols): 
            dfs(0, c, pacific_reachable, heights[0][c])   # top row
            dfs(rows-1, c, atlantic_reachable, heights[rows-1][c]) # bottom row

        for r in range(rows):
            dfs(r, 0, pacific_reachable, heights[r][0])   # left column
            dfs(r, cols-1, atlantic_reachable, heights[r][cols-1]) # right column

        # Intersection of cells reachable by both oceans
        result = list(pacific_reachable & atlantic_reachable)
        return result

heights = [
 [1,2,2,3,5],
 [3,2,3,4,4],
 [2,4,5,3,1],
 [6,7,1,4,5],
 [5,1,1,2,4]
]

sol = Solution()

print(sol.pacificAtlantic(heights))
