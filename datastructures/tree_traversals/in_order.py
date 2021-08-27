class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = left
        self.right = right


""" Recursive Implementation """


def recursive_inorder(root):
    result = []

    def recursive(node):
        if not node:
            return

        recursive(node.left)
        result.append(node.val)
        recursive(node.right)

    recursive(root)
    return result
