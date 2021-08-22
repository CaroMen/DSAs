# Create a queue using classes

"""
    LIFO - Last In, First Out
    adding is called pushing
    deleting is called pooping

    works very similar to stacking plates
    note:
        when we add, the new node will point to the top and the top points to the new node

        when we remove, we need to get the back. the back will now point to the top will now point to None and the new top will be the removed top's .next
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
