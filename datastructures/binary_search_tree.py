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

        current_node = self.root

        while current_node:
            if current_node.val > val:
                if not current_node.left:
                    current_node.left = node
                    return
                current_node = current_node.left
            else:
                if not current_node.right:
                    current_node.right = node
                    return
                current_node = current_node.right

    def search(self, val, current_node=self.root):
        if not current_node:
            return False

        if val < current_node.val:
            return self.search(val, current_node.left)
        elif val > current_node.val:
            return self.search(val, current_node.right)
        else:
            return True

    def bfs(self, root):
        if not root:
            return []
        lst = []
        queue = [root]

        while len(queue):
            current = queue.pop(0)
            lst.append(current.val)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return lst

    def dfs(self, root):
        if not root:
            return []

        stack = [root]
        lst = []

        while len(stack):
            current = stack.pop()

            if current.right:
                stack.append(current.right)
            lst.append(current.val)
            if current.left:
                stack.append(current.left)
