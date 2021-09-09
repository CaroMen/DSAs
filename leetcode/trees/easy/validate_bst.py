"""
    Given the root of a binary tree, determine if it is a valid binary search tree (BST).

    A valid BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.


    NOTES
        - a tree will have the root node
            - this root node can have a left and right subtree OR it might have just one or the other
        - if the node has a node.left, then we need to see if that value is less than our parent node's value
            - we might need nested if statements here
        - we do the same for the node.right
        - since we need to do a depth first search, we need to have a stack
        - we have to make sure that each subtree is also following the bst rules
            - if the left node of the right subtree is less than our initial parent node, then it's not valid
        - since we need to make sure that each subtree is valid as well we might be able to use a helper function that will check if the tree is valid
"""


def isValidBST(root):
    return valid(root, float("-inf"), float("inf"))


def valid(node, left, right):
    if not node:
        return True

    if not (node.val < right and node.val > left):
        return False

    return (valid(node.left, left, node.val) and valid(node.right, node.val, right))
