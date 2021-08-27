# You are given two binary trees root1 and root2.

# Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

# Return the merged tree.

# Note: The merging process must start from the root nodes of both trees.

"""
    INPUTS/OUTPUTS
        root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7] => [3, 4, 5, 5, 4, null, 7]

            our root is 1 and 2, so we add them
            [3]
            first left node is 3, second left node is 1, so
            [3, 4]
            first left node is 5, second is null, so just put 5
            [3, 4, 5]
            first right node is 2, second right node is 3, so
            [3, 4, 5, 5]


    NOTES
        order we need to iterate through is breadth first or level order
        since it's bfs, we need a queue and then a lst variable to store the new merged bst

        we might need two queues for each of the trees to then do the two loops, but this might not be the most optimal solution

        if tree1 and tree2 are null, then we just return null
            this can be our base case if we solve it recursively
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(root1, root2):
        if not root1 and not root2:
            return None

        value_1 = root1.val if root1 else 0
        value_2 = root2.val if root2 else 0

        new_root = TreeNode(value_1, value_2)

        new_root.left = self.mergeTrees(
            root1.left if root1 else None, root2.left if root2 else None)

        new_root.right = self.mergeTrees(
            root1.right if root1 else None, root2.right if root1 else None)

        return new_root
