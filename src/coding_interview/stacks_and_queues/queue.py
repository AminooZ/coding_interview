from coding_interview.linked_lists.linked_lists import Node


class Queue:

    def __init__(self):
        self.first = None
        self.last = None

    def remove(self):
        # Remove the first item from the queue
        assert self.first is not None, "Can not remove the top item from an empty queue"
        self.first = self.first.next
        if self.first is None:
            self.last = None

    def add(self, item):
        # Add an item at the end of the queue
        if self.first is None:
            self.first = Node(value=item)
        else:
            node = self.first
            while node.next:
                node = node.next
            node.next = Node(value=item, next=None)
        self.last = Node(value=item, next=None)

    def peek(self):
        # Return the first of the queue
        assert self.first is not None, "Can not return the top item from an empty queue"
        return self.first.value

    def is_empty(self):
        # Return True if and only if the queue is empty
        return self.first is None

    @classmethod
    def from_list(cls, items):
        # Build a queue from a list of items
        queue = cls()
        for item in items:
            queue.add(item=item)
        return queue

    def to_list(self):
        items = []
        while not self.is_empty():
            items.append(self.peek())
            self.remove()
        return items

    def display(self):
        items = []
        node = self.first
        while node is not None:
            items.append(node.value)
            node = node.next
        print(items)
