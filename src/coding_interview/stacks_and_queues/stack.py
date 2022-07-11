from coding_interview.linked_lists.linked_lists import Node


class Stack:

    def __init__(self):
        self.top = None

    def pop(self):
        # Remove the top item from the stack
        assert self.top is not None, "Can not remove the top item from an empty stack"
        self.top = self.top.next

    def push(self, item):
        # Add an item to the top of the stack
        self.top = Node(value=item, next=self.top)

    def peek(self):
        # Return the top of the stack

        assert self.top is not None, "Can not return the top item from an empty stack"
        return self.top.value

    def is_empty(self):
        # Return True if and only if the stack is empty
        return self.top is None

    @classmethod
    def from_list(cls, items):
        # Build a stack from a list of items
        stack = cls()
        for item in items:
            stack.push(item=item)
        return stack

    def to_list(self):
        items = []
        while not self.is_empty():
            items.append(self.peek())
            self.pop()
        items.reverse()
        return items
