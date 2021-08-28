class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


""" Recursive Implementation """


def recursive_levelorder(root):
    result = []

    def recursive(node, level):
        if not node:
            return

        if len(result) == level:
            result.append([])

        result[level].append(node.val)

        recursive(node.left, level + 1)
        recursive(node.right, level + 1)

    recursive(root, 0)
    return result


def iterative_levelorder(root):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        result.append([])
