# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

"""
    INPUTS/OUTPUTS
        root = [4, 2, 7, 1, 3], val = 2 => [2, 1, 3]

    NOTES
        possibly do a dfs
            use a stack, means we pop last item
        create a lst variable
        create a stack variable with root inside of it
        while stack:
            current = stack.pop()

            if current.val == val:
                return current
            if current.val < val and current.left:
                stack.append(current.left)
            elif current.val > val and current.right:
                stack.append(current.right)
            else:
                if current.left:
                    stack.append(current.left)
                if current.right:
                    stack.append(current.right)
        return None
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(root, val):
        pass
