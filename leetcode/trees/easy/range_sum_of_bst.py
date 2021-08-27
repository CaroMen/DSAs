# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

"""
    INPUTS/OUTPUTS
        root = [10, 5, 15, 3, 7, null, 18], low = 7, high = 15
            nodes 7 + 10 + 15 = 32

    NOTES
        we need to get the nodes that are in the inclusive range of low and high, so the node can equal exactly the low and high and we need everything in between

        not sure how, but we can use the fact that it's a bst to our advantage to cut down the loops
        if our low is 7 and it's smaller than our root node, then we need to go to the left side of the tree

        seems like we need to go deep rather than wide, so i might do a depth first
            - with a depth we can use a stack
            - pop the first number and use that to see where we need to go next
            - we need a sum variable to keep track of everything

        if our current node is between the low and high, we can add that to our sum variable

        if our current node val is less than the low, then we need to only look at what's to the right of the node and if there's anything there, we need to append it to our stack
            - the reason is because if our root node is a 5 and our low is 4, then anything to the left of our root node is going to be less than 5 and we need it to be in range of low to high

        if our current node val is greater than the high, then we need to look at what's in to the left of the node to keep everything within range
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low, high):
        if not root:
            return 0

        sum_range = 0
        stack = [root]

        while len(stack) > 0:
            current_node = stack.pop()

            if low <= current_node.val and current_node.val <= high:
                sum_range += current_node.val

                if current_node.left:
                    stack.append(current_node.left)
                if current_node.right:
                    stack.append(current_node.right)

            if current_node.val < low:
                if current_node.right:
                    stack.apend(current_node.right)
            # if high is 15, our node is 10
            if current_node.val > high:
                if current_node.left:
                    stack.append(current_node.left)

        return sum_range
