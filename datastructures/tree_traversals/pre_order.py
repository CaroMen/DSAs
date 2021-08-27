class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


""" Recursive Implementation """


def preorder_traversal(root):
    result = []

    def recursive(node):
        if not node:
            return

        result.append(node.val)
        recursive(node.left)
        recursive(node.right)

    recursive(root)
    return result
