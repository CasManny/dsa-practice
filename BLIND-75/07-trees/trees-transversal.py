from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS Traversals
def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]

# BFS Traversal (Level Order)
def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

# Build example tree
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3, None, TreeNode(6))

# Run traversals
print("Preorder:", preorder(root))     # [1, 2, 4, 5, 3, 6]
print("Inorder:", inorder(root))       # [4, 2, 5, 1, 3, 6]
print("Postorder:", postorder(root))   # [4, 5, 2, 6, 3, 1]
print("Level Order:", level_order(root)) # [1, 2, 3, 4, 5, 6]



