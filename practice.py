def isSameTree(p, q):
    if not p and not q:
        return True 

    if not p or not q:
        return False 

    if p.value != q.value:
        return False 

    return ((isSameTree(p.left, q.left)) and (isSameTree(p.right, q.right)))


def isSubTree(root, subTree):
    if not root:
        return False 

    if isSameTree(root, subTree):
        return True 

    return ((isSubTree(root.left, subTree)) or (isSubTree(root.right, subTree)))

