import pytest

from coding_interview.linked_lists.linked_lists import LinkedList
from coding_interview.linked_lists.kth_to_last import kth_to_last
from tests.coding_interview.linked_lists.test_linked_lists import \
    assert_linked_list_equality


@pytest.mark.parametrize("linked_list, k, expected", [
    (LinkedList.from_list([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]), 0, 0),
    (LinkedList.from_list([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]), 3, 3),
    (LinkedList.from_list([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]), 7, 7),
    (LinkedList.from_list([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]), 10, 10),
    (LinkedList.from_list([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]), 11, None),
    (LinkedList.from_list([0]), 0, 0),
    (LinkedList.from_list([0]), 1, None),
    (None, 10, None)
])
def test_kth_to_last(linked_list, k, expected):
    assert kth_to_last(linked_list=linked_list, k=k) == expected
