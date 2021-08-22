# Create a queue using classes

class Queue:
    def __init__(self):
        # difference between passing it in the constructor vs just assigning it like that
        self.queue = []

    def get_front(self):
        self.queue[-1]

    def get_end(self):
        self.queue[0]

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def dequeue(self):
        return self.queue.pop(0)

    def enqueue(self, val):
        return self.queue.append(val)
