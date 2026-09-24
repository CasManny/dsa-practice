class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None
    
    # Root is the first element in preorder
    root_val = preorder[0]
    root = TreeNode(root_val)
    
    # Find root index in inorder
    mid = inorder.index(root_val)
    
    # Build left and right subtrees
    root.left = buildTree(preorder[1:mid+1], inorder[:mid])
    root.right = buildTree(preorder[mid+1:], inorder[mid+1:])
    
    return root
