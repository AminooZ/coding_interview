class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:

    def __init__(self, value):
        self.head = Node(value=value, next=None)

    @classmethod
    def from_node(cls, node):
        linked_list = cls()
        linked_list.head = node
        return linked_list

    def append_to_tail(self, value):
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value=value, next=None)

    def delete(self, value):
        node = self.head
        if node.value == value:
            self.head = self.head.next  # move head
            return
        while node.next:
            if node.next.value == value:
                node.next = node.next.next
                return  # head didn't change
            node = node.next
        return  # linked list didn't change

    @classmethod
    def from_list(cls, values):
        linked_list = cls(value=values[0])
        for value in values[1:]:
            linked_list.append_to_tail(value=value)
        return linked_list

    def display(self):
        node = self.head
        while node.next:
            print(node.value)
            node = node.next
        print(node.value)
