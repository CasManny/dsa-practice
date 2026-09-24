class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

def build_trie(words):
    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word
    return root

class Solution:
    def findWords(self, board, words):
        root = build_trie(words)
        result = []
        rows, cols = len(board), len(board[0])

        def dfs(r, c, node):
            char = board[r][c]
            if char not in node.children:
                return
            nxt = node.children[char]

            # Found a word
            if nxt.word:
                result.append(nxt.word)
                nxt.word = None  # avoid duplicates

            board[r][c] = "#"  # mark visited
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, nxt)
            board[r][c] = char  # restore

            # Optimization: prune empty nodes
            if not nxt.children:
                node.children.pop(char)

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result
