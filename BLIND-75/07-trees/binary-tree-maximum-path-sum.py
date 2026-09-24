class Solution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')
        
        def dfs(node):
            if not node:
                return 0
            
            # Max gain from left and right, ignore negatives
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)
            
            # Path through current node
            current_path = node.val + left_gain + right_gain
            
            # Update global max
            self.max_sum = max(self.max_sum, current_path)
            
            # Return max gain to parent
            return node.val + max(left_gain, right_gain)
        
        dfs(root)
        return self.max_sum
