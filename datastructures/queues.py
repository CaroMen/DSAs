# Create a queue using classes

"""
    LIFO - Last In, First Out
    adding is called pushing
    deleting is called pooping

"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        # difference between passing it in the constructor vs just assigning it like that
        self.front = None
        self.back = None
        self.length = 0

    def enqueue(self, val):
        node = Node(val)
        if self.length == 0:
            self.front = node
            self.back = node
        else:
            # we have a front
            self.back.next = node
            self.back = node

        self.length += 1
        return self.length

    def dequeue(self):
        if self.length == 0:
            return None

        removed = self.front
        self.front = removed.next
        self.length -= 1

        return removed.val
