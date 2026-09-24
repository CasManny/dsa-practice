class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = ""

def build_tree(words):
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
    def find_word(board, words):
        root = build_tree(words)
        rows = len(board)
        cols = len(board[0])

        result = []

        def dfs(r, c, node):
            char = board[r][c]
            if char not in node.children:
                return 

            nxt = node.children[char]
            if nxt.word:
                result.append(nxt.word)
                nxt.word = None 

            board[r][c] = "#"

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                nr = dr + r 
                nc = dc + c 

                if 0 <= nr < rows and 0 <= nc < cols and board[r][c] != "#":
                    dfs(nr, nc, nxt)
            board[r][c] = char 

            if not nxt.children:
                node.children.pop(char)

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result