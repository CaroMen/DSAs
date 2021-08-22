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
            while current.next != self.tail:
                current = current.next
            current.next = None
            self.tail = current

        self.length -= 1
        return removed

    def add_to_head(self, val):
        node = Node(val)

        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

        self.length += 1
        return self

    def remove_head():
        if self.head == None:
            return undefined

        removed = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = removed.next
            removed.next = None

        self.length -= 1
        return removed

    def contains(target):
        node = self.head

        while node:
            if node.value == target:
                return True
            node = node.next

        return False

    def get(index):
        if index < 0 or index >= self.length:
            return None

        counter = 0
        current = self.head

        while counter != index:
            current = current.next
            counter += 1

        return current
