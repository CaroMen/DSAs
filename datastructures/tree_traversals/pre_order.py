class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


""" Recursive Implementation """


def recurisve_preorder(root):
    result = []

    def recursive(node):
        if not node:
            return

        result.append(node.val)
        recursive(node.left)
        recursive(node.right)

    recursive(root)
    return result


""" Iterative Implementation """


def iterative_preorder(root):
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        current = stack.pop()

        result.append(current.val)

        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    return result
