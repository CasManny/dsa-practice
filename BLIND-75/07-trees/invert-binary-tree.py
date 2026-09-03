class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

class Solution:
    def invertTree(self, root: TreeNode):
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
