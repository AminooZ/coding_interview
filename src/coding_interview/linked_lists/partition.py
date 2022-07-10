# Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater
# or equal to x. If x is contained within the list, the values of x only need to be after the elements less than x (see
# below). The partition element x can appear anywhere in the "right partition"; it does not need to appear between the
# left and right partitions.
# Example:
# input:  3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1
# output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
from coding_interview.linked_lists.linked_lists import LinkedList, Node


def partition(linked_list: LinkedList, k: int) -> LinkedList:
    # Complexity
    #   Time: O(N)
    #   Memory: O(N)
    right_values = []
    node = linked_list.head
    if node.value >= k:  # remove head
        right_values.append(node.value)
        linked_list.head = node.next
    while node.next:  # remove middle
        if node.next.value < k:
            node = node.next
        else:
            right_values.append(node.next.value)
            node.next = node.next.next
    for value in right_values:  # add all right nodes at the end
        node.next = Node(value=value, next=None)
        node = node.next
    return linked_list
