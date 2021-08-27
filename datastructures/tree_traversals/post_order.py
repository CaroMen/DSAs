class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


""" Recursive Implementation """


def recursive_postorder(root):
    result = []

    def recursive(node):
        if not node:
            return

        recursive(node.left)
        recursive(node.right)
        result.append(node.val)

    recursive(root)
    return result


""" Iterative Implementation """


def iterative_postorder(root):
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        current = stack.pop()
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
        result.append(current.val)

    return result[::-1]
