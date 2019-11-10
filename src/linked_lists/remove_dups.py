# Write code to remove duplicates from an unsorted linked list.
# How would you solve this problem if a temporary buffer is not allowed?

from copy import deepcopy


def remove_duplicates(linked_list):
    this = deepcopy(linked_list)
    unique_values = [this.head.value]
    node = this.head
    while node.next:
        if node.next.value in unique_values:
            node.next = node.next.next
        else:
            unique_values.append(node.next.value)
            node = node.next
    return this
