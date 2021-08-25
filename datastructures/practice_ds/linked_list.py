class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.length = 0

    def add_tail(self, val):
        node = Node(val)

        # 1 -> 2 -> 3 -> x
        if self.length == 0:
            self.tail = node
            self.head = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
        return self

    def remove_tail(self):
        # 1 -> 2 -> 3
        # 1 -> 2

        if self.length == 0:
            return None

        removed = self.tail
        current = self.head

        if self.length == 1:
            self.tail = None
            self.head = None
        else:
            while current.next != self.tail:
                current = current.next
            current.next = None

        return removed
