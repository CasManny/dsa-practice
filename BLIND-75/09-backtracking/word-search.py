board = [
  ["A","B","C","E"],
  ["S","F","C","S"],
  ["A","D","E","E"]
]
word = "ABCB"

def exist(board, word):
    rows, cols = len(board), len(board[0])

    def dfs(r, c, i):
        # Base case: all characters matched
        if i == len(word):
            return True
        # Out of bounds or mismatch
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
            return False

        # Choose: mark cell as visited
        temp = board[r][c]
        board[r][c] = "#"

        # Explore neighbors
        found = (dfs(r+1, c, i+1) or
                 dfs(r-1, c, i+1) or
                 dfs(r, c+1, i+1) or
                 dfs(r, c-1, i+1))

        # Unchoose: restore cell
        board[r][c] = temp
        return found

    # Try starting from every cell
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False
