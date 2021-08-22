# create a singly linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.length = 0

    def add_to_tail(self, val):
        node = Node(val)

        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.length += 1
        return self

    def remove_tail(self):
        if self.length == 0:
            return undefined

        removed = self.tail
        current = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            # 1 -> 2 -> 3 -> 4
            # current = 3
            # current.next = 4
            # removed = 4
            while current.next != self.tail:
                current = current.next
            current.next = None
            self.tail = current

        self.length -= 1
        return removed
