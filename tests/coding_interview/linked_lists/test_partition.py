import pytest

from coding_interview.linked_lists.linked_lists import LinkedList
from coding_interview.linked_lists.kth_to_last import kth_to_last
from coding_interview.linked_lists.partition import partition
from tests.coding_interview.linked_lists.test_linked_lists import \
    assert_linked_list_equality


@pytest.mark.parametrize("linked_list, k", [
    (LinkedList.from_list([3, 5, 8, 5, 10, 2, 1]), 5)
])
def test_partition(linked_list, k):
    partitioned_linked_list = partition(linked_list=linked_list, k=k)
    # Test linked_list values equality without order
    assert sorted(partitioned_linked_list.to_list()) == sorted(linked_list.to_list())
    # Test partition
    cross_partition = False
    node = partitioned_linked_list.head
    while node.next:
        if node.value < k:
            assert cross_partition is False
        else:
            cross_partition = True
        node = node.next
    assert (node.value < k) != cross_partition
