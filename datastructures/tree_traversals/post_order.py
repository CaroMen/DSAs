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
