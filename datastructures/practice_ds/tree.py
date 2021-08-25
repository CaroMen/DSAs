class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
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

    def bfs(self, root):
        if not root:
            return []

        queue = [root]
        lst = []

        while len(queue):
            current_node = queue.pop(0)
            lst.append(current_node)

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)

        return lst
