# Given the root of a binary tree, invert the tree, and return its root.

"""
    INPUTS/OUTPUTS
        root = [4, 2, 7, 1, 3, 6, 9] => [4, 7, 2, 9, 6, 3, 1]
                            4
                         2     7
                       1   3  6  9

    NOTES
        at each level we need to swap the left and right nodes

        this is a bfs sort of traversal, so we need a queue
        loop while we have something in our queue
            pop the last item in the queue and that'll be our current node
            swap the current node left and right

            if current node has a left, add it to queue
            if current node has a right, add it to queue
        return the root because swapping was done in place

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root):
        if root is None:
            return []

        queue = [root]

        while queue:
            current_node = queue.pop()

            current_node.left, current_node.right = current_node.right, current_node.left

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return root
