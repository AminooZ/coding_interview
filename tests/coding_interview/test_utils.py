import pytest

from coding_interview.utils import SuperDict


def test_super_dict_init():
    super_dict = SuperDict()
    assert isinstance(super_dict.dict, dict)


@pytest.mark.parametrize("items,expected_items",
                         [((('A', 1), ('B', 2), ('A', 3)), (('A', 4), ('B', 2))),
                          ((('A', 4), ('A', 3), ('A', -2)), (('A', 5),))])
def test_super_dict_add(items, expected_items):
    super_dict = SuperDict()
    for key, value in items:
        super_dict.add(key=key, value=value)
    for key, value in expected_items:
        assert super_dict.dict[key] == value


@pytest.mark.parametrize("items,expected_items",
                         [((('A', -1), ('B', -2), ('A', -3)), (('A', 4), ('B', 2))),
                          ((('A', -4), ('A', -3), ('A', 2)), (('A', 5),))])
def test_super_dict_subtract(items, expected_items):
    super_dict = SuperDict()
    for key, value in items:
        super_dict.subtract(key=key, value=value)
    for key, value in expected_items:
        assert super_dict.dict[key] == value
