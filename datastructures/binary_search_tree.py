"""
    val = 2
            5

"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        node = Node(val)
        if not self.root:
            self.root = node
            return

        this_value = self.root
        while this_value:
            if this_value > val:  # 5 > 2
                if not this_value.left:
                    this_value.left = node
                    return
                this_value = this_value.left
            else:
                if not this_value.right:
                    this_value.right = node
                    return
                this_value = this_value.right

    def search(self, val, current_node=self.root):
        if not current_node:
            return False

        if val < current_node.val:
            return self.search(val, current_node.left)
        elif val > current_node.val:
            return self.search(val, current_node.right)
        else:
            return True
