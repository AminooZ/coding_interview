# Implement an algorithm to find the kth to last element of a singly linked list

from coding_interview.linked_lists.linked_lists import LinkedList


def kth_to_last(linked_list: LinkedList, k: int) -> int:
    if linked_list is None:
        return None
    fast_pointer = linked_list.head
    slow_pointer = linked_list.head
    for _ in range(k):
        if fast_pointer.next:
            fast_pointer = fast_pointer.next
        else:
            return None
        # fast_pointer is k positions ahead of slow_pointer
    while fast_pointer.next:
        fast_pointer = fast_pointer.next
        slow_pointer = slow_pointer.next
    return slow_pointer.value
