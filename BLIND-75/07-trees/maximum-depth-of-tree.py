class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

tree_root = TreeNode(3)
tree_root.left = TreeNode(9)
tree_root.right = TreeNode(20, TreeNode(15), TreeNode(7))

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1

sol = Solution()
print(sol.maxDepth(tree_root))