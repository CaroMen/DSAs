# Create a stack using classes

"""
    FIFO - First In, First Out
    adding is called pushing
    deleting is called pooping

    works very similar to stacking plates
    note:
        when we add, the new node will point to the top and the top points to the new node

        when we remove, the top will now point to None and the new top will be the removed top's .next
"""


class Node:
    def __init__(val):
        this.val = val
        this.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def add(self, val):
        node = Node(val)

        if not self.length:
            self.top = node
        else:
            node.next = self.top
            self.top = node

        self.length += 1
        return self.length

    def pop(self):
        if not self.top:
            return None
        else:
            removed = self.top
            self.top = removed.next
            self.length -= 1
            return removed.val

    # def add(self, val):
    #     node = Node(val)

    #     if not self.length:
    #         self.top = node
    #     else:
    #         # we have a top
    #         node.next = self.top
    #         self.top = node

    #     self.length += 1
    #     return self.length

    # def pop(self):
    #     if not self.top:
    #         return None
    #     else:
    #         removed = self.top
    #         self.top = removed.next
    #         self.length -= 1

    #         return removed.val
