import pytest

from coding_interview.linked_lists.linked_lists import LinkedList
from coding_interview.linked_lists.remove_dups import remove_duplicates
from tests.coding_interview.linked_lists.test_linked_lists import \
    assert_linked_list_equality


@pytest.mark.parametrize("linked_list,expected", [
    (LinkedList.from_list([1, 2, 2, 2, 3, 4, 4, 5]),
     LinkedList.from_list([1, 2, 3, 4, 5])),
    (LinkedList.from_list([1, 1, 1, 2, 3, 4, 5, 5]),
     LinkedList.from_list([1, 2, 3, 4, 5]))
])
def test_value_init(linked_list, expected):
    assert assert_linked_list_equality(remove_duplicates(linked_list=linked_list),
                                       expected)
