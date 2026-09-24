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

def print_trie(node, prefix=""):
    if node.word:
        print(f"word found {node.word} -> prefix path ({prefix})")

    for char, child in node.children.items():
        print(f"{prefix} --> {char}")
        print_trie(child, prefix + char)

words = ['oath', 'car', 'goat']
trie_node = build_trie(words)

print_trie(trie_node)
