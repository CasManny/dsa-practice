from collections import deque
def maximum_dept(root):
    if not root:
        return 0
    
    left = maximum_dept(root.left)
    right = maximum_dept(root.right)

    return 1 + max(left, right)

def solution(root):

    if not root:
        return 0

    q = deque([root])

    depth = 0

    while q:
        level_level = len(q)

        for _ in range(level_level):
            node = q.popleft()

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        depth += 1

    return depth;
            