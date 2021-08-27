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


"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(root1, root2):
        pass
